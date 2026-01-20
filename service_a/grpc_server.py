import grpc
from concurrent import futures
import proto.user_pb2 as user_pb2
import proto.user_pb2_grpc as user_pb2_grpc

# สร้าง Class เพื่อจัดการคำขอจาก gRPC
class UserServiceHandler(user_pb2_grpc.UserServiceServicer):
    def GetUserDetail(self, request, context):
        # จำลองการหาข้อมูลใน Database
        print(f"Service A: Receiving gRPC request for ID {request.user_id}")
        return user_pb2.UserResponse(
            name="ชนาธิป สร้อยจิตร",
            email=f"user_{request.user_id}@university.ac.th"
        )

def serve():
    # ตั้งค่า Server ให้ทำงานที่ Port 50051
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserServiceHandler(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC Server started on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()