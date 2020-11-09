'''

Get the index of the first non-repeating character

'''

def first_unique_char(s):

    s_lookup={}

    for c in s:
        if c not in s_lookup:
            s_lookup[c]=1
        else:
            s_lookup[c]+=1

    for k in s_lookup:
        if s_lookup[k]==1:
            return str(s).index(k)

    return -1

## test cases
inputs=['abbacffee','plant','maam', 'belle','allay']
outputs=[4,0,-1,0, 4]
for i, input in enumerate(inputs):
    print(outputs[i], first_unique_char(input))