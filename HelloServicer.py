import grpc
from concurrent import futures
import service_pb2
import service_pb2_grpc

class HelloServicer(service_pb2_grpc.HelloServiceServicer):
    def SayHello(self, request, context):
        return service_pb2.HelloResponse(message=f"Xin chào, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_HelloServiceServicer_to_server(HelloServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
