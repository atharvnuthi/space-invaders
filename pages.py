from PPlay.window import * 
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *

janW = 960
janH = 40 
janela = Window(janW, janH)
key = keyboard.Keyboard()
mouse = mouse.Mouse()
background = GameImage("assets/start_background.png")

def pageStart():
    while True:
        background.draw()
        janela.update()

def pageOptions():
    print("Options")