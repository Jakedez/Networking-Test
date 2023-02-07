import socket

PORT: int = 8090

def main():
    confirmed: bool = False
    while not confirmed:
        print("Please Select Host, or Client:\nA. Host\nB. Client\n\n")
        answer: str = str(input("Please select an option: ").upper())
        print("\n\n\n")
        if answer == "A":
            confirmed = True
            runHost()
        elif answer == "B":
            confirmed = True
            runClient()
        else:
            print("Please select a valid option.\n\n")
        
    return

def runHost():
    HOST = socket.gethostname()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    client, address = server.accept()
    print("Connection Established!\n\n")
    connected: bool = True
    while connected:
        try:
            data = input("Type something to send: ")
            client.send(bytes(data.encode("UTF-8")))
        except (BrokenPipeError, ConnectionResetError):
            connected = False

def runClient():
    HOST = input("please type the host IP Address: ")
    confirmed = False
    while not confirmed:
        print(HOST)
        select = input("Is this the correct IP Address? (Y/N): ").upper()
        if select == "Y":
            confirmed = True
        elif select == "N":
            HOST = input("please type the host IP Address: ")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print("Connection Established!\n\n")
    connected: bool = True
    while connected:
        try:
            data = client.recv(2048)
            print(data.decode("UTF-8"))
        except (BrokenPipeError, ConnectionResetError):
            connected = False
    pass


if __name__ == "__main__":
    main()
