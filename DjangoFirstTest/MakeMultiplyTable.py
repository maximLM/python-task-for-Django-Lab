out = open("output.html", "w")

out.write('<table style="width:100%">\n')

for i in range(1,10):
    out.write('<tr>\n')
    for j in range(1,10):
        out.write('<td>' + str(j) + ' * ' + str(i) + ' = ' + str(i * j) + ' </td> \n')
    out.write('</tr>\n')

out.write('</table>')