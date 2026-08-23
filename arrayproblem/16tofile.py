from array import array
arr=array('i',[10,20,30])
f=open("data.bin","wb")
arr.tofile(f)
f.close()
print("Data written to file")