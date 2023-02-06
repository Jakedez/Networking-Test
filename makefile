


SOURCES = $(wildcard *.c)
# Specify the target executable
TARGET = networking.exe

# List the object files that make up the target
OBJS = 

# Specify the compiler and flags
CC = gcc
CFLAGS = -Wall -O2

# Define the default target
$(TARGET): $(OBJS)
	$(CC) $(SOURCES) $(CFLAGS) -o $(TARGET) -lws2_32

# Define the pattern for creating object files from source files
%.o: %.c
	$(CC) $(CFLAGS) -c $<

# Define a clean target to remove object files and the target
.PHONY: clean
clean:
	rm -f $(OBJS) $(TARGET)