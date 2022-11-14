import string

def indexes(iterable, obj):
    result = []
    for index, elem in enumerate(iterable):
        if elem == obj:
           result.append(index)
    return result

class Encoder:
    def __init__(self):
        self.digit_char_dict = self.createDictionary()
        self.createEncodedFile()
        self.recommended_word_list = []

    '''Creating dictionary where key is Number/Digit in mobile keypad 
    and value is list of all characters written over that digit'''

    def createDictionary(self):
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
        for j in range(i + 3, 25, 4):
            groupList = alphabet[j:j + 4]
            if j == 19:
                groupList = alphabet[j:j + 3]
            if j == 23:
                groupList = alphabet[j - 1: j + 4]
            map_dict[digit] = groupList
            digit = digit + 1
        return map_dict

    '''Creating Encoded.txt file which has replaced each alphabet in file with their Number/Digit in Mobile Keypad'''

    def createEncodedFile(self):
        with open("sample_dictionary.txt", "r+") as fread, open("encoded.txt", "w+") as fwrite:
            while True:
                count = 0
                line = fread.readline()
                if line != "":
                    count += 1
                    encoded_word = ""
                    for char in line:
                        for key, value in self.digit_char_dict.items():
                            if char in value:
                                if encoded_word == "":
                                    encoded_word = str(key)
                                else:
                                    encoded_word = encoded_word + str(key)
                else:
                    # print("End of File")
                    break
                fwrite.write(f"{encoded_word}\n")

    '''
                  Recommendation Processing...
    If Entered Phone Number matches any String in Encoded.txt, then return all index position of matched items.
    Word in file and their corresponding encoded value are at same line position in both files as well as list.
    It means in file sample_dictionary.txt, first word is aa and in file Encoded.txt, first value is the encoded 
    form of aa that is the first word in sample_dictionary.txt.
    '''

    def encoding_fun(self, phn_no):
        fread = open("sample_dictionary.txt", "r")
        word_list = fread.readlines()
        fptr = open("encoded.txt", "r")
        encoded_list = fptr.readlines()
        matched_index_lst = indexes(encoded_list, phn_no + "\n")
        print("Recommended Encoded Word for Your Phone Numbers are:\t")
        if len(list(matched_index_lst)) == 0:
            print("Opps !!! No words in Dictionary for that Number.")
        else:
            for index in list(matched_index_lst):
                print(word_list[index].split("\n")[0])
                self.recommended_word_list.append(word_list[index].split("\n")[0])






























