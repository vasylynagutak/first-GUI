import tkinter


def button_clicked():
    my_label.config(text=input.get())


window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


# button
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

#entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

new_button = tkinter.Button(text="exit", command=button_clicked)
new_button.grid(column=2, row=0)






window.mainloop()