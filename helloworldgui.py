import tkinter
from tkinter import END, IntVar

#create window
root = tkinter.Tk()
root.title("Hello World!")
root.iconbitmap('icon.ico')
root.geometry('400x450')
root.resizable(0,0)
root.config(bg='#3f5d7d')


#define functions
def outputMessage():
    name = text_entry.get()
    if choice.get() == 1:
        message = tkinter.Label(output_frame, bg='#008ab8', text="Hey "+name+ ", \nI hope you don't have any expectations. \nThis shit is not going to be a good time, \nbut atleast one day you'll get to die. \n\nTry not to cry till then. \nBest of luck!")
    elif choice.get() == 2:
        message = tkinter.Label(output_frame, bg='#008ab8', text="Hey "+name+ ", \nI know you have alot of expectations \nand some image inside of your head about how life is going to be, \nbut i just hope you know that it wont be like that... \n\nIt wont be anything like that at all. \nBest of luck!")
    elif choice.get() == 3:
        message = tkinter.Label(output_frame, bg='#008ab8', text="Hey "+name+ ", \nYou're doing a great job! \nAnd it only gets easier form here... \nGet out there and keep giving it your best, \nand you'll never be dissapointed. \nBest of luck!")
    message.pack(pady=(45,0))
    text_entry.delete(0,END)

#create frames
input_frame = tkinter.LabelFrame(root, width=200, height=150, borderwidth=1, bg='#008ab8')
output_frame = tkinter.LabelFrame(root, bg='#008ab8', width=370, height=250)
input_frame.pack(pady=(40,0))
output_frame.pack(pady=(25,0))

#add to input frame
input_frame.pack_propagate(0)
hello = tkinter.Label(input_frame, text="Ayo, what's your name?", bg='#008ab8',)
hello.grid(row=1,column=2)
text_entry = tkinter.Entry(input_frame, width=20)
text_entry.grid(row=2,column=2)
choice = IntVar()
choice.set(2)
choice1 = tkinter.Radiobutton(input_frame, text="Sad", variable=choice, value=1, bg='#008ab8')
choice2 = tkinter.Radiobutton(input_frame, text="Neutral", variable=choice, value=2, bg='#008ab8')
choice3 = tkinter.Radiobutton(input_frame, text="Happy", variable=choice, value=3, bg='#008ab8')
choice1.grid(row=3,column=1)
choice2.grid(row=3,column=2)
choice3.grid(row=3,column=3)
input_button = tkinter.Button(input_frame, text="Submit", command=outputMessage)
input_button.grid(row=4,column=2)

#add to output frame
output_frame.pack_propagate(0)


#run root main loop
root.mainloop()
