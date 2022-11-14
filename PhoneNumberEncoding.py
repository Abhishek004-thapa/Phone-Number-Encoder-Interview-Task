import string
import time

'''Function that returns all index position of matched items in list...'''

def indexes(iterable, obj):
    result = []
    for index, elem in enumerate(iterable):
        if elem == obj:
           result.append(index)
    return result

print("\n\t\t----------Welcome to Your Mobile Number Encoders-------------\n".upper())

'''Creating dictionary where key is Number/Digit in mobile keypad 
and value is list of all characters written over that digit'''

alphabet = list(string.ascii_lowercase)

digit = 2
map_dict = {}
groupList = []
mapList = []
for i in range(0, 15, 3):
    if i <= 15:
        groupList = alphabet[i:i + 3]
        map_dict[digit] = groupList
        digit = digit + 1
for j in range(i+3, 25, 4):
    groupList = alphabet[j:j + 4]
    if j == 19:
        groupList = alphabet[j:j + 3]
    if j == 23:
         groupList = alphabet[j-1: j+4]
    map_dict[digit] = groupList
    digit = digit + 1
# print(map_dict)

'''Creating Encoded.txt file which has replaced each alphabet in file with their Number/Digit in Mobile Keypad'''

with open("sample_dictionary.txt", "r+") as fread, open("encoded.txt", "w+") as fwrite:
    word_dict = fread.readlines()
    fread.seek(0)
    # print(len(word_dict))
    while True:
        count = 0
        line = fread.readline()
        if line != "":
            count += 1
            encoded_word = ""
            for char in line:
                for key, value in map_dict.items():
                    if char in value:
                        if encoded_word == "":
                            encoded_word = str(key)
                        else:
                            encoded_word = encoded_word + str(key)
        else:
            # print("End of File....")
            break
        fwrite.write(f"{encoded_word}\n")


phn_no = str(input("Enter your Phone Number to be Encoded:  "))

'''Recommendation Processing...
If Entered Phone Number matches any String in Encoded.txt, then return all index position of matched items.
Word in file and their corresponding encoded value are at same line position in both files as well as list.
It means in file sample_dictionary.txt, first word is aa and in file Encoded.txt, first value is the encoded form of aa.
'''

fptr = open("encoded.txt", "r")
encoded_list = fptr.readlines()
# print(encoded_list)
recommended_word_list = []
matched_index_lst = indexes(encoded_list, phn_no + "\n")
# print(len(list(matched_index_lst)))
# print(list(matched_index_lst))
print("Please Wait...")
time.sleep(3)
print("Recommended Encoded Word for Your Phone Numbers are:\t")
if len(list(matched_index_lst)) == 0:
    print("Opps !!! No words in Dictionary for that Number.")
else:
    for index in list(matched_index_lst):
        print(word_dict[index].split("\n")[0])
        recommended_word_list.append(word_dict[index])
