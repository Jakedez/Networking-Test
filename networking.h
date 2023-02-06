#ifndef NETWORKING_H_
#define NETWORKING_H_

#include <sys/types.h>

#include <winsock2.h>
#include <WS2tcpip.h>

#define SERVER_PORT 80

#define MAXLINE 4096

#define SA struct sockaddr

typedef struct sockaddr_in SocketAddress;

void initP2P(char * ipAddress){
    WSADATA wsaData;
    SOCKET socket_desc;
    SocketAddress server;
    int iResult;
    
    // Initialize Winsock
    iResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (iResult){
        printf("WSA Initialization failed, with error code: %d", iResult);
        exit(EXIT_FAILURE);
    }

    // Create Socket
    socket_desc = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (socket_desc == INVALID_SOCKET){
        printf("Socket Initialization failed, with error code: %d", WSAGetLastError());
        WSACleanup();
        exit(EXIT_FAILURE);
    }

    server.sin_addr.s_addr = inet_addr(ipAddress);
    server.sin_family = AF_INET;
    server.sin_port = htons(8888);

     if (connect(socket_desc, (struct sockaddr *)&server, sizeof(server)) < 0)
    {
        printf("connection error");
        exit(EXIT_FAILURE);
    }

    puts("Connected!!");

    return;
}


#endif