a="file1,file2,file3"
c=a.split(",")
r=",".join("'"+i+"'"for i in c)
print(r)
