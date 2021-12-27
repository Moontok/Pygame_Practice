import socket


def main():
    host = '192.168.1.239'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    print('Received', repr(data))


if __name__ == '__main__':
    main()