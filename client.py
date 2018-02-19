from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = []

operator = raw_input('''What operation do want to perform:
						1 for MULTIPLICATION
						2 for DIVISION
						3 for ADDITION
						4 for SUBTRACTION
						5  for MODULUS ___> ''')
message.append(operator)

operand1 = raw_input('enter the first operand: ')
message.append(operand1)

operand2 = raw_input('enter the second operand: ')
message.append(operand2)

message = ",".join(message)


clientSocket.sendto(message,(serverName, serverPort))
resultMessage, serverAddress = clientSocket.recvfrom(2048)
print "the answer is " + resultMessage

clientSocket.close()