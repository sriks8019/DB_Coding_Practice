'''
Valid Palidrome with Removal
examples:
"abcba", return true
"foobof", return true (remove the first 'o', the second 'o', or 'b')
"abccab", return false

'''

def valid_palindrome_w_removal(str):

    if len(str)==0 or not str:
        return False

    if str==str[::-1]:
        return True

    i=0
    j=len(str)-1

    while i<j:

        if str[i]!=str[j]:
            temp = list(str)
            del temp[i]
            if temp==temp[::-1]:
                return True
            temp = list(str)
            del temp[j]
            if temp==temp[::-1]:
                return True
        i+=1
        j-=1

    return False
#testcases

inputs = ["abcba", "foobof", "abccab", "mladam"]
outputs = [True, True, False, True]

for i in range(len(inputs)):
    assert outputs[i] == valid_palindrome_w_removal(inputs[i])
    print(outputs[i], valid_palindrome_w_removal(inputs[i]))