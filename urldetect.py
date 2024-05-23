from __future__ import print_function
from platform import python_version
from sys import exit, argv

version = python_version().startswith('2', 0, len(python_version()))
if version:
    print('Are you using python version {}\n'
          'Please, use version 3.X of python'.format(python_version()))
    exit(1)

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from textwrap import dedent
from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, gaierror

white, red, yellow, green, END = '\33[;97m', '\33[1;91m', '\33[1;93m', '\33[1;32m', '\33[0m'


def banner():
    '''
    Show banner of tool checkURL
    :return: banner
    '''

 
    return msg.format(green,END,red,white)









# main fn

def main():

    '''
    Main
    :return: execution of the program 
    '''
    args = parse_args()[0]
    parse = parse_args()[1]

    if len(argv) < 2:
        parse.print_help()
        exit(1)

    print(banner())

    if args.url: print(check_EVIL(args.url))
    if args.url and args.check_url: print(check_url(args.url))
    if args.url_list and not args.check_url: urls_list(args.url_list)
    if args.url_list and args.check_url: print(check_list_url(args.url_list))

if __name__ == '__main__':
    try: main()
    except KeyboardInterrupt: exit()
    except SystemExit: pass









