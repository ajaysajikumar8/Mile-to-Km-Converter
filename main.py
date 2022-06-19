from tkinter import *

def button_clicked():
    mile = int(input.get())
    km = round((mile) * 1.60934)
    label_3["text"] = km

#window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=40,pady=10)

#entry 
input = Entry()
input.config(width=15)
input.grid(column=1, row=0)

#label1
label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)

#label2
label_2 = Label(text= "is equal to")
label_2.grid(column=0, row=1)

#label3
label_3 = Label(text="0")
label_3.grid(column=1,row=1)

#label4
label_4 = Label(text = "Km")
label_4.grid(column=2, row=1)

#button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()




