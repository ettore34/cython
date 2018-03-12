cpdef int  test(int x):
    cpdef int  y = 0 
    cpdef int i 
    for i in range (x):
        y+= i
    return y     