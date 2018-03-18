import grpc

# import the generated classes
import chatbot_pb2
import chatbot_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = chatbot_pb2_grpc.ChatbotStub(channel)


while True:

    # create a valid request message
    client_message = chatbot_pb2.Message(name= input("Enter your message: "))
    print("\n")

    # make the call
    response = stub.Sendmessage(client_message)

    # et voilà
    print(response.name)
    print("\n")
    print("###################################################################")
