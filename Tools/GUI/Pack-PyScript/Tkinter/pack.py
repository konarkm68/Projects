import os, PyInstaller  ## py -m pip install PyInstaller
from tkinter import Tk, ttk, Label, Button, filedialog, messagebox

master = Tk(".py ---> .exe")
master.geometry("500x250")
master.resizable(False, False)
master.configure(background="blue")
master.title(".py ---> .exe")

console_lbl = Label(
    master,
    text="Do you want the console ?",
    bg="blue",
    fg="yellow",
    font=("Comic Sans MS", 14, "bold"),
    bd=5,
    relief="groove",
)
console = ttk.Combobox(master, font=("Comic Sans MS", 14, "bold"))
console["values"] = ("YES", "NO")
console.current(1)
console.config(state="readonly")
console_lbl.place(x=0, y=0, width=400, height=39)
console.place(x=400, y=0, width=100, height=39)

onefile_lbl = Label(
    master,
    text="Do you want package in one file ?",
    bg="blue",
    fg="yellow",
    font=("Comic Sans MS", 14, "bold"),
    bd=5,
    relief="groove",
)
onefile = ttk.Combobox(master, font=("Comic Sans MS", 14, "bold"))
onefile["values"] = ("YES", "NO")
onefile.current(0)
onefile.config(state="readonly")
onefile_lbl.place(x=0, y=39, width=400, height=39)
onefile.place(x=400, y=39, width=100, height=39)

onedir_lbl = Label(
    master,
    text="Do you want package in one directory ?",
    bg="blue",
    fg="yellow",
    font=("Comic Sans MS", 14, "bold"),
    bd=5,
    relief="groove",
)
onedir = ttk.Combobox(master, font=("Comic Sans MS", 14, "bold"))
onedir["values"] = ("YES", "NO")
onedir.current(1)
onedir.config(state="readonly")
onedir_lbl.place(x=0, y=78, width=400, height=39)
onedir.place(x=400, y=78, width=100, height=39)

icon_lbl = Label(
    master,
    text="Do you want an icon ?",
    bg="blue",
    fg="yellow",
    font=("Comic Sans MS", 14, "bold"),
    bd=5,
    relief="groove",
)
icon = ttk.Combobox(master, font=("Comic Sans MS", 14, "bold"))
icon["values"] = ("YES", "NO")
icon.current(1)
icon.config(state="readonly")


def select_icon_file():
    if icon.get() == "NO":
        icon.current(0)
        select_icon_file()
    elif icon.get() == "YES":
        icon_file = filedialog.askopenfilename(
            parent=master, filetypes=[("Icon Files", ".ico")]
        )
        if icon_file == "":
            icon.current(1)
        else:
            icon_file = os.path.split(icon_file)
            global icon_file_path, icon_file_name
            icon_file_path = icon_file[0]
            icon_file_name = icon_file[1]


select_icon_btn = Button(
    master,
    text="Select file: ",
    command=select_icon_file,
    bg="blue",
    fg="yellow",
    font=("Comic Sans MS", 14, "bold"),
    bd=5,
)
icon_lbl.place(x=0, y=117, width=250, height=39)
icon.place(x=250, y=117, width=100, height=39)
select_icon_btn.place(x=350, y=117, width=150, height=39)


def select_file():
    file = filedialog.askopenfilename(
        parent=master, filetypes=[("Python Files", ".py")]
    )
    if file == "":
        messagebox.showerror("ERROR", "FILE SELECTION IS MANDATORY...!!")
    else:
        file = os.path.split(file)
        file_path = file[0]
        file_name = file[1]
        query = "pyinstaller" + " " + file_name
        comboboxes = {
            "console": console.get(),
            "onefile": onefile.get(),
            "onedir": onedir.get(),
            "icon": icon.get(),
        }
        if comboboxes["console"] == "NO":
            query += " --noconsole"
        if comboboxes["onefile"] == "YES":
            query += " --onefile"
        if comboboxes["onedir"] == "YES":
            query += " --onedir"
        if comboboxes["icon"] == "YES":
            global icon_file_name
            query += " --icon " + icon_file_name
        os.chdir(file_path)
        os.system(query)


convert = Button(
    master,
    text="Start the process...",
    command=select_file,
    bg="blue",
    fg="yellow",
    font=("Comic Sans MS", 14, "bold"),
    bd=5,
)
convert.place(x=100, y=195, width=300, height=39)

master.mainloop()
