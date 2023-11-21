import socket
import time

time. sleep(1)
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65430  # The port used by the server

# ------------- SQL commands -------------
#SELECT TOP 3 * FROM Customers;


#data= "SELECT FROM *books WHERE BookTitle LIKE ‘example_book"
data = "SELECT * FROM users"
byte_data = bytes(data, 'utf-8')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))
    print(f"Sending sql query: {data}")
    # uses .sendall to send the message to the server
    s.sendall(byte_data)

    data = s.recv(1024)
print("----------------------------------------------------------------------------------------------------------")
print(f"|Received the following book data back: {data!r} |")
