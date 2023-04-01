# Swaping method
def array_rev(A,start,end):
    while start < end:
        A[start],A[end] = A[end],A[start]
        start += 1
        end -= 1
    print(A);

A=[3,5,2,7,1,8]
array_rev(A,0,5);

# Slicing
def reverse_arr(B):
    print(B[::-1])
B=[2,21,3,4,]
reverse_arr(B)

#Recursion
def array_reverse(A,start,end):
    while start >= end:
        return
    A[start],A[end] = A[end],A[start]
    start += 1
    end -= 1
    # array_reverse(A,start+1,end-1)
A = [10, 20, 30, 40, 50]
array_reverse(A, 0, 4)
print(A)






