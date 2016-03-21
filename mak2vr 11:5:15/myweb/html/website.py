# Matthew Keitelman (mak2vr)

# Matthew Keitelman (mak2vr)

import webbrowser


url = 'google.com'

file = open('index.html','w')
file.write('<html>\n')



title = input("Please add title: ").upper()

file.write("<head><title>"+title+"</title></head>\n")

line1 = '<body><marquee scrollamount = "25"><font size = 20><h2>' + input("Line 1: ").upper() + '<br></h2></font></marquee></body>\n'
line2 = '<body><font size = 15><h2>' + input("Line 2: ") + '<br></h2></font></body>\n'
line3 = '<body><font size = 10><h2>' + input("Line 3: ") + '</h2></font></body>\n'
file.write(line1+line2+line3)



# webbrowser.open_new('http://www.google.com')

file.write('</html>')
file.close()
webbrowser.open('file:///users/matthewkeitelman/PycharmProjects/other/poop.html')