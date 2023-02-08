# Overview

This is a simple networking application allowing a client to connect to a host to send messages over a Local Area Network.

For a Host, one simply needs to initialize the application, and select the "Host" option. For a Client, a user needs to select the client option, and provide the IP address of the Host, and confirm the IP address. Once both Host, and Client have been set up on the same Local Area Network, the connection should automatically establish. Once the connection is established, the host can type messages, and they will appear on the client's device.
The purpose of this software was to demonstrate and test basic networking Capabilities through python.



[Software Demo Video](https://youtu.be/ue-8KJmLoHs)

# Network Communication

This program uses a Client - Server Model by having a Host, and a Client.

This program utilizes a TCP protocol to transmit data.

Messages that are sent are sent in UTF-8 format.

# Development Environment

This program was written using primarily the Visual Studio Code Integrated Development Enviornment and Utilizing the Python Programming Language, and the "Socket" module.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Low-level Networking Interface](https://docs.python.org/3/library/socket.html)
* [Wikipedia - Network Socket](https://en.wikipedia.org/wiki/Network_socket)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Add Client to Host Messages
* Add Manual Disconnect
* Add Return to Main Menu Screen