'''

jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0


'''


def jewels_and_stones(jewels,stones):

    jewel_set=set(jewels)
    cnt=0
    for s in stones:
        if s in jewel_set:
            cnt+=1
    return cnt

#test
inputs=[["abc","ac"], ["Af", "AaadfFf"], ["AYOPD", "ayopd"],["AYOPD", ""],["", "ayopd"]]
outputs=[2,3,0,0,0]

for i in range(len(inputs)):
    print(outputs[i], jewels_and_stones(inputs[i][0], inputs[i][1]))
