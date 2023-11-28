import hashlib
import socket  # used to establish the connection between client and server
import sqlite3
import threading  # two things happening at once

# Create a socket object
try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # internet socket, connection oriented protocol (TCP)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

# Define the server address and port
server_binding = ("localhost", 9999)
# Bind the socket to the server address
ss.bind(server_binding)
# Listen for incoming connections
ss.listen()

# Connect to database
def connect_db():
    conn = sqlite3.connect('a.db')
    return conn

def authenticate(username, password):
    conn = connect_db
    cursor = conn.cursor
    # Execute a query to check if the username and password match
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    conn.close()

    return user is not None

def start_connection(c): # taking client as parameter
    '''
    msg = "Welcome to Blueprint squad!"
    c.send(msg.encode())
    """ reponse = "THANK YOU!"
                    "no." "im sleepy"
                    variable. --> we need something to pull the client's response.
    """
    '''

    response = c.recv(1024).decode() # 1024 bytes tells us the size / buffer of the content we are recieving so that the socket knows how much to expect
    print("[S]: Data received from client: " + response)    

    '''
    msg = "How are you?" # make own riddle / joke & respond with answer
    c.send(msg.encode())
    '''

    # Receive from client format
    '''
    response = c.recv(1024).decode()
    print("[S]: Data received from client: " + response)    
    '''
    
    # Receive username and password from the client
    c_username = c.recv(1024).decode()
    c_password = c.recv(1024).decode()

    # Validate the user credentials
    if authenticate(username, password):
        # c.send(b"Login successful!")
        print("Login successful!")
    else:
        #c.send(b"Invalid username or password")
        print("Invalid username or password!")

    '''
    count = 0
    while(count < 5): # use loop to send 1, 2, 3, 4, 5 to client
        c.send(str(count).encode())
        response = c.recv(1024).decode()
        print("[S]: Data received from client: " + response)
        count+-1

    print("Done")
    '''



while True:
    # Accept incoming connection
    client, addr = ss.accept()

    t2 = threading.Thread(target=start_connection, args=(client,))
    t2.start()

    # Close the server socket
    ss.close()
    exit()