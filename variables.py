from PPlay.window import * 
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *

janW = 960
janH = 540 
janela = Window(janW, janH)
key = keyboard.Keyboard()
ms = mouse.Mouse()

state = True

start = Sprite("assets/start.png")
options = Sprite("assets/options.png")
exit = Sprite("assets/exit.png")
menu = Sprite("assets/menu.png")
start.set_position(0 + start.width/2 + 10, janH/2 - start.height/2)
options.set_position(0 + options.width/2 + 10, (janH/2 - options.height/2) + 75)
exit.set_position(0 + exit.width/2 + 10, (janH/2 - exit.height/2) + 150)
menu.set_position(janW-menu.width-10, 10)

backgroundMenu = GameImage("assets/1.png")
backgroundStart = GameImage("assets/2.png")
backgroundOptions = GameImage("assets/3.png")

#objects
astro = Sprite("assets/astro.png")
ship = Sprite("assets/shipm.png")
fire = Sprite("assets/fire.png")
astro.set_position(janW/2 - astro.width/2, janH-astro.height)


#movements
velShip = 400
velAstro = 400
velFire = 400

#time
shootFireTime = 3
canShootFire = 0

#ships
x = 4
y = 2

fires = []
ships = []