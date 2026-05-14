#!/usr/bin/env python3
"""跨平台开发启动脚本.

启动所有微服务，支持 Windows、Linux 和 macOS。
"""

import subprocess
import sys
import os
import signal
from typing import List

# 服务配置: (模块路径, 端口)
SERVICES = [
    ("services.api_gateway.app.main:app", 8000),
    ("services.admin_console.app.main:app", 8010),
    ("services.identity_access.app.main:app", 8001),
    ("services.org_user.app.main:app", 8002),
    ("services.academic_master.app.main:app", 8003),
    ("services.academic_core.app.main:app", 8004),
    ("services.student_growth.app.main:app", 8005),
    ("services.oa_collaboration.app.main:app", 8006),
    ("services.question_bank.app.main:app", 8007),
    ("services.exam_orchestration.app.main:app", 8008),
    ("services.marking_engine.app.main:app", 8009),
]


class ServiceManager:
    """服务管理器."""

    def __init__(self):
        self.processes: List[subprocess.Popen] = []
        self._shutdown_requested = False

    def start_service(self, module: str, port: int) -> subprocess.Popen:
        """启动单个服务."""
        service_name = module.split(".")[1]  # 从模块路径提取服务名
        cmd = [
            sys.executable,
            "-m",
            "uvicorn",
            module,
            "--reload",
            "--port",
            str(port),
            "--host",
            "0.0.0.0",
        ]

        # 设置环境变量，标识当前服务
        env = os.environ.copy()
        env["SERVICE_NAME"] = service_name
        env["SERVICE_PORT"] = str(port)

        print(f"🚀 启动 {service_name} (端口: {port})...")

        # Windows 需要特殊处理
        if sys.platform == "win32":
            proc = subprocess.Popen(
                cmd,
                env=env,
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
            )
        else:
            proc = subprocess.Popen(
                cmd,
                env=env,
                preexec_fn=os.setsid,  # 创建新进程组
            )

        return proc

    def start_all(self):
        """启动所有服务."""
        print("=" * 60)
        print("智慧校园微服务开发启动器")
        print("=" * 60)
        print(f"Python: {sys.version}")
        print(f"平台: {sys.platform}")
        print("-" * 60)

        for module, port in SERVICES:
            try:
                proc = self.start_service(module, port)
                self.processes.append(proc)
            except Exception as e:
                print(f"❌ 启动失败 {module}: {e}")
                self.shutdown()
                sys.exit(1)

        print("-" * 60)
        print(f"✅ 已启动 {len(self.processes)} 个服务")
        print("按 Ctrl+C 停止所有服务")
        print("=" * 60)

    def shutdown(self):
        """关闭所有服务."""
        if self._shutdown_requested:
            return

        self._shutdown_requested = True
        print("\n🛑 正在停止所有服务...")

        for proc in self.processes:
            try:
                if sys.platform == "win32":
                    # Windows: 发送 CTRL_BREAK_EVENT
                    proc.send_signal(signal.CTRL_BREAK_EVENT)
                else:
                    # Unix: 发送 SIGTERM 到进程组
                    os.killpg(os.getpgid(proc.pid), signal.SIGTERM)

                # 等待进程结束
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                print(f"⚠️ 服务 {proc.pid} 未响应，强制终止")
                proc.kill()
            except Exception as e:
                print(f"⚠️ 停止服务 {proc.pid} 时出错: {e}")

        print("✅ 所有服务已停止")

    def run(self):
        """运行服务管理器."""
        self.start_all()

        try:
            # 等待所有进程
            for proc in self.processes:
                proc.wait()
        except KeyboardInterrupt:
            print("\n⚠️ 收到中断信号")
        finally:
            self.shutdown()


def main():
    """主入口."""
    manager = ServiceManager()
    manager.run()


if __name__ == "__main__":
    main()
