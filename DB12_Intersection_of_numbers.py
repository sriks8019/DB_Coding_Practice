'''

nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []


'''


def intersection_of_numbers(nums1,nums2):

    nums1_set=set(nums1)
    nums2_set=set(nums2)

    return list(nums1_set.intersection(nums2_set))


def intersection_of_numbers_v2(nums1, nums2):
    intersection={}

    nums1_set=set(nums1)

    for i in nums2:
        if i in nums1_set:
            intersection[i]=1


    return intersection.keys()

inputs=[[[2, 4, 4, 2],[2, 4]], [[1, 2, 3, 3],[3, 3]],[[2, 4, 6, 8],[1, 3, 5, 7]]]
outputs=[[2, 4],[3],[]]

for i in range(len(inputs)):
    print("using sets")
    print(outputs[i], intersection_of_numbers(inputs[i][0],inputs[i][1]))
    print("without using sets")
    print(outputs[i], intersection_of_numbers(inputs[i][0], inputs[i][1]))

