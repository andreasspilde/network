from socket import *


serverName2 = "localhost"
serverPort2 = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = "input lower case sentence: \n"
clientSocket.sendto(message.encode(), (serverName2, serverPort2))
modifiedMessage, serverAdress = clientSocket.recvfrom(2084)
templist = modifiedMessage.decode()
modifiedMessage2, serverAdress = clientSocket.recvfrom(2084)
templist2 = modifiedMessage2.decode()
modifiedMessage3, serverAdress = clientSocket.recvfrom(2084)
regnlist = modifiedMessage3.decode()
modifiedMessage4, serverAdress = clientSocket.recvfrom(2084)
regnlist2 = modifiedMessage4.decode()
clientSocket.close()

print(templist)
print(templist2)
print(regnlist)
print(regnlist2)



if(templist[0] == "b"):
    with open("bergenTemp.txt", "a") as myfile:
        myfile.write(templist)
if(templist2[0] == "b"):
    with open("bergenTemp.txt", "a") as myfile:
        myfile.write(templist2)
if(templist2[0] == "o"):
    with open("osloTemp.txt", "a") as myfile:
        myfile.write(templist2)
if(regnlist[0] == "p"):
    with open("osloPrecipitation.txt", "a") as myfile:
        myfile.write(regnlist) 
if(regnlist2[0] == "p"):
    with open("osloPrecipitation.txt", "a") as myfile:
        myfile.write(regnlist2)  
if(regnlist[0] == "r"):
    with open("bergenPrecipitation.txt", "a") as myfile:
        myfile.write(regnlist)   
if(regnlist2[0] == "r"):
    with open("bergenPrecipitation.txt", "a") as myfile:
        myfile.write(regnlist2)
     
else:
    with open("osloTemp.txt", "a") as myfile:
        myfile.write(templist)
#^UDP client,    below tcp server

serverName = "localhost"
serverport = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverport))
serverSocket.listen(1)

while True:
    connectionSocket, clientAdr = serverSocket.accept()
    message = connectionSocket.recv(2084)
    if (message.decode() == "b"):
        f = open("bergenTemp.txt", "r")
        new_message = f.read()[1:]
        connectionSocket.send(new_message.encode())
        connectionSocket.close()
    if (message.decode() == "o"):
        f = open("osloTemp.txt", "r")
        new_message = f.read()[1:]
        connectionSocket.send(new_message.encode())
        connectionSocket.close()
    if (message.decode() == "p"):
        f = open("osloPrecipitation.txt", "r")
        new_message = f.read()[1:]
        connectionSocket.send(new_message.encode())
        connectionSocket.close()
    if (message.decode() == "r"):
        f = open("bergenPrecipitation.txt", "r")
        new_message = f.read()[1:]
        connectionSocket.send(new_message.encode())
        connectionSocket.close()    
    
