from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    # หน้าแรกสำหรับเช็คว่า Service A (FastAPI) ทำงานอยู่ไหม
    return {"service": "Service A", "status": "Online", "mode": "gRPC Provider"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}