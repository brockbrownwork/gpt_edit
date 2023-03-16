import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

text_box = tk.Text(root, height=5, width=30, undo = True)
text_box.pack()

# Define a function to highlight all occurrences of the word "text"
def highlight_text(event=None):
    search_str = "text"
    start_index = "1.0"
    while True:
        start_index = text_box.search(search_str, start_index, tk.END)
        if not start_index:
            break
        end_index = f"{start_index}+{len(search_str)}c"
        text_box.tag_add("highlight", start_index, end_index)
        start_index = end_index

# Bind the KeyRelease event to the Textbox and call the highlight_text function
text_box.bind("<KeyRelease>", highlight_text)

# Configure the tag to make the text yellow with a red background
text_box.tag_configure("highlight", foreground="yellow", background="red")

# Define a function to save the text to a file
def save_file(event=None):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_box.get("1.0", tk.END))

# Bind the "ctrl+s" key combination to the save_file function
root.bind("<Control-s>", save_file)

# Define a function to save the text to a new file
def save_as_file(event=None):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_box.get("1.0", tk.END))

# Bind the "ctrl+shift+s" key combination to the save_as_file function
root.bind("<Control-Shift-s>", save_as_file)

# Define a function to open a file
def open_file(event=None):
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            text_box.delete("1.0", tk.END)
            text_box.insert("1.0", file.read())
    highlight_text()

# Bind the "ctrl+o" key combination to the open_file function
root.bind("<Control-o>", open_file)


root.mainloop()
