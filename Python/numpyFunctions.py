from numpy import *
m1 = matrix ('1 2 3; 3 6 5; 4 5 10')
m2 = matrix ('1 4 3; 3 7 5; 8 5 10')
print ("m1: ", m1, "\n")
print ("m2: ", m2, "\n")
print ("diagonal(m1): ", diagonal(m1))
print ("m1.min(): ", m1.min())
print ("m1.max(): ", m1.max())
m3 = m1+m2
print ("m3: \n", m3)
print ("m1.dtype", m1.dtype)
print ("m1.ndim: ", m1.ndim)
print ("m1.shape: ", m1.shape)
print ("m1.size: ", m1.size)
m4 = m1.flatten()
print ("m1 flattened: ", m4)
arr3 = m4.reshape(3,3)
print ("m4.reshape: \n", arr3)

