import tkinter as tk
import system.glade.Tools as gt
import system.glade.TEyes as te
import system.glade.Compiler as gc

global settings
settings = gt.init(edit=False, todo = None, debug_print = False, sys_print = False, make_log = False, loop_compil = True)

fenetre = tk.Tk()
fenetre.geometry('1210x700')
fenetre.resizable(width=0, height=0)
fenetre.title("direct time")
fenetre.configure(background="#000000")

py = tk.Text(fenetre, width=30,background="#212338",foreground="#b1e1f0",insertbackground="#00ffff",font=("consolas", 12))
py.place(x= 10 ,y=10,width= 460,height=680)

cpp = tk.Text(fenetre, width=30, background="#212338",foreground="#b1e1f0",font=("consolas", 12))
cpp.place(x= 480 ,y=10,width= 460,height=680)
cpp.configure(state='disabled')

err = tk.Text(fenetre, width=30, background="#212338",foreground="#b1e1f0",font=("consolas", 12))
err.place(x= 950 ,y=10,width= 250,height=680)
err.configure(state='disabled')

def py_actu():
    global cont
    temp = py.get("0.0","end")
    while "	" in temp: temp = temp.replace("	","    ")
    if temp != cont:
        cont = temp
        sortie, msg = te.main(fichier = temp,settings=settings)
        
        cpp.configure(state='normal')
        err.configure(state='normal')
        cpp.delete ("0.0", "end")
        err.delete ("0.0", "end")
        for e in msg:
            err.insert(0.0,f" |{e[0]}| {e[1]}\n")
        cpp.insert(0.0,"".join((l+"\n") for l in gc.compiler(sortie,settings)))
        cpp.configure(state='disabled')
        err.configure(state='disabled')
    py.after(250,py_actu)

cont = ""
py_actu()

fenetre.mainloop()