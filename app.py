from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# CORS 설정 (앱에서 호출 가능하게)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 가짜 공정 상태 데이터
process_status = {
    "progress": 78.5,
    "defect_rate": 4.2,
    "status": "RUNNING",
    "last_updated": datetime.now().isoformat()
}

# 가짜 심박수 데이터
heart_rate_data = {
    "worker_id": "W001",
    "bpm": 88,
    "measured_at": datetime.now().isoformat()
}

# 가짜 설비 상태 목록
equipment_status = [
    {"equipment": "프레스기1", "status": "RUNNING"},
    {"equipment": "레이저기2", "status": "IDLE"},
    {"equipment": "용접기3", "status": "ERROR"}
]

# 가짜 설비 알림
equipment_alerts = [
    {
        "equipment": "프레스기1",
        "message": "진동 이상 감지",
        "timestamp": "2025-08-30T14:20"
    },
    {
        "equipment": "레이저기2",
        "message": "온도 초과",
        "timestamp": "2025-08-30T13:50"
    }
]

# 📡 공정 상태 API
@app.get("/api/process/status")
def get_process_status():
    return process_status

# 📡 심박수 API
@app.get("/api/worker/heart-rate")
def get_heart_rate():
    return heart_rate_data

# 📡 설비 상태 API
@app.get("/api/equipment/status")
def get_equipment_status():
    return equipment_status

# 📡 설비 알림 API
@app.get("/api/equipment/alerts")
def get_equipment_alerts():
    return equipment_alerts
