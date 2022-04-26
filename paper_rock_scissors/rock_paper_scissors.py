# import the required libraries
from tkinter import *
import random

# initial window
# create an instance of tkinter frame
root = Tk()
# set the geometry of the frame
root.geometry("400x400")
# to create the fixed window size we use the method is called resizable ();
# in resizeable() method user can pass either positive integer or true, to make the window resizable
root.resizable(0, 0)
# used to set the title of the window
root.title("Game-Rock,Paper,Scissors")
# used to set the color of the background
root.config(bg='seashell3')

# heading
Label(root, text='Rock,Paper, Scissors', font='arial 20 bold', bg='seashell2').pack()

# input from the  user choice
# user_take is a string type variable that store the choice that the user enters
user_take = StringVar()
# create label for the input that user inserted
# Label(root,text,font,pack=used to organized widget in form of block)
Label(root, text='choose any one : rock ,paper, scissors', font='arial 15 bold', bg='seashell2').pack()
# enter widget used when we want to create an input text field
Entry(root, font='arial 15', textvariable=user_take, bg='antiquewhite2').pack()

# computer choice
# random.randint() function will randomly take any number from the given number
computer_pick = random.randint(1, 3)
# if the computer choose 1 then the rock will set to computer_pick variable
if computer_pick == 1:
    computer_pick = 'rock'
elif computer_pick == 2:
    # if the computer choose 2 then the paper will set to computer_pick variable
    computer_pick = 'paper'
else:
    # if the computer choose 3 then scissors will set to computer_pick variable
    computer_pick = 'scissor'
# Function to Start Game

Result = StringVar()

Result = StringVar()


def play():
    user_pick = user_take.get()
    if user_pick == computer_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and computer_pick == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and computer_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and computer_pick == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and computer_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and computer_pick == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and computer_pick == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')


# to make function reset the value again bother user and computer
def Reset():
    Result.set("")
    user_take.set("")


# function to exit
def Exit():
    root.destroy()


Entry(root, font='arial 10 bold', textvariable=Result, bg='antiquewhite2', width=50, ).place(x=25, y=250)

Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='seashell4', command=play).place(x=150, y=190)

Button(root, font='arial 13 bold', text='RESET', padx=5, bg='seashell4', command=Reset).place(x=70, y=310)

Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='seashell4', command=Exit).place(x=230, y=310)

root.mainloop()
