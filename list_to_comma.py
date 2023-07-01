#!/usr/bin/env python3

__author__ = 'pkecho'
__version__ = '1.0.1'
__maintainer__ = 'pkecho'
__status__ = 'Development'

import sys


def list_to_comma(input_file):
    with open(input_file, 'r') as file: 
        urls_temp= []
        for line in file: 
            list_string = line.split()
            string_string = ''.join(list_string)
            urls_temp.append(string_string)
        urls_string = ','.join(urls_temp)
        with open(input_file + '__list_to_comma.txt', 'w') as filee:
            filee.write(urls_string)

def main():
    list_to_comma(str(sys.argv[1]))

if __name__ == '__main__':
    main()
