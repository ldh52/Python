import numpy

array1 = numpy.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
print(array1)
[ 2  3  5  7 11 13 17 19 23 29 31]
    
array1 = numpy.full(6, 7)
print(array1)
[7 7 7 7 7 7]
    
array1 = numpy.full(6, 0)
array2 = numpy.zeros(6, dtype=int)
    
print(array1)
print()
print(array2)
[0 0 0 0 0 0]
    
[0 0 0 0 0 0]
    
array1 = numpy.full(6, 1)
array2 = numpy.ones(6, dtype=int)
    
print(array1)
print()
print(array2)
[1 1 1 1 1 1]
    
[1 1 1 1 1 1]
    
array1 = numpy.random.random(6)
array2 = numpy.random.random(6)
    
print(array1)
print()
print(array2)
[0.60341438 0.57950098 0.68500432 0.18012413 0.88013734 0.3860552 ]
    
[0.06129336 0.47263043 0.14601803 0.18543333 0.17457547 0.57746894]
    
python
array1 = numpy.arange(6)
print(array1)
[0 1 2 3 4 5]
    
python
array1 = numpy.arange(2, 7)
print(array1)
[2 3 4 5 6]
    
python
array1 = numpy.arange(3, 17, 3)
print(array1)
[ 3  6  9 12 15]
