from socket import *
import optparse
from threading import *


def main():
    parser = optparse.OptionParser("Usage of program: " + "-h <target Host> -p <target Ports>")
    parser.add_option("-h", dest="tgtHost", type='string', help='specify target host')
    parser.add_option("-p", dest="tgtPort", type='string', help='specify target ports seperated by commas')
    (option, args) = parser.parser_args()
    tgtHost = options.tgtHost
    tgtPort = str(options.tgrPort).split(",")
    if (tgtHost == None) | (tgtPort[0] ==  None):
        print(parser.usage)
        exit(0)
        
main()
