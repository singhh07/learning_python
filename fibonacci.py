
#number = int(input('How many Fibonacci number you want? '))

#def fibb_list():
#    i = 1
#   if number == 0:
#        fib = []
#    elif number == 1:
#        fib = [1]
#    elif number == 2:
#        fib = [1,1]
#    elif number > 2:
#        fib = [1,1]
#        while i < (number -1):
#            fib.append(fib[i] + fib[i-1])
#            i += 1
#    return fib

#x = fibb_list()

#print(x)


#arr = [0, 2 ,8, 5, 2, 1, 5, 13, 23]
#subset = []

#def is_fibno(num):
 #   global test
  #  count = 1
# if num == 0:
#        return False
#    elif num == 1:
#        return True
#    test = [1,1]
#    while count < (num - 1):
#        test.append(test[count] + test[count -1])
#        count += 1
#        if num in test:
#            return True

#for i in arr:
#    if is_fibno(i):
#        subset.append(i)

#print(subset)                    


# python3 program to find largest Fibonacci subset 
   
# Prints largest subset of an array whose 
# all elements are fibonacci numbers 
#arr = [4, 2, 8, 5, 20, 1, 40, 13, 23]
def findFibSubset(arr, n): 
  
    # Find maximum element in arr[] 
    m= max(arr) 
   
    # Generate all Fibonacci numbers till 
    # max and store them in hash. 
    a = 0
    b = 1
    hash = [] 
    hash.append(a) 
    hash.append(b) 
    while (b < m): 
      
        c = a + b 
        a = b 
        b = c 
        hash.append(b) 
    
    # Npw iterate through all numbers and 
    # quickly check for Fibonacci using 
    # hash. 
    for i in range (n): 
        if arr[i] in hash : 
            print( arr[i],end=" ") 
   
# Driver code 
if __name__ == "__main__": 
    
    arr = [4, 2, 8, 5, 20, 1, 40, 13, 23] 
    n = len(arr) 
    findFibSubset(arr, n)
    

    