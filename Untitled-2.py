

print('\n')
file_object = open('HoaDon_0106053900__0002867.xml', encoding= 'utf-8-sig')
data1 = str(file_object.read()).index('<Ten>')
#print(data1,'\n')
file_object = open('HoaDon_0106053900__0002867.xml', encoding= 'utf-8-sig')
data2 = str(file_object.read()).index('</Ten>')
#print(data2,'\n')
file_object = open('HoaDon_0106053900__0002867.xml', encoding= 'utf-8-sig')
data3 = file_object.read(data1+5)
data4 = file_object.read(data2-data1-5)
print(data4.replace("&amp;","&"), '\n')

file_object = open('HoaDon_0106053900__0002867.xml', encoding= 'utf-8-sig')
data1 = str(file_object.read()).index('<MST>')
#print(data1,'\n')
file_object = open('HoaDon_0106053900__0002867.xml', encoding= 'utf-8-sig')
data2 = str(file_object.read()).index('</MST>')
#print(data2,'\n')
file_object = open('HoaDon_0106053900__0002867.xml', encoding= 'utf-8-sig')
data3 = file_object.read(data1+5)
data4 = file_object.read(data2-data1-5)
print(data4, '\n')


file_object = open('HoaDon_0106053900__0002867.xml', encoding= 'utf-8-sig')
data1 = str(file_object.read()).index('<DChi>')
#print(data1,'\n')
file_object = open('HoaDon_0106053900__0002867.xml', encoding= 'utf-8-sig')
data2 = str(file_object.read()).index('</DChi>')
#print(data2,'\n')
file_object = open('HoaDon_0106053900__0002867.xml', encoding= 'utf-8-sig')
data3 = file_object.read(data1+6)
data4 = file_object.read(data2-data1-6)
print(data4, '\n')


print(type(data4), '\n')
