from tkinter import *
from random import *

#область функций
def final_t():

    if 0<=score<8:
        canvas.create_text(400,300,
                             fill = 'black',
                             font = 'Times 24 bold',
                             text = f'Ты можешь лучше!',
                             anchor = NE)
        canvas.create_image(200, 700, image=smail3, anchor=S)
    elif 7<score<20:
        canvas.create_text( 400, 300,
                           fill='black',
                           font='Times 24 bold',
                           text=f'Хороший результат!',
                           anchor=NE)
        canvas.create_image(200, 700, image=smail2, anchor=S)
    elif 19<score<40:
        canvas.create_text(400, 300,
                           fill='black',
                           font='Times 24 bold',
                           text=f'Отличный результат!',
                           anchor=NE)
        canvas.create_image(200, 700, image=smail1, anchor=S)

def game_over():

    canvas.itemconfig(fon_i,state ='hidden')
    canvas.itemconfig(fon2_i, state = 'normal')
    canvas.itemconfig(myxa,state = 'hidden')
    canvas.itemconfig(myxoboika,state = 'hidden')
    canvas.itemconfig(text_id, state='hidden')
    canvas.itemconfig(time_id, state='hidden')
    canvas.itemconfig(final_text,text = f'Время вышло! Набрано: {score} очков.', state = 'normal')
    final_t()

def update_time():
    global time
    time-=1
    if time < 0:
        game_over()
    else:
        canvas.itemconfig(time_id, text = f"Таймер:{time}")
        canvas.after(1000,update_time)

def hit():
    global score
    score+=1
    canvas.itemconfig(text_id,text = f'Очки : {score}')

def collision_detection(x,y):
    position = canvas.coords(myxa)
    print(position)
    left = position[0]
    top = position[1]
    right = position[0] + npc_width
    bottom = position[1] + npc_height
    return left<=x<=right and top<=y<=bottom

def animate_frame(frame=0):
    canvas.itemconfigure(myxa,image = photos[frame],anchor = 'nw')
    canvas.after(50,animate_frame,(frame+1) % len(photos))
def move_to():
    global mux_vx, mux_vy
    x = canvas.coords(myxa)[0]+mux_vx
    y = canvas.coords(myxa)[1] +mux_vy
    if x<0:
        x=0
        mux_vx = mux_vy
    if x> game_width -npc_width:
        x = game_width-npc_width
        mux_vx = -mux_vx
    if y<0:
        y=0
        mux_vy = -mux_vy
    if y>game_height-npc_height:
        y = game_height-npc_height
        mux_vy = -mux_vy
    canvas.moveto(myxa,x,y)
    canvas.after(10,move_to)



def mouse_click_up(e):
    canvas.itemconfig(myxoboika, image= actor3 )

def mouse_click_down(e):
    canvas.itemconfig(myxoboika, image=actor2)
    if collision_detection(mouse_x-75,mouse_y):
        hit()



def mouse_motion(event):
    global mouse_x,mouse_y
    mouse_x, mouse_y = event.x, event.y
    canvas.moveto(myxoboika, mouse_x-75,mouse_y-75)

def spuwn():
    global mux_vx,mux_vy
    x = randint(1,game_width - npc_width)
    y = randint(1, game_height - npc_height)
    if abs(mouse_x - x)<100 and abs(mouse_y - y) <100:
        x = randint(1, game_width - npc_width)
        y = randint(1, game_height - npc_height)
    canvas.moveto(myxa, x, y)
    k1 = choice(koef)
    k2 = choice(koef)
    mux_vx, mux_vy = randint(1, 5) * k1, randint(1, 5) * k2

def game_update():
    spuwn()
    canvas.after(1000, game_update)


#область глобальных переменных
game_width = 720
game_height = 720

npc_width = 100
npc_height = 100

mouse_x = mouse_y = 0
x=y=0
score = 0
time = 20


#оэффициент движения и начальная скорость
koef = [-1,1]
mux_vx =3
mux_vy = 5
#пределить вектора движения


#создание и обработка окна и виджетов
window = Tk()
window.title("Проучи муху")
window.resizable(width = False, height = False)
canvas = Canvas(window, width = game_width, height = game_height )
canvas.pack()


#объекты
smail1 = PhotoImage(file = 'всмайл.png')
smail2 = PhotoImage(file = 'лайк.png')
smail3 = PhotoImage(file = 'гсмайл.png ' )
fon = PhotoImage (file = 'фон для мухи.png')
fon2 = PhotoImage(file = 'фон2.png')
fon_i = canvas.create_image(0,0,image=fon,anchor = NW,state = 'normal')
fon2_i=canvas.create_image(380,380,image = fon2,state = 'hidden')

photos = [PhotoImage(file = f"муха{i}.png") for i in range(1,3)]
myxa = canvas.create_image(0,0, image =photos[0], anchor = 'nw')


actor2= PhotoImage(file= 'мухобойка.png')
actor3 =PhotoImage(file = 'мухобойка2.png')
myxoboika =canvas.create_image(x,y,image = actor3, anchor = S)
text_id = canvas.create_text(game_width - 10,10,
                             fill = 'black',
                             font = 'Times 20 bold',
                             text = f'Очки: {score}',
                             anchor = NE)
time_id= canvas.create_text(game_width - 170,10,
                             fill = 'black',
                             font = 'Times 20 bold',
                             text = f'Таймер: {time}',
                             anchor = NE)
final_text= canvas.create_text(600,200,
                             fill = 'black',
                             font = 'Times 24 bold',
                             text = f'Время вышло! Набрано: {score} очков.',
                             anchor = NE, state = 'hidden')

#функции обратнорго вызова
update_time()
animate_frame()
move_to()
game_update()
canvas.bind ('<ButtonPress>',mouse_click_down)
canvas.bind ('<ButtonRelease>',mouse_click_up)
canvas.bind ( '<Motion >', mouse_motion)

window.mainloop()