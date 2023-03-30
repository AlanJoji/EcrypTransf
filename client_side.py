# # Client Side
# from socket import *
# from constants import *

# def read_file (filepath) :
#     file = open(filepath, "r")
#     data = file.read()

#     file.close()

#     return data

# def send_file (filename) :
#     IP = gethostbyname(gethostname())
#     PORT = get_server_port()
#     FORMAT = get_format()
#     SIZE = get_size()

#     # Eastablish TCP Connection
#     client = socket(AF_INET, SOCK_STREAM)

#     ADDR = get_server_addr(IP, PORT)
#     client.connect(ADDR)

#     print("Connection Established")

#     # Todo: The folder names should be changed based on the folder that the user wants
#     absolute_filepath = "Client_Data/" + filename + ".txt"
#     relative_filepath =  filename + ".txt"

#     data = read_file(absolute_filepath)
#     client.send(filename.encode(FORMAT))
    
#     recv_file_msg = client.recv(SIZE).decode(FORMAT)
#     print("From SERVER: ", recv_file_msg)

#     client.send(data.encode(FORMAT))

#     recv_data_msg = client.recv(SIZE).decode(FORMAT)
#     print("From SERVER: ", recv_data_msg)

#     print("Closing connection")
#     print("Ending Communication")
#     client.close()


from socket import *
from constants import *
from cryptography.fernet import Fernet


def encrypt_data(key, data):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data


def read_file (filepath) :
    file = open(filepath, "r")
    data = file.read()

    file.close()

    return data


def send_file (filename) :
    IP = gethostbyname(gethostname())
    PORT = get_server_port()
    FORMAT = get_format()
    SIZE = get_size()

    # Establish TCP Connection
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((IP, PORT))

    # filename = input("Enter Filename: ")
    absolute_filepath = "Client_Data/" + filename + ".txt"
    relative_filepath =  filename + ".txt"

    client.send(filename.encode(FORMAT))

    # with open(filename, "r") as f:
        # data = f.read()

    data = read_file(absolute_filepath)
    key = Fernet.generate_key()
    encrypted_data = encrypt_data(key, data)
    client.send(key)
    client.send(encrypted_data)

    response = client.recv(SIZE).decode(FORMAT)
    print(response)

    client.close()
