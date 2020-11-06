'''

Two Sum
'''

def two_sum(l,k):

    if not l:
        return l

    lookup={}

    for i in range(len(l)):
        if l[i] in lookup:
            return [lookup[l[i]], l[i]]
        if k-l[i] not in lookup: # store the difference and its corresponing element in the lookup.
            lookup[k-l[i]]=l[i]


    return []

#test
inputs=[[4,2,5,9,10,1], 19]

print([9,10], two_sum(inputs[0], inputs[1]))
print([], two_sum([], inputs[1]))