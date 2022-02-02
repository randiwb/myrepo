filename=input("What is the title of document = ")
f = open(filename+".svg", "w")

#ask for details
print("We will now make your .svg file. Please input details as below\n")
w=int(input("Enter desired width = "))
h=int(input("Enter desired height = "))
name=str(input("What text do you want for the square = "))

f.write('<?xml version="1.0" encoding="UTF-8" ?>\n'
'<svg xmlns="http://www.w3.org/2000/svg" version="1.1">\n'
'\t<rect x="25" y="25" width="%i" height="%i" fill="lime" stroke-width="4" stroke="pink" />\n' % (w, h))

f.write('\t<text x="%i" y="%i" fill="black">%s </text>\n' % (25+50, h-10, name))
f.write('</svg>\n')

print("\n\nYOUR FILE IS READY! filename is = "+filename+".svg")
f.close()
