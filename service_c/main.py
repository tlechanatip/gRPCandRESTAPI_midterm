from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def get_status():
    # ตอบกลับเป็น JSON ธรรมดาผ่าน REST
    return {
        "service": "Service C",
        "status": "Running",
        "database": "Connected"
    }