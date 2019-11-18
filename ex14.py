from sys import argv
script,beinganukul=argv
prompt='>'
print "Hi %s,I'm the %s script." %(beinganukul,script)
print "I'd like to ask you a few questions."
print "Do you like %s?"% beinganukul
likes=raw_input(prompt)
print "Where do you live %s?"%beinganukul
lives=raw_input(prompt)
print "What kind of computer do you have?"
computer=raw_input(prompt)
print"""
Alright,so you said %r about liking me.
You live in %r.Not sure where that is.
And you have a%r computer.Nice.
""" %(likes,lives,computer)
