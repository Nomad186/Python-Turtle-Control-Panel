import turtle
import PySimpleGUI as sg
import random
import math
rainbow = False
t = turtle.Turtle()
scr = turtle.getscreen()
turtlerunning = False
tleftright = 'right'
colorlist = ['red', 'blue', 'purple', 'yellow', 'orange', 'green',]
stop = False

layout = [[sg.Text("Please choose the shape you want to create.")],
          [sg.Button('Square'), sg.Button('Triangle'), sg.Button('Hexagon'), sg.Button('IcosCube'), sg.Button('Flower')],
          [sg.Button('amogus')],
          [sg.Input(size=(10,1), key='length'), sg.Text('Input length of sides leave blank for default')],
          [sg.Input(size=(10,1), key='circle'), sg.Text('Size of circle'), sg.Button('Create Circle')],
          [sg.Input(size=(10,1), key='sideA'), sg.Input(size=(10,1), key='sideB'), sg.Input(size=(10,1), key='sideC'), sg.Text('Length of Side A, B, C of triangle.'),sg.Button('Create Triangle')],
          [sg.Input(size = (5,1), key = '-scalar-'), sg.Text("Blackhole with custom size"), sg.Button("Launch V1"), sg.Button("Launch V2"), sg.Text("x turns left", key = '-turns-')],
          [sg.Text("Colors")],
          [sg.Button('Red'), sg.Button('Blue'), sg.Button('Purple'), sg.Button('Black'), sg.Button('Green'), sg.Button('Yellow'), sg.Button('Yellow')],
          [sg.Button('Rainbow Mode'), sg.Text("De-Activated     ", key=('rainbow'))],
          [sg.Text("Current Color: Black", key='-OUTPUT-')],
          [sg.Input(size=(10,1), key='speed'), sg.Button('Change Speed')],
          [sg.Text("Move the turtle to draw new shapes")],
          [sg.Button('Left'), sg.Button('Right')],
          [sg.Input(size=(20,1), key='-degrees-'), sg.Text("Degress to turn (Right)    ", key='leftright'), sg.Button('Turn This Amount')],
          [sg.Input(size=(20,1), key='-forward-'), sg.Text("Pixels to move forward"), sg.Button('Move Forward This Amount')],
          [sg.Button('Pen Up'), sg.Button('Pen Down')],
          [sg.Button('Go to 0,0')],
          [sg.Text('Go to (x box, then y box)'), sg.Input(size=(10,1), key ='gotox'), sg.Input(size=(10,1), key = 'gotoy'), sg.Button('goto')],
          [sg.Button('Quit'), sg.Button('Clear Screen')]]

        
window = sg.Window('Turtle Graphics Control Panel', layout, size=(700,700))
BODY_COLOR =  'skyblue'
BODY_SHADOW = ''
GLASS_COLOR = '#9acedc'
GLASS_SHADOW = ''
def blackhole():
    x = 0
    for i in range(int(float(values["-scalar-"]))):
        window['-turns-'].update(str(int(float(values["-scalar-"]))-i) + " turns left")
        t.speed(7457)
        if rainbow == True:
            randomclr = random.choice(colorlist)
            t.color(randomclr)
            print("rainbow")
        x = x + 1
        t.circle(x)
        t.speed(10)

def blackhole2():
    x = 0
    for i in range(int(float(values['-scalar-']))):
        window['-turns-'].update(str(int(float(values["-scalar-"]))-i) + " turns left")
        t.speed(7457)
        if rainbow == True:
            randomclr = random.choice(colorlist)
            t.color(randomclr)
        x = x + 1
        t.lt(179)
        t.fd(x)
        t.speed(10)

def backpack():
    t.up()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)
    t.fillcolor(BODY_COLOR)
    t.begin_fill()
    t.down()
    t.forward(30)
    t.right(255)
    t.circle(300, -30)
    t.right(260)
    t.forward(30)
    t.end_fill()
def body():
    """ draws the body """
    t.pensize(20)
    #t.speed(15)
    t.fillcolor(BODY_COLOR)
    t.begin_fill()
    # right side
    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)
    # head curve
    t.right(180)
    t.circle(100, -180)
    # left side
    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)
    #t.backward(200)
    t.circle(40, -180)
    #t.right(90)
    t.left(7)
    t.backward(50)
    # hip
    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()
    #t.right(180)
    #t.circle(25, -180)
    t.right(240)
    t.circle(50, -70)
    t.end_fill()
def glass():
    t.up()
    #t.right(180)
    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.down()
    t.fillcolor(GLASS_COLOR)
    t.begin_fill()
    t.right(150)
    t.circle(90, -55)
    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)
    
    #t.right(180)
    t.circle(50, -190)
    t.right(170)
    t.forward(80)
    t.right(180)
    t.circle(45, -30)
    t.end_fill()


