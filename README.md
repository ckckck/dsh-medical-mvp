# dsh-medical-mvp

MVP for hospital AI agent focused on real-time ED length of stay monitoring and antibiotic stewardship (DDDs).

## Tech Stack
- Backend: FastAPI
- Agent Framework: dsh
- Database: PostgreSQL (simulated HIS)
- Frontend: React (planned)

## Core Scenarios
1. ED Length of Stay > 4 hours real-time alert
2. Antibiotic use intensity (DDDs / 100 patient-days) monitoring

## First Engineering Step
Build mock HIS service + ED LOS query endpoint with alert routing.
