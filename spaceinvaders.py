from PPlay.window import * 
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from pages import pageStart, pageOptions

janW = 960
janH = 540 
janela = Window(janW, janH)
janela.set_title("Space Invaders")
key = keyboard.Keyboard()
mouse = mouse.Mouse()
background = GameImage("assets/b.png")

start = Sprite("assets/start.png")
exit = Sprite("assets/exit.png")
options = Sprite("assets/options.png")
start.set_position(janW/2 - start.width/2, janH/2 - start.height/2)
options.set_position(janW/2 - start.width/2, (janH/2 - start.height/2) + 75)
exit.set_position(janW/2 - start.width/2, (janH/2 - start.height/2) + 150)

while True:
    if(mouse.is_over_object(start)):
        if(mouse.is_button_pressed(1)):
            pageStart()
    
    if(mouse.is_over_object(options)):
        if(mouse.is_button_pressed(1)):
            pageOptions()
    
    if(mouse.is_over_object(exit)):
        if(mouse.is_button_pressed(1)):
            break
            
    
    background.draw()

    start.draw()
    options.draw()
    exit.draw()

    janela.update()