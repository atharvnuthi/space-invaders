from PPlay.window import * 
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *

from variables import janela, janH, janW, ms, key, backgroundStart, backgroundOptions, backgroundMenu
from variables import start, options, exit, menu, state, astro, velAstro, velFire, fires, fire, velShip, ships, ship, shootFireTime, canShootFire, x, y

def shipsMatrix(x,y):
    global ships
    for i in range(x):
        line = []
        for j in range(y):
            ship = Sprite("assets/shipm.png")
            ship.x = 20 + i * ship.width * 1.5
            ship.y = 20 + j * ship.height * 1.5
            line.append(ship)
        ships.append(line)

def designShips():
    global ships
    for line in ships:
        for ship in line:
            ship.draw()

def shootFire(): 
    global fires, fire
    fire = fire
    fire.set_position(astro.x+45, astro.y-10)
    fires.append(fire)

def designFires():
    global fires
    for fire in fires:
        fire.y -= velFire * janela.delta_time()
        fire.draw()
    for fire in fires:
        if fire.y < 0:
            fires.remove(fire)

def pageStart():
    global state, shootFireTime, canShootFire, fires, ships, velShip
    bateu_r = False
    bateu_l = False
    bt = 0
    pi_x = 0
    pi_y = 0
    while state:
        if(ms.is_over_object(menu)):
            if(ms.is_button_pressed(1)):
                canShootFire = 0
                fires = []
                astro.set_position(janW/2 - astro.width/2, janH-astro.height)
                pageMenu()
        
        shipsMatrix(x,y)
        pi_x = ships[0][0].x
        pi_y = ships[0][0].y

        #movimentação dos ships
        for line in ships:
            for ship in line:
                ship.x += velShip * janela.delta_time()

                if ship.x <= 0:
                    bateu_r = True
                    velShip *= -1
                    for line in ships:
                        for ship in line:
                            ship.x += 1

                if ship.x >= janela.width - ship.width:
                    velShip *= -1
                    bateu_l = True
                    for line in ships:
                        for ship in line:
                            ship.x -= 1

                if bateu_r == True or bateu_l == True:
                    for line in ships:
                        for ship in line:
                            ship.y += janela.height//20
                    bateu_l = False
                    bateu_r = False
                    bt = 1

        pi_x += velShip * janela.delta_time()
        if bateu_r == True:
            pi_x += 1
        if bateu_l == True:
            pi_x -= 1
        if bt == 1:
            pi_y += janela.height // 20
            bt = 0
        
        if astro.x >= 0:
            if(key.key_pressed("LEFT")):
                astro.x -= velAstro * janela.delta_time()
        if astro.x <= janW - astro.width:
            if(key.key_pressed("RIGHT")):
                astro.x += velAstro * janela.delta_time()

        if key.key_pressed("UP"):
            if canShootFire == 0:
                shootFire()
                canShootFire += 1

        #recharge to shoot again
        if canShootFire != 0:
            canShootFire += janela.delta_time()
            if canShootFire >= shootFireTime:
                canShootFire = 0

        backgroundStart.draw()
        
        designFires()
        astro.draw()
        designShips()

        menu.draw()
        janela.set_title("Start")
        janela.update()

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

        janela.set_title("Menu")
        janela.update()

def pageOptions():
    global state, velAstro, velFire
    while state: 
        if(ms.is_over_object(menu)):
            if(ms.is_button_pressed(1)):
                pageMenu()

        backgroundOptions.draw()
        menu.draw()

        janela.set_title("Options")
        janela.update()

while state == True:
    pageMenu()