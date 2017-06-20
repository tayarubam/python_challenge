#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import mmap
import contextlib
import sys


def read_file_in_onek(file, data_size=1024):
    """Function  to read a file in one kilobyte size"""

    while True:
        content = file.read(data_size)
        if not content:
            break
        yield content


def extract_ips(file_name):
    """extract ip addresses from 1K chunk data"""

    reg = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

    with open("list_of_ips.txt", "r") as f:
        with open('JustIP.txt', 'w') as output:

            for piece in read_file_in_onek(f):
                for line in piece.splitlines():
                    matches = reg.findall(line)
                    for match in matches:
                        output.write(match)
                        output.write('\n')


def find_ip(output, ip_to_lookup):
    """Find if a given ip is existing in the file"""

    with open(output, 'rb', 0) as file:
        with contextlib.closing(mmap.mmap(file.fileno(), 0,
                                access=mmap.ACCESS_READ)) as s:
            if s.find(ip_to_lookup) != -1:
                print 'Found the ip in the list'
            else:
                print 'Given ip does not exist in the list'


def main():
    """Main function for parsing the ip addresses
       Takes one command line ip address to search"""

    ip_to_lookfor = ''

    if(len(sys.argv) == 2 ):
        ip_to_lookfor.join(sys.argv[1:])

        #Exctract IP addresses from a given text file
        extract_ips("list_of_ips.txt")

        #Finds the given Ip address from list of IPs
        #find_ip('JustIP.txt', '3.173.155.119')

        find_ip('JustIP.txt', ip_to_lookfor)
    else: 
        print "Please execute extract_ips.py with ip as command line argument"


if __name__ == '__main__':
    main()
