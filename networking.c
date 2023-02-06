#include <stdio.h>
#include <stdlib.h>
#include "networking.h"

int main(int argc, char ** argv){
    char * ipAddress = "2600:100e:b1c6:8607:4d3c:1420:33a2:7a76";
    initP2P(ipAddress);

 
    return EXIT_SUCCESS;
}