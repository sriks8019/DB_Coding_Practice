'''

For each array element, find the product of all array elements except self
Note: Do it without using division operator
'''

def product_except_self(l):
    N=len(l)
    output=[1]*N

    left=[1]*N
    right=[1]*N
    for i in range(1,N):
        left[i]=left[i-1]*l[i-1]

    for j in range(N-2,-1,-1):
        right[j]=right[j+1]*l[j+1]

    for k in range(N):
        output[k]=left[k]*right[k]
    return output

def product_except_self_v2(l):
    N=len(l)
    output=[1]*N

    left=[1]*N
    right=1
    for i in range(1,N):
        left[i]=left[i-1]*l[i-1]

    for j in range(N-1,-1,-1):
        output[j] = left[j] * right
        right = right * l[j]


    return output
#test cases
input=[5,6,3,2,10,4]
output=[1440,1200,2400, 3600, 720, 1800]

print(output, product_except_self(input))
print(output==product_except_self(input))

print(output, product_except_self_v2(input))
print(output==product_except_self_v2(input))