while True:
    event, values = window.read()
    if event == 'amogus':
        body()
        glass()
        backpack()
    if values['length'] != '':
        tlength = int(float(values['length']))
    elif values['length'] == '':
        tlength = 100
    if event == 'Create Circle':
        size = int(float(values['circle']))
        t.circle(size)
    #if event == 'Create Triangle':
     #   a = int(float(values['sideA']))
      #  b = int(float(values['sideB']))
       # c = int(float(values['sideC']))
        #cosa = ((c*c)+(b*b)-(a*a)) / (2(b*c))
        #cosb = ((c*c)+(a*a)-(b*b)) / (2*(c*a))
        #angleB = math.acos(cosb)
        #angleA = math.acos(cosa)
        #angleC = (180-(angleB + angleA))
        #print(angleB)
        #print(angleA)
        #print(angleC)
    if event == 'Stop':
        stop = True
    if event == 'Flower':
        for i in range(2):
            for i in range(3):
                for i in range(13):
                    t.left(90)
                    t.forward(tlength)
                    t.right(60)
                    t.forward(tlength)
                    t.right(120)
                    t.forward(tlength)
                    t.goto(0,0)
                    t.right(180)
                    t.forward(tlength)
                    t.left(60)
                    t.forward(tlength)
                    t.left(120)
                    t.forward(tlength)
                    t.goto(0,0)
                    t.left(180)
                    t.forward(tlength)
                    t.left(60)
                    t.forward(tlength)
                    t.right(120)
                    t.forward(tlength)
                    t.right(60)
                    t.forward(tlength)
                    if rainbow == True:
                        color = random.choice(colorlist)
                        t.color(color)
                t.goto(0,0)
                t.right(10)
            t.right(5) 

    if event == 'Change Speed':
       t.speed(int(float(values['speed']))) 
    if event == 'Launch V1':
       blackhole2()

    if event == 'Launch V2':
        blackhole()
    if event == 'goto':
        x = float(values['gotox'])
        y = float(values['gotoy'])
        t.goto(x,y)
    if event == 'Go to 0,0':
        t.goto(0,0)
    if event == 'Rainbow Mode':
        if rainbow == False:
            rainbow = True
            window['rainbow'].update('Activated')
        elif rainbow == True:
            rainbow = False
            window['rainbow'].update('De-activated')
    if event == 'Pen Down':
        t.pendown()
    if event == 'Pen Up':
        t.penup()
    if event == 'Turn This Amount':
        if tleftright == 'right':
            t.right(float(values['-degrees-']))
        elif tleftright == 'left':
            t.left(float(values['-degrees-']))
        
    if event == 'Move Forward This Amount':
        if rainbow == True:
            color = random.choice(colorlist)
            t.color(color)
        t.forward(float(values['-forward-']))
    if event == 'Hexagon':
        for i in range(6):
            t.forward(tlength)
            t.right(60)
    if event == 'IcosCube':
        t.left(90)
        t.forward(tlength)
        t.right(60)
        t.forward(tlength)
        t.right(120)
        t.forward(tlength)
        t.goto(0,0)
        t.right(180)
        t.forward(tlength)
        t.left(60)
        t.forward(tlength)
        t.left(120)
        t.forward(tlength)
        t.goto(0,0)
        t.left(180)
        t.forward(tlength)
        t.left(60)
        t.forward(tlength)
        t.right(120)
        t.forward(tlength)
        t.right(60)
        t.forward(tlength)
        if rainbow == True:
            color = random.choice(colorlist)
            t.color(color)
    if event == 'Square':
        if turtlerunning == False:
            turtlerunning = True
            for i in range(4):
                t.forward(tlength)
                t.right(90)
                if rainbow == True:
                    color = random.choice(colorlist)
                    t.color(color)
            turtlerunning = False
        elif turtlerunning == True:
            print("Cant do this, turtle is drawing something")
    if event == 'Triangle':
        if turtlerunning == False:
            turtlerunning = True
            for i in range(3):
                t.forward(tlength)
                t.right(120)
                if rainbow == True:
                    color = random.choice(colorlist)
                    t.color(color)
            turtlerunning = False
        elif turtlerunning == True:
            print("Cant do this, turtle is drawing something")
    if event == 'Red':
        window['-OUTPUT-'].update('Current Color: Red')
        t.color("red")
    if event == 'Blue':
        window['-OUTPUT-'].update('Current Color: Blue')
        t.color("blue")
    if event == 'Purple':
        window['-OUTPUT-'].update('Current Color: Purple')
        t.color("purple")
    if event == 'Black':
        window['-OUTPUT-'].update('Current Color: Black')
        t.color("black")
    if event == 'Green':
        window['-OUTPUT-'].update('Current Color: Green')
        t.color("green")
    if event == 'Yellow':
        window['-OUTPUT-'].update('Current Color: Yellow')
        t.color("yellow")
    if event == 'Orange':
        window['-OUTPUT-'].update('Current Color: Orange')
        t.color("orange")
    if event == 'Quit':
        window.close()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Clear Screen':
        t.clear()
        t.penup()
        t.goto(0,0)
        t.pendown()
    if event == 'Left':
        tleftright = 'left'
        window['leftright'].update("Degrees to turn in (Left)")
    if event == 'Right':
        tleftright = 'right'
        window['leftright'].update("Degress to turn in (Right)")
            


