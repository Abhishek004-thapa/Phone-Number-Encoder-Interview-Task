import tkinter
import encoderModel

def encoder():
    phn_no = number_entry.get()
    if phn_no == "":
        T.insert(tkinter.END, "Phone Number Field is Empty.")
        return 0
    else:
        en = encoderModel.Encoder()
        en.encoding_fun(phn_no)
        T.delete("1.0", "end")
        for word in en.recommended_word_list:
            T.insert(tkinter.END, word + "\n")

# Creating Window

window = tkinter.Tk()
window.title("Phone Number Encoder App")
window.minsize(width=800, height=600)
window.config(bg='#f7f5dd', pady=20, padx=100)

canvas = tkinter.Canvas(height=286, width=206)

img = tkinter.PhotoImage(file="keypadImage.png")
canvas.create_image(103, 143, image=img)
canvas.grid(column=0, row=0, columnspan=3)

title = tkinter.Label(text="Phone Number Encoder".upper(), font=('Courier', 18, "bold"), fg="orange", bg='#f7f5dd')
title.grid(column=0, row=1, columnspan=3)

number_entry = tkinter.Entry(width=30, font=('Courier', 15, 'bold'))
number_entry.grid(column=1, row=2, pady=(30, 10))

label = tkinter.Label(text="Enter Phone Number :", font=('Courier', 14, 'bold'), fg='black',  bg='#f7f5dd')
label.grid(column=0, row=2, pady=(30, 10))

encode_Btn = tkinter.Button(text="Encode".upper(), fg='#CCF381', bg='#4831D4', width=10, font=('Courier', 18, 'bold'),
                            command=encoder)
encode_Btn.grid(column=0, row=3, columnspan=3)

# Create text widget and specify size.
T = tkinter.Text(height=5, width=30)
T.grid(column=0, row=5, columnspan=3)
T.config(font=('Courier', 12, 'bold'), fg='black')
# Create label
l = tkinter.Label(text="Recommended Phone Numbers".upper())
l.config(font=('Courier', 14, 'bold'), fg='blue', bg='#f7f5dd')
l.grid(column=0, row=4, columnspan=3, pady=(5, 2))

window.mainloop()

