'''

"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"


'''

def add_binary(a,b):
    def add_bits(a, b, carry):
        s=""
        if a =='1' and b=='1':
            s+="0" if carry=="0" else "1"
            carry="1"

        elif a=='1' or b=='1':
            if carry=="0":
                s+="1"
            else:
                s+="0"
                carry="1"
        else:
            s += "0" if carry == "0" else "1"
            carry = "0"
        return s, carry
    l=min(len(a), len(b))
    i=l-1
    carry="0"
    s=""
    a=a[::-1]
    b=b[::-1]
    while i >=0:
        bit_sum, carry=add_bits(a[i], b[i], carry)
        s+=bit_sum
        i-=1
    print(s)
    s2=""
    if len(a)!=len(b):
        if l==len(a):

            for i in range(l,len(b)):
                bit_sum, carry= add_bits("0", b[i], carry)
                s2+=bit_sum
        elif l==len(b):

            for i in range(l,len(a)):
                bit_sum, carry= add_bits("0", a[i], carry)
            s2+=bit_sum


    if carry=="1":
        s2+="1"
    s+=s2
    return s[::-1]







#testcases

inputs = ["101", " 1"]
output="110"


#assert output == add_binary(inputs[0], inputs[1])
print(output, add_binary(inputs[0], inputs[1]))