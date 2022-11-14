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
 
   Firstly, I created a dictionary with key as Digit/Number in Mobile Keypad and value as list of characters written over that Digit/Number. Below is glimspe of our      dicionary.

  `{2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y',    'z']}`

  Then, I read word from each line of input file `sample_dictionary.txt` and encoded each char in word to their corresponding key value of above created dictionary.

  That encoded word is written line by line to `encoded.txt` file. 

  After that, It checks for every matched items in encoded.txt with the phone number entered by user and save its matched index position. 

  Using `word_list = fread.readlines()` method, all words in each line of file `sample_dictionary.txt` will be stored as element of list in `word_list`.
  Then, From that list, all items of matched index position are stored which are the required `List of Recommended Words`.

### `GUI-Based Model:`

<img src="https://user-images.githubusercontent.com/52848973/201776523-db95b078-feb4-48e1-ae00-966f3a969a1e.png" width="800" height="500" />

### This project took lots of effort. Don't forget to tap `STAR`⭐ on top-right corner.

### Please DO VISIT my Youtube Channel-- `64bitCODING`: https://www.youtube.com/channel/UC7kCwIjNR9wECvxJ8jbn0fQ

### HIT LIKE 👍 and SUSCRIBE 🔔 BUTTON.
#### Your one LIKE 👍 gives us MOTIVATION.

### CONTACT ME ON:

linkedin --> https://www.linkedin.com/in/abhishek-thapa-b9a733199/

