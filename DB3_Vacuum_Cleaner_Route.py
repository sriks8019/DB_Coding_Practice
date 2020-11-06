'''

"LR", return true
"URURD", return false
"RUULLDRD", return true


'''

def vacuum_cleaner(str):
    origin=[0,0]
    final=[0,0]

    for d in str:

        if d=='L':
            final[0]-=1
        elif d=='R':
            final[0]+=1
        elif d=='U':
            final[1]+=1
        else:
            final[1]-=1




    return final==origin

inputs = ["LR", "URURD", "RUULLDRD"]
outputs = [True, False, True]

for i in range(len(inputs)):
    assert outputs[i] == vacuum_cleaner(inputs[i])
    print(outputs[i], vacuum_cleaner(inputs[i]))