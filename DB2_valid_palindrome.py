'''

"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true

'''
def valid_palindrome(str):

    alphabets=set('abcdefghijklmnopqrstuvwxyz')
    temp=[]
    for c in str:
        if c.lower() in alphabets:
            temp.append(c.lower())

    temp="".join(temp)
    #print(temp)
    return temp==temp[::-1]

def valid_palindrome_v2(str):

    alphabets=set('abcdefghijklmnopqrstuvwxyz')
    i=0
    j=len(str)-1
    while i<j and i<len(str):

        while str[i].lower() not in alphabets:
            i+=1
        while str[j].lower() not in alphabets:
            j-=1

        if str[i].lower()==str[j].lower():
            i+=1
            j-=1
        else:
            return False


    #print(temp)
    return True

#Tests
inputs = ["level", "algorithm", "A man, a plan, a canal: Panama."]
outputs = [True, False,True]

for i in range(len(inputs)):
    ##assert outputs[i] == valid_palindrome(inputs[i])
    print(outputs[i], valid_palindrome_v2(inputs[i]))