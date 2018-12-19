import socket

print('-' * 70)

# Create the socket object
obj = socket.socket()

# Connect to the server
obj.connect(('127.0.0.1', 6001))

# Start sending the request
while True:
    req = input('Request -> ')

    if not req:
        break

    obj.send(req.encode())

    # Receive the response
    resp = obj.recv(1024).decode()
    print('Server Says ->', resp)

# Close the socket
obj.close()

print('-' * 70)
