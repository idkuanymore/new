#Создай собственный Шутер!

from random import *
from pygame import *

font.init()
font1 = font.Font(None, 80)
win = font1.render('you win', True, (225, 225, 225))
lose = font1.render('you lose', True, (180, 0, 0))
font2 = font.Font(None, 36)

score = 0
max_lost = 3

global number
lost = 0
number = 0

class Gamesp(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesp):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_RIGHT] and self.rect.x < 690:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed

    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

class Enemy(Gamesp):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_height - 80)
            self.rect.y = 0
            lost += 1

class Bullet(Gamesp):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

win_width = 700
win_height = 500

wind = display.set_mode((win_width, win_height))
display.set_caption('shooter')
bg = transform.scale(image.load('galaxy.jpg'), (700, 500))
wind.blit(bg, (0, 0))

clock = time.Clock()
fps = 128

x = 350
y = 425
rocket = Player('rocket.png', x, y, 10)

enemies = sprite.Group()

for i in range(1,6):
    enemy = Enemy('ufo.png', randint(10, win_width - 80), 10, randint(4,8))
    enemies.add(enemy)

bullets = sprite.Group()

finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == K_DOWN:
            if e.type == K_SPACE:
                rocket.fire()

    if not finish:        
        wind.blit(bg, (0, 0))
        text_win = font2.render('Score: ' + str(score), 1, (0, 0, 0))
        text_lose = font2.render('Lost: ' + str(lost), 1, (0, 0, 0))
        wind.blit(text_lose, (10, 50))


        rocket.update()
        enemy.update()
        bullets.update()

        rocket.reset()
        enemies.draw(wind)
        bullets.draw(wind)

        display.update() 
    clock.tick(fps)
    time.delay(50)