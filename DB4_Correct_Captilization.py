'''

"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true


'''


def correct_capitalization(str):

    if str.isupper():
        return True
    elif str.islower():
        return True
    elif str[0].isupper() and str[1:].islower():
        return True

    return False

#testcases

inputs = ["USA", "Calvin", "compUter", "level"]
outputs = [True, True, False, True]

for i in range(len(inputs)):
    assert outputs[i] == correct_capitalization(inputs[i])
    print(outputs[i], correct_capitalization(inputs[i]))