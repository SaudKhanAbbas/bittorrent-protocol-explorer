import socket
import threading

HOST = "127.0.0.1"
PORT = 555


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)

            if not message:
                break

            print(f"\n{message.decode()}")

        except:
            break


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

print(f"Connected to server at {HOST}:{PORT}")

receive_thread = threading.Thread(
    target=receive_messages,
    args=(client_socket,)
)

receive_thread.start()

while True:
    message = input("You: ")

    if message.lower() == "exit":
        break

    client_socket.send(message.encode())

client_socket.close()
