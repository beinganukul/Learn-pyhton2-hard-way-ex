from sys import argv #importing packages from python library and calling modules to enable argument variable

script,filename=argv #opening up argument package

txt=open(filename) #opens text file

print "Here's your file %r" %filename #shows text file name in first sentence

print txt.read()
print "Type the filename again:"
file_again =raw_input(">")
txt_again=open(file_again)
print txt_again.read()