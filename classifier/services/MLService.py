from grpc import aio
from protos import MLService_pb2
from protos import MLService_pb2_grpc
from ML import TelecomClassifier

class MLService(MLService_pb2_grpc.MLServiceServicer):
    def classify(self, request, context):
        # result = ToxicClassifier.classify(request.text)
        result = TelecomClassifier.pipeline(request.text)
        print(result)
        return MLService_pb2.MLResponse(text=request.text, label=result['label'], score=result['score'])

async def run():
    server = aio.server()
    MLService_pb2_grpc.add_MLServiceServicer_to_server(MLService(), server)
    address = "127.0.0.1:50051"
    server.add_insecure_port(address)
    await server.start()
    await server.wait_for_termination()