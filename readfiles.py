from sys import argv 

script, filename = argv 

txt = open(filename)

print "%r" % filename 

print txt.read()

print "type the file name agian"

file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read() 
