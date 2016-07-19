from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
#%r打印时能够重现它所代表的对象,We're going to erase 'hello.txt'.

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate() #truncate – 清空文件

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
#法1
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
#法2
target.write(("%s %s %s %s %s %s") %(line1, "\n", line2, "\n", line3, "\n"))
#法3
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
