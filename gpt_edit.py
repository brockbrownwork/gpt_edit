import tkinter as tk
from tkinter import filedialog
import os
from pygments import lex
from pygments.lexers import PythonLexer
from pygments.token import Token

root = tk.Tk()
root.title("Untitled")

text_box = tk.Text(root, height=5, width=30, undo=True, wrap=tk.WORD)
text_box.pack_propagate(False)
text_box.pack(fill=tk.BOTH, expand=True)

current_file = None

def highlight_syntax(event=None):
    # Remove existing tags
    for tag in text_box.tag_names():
        if tag != "highlight":
            text_box.tag_delete(tag)

    # Apply syntax highlighting
    code = text_box.get("1.0", tk.END)
    for token, value in lex(code, PythonLexer()):
        tag = str(token)
        start_index = text_box.search(value, "1.0", stopindex=tk.END)
        end_index = f"{start_index}+{len(value)}c"
        text_box.tag_add(tag, start_index, end_index)
        text_box.tag_configure(tag, foreground=get_color(token))

def get_color(token):
    if token in Token.Keyword:
        return "blue"
    elif token in Token.String:
        return "green"
    elif token in Token.Name.Function:
        return "darkorange"
    elif token in Token.Name.Namespace:
        return "purple"
    elif token in Token.Comment:
        return "red"
    else:
        return "black"

text_box.bind("<KeyRelease>", highlight_syntax)

def save_file(event=None):
    global current_file
    if current_file is None:
        current_file = filedialog.asksaveasfilename(defaultextension=".txt")
    if current_file:
        with open(current_file, "w") as file:
            file.write(text_box.get("1.0", tk.END))
        root.title(os.path.basename(current_file))

root.bind("<Control-s>", save_file)

def save_as_file(event=None):
    global current_file
    current_file = filedialog.asksaveasfilename(defaultextension=".txt")
    if current_file:
        with open(current_file, "w") as file:
            file.write(text_box.get("1.0", tk.END))
        root.title(os.path.basename(current_file))

root.bind("<Control-Shift-s>", save_as_file)

def open_file(event=None):
    global current_file
    current_file = filedialog.askopenfilename()
    if current_file:
        with open(current_file, "r") as file:
            text_box.delete("1.0", tk.END)
            text_box.insert("1.0", file.read())
        root.title(os.path.basename(current_file))
    highlight_syntax()

root.bind("<Control-o>", open_file)

root.mainloop()
