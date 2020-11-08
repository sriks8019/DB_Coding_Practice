'''

check if two strings are valid angrams of each other

'''

def valid_anagram(s,t):

    s_dict={}
    for c in s: #get char counts
        if c not in s_dict:
            s_dict[c]=1
        else:
            s_dict[c]+=1

    print(s_dict)
    for d in t:
        if d not in s_dict:
            return False
        else:
            s_dict[d]-=1
    print(s_dict)
    return all([ v==0 for v in s_dict.values()])
#test cases
inputs=[['anna', 'naan'], ['bird', 'drib'],['bulb', 'bub'],['laura', 'laurel']]
outputs=[True,True, False, False]

for i, input in enumerate(inputs):
    print(outputs[i], valid_anagram(input[0], input[1]))
