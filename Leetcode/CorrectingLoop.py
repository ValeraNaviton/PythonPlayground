#https://www.hackerrank.com/challenges/correctness-invariant/submissions/code/225539739

def Qsort(array, low, high):
    if (low < high):
        pivot = low
        i = low
        j = high
 
        while (i < j):     # Main While Loop
            while array[i] <= array[pivot] and i < high:    # While Loop "i"
                i += 1
            while array[j] > array[pivot]:                  # While Loop "j"
                j -= 1
 
            if (i < j):
                array[i], array[j] = array[j], array[i]
                 
        array[pivot], array[j] = array[j], array[pivot]
        Qsort(array, low, j - 1)
        Qsort(array, j + 1, high)
        return array
 
    else:
      return array
    
def insertion_sort(l):
    result = Qsort(l,0,len(l)-1)
    return result


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]

res = insertion_sort(ar)
output ="" 
for i in res:
    output = output + str(i) + " "
    
print(output)
