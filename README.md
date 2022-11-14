# Phone-Number-Encoder-WISEYAK-Interview-Task

## `WISEYAK TECHNICAL INTERVIEW QUESTION`
 
 ### `PROBLEM STATEMENT:`

![image](https://user-images.githubusercontent.com/52848973/201769237-de8b5140-8155-4412-bd5b-537b47535d4b.png)

### `ABOUT FILES:`

   i) `PhoneNumberEncoding:` Console-Based Model.

   ii) `sample_dictionary.txt:` Consists of Possible words for Recommendation.

   iii) `keypadImage.png:` This image is used in Canvas of Tkinter Model.

   iv) `encoderModel.py:` This file consists of class name `encoder` that is being imported in `EncodingPhoneNumber-Tkinter.py` for all encoding function except GUI of         Tkinter.

    v) `EncodingPhoneNumber-Tkinter.py:` This is Tkinter-based Graphical User Interface(GUI) model.

#### `NOTE:`

   For Console-Based Model -- You will require files (i) and (ii) only. 

   But for Tkinter-GUI based model -- You will require files(ii), (iii), (iv) & (v).
 
 ### `APPROACH TO THIS PROBLEM:`
 
 Firstly, I created a dictionary with key as Digit/Number in Mobile Keypad and value as list of characters written over that Digit/Number.
 
{2: ['a', 'b', 'c'],
3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
