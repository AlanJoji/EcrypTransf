# File Transfer Application
Computer Networks Project Application

> The project is not running using a concurrent server.

The application will allow for transfer of data:
- From the client to the server(server here will act like a file backup, can be external to the users folder)
- ~~The current program can handle only 1 client at a time. First the first client is served then the next client will be served - **One at a Time**.~~
The current version is capable of handling multiple client connections to the server. But the connections are not multithreded, there is a single TCP welcoming socket and an individual connection socket created (and closed) for each client communication.
To make this work with multiple clients at the same time - ***multi-threaded application using socket***.
- The program supports sending a file from a client folder to a server folder, the user will have to change these folders to transfer files.
- The program encrypts the files in transit using AES in Block Cipher Mode with a 128-bit key for encryption during transit using symmetric key encryption facilitated by the Fernet library.
- The files to be sent are located from the file system using os module


## Languages

Python

## Libraries

1. ```socket```
2. ```fernet```
3. ```os```

## Features

- **Encryption during transit**
- **File transfer from client to server**
- **Support for multiple clients**
- Can be used to backup onto a different folder on another device in LAN 
> Will not work if there is a firewall
- **Support for a wide variety of file types - txt, script**

## Dependencies
Cryptography module needs to be installed, other modules are built-in
```shell
pip install cryptography
```

## Execution 

Clone the repository using
```shell
git clone https://github.com/AlanJoji/EcrypTransf.git
```

And enter the working directory
```shell
cd EcrypTransf
```

A server terminal for running the server side to receive the file(s)
```bash
python server.py
```

A client terminal for running the client side to send the file(s)
```bash
python client.py
```

## Future developments
- [ ] File backup system
- [ ] Multi-threading socket creation
