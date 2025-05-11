import grpc
from concurrent import futures
import hello_pb2
import hello_pb2_grpc
import threading

class HelloServicer(hello_pb2_grpc.HelloServiceServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloResponse(message=f"Xin chào, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServiceServicer_to_server(HelloServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Server is starting...")
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

def run():
    # Kết nối đến server ở cổng 50051
    channel = grpc.insecure_channel('localhost:50051')
    stub = hello_pb2_grpc.HelloServiceStub(channel)

    # Tạo request
    request = hello_pb2.HelloRequest(name="World")

    # Gửi request và nhận response
    response = stub.SayHello(request)
    print("Response received: ", response.message)

if __name__ == "__main__":
    server_thread = threading.Thread(target=serve)
    server_thread.start()

    run()
