#!/usr/bin/env bash
set -euo pipefail

SERVICES=(
  "services.api_gateway.app.main:app 8000"
  "services.admin_console.app.main:app 8010"
  "services.identity_access.app.main:app 8001"
  "services.org_user.app.main:app 8002"
  "services.academic_master.app.main:app 8003"
  "services.academic_core.app.main:app 8004"
  "services.student_growth.app.main:app 8005"
  "services.oa_collaboration.app.main:app 8006"
  "services.question_bank.app.main:app 8007"
  "services.exam_orchestration.app.main:app 8008"
  "services.marking_engine.app.main:app 8009"
)

for service in "${SERVICES[@]}"; do
  module="${service% *}"
  port="${service##* }"
  uvicorn "$module" --reload --port "$port" &
done

wait
