import tkinter as Tk
from tkinter import *
#define the first story
def Story1(win):
  def final(tl: Toplevel, name, sports, City, playername, drinkname, snacks):
 
    text = f'''
       One day me and my friend {name} decided to play a {sports} game in {City}.
       We wanted to watch {playername}.
       We drank {drinkname} and also ate some {snacks} 
       We really enjoyed! We are looking forward to go again and enjoy '''
 
    tl.geometry(newGeometry='500x550')
 
    Label(tl, text='Story:',  wraplength=tl.winfo_width()).place(x=160, y=310)
    Label(tl, text=text,wraplength=tl.winfo_width()).place(x=0, y=330)
 
  NewScreen = Toplevel(win, bg='yellow')
  NewScreen.title("A memorable day")
  NewScreen.geometry('500x500')
  #creating labels
  Label(NewScreen, text='Memorable Day').place(x=100, y=0)
  Label(NewScreen, text='Name:').place(x=0, y=35)
  Label(NewScreen, text='Enter a game:').place(x=0, y=70)
  Label(NewScreen, text='Enter a city:').place(x=0, y=110)
  Label(NewScreen, text='Enter the name of a player:').place(x=0, y=150)
  Label(NewScreen, text='Enter the name of a drink:').place(x=0, y=190)
  Label(NewScreen, text='Enter the name of a snack:').place(x=0, y=230)
  #asking the users for entries
  Name = Entry(NewScreen, width=17)
  Name.place(x=250, y=35)
  game = Entry(NewScreen, width=17)
  game.place(x=250, y=70)
  city = Entry(NewScreen, width=17)
  city.place(x=250, y=105)
  player = Entry(NewScreen, width=17)
  player.place(x=250, y=150)
  drink = Entry(NewScreen, width=17)
  drink.place(x=250, y=190)
  snack = Entry(NewScreen, width=17)
  snack.place(x=250, y=220)

  SubmitButton = Button(NewScreen, text="Submit", background="Blue", font=('Times', 12), command=lambda:final(NewScreen, Name.get(), game.get(), city.get(), player.get(), drink.get(), snack.get()))
  SubmitButton.place(x=150, y=270)
 

 
  NewScreen.mainloop()
def Story2(win):
  def final(tl: Toplevel, profession, noun, feeling, emotion, verb):
 
    text = f'''
       Jessy and {noun}Growing up I dream of becoming a {profession} but on my terminal grade I devlop a {feeling}.      
       towards this. I started to adapt myself with some basics concept about math and tech and i felt{emotion}.     
       then. {verb} is what i push myself to do every single day. I feel very proud by choosing this path. I have no regrets.    
       Wish me luck on this long journey.'''
 
    tl.geometry(newGeometry='500x550')
 
    Label(tl, text='Story:',  wraplength=tl.winfo_width()).place(x=160, y=310)
    Label(tl, text=text,wraplength=tl.winfo_width()).place(x=0, y=330)
 
  NewScreen = Toplevel(win, bg='yellow')
  NewScreen.title("A memorable day")
  NewScreen.geometry('500x500')
  Label(NewScreen, text='Ambitions').place(x=100, y=0)
  Label(NewScreen, text='noun:').place(x=0, y=35)
  Label(NewScreen, text='Enter a profession:').place(x=0, y=70)
  Label(NewScreen, text='Enter an emotion:').place(x=0, y=110)
  Label(NewScreen, text='Enter a feeling:').place(x=0, y=150)
  Label(NewScreen, text='Enter a verb:').place(x=0, y=190)
  
  profession= Entry(NewScreen, width=17)
  profession.place(x=250, y=35)
  noun = Entry(NewScreen, width=17)
  noun.place(x=250, y=70)
  verb = Entry(NewScreen, width=17)
  verb.place(x=250, y=105)
  feeling = Entry(NewScreen, width=17)
  feeling.place(x=250, y=150)
  emotion = Entry(NewScreen, width=17)
  emotion.place(x=250, y=190)
  
  SubmitButton = Button(NewScreen, text="Submit", background="Blue", font=('Times', 12), command=lambda:final(NewScreen, noun.get(), profession.get(), feeling.get(), emotion.get(), verb.get()))
  SubmitButton.place(x=150, y=270)
# Our app main screen
Screen = Tk()
Screen.title("Obenson Mad libs project")
Screen.geometry('400x400')
Screen.config(bg="pink")
Label(Screen, text='Obenson mad libs project').place(x=100, y=20)
#creating buttons
Story1Button = Button(Screen, text='A remarkable day++', font=("Times New Roman", 13), command=lambda:Story1(Screen), bg='Blue')
Story1Button.place(x=140, y=90)
Story2Button = Button(Screen, text='Ambitions', font=("Times New Roman", 13),command=lambda: Story2(Screen), bg='Yellow' )
Story2Button.place(x=150, y=150)
 
Screen.update()
Screen.mainloop()
