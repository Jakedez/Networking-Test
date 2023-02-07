import socket

PORT: int = 8090
HOST = socket.gethostname()

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
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    client, address = server.accept()
    print("Connection Established!\n\n")
    connected: bool = True
    while connected:
        try:
            data = input("Type something to send: ")
            client.send(data)
        except (BrokenPipeError, ConnectionResetError):
            connected = False

def runClient():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    connected: bool = True
    while connected:
        try:
            data = client.recv(2048)
            print(data.decode())
        except (BrokenPipeError, ConnectionResetError):
            connected = False
    pass


if __name__ == "__main__":
    main()
