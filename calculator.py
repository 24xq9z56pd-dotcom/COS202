from tkinter import *

root=Tk()
root.title("Mathematical Calculator")
root.geometry("400x500")
expr=""
e=Entry(root,font=("Arial",20),justify="right")
e.pack(fill="x",padx=10,pady=10)

def press(v):
    global expr
    expr+=str(v); e.delete(0,END); e.insert(END,expr)
def clear():
    global expr
    expr=""; e.delete(0,END)
def eq():
    global expr
    try:
        res=str(eval(expr.replace("^","**")))
        e.delete(0,END); e.insert(END,res); expr=res
    except:
        e.delete(0,END); e.insert(END,"Error"); expr=""
def off(): root.destroy()
rows=[["7","8","9","/"],["4","5","6","*"],["1","2","3","-"],["0",".","%","+"],["^","C","=","OFF"]]
f=Frame(root); f.pack(expand=True,fill="both")
for r in rows:
    rf=Frame(f); rf.pack(expand=True,fill="both")
    for b in r:
        cmd={"=":eq,"C":clear,"OFF":off}.get(b,lambda x=b:press(x))
        Button(rf,text=b,font=("Arial",16),command=cmd).pack(side="left",expand=True,fill="both")
root.mainloop()
