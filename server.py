from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print'The server is ready to receive'

MULTIPLICATION = 1
DIVISION = 2
ADDITION = 3
SUBTRACTION = 4
MODULUS = 5

def calc(message):
	message = message.split(",")

	operator = int(message[0])
	operand1 = int(message[1])
	operand2 = int(message[2])

	if operator == MULTIPLICATION:
		return operand1 * operand2
	elif operator == DIVISION:
		return operand1 / operand2
	elif operator == ADDITION:
		return operand1 + operand2
	elif operator == SUBTRACTION:
		return operand1 - operand2
	elif operator == MODULUS:
		return operand1 % operand2

while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	result = str(calc(message))
	serverSocket.sendto(result, clientAddress)
