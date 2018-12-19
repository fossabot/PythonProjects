import socket

print('-' * 70)

# Create the socket object
obj = socket.socket()

# Bind IP Address with the Port
obj.bind(('127.0.0.1', 6001))

while True:
    # Listen for the connection
    obj.listen(1)

    # Receive the connection details
    conn, addr = obj.accept()
    print('Connection From -> ' + str(addr))

    # Communication between the client and server
    while True:
        req = conn.recv(1024).decode()

        # Stop the connection if there is no request
        if not req:
            break

        print('Client Says ->', req)

        # Sending the response back to the client
        resp = input('Response -> ')
        conn.send(resp.encode())

    # close the connection
    conn.close()

print('-' * 70)
