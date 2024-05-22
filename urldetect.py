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












