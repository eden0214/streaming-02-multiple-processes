# Eden Anderson 
## Streaming Data - Module 2 / Task 4

# Reuse script from process_streaming_9.py

import csv
import socket
import time
import pandas 

host = "localhost"
port = 9999
address_tuple = (host, port)

# use an enumerated type to set the address family to (IPV4) for internet
socket_family = socket.AF_INET 

# use an enumerated type to set the socket type to UDP (datagram)
socket_type = socket.SOCK_DGRAM 

# use the socket constructor to create a socket object we'll call sock
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# read from a file to get some data
input_file = open("Nebraska_A_Cities.csv", "r")

# create a csv reader for our comma delimited data
reader = csv.reader(input_file, delimiter=",")

for row in reader:
    # read a row from the file
    CITY, STNAME, ESTIMATESBASE2020, POPESTIMATE2020, POPESTIMATE2021 = row 

    # use an fstring to create a message from our data
    # notice the f before the opening quote for our string?
    fstring_message = f"[{CITY}, {STNAME}, {ESTIMATESBASE2020}, {POPESTIMATE2020}, {POPESTIMATE2021}]"
    
    # prepare a binary (1s and 0s) message to stream
    MESSAGE = fstring_message.encode()

    # use the socket sendto() method to send the message
    sock.sendto(MESSAGE, address_tuple)
    print (f"Sent: {MESSAGE} on port {port}.")

    # sleep for a few seconds
    time.sleep(3)
