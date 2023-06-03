from PPlay.window import * 
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *

from variables import janela, janH, janW, ms, key, backgroundStart, backgroundOptions, backgroundMenu
from variables import start, options, exit, menu, state, astro, ship, velAstro, velFire, fires, fire

def shoot(): 
    fire.set_position(astro.x+45, astro.y-10)

def shoots():
    fire.y -= velFire * janela.delta_time()
    fire.draw()

def pageMenu():
    global state
    while state: 
        if(ms.is_over_object(start)):
            if(ms.is_button_pressed(1)):
                pageStart()
                        
        if(ms.is_over_object(options)):
            if(ms.is_button_pressed(1)):
                pageOptions()
                    
        if(ms.is_over_object(exit)):
            if(ms.is_button_pressed(1)):
                state = False
                        
        backgroundMenu.draw()
        start.draw()
        options.draw()
        exit.draw()

        janela.set_title("Space Invaders - Menu")
        janela.update()

def pageStart():
    global state
    while state:
        if(ms.is_over_object(menu)):
            if(ms.is_button_pressed(1)):
                pageMenu()
        
        if astro.x >= 0:
            if(key.key_pressed("LEFT")):
                astro.x -= velAstro * janela.delta_time()
        if astro.x <= janW - astro.width:
            if(key.key_pressed("RIGHT")):
                astro.x += velAstro * janela.delta_time()

        if key.key_pressed("UP"):
            shoot()

        if fire.collided(ship):
            ship.hide()
            fire.hide()

        backgroundStart.draw()
        menu.draw()
        astro.draw()
        ship.draw()

        shoots()

        janela.set_title("Space Invaders - Start")
        janela.update()

def pageOptions():
    global state, velAstro, velFire
    while state: 
        if(ms.is_over_object(menu)):
            if(ms.is_button_pressed(1)):
                pageMenu()

        backgroundOptions.draw()
        menu.draw()

        janela.set_title("Space Invaders - Options")
        janela.update()

while state == True:
    pageMenu()