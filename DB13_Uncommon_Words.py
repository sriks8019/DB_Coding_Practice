'''

sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
sentence1 = "the tortoise beat the hare", sentence2 = "the tortoise lost to the hare", return ["beat", "to", "lost"]
sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]

'''

def uncommon_words(sentence1, sentence2):

    sent1=set(sentence1.split())
    sent2= set(sentence2.split())



    return list(sent1.symmetric_difference(sent2))

def uncommon_words_v2(sentence1, sentence2):

    sent1=set(sentence1.split())
    sent2= set(sentence2.split())

    diff1=sent1.difference(sent2)
    diff2=sent2.difference(sent1)

    return list(diff1.union(diff2))

inputs=[["the quick","brown fox"],["the tortoise beat the hare","the tortoise lost to the hare"],["copper coffee pot","hot coffee pot"]]
outputs=[["the", "quick", "brown", "fox"], ["beat", "to", "lost"], ["copper", "hot"] ]

for i in range(len(inputs)):
    print("using symmetric diff")
    print(outputs[i], uncommon_words(inputs[i][0],inputs[i][1]))
    print("without symmetric diff")
    print(outputs[i], uncommon_words_v2(inputs[i][0], inputs[i][1]))