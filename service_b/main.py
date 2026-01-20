from fastapi import FastAPI
import requests
from grpc_client import get_user_data_from_a

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Service B (Gateway)"}

@app.get("/get-all-data/{user_id}")
def get_combined_data(user_id: str):
    # 1. เรียก Service A ผ่าน gRPC
    user_info = get_user_data_from_a(user_id)
    
    # 2. เรียก Service C ผ่าน REST API (เรียกข้าม Docker container)
    try:
        response_c = requests.get(f"http://service_c:8000/status")
        service_c_data = response_c.json()
    except:
        service_c_data = {"error": "Service C is unreachable"}

    # รวมผลลัพธ์จากทั้งสองที่
    return {
        "source": "Service B (Gateway)",
        "data_from_a_grpc": user_info,
        "data_from_c_rest": service_c_data
    }