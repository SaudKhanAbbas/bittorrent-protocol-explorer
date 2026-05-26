import socket

HOST = "127.0.0.1"
PORT = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

print(f"Connected to server at {HOST}:{PORT}")

while True:
    message = input("You: ")

    if message.lower() == "exit":
        print("Disconnecting from server...")
        break

    client_socket.send(message.encode())

client_socket.close()