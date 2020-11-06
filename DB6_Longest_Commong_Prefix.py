'''

Idenitfy the longest common prefix from a bunch of strings
'''

def longest_common_prefix(inputs):

    if not inputs:
        return None


    common_prefix=inputs[0] ## assume common prefix is the first string

    for s in range(1, len(inputs)):

        if s==common_prefix: #if new string is same as the prefix, prefix remains unchanged
            continue

        l=min(len(common_prefix),len(inputs[s]))

        for i in range(l):

            if inputs[s][i]!=common_prefix[i]: # in each iteration identify the common chars
                common_prefix = common_prefix[:i] #and trim the prefix accordingly
                break                            # break out of inner loop at first mismatch

        #print(common_prefix)
    return common_prefix







#testcases

inputs = ["colorado", "color", "college", "collin"]
output = "col"

#for i in range(len(inputs)):
#assert output == longest_common_prefix(inputs[i])
print(output, longest_common_prefix(inputs))