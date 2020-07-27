from tkinter import *

root = Tk()
root.title('Live Camarote')
root.iconbitmap('c:/gui/code.jpg') #python iconbitmap error?
root.geometry("400x400")

# Listbox!
my_listbox = Listbox(root)
my_listbox.pack(pady=15)

# Add item to listbox
my_listbox.insert(END, "This is an item")
my_listbox.insert(END, "Second Item!")

# Add list of items
my_list = ["One", "Two", "Three"]

for item in my_list:
    my_listbox.insert(END, item)

    my_listbox.insert(2, "A new Thing")

root.mainloop()

