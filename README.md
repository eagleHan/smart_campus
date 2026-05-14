# 智慧校园 Smart Campus

智慧校园微服务平台，采用微服务架构，覆盖教务、教学、考试、学情、办公、后勤等核心业务领域。

## 技术栈

- **后端**: Python 3.11+ / FastAPI / Uvicorn
- **数据库**: PostgreSQL 16 / SQLAlchemy 2.0 / Alembic
- **缓存**: Redis 7
- **消息队列**: RabbitMQ 3
- **容器化**: Docker + Docker Compose
- **前端**: HTML5 / Vue / React（规划中）

## 项目结构

```
smart_campus/
├── packages/                  # 公共包
│   └── platform_core/         # 平台核心（服务目录、工厂函数、公共模型、配置）
├── services/                  # 微服务
│   ├── api_gateway/           # API 网关（端口 8000）
│   ├── admin_console/         # 统一管理后台（端口 8010）
│   ├── identity_access/       # 认证与访问控制（端口 8001）
│   ├── org_user/              # 组织与用户中心（端口 8002）
│   ├── academic_master/       # 教务主数据中心（端口 8003）
│   ├── academic_core/         # 教务核心服务（端口 8004）
│   ├── student_growth/        # 学生成长服务（端口 8005）
│   ├── oa_collaboration/      # OA 协同服务（端口 8006）
│   ├── question_bank/         # 题库服务（端口 8007）
│   ├── exam_orchestration/    # 考试编排服务（端口 8008）
│   └── marking_engine/        # 阅卷引擎（端口 8009）
├── frontends/                 # 前端
│   ├── admin-portal/          # 统一管理后台前端
│   └── apps/                  # 各业务系统前端
├── scripts/                   # 脚本
│   ├── run_dev.sh             # Linux/Mac 开发启动脚本
│   └── run_dev.py             # 跨平台开发启动脚本
├── docs/                      # 文档
│   └── 需求文档.md             # 项目需求文档
├── docker-compose.yml         # Docker Compose 配置
├── Dockerfile                 # Docker 镜像配置
└── pyproject.toml             # Python 项目配置
```

## 快速开始

### 环境要求

- Python 3.11+
- Docker & Docker Compose（可选，用于容器化部署）

### 方式一：Docker 一键启动（推荐）

```bash
# 复制环境变量模板
cp .env.example .env

# 启动所有服务
docker compose up --build

# 查看服务状态
docker compose ps
```

服务启动后访问：
- API 网关: http://localhost:8000
- 管理后台: http://localhost:8010
- 各业务服务: http://localhost:8001-8009

### 方式二：本地开发

```bash
# 1. 创建虚拟环境
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# 2. 安装依赖（包含开发依赖）
pip install -e ".[dev]"

# 3. 启动基础设施（PostgreSQL、Redis、RabbitMQ）
docker compose up postgres redis rabbitmq -d

# 4. 启动所有服务
python scripts/run_dev.py
```

## 服务清单

| 服务编码 | 服务名称 | 端口 | 业务域 | 前端路径 |
|---------|---------|------|--------|---------|
| api-gateway | API 网关 | 8000 | 平台基础能力层 | - |
| admin-console | 统一管理后台 | 8010 | 平台基础能力层 | frontends/admin-portal |
| identity-access | 认证与访问控制 | 8001 | 基础平台域 | frontends/apps/identity-access |
| org-user | 组织与用户中心 | 8002 | 基础平台域 | frontends/apps/org-user |
| academic-master | 教务主数据中心 | 8003 | 基础平台域 | frontends/apps/academic-master |
| academic-core | 教务核心服务 | 8004 | 教务管理域 | frontends/apps/academic-core |
| student-growth | 学生成长服务 | 8005 | 学人发展域 | frontends/apps/student-growth |
| oa-collaboration | OA 协同服务 | 8006 | 协同办公域 | frontends/apps/oa-collaboration |
| question-bank | 题库服务 | 8007 | 教学评测域 | frontends/apps/question-bank |
| exam-orchestration | 考试编排服务 | 8008 | 教学评测域 | frontends/apps/exam-orchestration |
| marking-engine | 阅卷引擎 | 8009 | 教学评测域 | frontends/apps/marking-engine |

## 开发指南

### 添加新服务

1. 在 `services/` 下创建新目录
2. 在 `packages/platform_core/src/platform_core/catalog.py` 的 `SERVICE_CATALOG` 中注册服务
3. 在 `docker-compose.yml` 中添加服务配置
4. 在 `scripts/run_dev.py` 中添加服务启动配置

### 运行测试

```bash
pytest
```

### 代码格式化

```bash
ruff check .
ruff format .
```

## 环境变量

| 变量名 | 说明 | 默认值 |
|-------|------|--------|
| APP_ENV | 应用环境 | dev |
| POSTGRES_HOST | PostgreSQL 主机 | localhost |
| POSTGRES_PORT | PostgreSQL 端口 | 5432 |
| POSTGRES_USER | PostgreSQL 用户名 | smartcampus |
| POSTGRES_PASSWORD | PostgreSQL 密码 | smartcampus |
| POSTGRES_DB | PostgreSQL 数据库 | platform_db |
| REDIS_HOST | Redis 主机 | localhost |
| REDIS_PORT | Redis 端口 | 6379 |
| RABBITMQ_HOST | RabbitMQ 主机 | localhost |
| RABBITMQ_PORT | RabbitMQ 端口 | 5672 |

## 文档

- [项目需求文档](docs/需求文档.md)

## 许可证

MIT License
