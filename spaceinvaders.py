from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.collision import *

from variables import janela, janH, janW, ms, key, backgroundStart, backgroundOptions, backgroundMenu
from variables import start, options, exit, menu, state
from variables import astro, velAstro, velFire, fire, velShip, ship
from variables import shootFireTime, canShootFire, x, y

def shipsMatrix(x, y):
    ships = []
    for i in range(x):
        line = []
        for j in range(y):
            ship = Sprite("assets/shipm.png")
            ship.x = 20 + i * ship.width * 1.5
            ship.y = 20 + j * ship.height * 1.5
            line.append(ship)
        ships.append(line)
    return ships

def designShips(ships):
    for line in ships:
        for ship in line:
            ship.draw()

def shootFire(fire, fires):
    fire = fire
    fire.set_position(astro.x + 45, astro.y - 10)
    fires.append(fire)
    return fires

def designFires(fires):
    for fire in fires:
        fire.y -= velFire * janela.delta_time()
        fire.draw()
    for fire in fires:
        if fire.y < 0:
            fires.remove(fire)

def pageStart():
    global state, shootFireTime, canShootFire, velShip, ship, fire
    ships = shipsMatrix(x, y)
    fires = []
    hitR = False
    hitL = False
    while state:
        if ms.is_over_object(menu):
            if ms.is_button_pressed(1):
                canShootFire = 0
                fires = []
                ships = []
                astro.set_position(janW/2 - astro.width/2, janH-astro.height)
                return

        # movimentação dos ships
        for line in ships:
            for ship in line:
                ship.x += velShip * janela.delta_time()

        if ships and ships[0]:
            if ships[0][0].x <= 0:
                hitL = True
                velShip *= -1

        if ships and ships[-1]:
            if ships[-1][-1].x >= janela.width - ship.width:
                velShip *= -1
                hitR = True

        if hitR or hitL:
            for line in ships:
                for ship in line:
                    ship.y += 10
            hitL = False
            hitR = False

        # movimentação do astro
        if astro.x >= 0:
            if key.key_pressed("LEFT"):
                astro.x -= velAstro * janela.delta_time()
        if astro.x <= janW - astro.width:
            if key.key_pressed("RIGHT"):
                astro.x += velAstro * janela.delta_time()

        # atirar fire e não atirar mais de um fire por vez 
        if key.key_pressed("UP"):
            if canShootFire == 0:
                shootFire(fire, fires)
                canShootFire += 1

        # recharge to shoot again
        if canShootFire != 0:
            canShootFire += janela.delta_time()
            if canShootFire >= shootFireTime:
                canShootFire = 0

        # Detect collisions between fires and ships
        for fire in fires:
            for line in ships:
                for ship in line:
                    if fire.collided(ship):
                        line.remove(ship)
                        fires.remove(fire)
                        break
                else:
                    continue
                break

        # Remove any empty lines in ships
        ships = [line for line in ships if line]

        # Check for collision with astro
        for line in ships:
            for ship in line:
                if ship.collided(astro):
                    return

        backgroundStart.draw()

        designFires(fires)
        designShips(ships)
        astro.draw()

        menu.draw()
        janela.set_title("Start")
        janela.update()

def pageMenu():
    global state
    while state:
        if ms.is_over_object(start):
            if ms.is_button_pressed(1):
                pageStart()

        if ms.is_over_object(options):
            if ms.is_button_pressed(1):
                pageOptions()

        if ms.is_over_object(exit):
            if ms.is_button_pressed(1):
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
        if ms.is_over_object(menu):
            if ms.is_button_pressed(1):
                pageMenu()

        backgroundOptions.draw()
        menu.draw()

        janela.set_title("Options")
        janela.update()

while state:
    pageMenu()
