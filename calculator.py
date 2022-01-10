#import all
from tkinter import *
from tkinter import font
#create window
root=Tk()

root.title('CALCULATOR')
root.geometry('325x410')
root.resizable(0,0)

btn_font=font.Font(weight='bold')
#set values in entry box
string=""
def set_text(text):
    global string
    string=string+str(text)
    variable.set(string)

#equal function
def equal():
    try:
        global string
        result=str(eval(string))
        variable.set(result)
    except:
        variable.set("Please check")

#clear function
def clr():
    global string
    string=""
    variable.set("")

#create calculator
variable=StringVar()
text_box=Entry(root,textvariable=variable)
text_box.place(x=1,y=1,height=100,width=325)

btn1=Button(root,text='1',height=3,width=5,bg='gray',font=btn_font,command=lambda:set_text('1'))
btn1.place(x=10,y=100)

btn2=Button(root,text='2',height=3,width=5,bg='gray',font=btn_font,command=lambda:set_text('2'))
btn2.place(x=90,y=100)

btn3=Button(root,text='3',height=3,width=5,bg='gray',font=btn_font,command=lambda:set_text('3'))
btn3.place(x=170,y=100) 

btn4=Button(root,text='4',height=3,width=5,bg='gray',font=btn_font,command=lambda:set_text('4'))
btn4.place(x=10,y=175)    

btn5=Button(root,text='5',height=3,width=5,bg='gray',font=btn_font,command=lambda:set_text('5'))
btn5.place(x=90,y=175)    

btn6=Button(root,text='6',height=3,width=5,bg='gray',font=btn_font,command=lambda:set_text('6'))
btn6.place(x=170,y=175)    

btn7=Button(root,text='7',height=3,width=5,bg='gray',font=btn_font,command=lambda:set_text('7'))
btn7.place(x=10,y=250)    

btn8=Button(root,text='8',height=3,width=5,bg='gray',font=btn_font,command=lambda:set_text('8'))
btn8.place(x=90,y=250)    

btn9=Button(root,text='9',height=3,width=5,bg='gray',font=btn_font,command=lambda:set_text('9'))
btn9.place(x=170,y=250)    

btn0=Button(root,text='0',height=3,width=5,bg='gray',font=btn_font,command=lambda:set_text('0'))
btn0.place(x=90,y=325)  

btn_clr=Button(root,text='CLR',height=3,width=5,bg='red',font=btn_font,command=clr)
btn_clr.place(x=10,y=325)    

btn_equal=Button(root,text='=',height=3,width=5,bg='green',font=btn_font,command=equal)
btn_equal.place(x=170,y=325)    

btn_add=Button(root,text='+',height=3,width=5,bg='brown',font=btn_font,command=lambda:set_text('+'))
btn_add.place(x=250,y=100)

btn_sub=Button(root,text='-',height=3,width=5,bg='brown',font=btn_font,command=lambda:set_text('-'))
btn_sub.place(x=250,y=175)

btn_multi=Button(root,text='x',height=3,width=5,bg='brown',font=btn_font,command=lambda:set_text('*'))
btn_multi.place(x=250,y=250)

btn_div=Button(root,text='/',height=3,width=5,bg='brown',font=btn_font,command=lambda:set_text('/'))
btn_div.place(x=250,y=325)

root.mainloop()
