# Reverse Each String

# “Cat”, return “taC”
# “The Daily Byte”, return "etyB yliaD ehT”


def reverse_each_string(str):

    output=[]

    str_split=str.split()

    for s in str_split:
        output.append(s[::-1])

    return " ".join(output[::-1])

inputs=["The Daily Byte","Cat"]
outputs=["etyB yliaD ehT","taC"]

for i in range(len(inputs)):
    assert outputs[i] == reverse_each_string(inputs[i])
    print(outputs[i], reverse_each_string(inputs[i]))




