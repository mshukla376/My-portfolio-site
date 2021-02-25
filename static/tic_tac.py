from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")


#X starts so Ttue
click = True
count = 0
ct = 0
cts = 0

#disable all buttons

def dis_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)




def win():
    global winner
    global ct, cts
    winner = False
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("","X WIN")
        ct += 1
        resets()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("","X WIN")
        ct += 1
        resets()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("","X WIN")
        ct += 1
        resets()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("","X WIN")
        ct += 1
        resets()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("","X WIN")
        ct += 1
        resets()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("X WIN")
        ct += 1
        resets()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("","X WIN")
        ct += 1
        resets()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("","X WIN")
        ct += 1
        resets()

    #check for O:
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="blue")
        b2.config(bg="blue")
        b3.config(bg="blue")
        winner = True
        messagebox.showinfo("","O WIN")
        cts += 1
        resets()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")
        winner = True
        messagebox.showinfo("","0 WIN")
        cts += 1
        resets()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="blue")
        b8.config(bg="blue")
        b9.config(bg="blue")
        winner = True
        messagebox.showinfo("","O WIN")
        cts += 1
        resets()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")
        winner = True
        messagebox.showinfo("","O WIN")
        cts += 1
        resets()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")
        winner = True
        messagebox.showinfo("","O WIN")
        cts += 1
        resets()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="blue")
        b6.config(bg="blue")
        b9.config(bg="blue")
        winner = True
        messagebox.showinfo("","O WIN")
        cts += 1
        resets()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="blue")
        b5.config(bg="blue")
        b9.config(bg="blue")
        winner = True
        messagebox.showinfo("","O WIN")
        cts += 1
        resets()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="blue")
        b5.config(bg="blue")
        b7.config(bg="blue")
        winner = True
        messagebox.showinfo("","O WIN")
        cts += 1
        resets()

    if count == 9 and winner == False:
        messagebox.showinfo("","TIE")
        resets()


    counter.set(ct)
    counters.set(cts)



# building buttons

def b_click(b):
    global click, count

    if b["text"] == " " and click == True:
        b["text"] = "X"
        click = False
        count += 1
        win()
    elif b["text"] == " " and click == False:
        b["text"] = "O"
        click = True
        count += 1
        win()
    else:
        messagebox.showerror("","ALREADY CLICKED")



def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global click, count, ct, cts
    click = True

    count = 0
    ct = 0
    cts = 0




    b1 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


def resets():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global click, count
    click = True
    count = 0



    b1 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("helvetica", 20), height=3, width=6,bg="SystemButtonFace", command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)



#check for the win
counter = IntVar()
counters = IntVar()

w = Label(root, text = "X_SCORE:").grid(row=7,column=0)
k = Label(root, text = "O_SCORE:").grid(row=8,column=0)
X_SCORE = Label(root, text="", textvariable=counter).grid(row=7,column=1)
O_SCORE = Label(root, text="", textvariable=counters).grid(row=8,column=1)



#create menu
My_menu = Menu(root)
root.config(menu=My_menu)

#create option menu
opt_menu = Menu(My_menu, tearoff=False)
My_menu.add_cascade(label="OPTION", menu=opt_menu)
opt_menu.add_command(label="RESET GAME", command=reset)


reset()
resets()


root.mainloop()





