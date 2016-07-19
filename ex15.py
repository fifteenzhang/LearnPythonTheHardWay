from sys import argv


print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()

#删掉 使用到 raw_input 的部分，再运行一遍脚本
#当我们用Python访问一个中文命名的文本时，经常会遇到如下错误：

#file open error: [Errno 2] No such file or directory: '\xe6\xb5\x8b\xe8\xaf\x95.txt'
#这是由于python默认的编码格式为unicode。
#因此我们需要将GBK格式的‘测试’解码为“UTF-8”，如下：
# coding: UTF-8
#from sys import argv
#print "Type the filename again:"
#try:
#    txt_again = open('让.txt'.decode('UTF-8'))
#except IOError,e:
#    print "file open error:",e
#else:
#    print txt_again.read()
#txt_again.close()
