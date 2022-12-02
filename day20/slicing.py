piano_keys = ["a", "b",  "c", "d", "e", "f", "g"]

reversed_keys = piano_keys[::-1]
print("reversed: ", reversed_keys)

inorder_keys = piano_keys[: : 1]
print("inorder: ", inorder_keys)

inorder_keys = piano_keys[0:5]
print(inorder_keys)

reversed_keys = piano_keys[-1 : -5 : -1]
print("reversed_segments", reversed_keys)

one_number = piano_keys[-1]
print("one_number", one_number)

two_numbers = piano_keys[-1 : -5]
print("two_numbers", two_numbers)
# print nothing due to the last step should put -1

redotwo_numbers = piano_keys[-1 : -5 : -1]
print("redotwo_numbers", redotwo_numbers)
# print reversed order, have to add -1 at the end
# [start : end: step] 1: inorder, -1, reversed order

whole_list = piano_keys[:]
print(whole_list)

# inorder segments

inorder_step1_segment = piano_keys[0 : 5 : 1]
print(inorder_step1_segment)
# abcde
inorder_step2_segment = piano_keys[0 : 5 : 2]
print(inorder_step2_segment)
# ace

reversedorder_step3_segment = piano_keys[-1 : -5 : -2]
print(reversedorder_step3_segment)





# for index in range (5):
#     print(index)
    
# for index in reversed (range(5)):
#     print(index)