from sys import argv

script,filename=argv

print "We're doing to erase %r."%filename
print "Tf you dont want that,hit CTRL-C (^C)."
print "If you dont want,hit RETURN."

raw_input("?")

print "Opening the file ...."
target=open(filename,"w")

print "Trunctating the file.Goodbye!!"
target.truncate()

print "Everything you type after this sentence will be saved in text file you just created."
paragraph=raw_input(">")
target.write(paragraph)

print "And finally,we close it."
target.close()
