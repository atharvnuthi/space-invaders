from PPlay.window import * 
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *

from variables import janela, janH, janW, ms, key, backgroundStart, backgroundOptions, backgroundMenu, start, options, exit, menu, state, astro, ship

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
    while state:
        if(ms.is_over_object(menu)):
            if(ms.is_button_pressed(1)):
                pageMenu()
        
        backgroundStart.draw()
        menu.draw()
        astro.draw()
        ship.draw()
        janela.set_title("Space Invaders - Start")
        janela.update()

def pageOptions():
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