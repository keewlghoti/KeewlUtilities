"""
The purpose of MAINTESTING.py is to ensure the operation of the other python modules while I write them

This file should not be used at any point during the operation of the code.

"""
import KeewlUtilities
from KeewlUtilities.Cli.DUMPTOCLI import printline, printline2, printline3
def main():
    printline('KeewlUtilities')
    printline2('Author', 'Keewlghoti')
    print('********************************************************************************')
    print('\n')
    printline2('Github', 'https://github.com/keewlghoti')
    print('********************************************************************************')
    print('\n')

    print('********************************************************************************')
    printline('This is the test run')
    print('********************************************************************************')
    printline2('test', 'test')
    print('********************************************************************************')
    printline2('test', 'testtest')
    print('********************************************************************************')
    printline3('test', 'test', '%')
    print('********************************************************************************')


if __name__ == '__main__':
    main()