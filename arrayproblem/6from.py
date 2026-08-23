from array import array
arr=array('i')
arr.frombytes(array('i',[10,20,30]).tobytes())
print(arr)