from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that hit CTRL-C (^C)."
print "If you don't want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w+') # W+ automatically truncates the file, type 'r' to read the file and
							# 'a' to append the file

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

target.write("%r\n%r\n%r" % (line1, line2, line3))


print "And finally, we close it."
target.close()