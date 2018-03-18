import grpc
from concurrent import futures
import time

# import the generated classes
import chatbot_pb2
import chatbot_pb2_grpc

# import the original calculator.py
import chatbot_logic

# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class ChatbotServicer(chatbot_pb2_grpc.ChatbotServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.Number
    def Sendmessage(self, request, context):
        response = chatbot_pb2.Message()
        response.name = chatbot_logic.message_to_send(request.name)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
chatbot_pb2_grpc.add_ChatbotServicer_to_server(
        ChatbotServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
