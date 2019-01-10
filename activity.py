import pygame as public
from map import *

public.init()
tela = public.display.set_mode((1000, 500))
cam = [0, 0]
jump = False
clock = public.time.Clock()

map = mapa

asset1 = public.image.load("assets/asset1.png")
asset1 = public.transform.scale(asset1, (50, 50))
asset2 = public.image.load("assets/asset2.png")
asset2 = public.transform.scale(asset2, (50, 50))
asset3 = public.image.load("assets/asset3.png")
asset3 = public.transform.scale(asset3, (50, 50))

class Player(public.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = asset2
        self.rect = self.image.get_rect()
        self.rect.center = (500, 250)
    def update(self):
        if cam[1] >= -1000:
            cam[1] += 10
        if cam[1] <= 500:
            cam[1] -= 10



class Sprite(public.sprite.Sprite):
    def __init__(self, x, y, asset):
        super().__init__()
        self.asset = asset
        self.x = x
        self.y = y
        self.image = self.asset
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x = self.x + cam[0]
        self.rect.y = self.y + (cam[1] + 100)


sprite = public.sprite.Group()

player = Player()


for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == 0:
            sprite.add(Sprite(50 * x, 50 * y, asset1))
        if map[y][x] == 1:
            tile1 = Sprite(50 * x, 50 * y, asset3)
            sprite.add(tile1)


sprite.add(player)
run = True
while run:
    tela.fill((0, 0, 255))
    sprite.draw(tela)
    sprite.update()
    for e in public.event.get():
        if e.type == public.QUIT:
            run = False
        k = public.key.get_pressed()
        if k[public.K_LEFT]:
            cam[0] += 50
        elif k[public.K_RIGHT]:
            cam[0] -= 50
        elif k[public.K_UP]:
            cam[1] += 50
        elif k[public.K_DOWN]:
            cam[1] -= 50
        elif k[public.K_BACKSPACE]:
            jump = True
    clock.tick(60)
    public.display.update()
