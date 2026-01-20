import grpc
import proto.user_pb2 as user_pb2
import proto.user_pb2_grpc as user_pb2_grpc

def get_user_data_from_a(user_id):
    # เชื่อมต่อไปยัง Service A (ชื่อ Host คือ service_a ตาม docker-compose)
    with grpc.insecure_channel('service_a:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        # ส่ง Request ไปที่ Service A
        response = stub.GetUserDetail(user_pb2.UserRequest(user_id=user_id))
        return {"name": response.name, "email": response.email}