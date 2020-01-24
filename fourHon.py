# ? IP [Block using iptc module to add in iptables] ?

#hoenypot
import sys
import argparse
from socket import socket, AF_INET, SOCK_STREAM
import iptc
VERSION = '0.1a'
welcome = b"Ubuntu 18.04.1 LTS\nserver login: "

def send_email(src_address):
    """ Todo: send an email if we're scanned / probed on this port """
    pass

def honeypot(address,port):
    """ create a single Threaded telnet listen port """
    print("i'm in honeypot")
    
    ski=socket(AF_INET,SOCK_STREAM)
    ski.bind((address, port))
    ski.listen(2)
    conn,addr = ski.accept()

    if(conn):
        print('honeypot has been visited by ' + addr[0])
        send_email(addr[0])
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
        rule = iptc.Rule()
        rule.in_interface = "lo"
        rule.src = addr[0]
        target = iptc.Target(rule, "DROP")
        rule.target = target
        chain.insert_rule(rule)
        
    
if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='honeypot prototype',
    #                              epilog='Version: ' + str(VERSION))
    # parser.add_argument('-a','--address',help='server ip address to use',action='store', required=True)   
    # args = parser.parse_args()
    inp = input("IP: ")
    port = int(input("Enter the port : "))
    honeypot(inp, port)
