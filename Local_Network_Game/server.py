import socket
import _thread
import sys

def main():    
    server = "192.168.1.114"
    port = 5555

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.bind((server, port))
    except socket.error as e:
        print(str(e))

    sock.listen(2)
    print("Waiting for a connection...server started.")

    while True:
        connection, address = sock.accept()
        print(f"Connected to: {address}")

        _thread.start_new_thread(threaded_client, (connection,))


def threaded_client(connection):
    connection.send(str.encode("Connected!"))
    reply = ""

    while True:
        try:
            data = connection.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                print("Disconnected...")
                break
            else:
                print(f"Received: {reply}")
                print(f"Sending: {reply}")

            connection.sendall(str.encode(reply))
        except:
            print("Something bad happened...")
            break

    print("Lost connection...")
    connection.close()


if __name__ == "__main__":
    main()