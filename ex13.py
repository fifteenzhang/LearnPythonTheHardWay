from sys import argv
print argv
script, first, second, third = argv

print "The script is classed:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
#需要传入参数，用的是pycharm可以在run -edit configurations-script parameters下传入参数。 
#script是命令（***.py）本身，first，second，third为三个参数
#把 argv 中的东西解包unpack，将所有的参数依次赋予左边的变量名

script, first, second= argv 
name_who = raw_input("who are you?") 
print "how do you do!", name_who 
first = raw_input() 
print "let's hang out", second 
second = raw_input() 
#将参数变得有意义，原来参数为pycharm可以在run -edit configurations-script parameters下传入的参数
#此代码将参数改变为name_who let's hang out的结果

