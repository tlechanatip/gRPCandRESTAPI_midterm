============================================================
โปรเจ็ค: Microservices (REST + gRPC)
ชื่อ-นามสกุล: [ชื่อของคุณ]
รหัสประจำตัว: [รหัส 3 ตัวท้ายของคุณ]
============================================================

### 1. โครงสร้างโปรเจ็ค (Project Tree)
.
├── docker-compose.yml
├── requirements.txt
├── service_a
│   ├── Dockerfile
│   ├── grpc_server.py
│   ├── main.py
│   └── proto
│       └── user.proto
├── service_b
│   ├── Dockerfile
│   ├── grpc_client.py
│   ├── main.py
│   └── proto
│       └── user.proto
└── service_c
    ├── Dockerfile
    └── main.py

---

### 2. อธิบายการทำงานสถาปัตยกรรม (Architecture)
โปรเจ็คนี้ประกอบด้วย 3 Microservices ที่ทำงานร่วมกันดังนี้:

1. Service A (Data Provider): 
   - ทำหน้าที่เป็น gRPC Server 
   - คอยให้บริการข้อมูล User (ชื่อและอีเมล) ผ่านโปรโตคอล gRPC (Port 50051)
   
2. Service B (Gateway & Orchestrator): 
   - ทำหน้าที่เป็น "ตัวกลาง" รับ Request จากผู้ใช้ผ่าน REST API (Port 8000)
   - เมื่อได้รับ Request จะไปดึงข้อมูลจาก Service A (ผ่าน gRPC) และ Service C (ผ่าน REST) มาประมวลผลร่วมกัน

3. Service C (Status Provider): 
   - ทำหน้าที่เป็น REST API ธรรมดา (Port 8002)
   - ให้ข้อมูลสถานะของระบบ (System Status)

---

### 3. ลำดับการ Request และ Response (Data Flow)
เมื่อผู้ใช้เรียกใช้งานผ่าน Browser หรือ Postman:

ขั้นตอนที่ 1: User ส่ง Request (GET) ไปที่ Service B 
         ที่ URL: http://localhost:8000/get-all-data/{user_id}

ขั้นตอนที่ 2: Service B ทำหน้าที่เป็น Client ส่งคำขอต่อดังนี้:
         - [Request A]: เรียก Service A ผ่าน gRPC เพื่อขอข้อมูล User
         - [Request C]: เรียก Service C ผ่าน HTTP REST เพื่อขอสถานะระบบ

ขั้นตอนที่ 3: การตอบกลับ (Response):
         - Service A ตอบกลับ (gRPC Response) มายัง Service B
         - Service C ตอบกลับ (JSON Response) มายัง Service B

ขั้นตอนที่ 4: Service B รวบรวมข้อมูลจากทั้งสองแหล่ง แล้วตอบกลับ (JSON) ให้ User ทันที

---

### 4. วิธีการรันโปรเจ็ค (How to Run)
1. ติดตั้ง Docker Desktop และตรวจสอบให้แน่ใจว่าได้เปิดโปรแกรมแล้ว
2. เปิด Terminal/PowerShell ในโฟลเดอร์โปรเจ็ค
3. รันคำสั่งเพื่อสร้างและเริ่มทำงาน Container:
   > docker-compose up --build

---

### 5. ผลลัพธ์ที่ควรแสดง (Expected Output)
เมื่อรันสำเร็จ ให้เปิด Browser ไปที่: 
http://localhost:8000/get-all-data/chanatip

คุณจะได้รับ JSON ที่รวมข้อมูลจากทุก Service ดังนี้:
{
  "source": "Service B (Gateway)",
  "data_from_a_grpc": {
    "name": "ชนาธิป สร้อยจิตร",
    "email": "user_chanatip@university.ac.th"
  },
  "data_from_c_rest": {
    "service": "Service C",
    "status": "Running",
    "database": "Connected"
  }
}
============================================================