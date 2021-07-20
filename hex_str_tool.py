import sys
import binascii
from optparse import OptionParser


def encode_hex(s):
    s_to_hex=""
    for i in range(len(s)):
        # print(i)
        s_to_hex += hex(ord(s[i])).replace("0x","\\x")
    print(s_to_hex)

def hex_to_str(s):
    try:
        s=s.replace("\\x","").replace("\\","").strip()
        strs=binascii.unhexlify(s)
        print(strs.decode('utf-8'))
    except UnicodeDecodeError as e:
        print(strs)

if __name__ == '__main__':
    if (len(sys.argv)) < 2:
        print('useage : python' + str(sys.argv[0]) + ' -h')
    else:
        usage = ("filename.py -e [--encode] str"
                 "filename.py -d [--decode] hex_str")
        parser = OptionParser(usage=usage)  #对象实体化
        parser.description = 'JS16进制<——>字符串互转小工具'
        parser.add_option('-e','--encode',dest='encode',type=str,help="filename.py -e [--encode] str")
        parser.add_option('-d','--decode',dest='decode',type=str,help="strfilename.py -d [--decode] hex_str")
        (option,args) =parser.parse_args()  # 把值传递给options
        encode = option.encode
        decode = option.decode
        if option.encode:
            encode_hex(option.encode)
        elif option.decode:
            hex_to_str(option.decode)

