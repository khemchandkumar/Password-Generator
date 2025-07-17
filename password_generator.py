from tkinter import *
import random
import string

def genpass():
    try:
        validlength=int(length.get())
    except ValueError:
        passwordbox.delete(0,END)
        passwordbox.insert(0,"Enter a valid length")
        return
    
    chars=""
    if capitalvar.get():
        chars+=string.ascii_uppercase
    if smallvar.get():
        chars+=string.ascii_lowercase
    if numbersvar.get():
        chars+=string.digits
    if symbolsvar.get():
        chars+=string.punctuation

    if not chars:
        passwordbox.delete(0,END)
        passwordbox.insert(0,"Select at least one option")
        return
    # random password generator
    password="".join(random.choice(chars) for _ in range(validlength))
    passwordbox.delete(0,END)
    passwordbox.insert(0,password)


def copypass():
    root.clipboard_clear()
    root.clipboard_append(passwordbox.get())

root=Tk()
root.geometry("600x600")
root.title("Password Generator")
root.configure(bg="#59CDE8")

# heading
heading=Label(root,text="Password Generator",font=("Arial",25,"bold","underline"),bg="#59CDE8",fg="red")
heading.pack(pady=20)



#password length frame
frameL = Frame(root,bg="#59CDE8")
frameL.pack(pady=20)
passlen=Label(frameL,text="Password Length",font=("Arial",15,"bold"),bg="#59CDE8",fg="red")
passlen.pack(side=LEFT,padx=5)
#enter box
length=Entry(frameL,font=("Arial",15,"bold"),width=5,borderwidth=5,fg="blue")
length.pack(side=LEFT,padx=5)

#variables
capitalvar=IntVar(value=1)
smallvar=IntVar(value=1)
numbersvar=IntVar(value=1)
symbolsvar=IntVar(value=1)
#checkbuttons
checkframe = Frame(root,bg="#59CDE8")
checkframe.pack(pady=20)
capital=Checkbutton(checkframe,text="Upper Case (A-Z)",font=("Arial",15,"bold"),bg="#59CDE8",variable=capitalvar,fg="red").pack(anchor="w",pady=5)
small=Checkbutton(checkframe,text="Lower Case (a-z)",font=("Arial",15,"bold"),bg="#59CDE8",variable=smallvar,fg="red").pack(anchor="w",pady=5)
numbers=Checkbutton(checkframe,text="Numbers (0-9)",font=("Arial",15,"bold"),bg="#59CDE8",variable=numbersvar,fg="red").pack(anchor="w",pady=5)
symbols=Checkbutton(checkframe,text="Special Characters",font=("Arial",15,"bold"),bg="#59CDE8",variable=symbolsvar,fg="red").pack(anchor="w",pady=5)

# passw_generate button
gen=Button(root,text="Generate Button",font=("Arial",15,"bold"),fg="red",bg="yellow",command=genpass)
gen.pack(pady=20)

#pass box
passwordbox=Entry(root,font=("Arial",15,"bold"),width=20,borderwidth=5,fg="blue")
passwordbox.pack()

# copy button
copybtn=Button(root,bg="yellow",fg="red",text="Copy Button",font=("Arial",15,"bold"), command=copypass)
copybtn.pack(pady=20)

root.mainloop()