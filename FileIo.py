


fd=open("Demo.txt",'r')

print("Information about file:",fd)

print("contents of whole file")
print(fd.read())

fd.seek(0)


print("Reading single line")
print(fd.readline())

print("Current file posotion",fd.tell())



fd=open("Demo.txt",'a')

fd.write("Hello world")
fd.writelines("my name is onakr ople i have done bachelors in engineeering from computer science stream with 8.35 CGPA in yaer 2021")

fd=open("Demo.txt",'r')

print(fd.read())



fd.seek(0)


fd.close()
