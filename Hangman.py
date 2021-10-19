#Build the Hangman Game using Python.

from random import *
import turtle
def film(f):
    word=list(f)
    check=[]
    while len(check)<(len(word)/2):
        wordindex=randint(0,len(word)-1)
        if wordindex not in check:
            word[wordindex]='_'
        check.append(wordindex)
    s=''
    return str(s.join(word))  

guess=['bootstrap','springboot','javascript','github','kanban','react','flutter','nodejs']
play=True
while play:
    guessindex=randint(0,len(guess)-1)
    show=guess[guessindex]
    turtle.bgcolor('teal')
    turtle.color('white')
    style = ('Courier', 30, 'italic')
    turtle.penup()
    turtle.goto(0,350)
    turtle.pendown()
    turtle.write('Welcome to Hangman Game!', font=style, align='center')
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0,310)
    turtle.pendown()
    turtle.color('black')
    techstyle = ('Courier', 20, 'italic')
    turtle.write('Guess the tech : '+str(film(show)), font=techstyle, align='center')
    print('\nGuess the tech : ',film(show))
    lives=10
    turtle.penup()
    turtle.goto(100,-100)
    turtle.pendown()
    while lives:
        print(str(lives) + " ❤  Remaining")
        answer=input('\nAnswer : ')
        if answer==show:
            style = ('Courier', 30, 'italic')
            turtle.penup()
            turtle.goto(0,-260)
            turtle.pendown()            
            turtle.color('black')
            turtle.write(str(show), font=style, align='center')
            turtle.penup()
            turtle.goto(0,-310)
            turtle.color('yellow')
            turtle.write('!! Hurray You won the game !!', font=style, align='center')
            turtle.hideturtle()
            print('\nHurray You won the game !!!!')
            break
        else:
            turtle.color('black')
            turtle.shape("turtle")
            lives -=1
            print('\nOops Wrong answer')
            print('Try again')
            if lives == 0:
                turtle.pensize(15)
                turtle.color('white')
                turtle.backward(60)
                turtle.right(90)
                turtle.forward(60)
                style = ('Courier', 25, 'italic')
                turtle.penup()
                turtle.goto(0,-240)
                turtle.pendown()
                turtle.color('yellow')
                turtle.write("\n!! GAME OVER !!", font=style, align='center')
                turtle.pu()
                turtle.goto(0,-280)
                turtle.write("\n!! BETTER LUCK NEXT TIME !! ", font=style, align='center')
                turtle.pu()
                turtle.goto(0,-320)
                turtle.write("\n: The word was :", font=style, align='center')
                turtle.color('black')
                turtle.pu()
                turtle.goto(0,-360)
                turtle.write(str(show), font=style, align='center')
                print('GAME OVER - BETTER LUCK NEXT TIME\nThe word was',show)
            elif lives == 1:
                turtle.pensize(15)
                turtle.color('white')
                turtle.left(135)
                turtle.forward(60)
                turtle.left(45)
                turtle.forward(60)
            elif lives == 2:
                turtle.pensize(15)
                turtle.color('white')
                turtle.backward(60)
                turtle.left(90)
                turtle.forward(60)
                turtle.backward(60)
            elif lives == 3:
                turtle.pensize(15)
                turtle.color('white')
                turtle.backward(60)
                turtle.left(135)
                turtle.forward(60)
            elif lives == 4:
                turtle.right(90)
                turtle.pensize(15)
                turtle.color('white')
                turtle.forward(120)
            elif lives == 5:
                turtle.pensize(15)
                turtle.color('white')
                turtle.fillcolor('white')
                turtle.circle(20)
                turtle.circle(20,180)
            elif lives == 6:
                turtle.pensize(10)
                turtle.color('black')
                turtle.right(90)
                turtle.forward(40)
                turtle.right(90)
                turtle.forward(0)
            elif lives == 7:
                turtle.pensize(30)
                turtle.color('black')
                turtle.right(90)
                turtle.forward(120)
            elif lives == 8:
                turtle.pensize(30)
                turtle.color('black')
                turtle.left(90)
                turtle.forward(350)
            elif lives == 9:
                turtle.color('brown')
                turtle.pensize(70)
                turtle.backward(300)
                turtle.forward(40)
    option=input('\nDo you want to play again :\nY/N : ')
    if option.lower()=='y':
        turtle.reset()
        play=True
    else:
        play=False