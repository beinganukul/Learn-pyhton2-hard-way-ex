from sys import argv

script,filename=argv
txt=open(filename)
print "This is the file you want to read %r" %filename
print "If yes them hit SHIFT+K"
raw_input("O")
print txt.read()

