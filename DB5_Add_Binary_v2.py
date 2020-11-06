'''

"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"


'''

def add_binary(a,b):

   i=len(a)-1
   j=len(b)-1
   carry=0
   out=[]
   while i >=0 or j>=0:
       sum=carry

       if i>=0:
           sum+=int(a[i])
           i-=1
       if j >= 0:
           sum += int(b[j])
           j -= 1


       out.insert(0,str(sum%2))
       carry=sum//2

   if carry>0:
       out.insert(0, str(1))


   return "".join(out)






#testcases

inputs = ["1101", "1"]
output="1110"


#assert output == add_binary(inputs[0], inputs[1])
print(output, add_binary(inputs[0], inputs[1]))