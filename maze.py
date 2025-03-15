from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, p_speed):
        super().__init__()
        self.image = transform.scale(image.load(p_image),(60,60))
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
        self.speed = p_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update_e(self):
        if self.rect.x <= 5:
            self.direction = 'right'
        if self.rect.x >= win_width - 70:
            self.direction = 'left'
        if self.rect.y <= 5:
            self.direction = 'right'
        if self.rect.y >= 480:
            self.direction = 'left'
        

        if self.direction == 'left':
            self.rect.x -= self.speed
            self.rect.y -= 1
        else:
            self.rect.x += self.speed
            self.rect.y += 1 

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
 
        # картинка стены - прямоугольник нужных размеров и цвета
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
 
        # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
 
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))


w1 = Wall(90, 60, 0, 50, 20 , 600, 10)
w2 = Wall(90, 60, 0, 640, 20, 10, 380)
w3 = Wall(90, 60, 0, 50, 20 , 10, 380)
w4 = Wall(90, 60, 0, 140, 110, 410, 10 )
w5 = Wall(90, 60, 0, 140, 110 , 10, 290)
w6 = Wall(90, 60, 0, 550, 110 , 10, 290)
w7 = Wall(90, 60, 0, 230, 200 , 10, 280)
w8 = Wall(90, 60, 0, 230, 200 , 230, 10)
w9 = Wall(90, 60, 0, 460, 200 , 10, 200)
w10 = Wall(90, 60, 0, 350, 200 , 10, 280)
w11 = Wall(90, 60, 0, 460, 400 , 100, 10)


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))

monster_y = randint(300,390)
monster_speed = randint(1,3)
'''monster_t_y = randint(170,250)'''

player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('monst.png', win_width - 80, monster_y, monster_speed )
final = GameSprite('ppp.png', win_width - 120, win_height - 80, 0)
'''monster_t = Enemy('monst.png', win_width - 80, monster_t_y, monster_speed +1 )'''

display.set_caption('Игра')
background = transform.scale(image.load('background.jpg'),(700,500))


game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.SysFont('Arial', 70)
win = font.render('Победа!', True, (209, 150, 0))
lose = font.render('Поражение!', True, (133, 0, 0))


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('win.ogg')
kick = mixer.Sound('ooo.ogg')

while game:
    
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))        
        player.update()
        monster.update_e()
        monster.reset()        
        '''monster_t.update_e()'''
        player.reset()
        
        '''monster_t.reset()'''
        final.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()




        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2)or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8)or sprite.collide_rect(player, w9) or sprite.collide_rect(player, w10) or sprite.collide_rect(player, w11):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()

    display.update()
    clock.tick(FPS)
    

    