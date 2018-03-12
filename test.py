
##import example_cy

##example_cy.test(5)
import timeit


# called a timing class that will store the time it took o fininsh runnign after reading the import statements of each program 
cy = timeit.timeit('example_cy.test(10000)', setup = 'import example_cy', number = 100)

py = timeit.timeit('pythonExample.test(10000)', setup = 'import pythonExample', number = 100)

# print 
print(cy , py )
print('cython is running at the a {}x faster rate'.format(py/cy) )