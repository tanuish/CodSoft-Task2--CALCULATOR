# calculator is a second task of codsoft of internship date 26/07/2023
from tkinter import *
first = second = operator = None
# function for digit 
def get_digit(digit):
    current = result_lable['text']
    new = current + str(digit)
    result_lable.config(text=new)

# function for clear 
def clear():
    result_lable.config(text=' ')


# function for operator 

def get_operator(op):
    global first,operator
    first = int(result_lable['text'])
    operator = op 
    result_lable.config(text=' ')

# function for result 

def get_result():
    global first,second,operator
    second = int( result_lable['text'])

    if operator == '+' :
        result_lable.config(text=str(first + second ))

    elif operator == '-' :
        result_lable.config(text=str(first - second ))
    
    elif operator == '*' :
        result_lable.config(text=str(first * second))

    else :
        if operator == 0 :
            result_lable.config(text='error')

        else:
            result_lable.config(text=str(first / second ))      
    


root =Tk()
root.title('calulator')
root.geometry('280x380')
root.resizable(0,0)
root.config(background='black')


# for resulting  display  

result_lable = Label(root,text=' ',bg='black',fg='white')
result_lable.grid(row=0,column=0,columnspan=1000,pady=(50,25),sticky='W')
result_lable.config(font=('verdana',30,'bold'))

# for button  of 16 from 0 to 9 and operator +,-,*,/
 
# button 7

button7 = Button(root,text='7',fg='white',bg='blue',width=5,height=2, command= lambda :get_digit(7))
button7.grid(row=1,column=0)
button7.config(font=('verdana',14,))

# button 8

button8 = Button(root,text='8',fg='white',bg='blue',width=5,height=2,command= lambda :get_digit(8))
button8.grid(row=1,column=1)
button8.config(font=('verdana',14))

# button 9

button9 = Button(root,text='9',fg='white',bg='blue',width=5,height=2,command= lambda :get_digit(9))
button9.grid(row=1,column=2)
button9.config(font=('verdana',14))

# button additon 

button_add = Button(root,text='+',fg="white",bg='blue',width=5,height=2,command= lambda : get_operator ('+'))
button_add.grid(row=1,column=3)
button_add.config(font=('verdana',14))

# button 4

button4 = Button(root,text='4',fg='white',bg='blue',width=5,height=2,command= lambda :get_digit(4))
button4.grid(row=2,column=0)
button4.config(font=('verdana',14))

# button 5 
button5 = Button(root,text='5',fg='white',bg='blue',width=5,height=2,command= lambda :get_digit(5))
button5.grid(row=2,column=1)
button5.config(font=('verdana',14))

# button 6
button6 = Button(root,text='6',fg='white',bg='blue',width=5,height=2,command= lambda :get_digit(6))
button6.grid(row=2,column=2)
button6.config(font=('verdana',14))

# button subtration

button_sub = Button(root,text='-',fg='white',bg='blue',width=5,height=2,command= lambda : get_operator('-'))
button_sub.grid(row=2,column=3)
button_sub.config(font=('verdana',14 ,))

# button 1

button1 = Button(root,text='1',fg='white',bg='blue',width=5,height=2,command= lambda :get_digit(1))
button1.grid(row=3,column=0)
button1.config(font=('verdana',14))

# button 2
button2= Button(root,text='2',fg='white',bg='blue',width=5,height=2,command= lambda :get_digit(2))
button2.grid(row=3,column=1)
button2.config(font=('verdana',14))

# button 3

button3 = Button(root,text='3',fg='white',bg='blue',width=5,height=2,command= lambda :get_digit(3))
button3.grid(row=3,column=2)
button3.config(font=('verdana',14))

# button  multipication 

button_mul = Button(root,text='*',fg='white',bg='blue',width=5,height=2,command= lambda : get_operator('*'))
button_mul.grid(row=3,column=3)
button_mul.config(font=('verdana',14))

# button clear

button_cl = Button(root,text='C',fg='white',bg='blue',width=5,height=2,command= lambda : clear())
button_cl.grid(row=4,column=0)
button_cl.config(font=('verdana',14))

# button 0
button0= Button(root,text='0',fg='white',bg='blue',width=5,height=2,command= lambda :get_digit(0))
button0.grid(row=4,column=1)
button0.config(font=('verdana',14))

# button =

button_equall = Button(root,text='=',fg='white',bg='blue',width=5,height=2, command= get_result)
button_equall.grid(row=4,column=2)
button_equall.config(font=('verdana',14))

# button  Division 

button_div = Button(root,text='/',fg='white',bg='blue',width=5,height=2,command= lambda : get_operator('/'))
button_div.grid(row=4,column=3)
button_div.config(font=('verdana',14))

root.mainloop()