#pygame
from pygame import *

#other
import time as t
from random import randint

#import files
from font import *
from properties import *
from sound import *




img_backgraund = "img\\background.jpg" 
backgraund = transform.scale(image.load(img_backgraund), (500, 500))






#🐍 IMG/png/gif 🐍
img_win = "img\win.jpg" 
img_gameOver = "img\gamE_Over.jpeg" #фон проигрыша  img_los
img_backgraund = "img\\background.jpg" #img\spaceBackgraund.jpg
img_bullet = "img\img_bullet.png" 
img_hero = "img\spaceShip.png" #player_2
img_enemy = "img\shrecksons.png" #враг
img_bonus = "img\heart1.png"


#🐍CLASSES🐍
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


        


class Player(GameSprite):

    def update(self):   
        global level_player 
        
        if keys[K_a] and self.rect.x > 5 or keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
            
        if keys[K_d] and self.rect.x < win_width - 105 or keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
            
        if keys[K_s] and self.rect.y < win_height -120 or keys[K_DOWN] and self.rect.y < win_height -80:
            self.rect.y += self.speed/2
            
        if keys[K_w] and self.rect.y > 5 or keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed/2

        

        if keys[K_1]:            level_player = 1
        if keys[K_2]:            level_player = 2
        if keys[K_3]:            level_player = 3  
        if keys[K_4]:            level_player = 4
        if keys[K_5]:            level_player = 5
        if keys[K_6]:            level_player = 6
        if keys[K_7]:            level_player = 7
        if keys[K_0]:            window = display.set_mode((0,0),FULLSCREEN)
        if keys[K_9]:            run = False

        


    def fire1(self):
        bullet1  = Bullet (img_bullet, self.rect.centerx-5 , self.rect.top, 15, 60, -6)
        bullets.add(bullet1)
        sound_kick.play()

    def fire2(self):
        bullet1 = Bullet (img_bullet, self.rect.centerx+20 , self.rect.top, 15, 60, -6)
        bullet2 = Bullet (img_bullet, self.rect.centerx-20 , self.rect.top, 15, 60, -6)
        bullets.add(bullet1, bullet2)
        sound_kick.play()

    def fire3(self):
        bullet1 = Bullet (img_bullet, self.rect.centerx  , self.rect.top, 40, 20, -6)
        bullet2 = Bullet (img_bullet, self.rect.centerx-30 , self.rect.top, 40, 20, -6)
        bullet3 = Bullet (img_bullet, self.rect.centerx+30 , self.rect.top, 40, 20, -6)
        bullets.add(bullet1, bullet2, bullet3)
        sound_kick.play()
        sound_kick.play()

    def fire4(self):
        bullet1  = Bullet (img_bullet, self.rect.x  , self.rect.top, 40, 20, -6)
        bullets.add(bullet1)
        sound_kick.play()

    def fire5(self):
        bullet1  = Bullet (img_bullet, self.rect.x - 20  , self.rect.top, 40, 40, -2)
        bullet2  = Bullet (img_bullet, self.rect.x +20 , self.rect.top, 40, 40, -2)
        bullet3  = Bullet (img_bullet, self.rect.x  , self.rect.top, 40, 40, -4)
        bullet4  = Bullet (img_bullet, self.rect.x - 20 , self.rect.top - 5, 40, 40, -5)
        bullet5  = Bullet (img_bullet, self.rect.x  + 20, self.rect.top -5 , 40, 40, -5)
        bullets.add(bullet1, bullet2, bullet3, bullet4, bullet5)
        sound_kick.play()


    def fire6(self):
        bullet1  = Bullet (img_bullet, self.rect.x, self.rect.top-2, 40, 40, -2)
        bullet2  = Bullet (img_bullet, self.rect.x, self.rect.top, 40, 40, -2)
        
        bullets.add(bullet1, bullet2)
        sound_kick.play()


    def fire7(self):
        bullet1  = Bullet (img_bullet, self.rect.x, self.rect.top-2, 40, 40, -2)
        bullet2  = Bullet (img_bullet, self.rect.x, self.rect.top, 40, 40, -2)
        
        bullets.add(bullet1, bullet2)
        sound_kick.play()




#👽 Enemy 👽
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = 500#randint(80, win_width - 80)
            self.rect.y = 0
            global lost
            lost = lost + 1
    


class Bonuses(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = 500#randint(80, win_width - 80)
            self.rect.y = 0
            


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y <0:
            self.kill()







bullets = sprite.Group()
monsters = sprite.Group()
bonuses = sprite.Group()

window = display.set_mode((win_width, win_height))
backgraund = transform.scale(image.load(img_backgraund), (win_width, win_height))


finish = False
run = True
pause_value = False
pause_value_time_1 = t.time()


def game_start():
    global finish
    global ship, time_start ,score, lost, ammunition_player, ship_001
    score_to_next_lvl = 0
    score = 0
    lost = 0 
    finish = False
    ammunition_player = 1000
    
    ship = Player(img_hero, win_width/2-40, win_height-150, 100, 100, 10)
    ship_001 = Player(img_hero, win_width/2-40, win_height-150, 100, 100, 0)
    time_start = t.time()-0.1


    #delete monsters from the map
    for monster in monsters:
        monster.kill()

    #delete bullets from the map
    for bullet in bullets:
        bullet.kill()

    for bonus in bonuses:
        bonus.kill()


        

    #add monsters 
    for i in range(0,amount_enemy):
        monster1 = Enemy(img_enemy, randint(80, win_width - 80), -100, randint(50,80), randint (50,80), randint(1, 3))
        monsters.add(monster1)

    for i in range(0,1):
        bonus = Bonuses(img_bonus, randint(80, win_width - 80), -100, randint(50,80), randint (50,80), randint(1, 3))
        bonuses.add(bonus)

    
def lvl_up():
    global level_player, score_to_next_lvl
    level_player+=1

    score_to_next_lvl = 0
    for monster in monsters:
        monster.kill()
    if level_player > 5:
        #add monsters 
        for i in range(1):
            monster1 = Enemy(img_enemy, randint(80, win_width - 80), -100, 200, 200, 1)
            monsters.add(monster1)
    else:
        #add monsters 
        for i in range(0,amount_enemy):
            monster1 = Enemy(img_enemy, randint(80, win_width - 80), -100, randint(50,80), randint (50,80), randint(1, 3))
            monsters.add(monster1)



    

game_start()
while run:
    if score_to_next_lvl > 4:
        lvl_up()

 

    time_ALL = t.time()
    keys = key.get_pressed()

    for e in event.get():
        if e.type == QUIT or keys[K_ESCAPE]:
            run = False
    if keys[K_r]:   game_start()
        

    if not finish:
        if keys[K_p]:
            time_kd_pause = 1
            if pause_value == False and t.time() - pause_value_time_1 > time_kd_pause:
                pause_value_time_1 = t.time()
                pause_value = True

            elif pause_value == True and t.time() - pause_value_time_1 > time_kd_pause:
                pause_value_time_1 = t.time()
                pause_value = False

            
                
            
        
        if keys[K_SPACE]:
            if level_player == 1 and ammunition_player>0 and time_start+0.2<time_ALL:
                ship.fire1()
                ammunition_player-=1
                time_start = t.time()

            if level_player == 2 and ammunition_player>1 and time_start+0.3<time_ALL:
                ship.fire2()
                ammunition_player-=2
                time_start = t.time()

            if level_player == 3 and time_start+0.1<time_ALL:
                ship.fire3()
                time_start = t.time()

            if level_player ==4 and time_start+0.3<time_ALL:
                ship.fire4()

            if level_player ==5 and time_start+0.3<time_ALL:
                ship.fire5()
                ammunition_player-=5
                time_start = t.time()
                
            if level_player ==6 and time_start+0.7<time_ALL:
                ship.fire6()
                ammunition_player-=5
                time_start = t.time()

        if level_player ==7 and time_start+0.7<time_ALL:
            ship_001.fire1()
            time_start = t.time()




        if pause_value == False:
            window.blit(backgraund,(0, 0))
        
            ship_001.update()
            ship.update()
            monsters.update()
            bonuses.update()
            bullets.update()

        ship_001.reset()
        ship.reset()
        monsters.draw(window)
        bonuses.draw(window)
        bullets.draw(window)

        if pause_value == True:

            text = font3.render("Pause", 1, (130, 105, 255))   
            window.blit(text, (win_width/2-100, win_height/2-50))


              
   

        collides = sprite.groupcollide(monsters, bullets, True, True)
        collides_2 = sprite.spritecollide(ship, bonuses, True)


        #Text
        text = font1.render("Score: " + str(score)+ "/" + str(goal), 1, (130, 105, 255))   
        window.blit(text, (10, 10))
        
        text_lose = font2.render("Omitted: " + str(lost) + "/" + str(max_lost), 1, (255, 100, 100))
        window.blit(text_lose, (10, 40))
        
        text_level_player = font1.render("Level: " + str(level_player) , 1, (255, 255, 0))
        window.blit(text_level_player, (10, 70))

        text_ammunition_player = font1.render("Ammunition: " + str(ammunition_player) , 1, (130, 105, 255))
        window.blit(text_ammunition_player, (10, 90))
        

        text_Game_Over = font1.render("Press F to Pay Respects", 1, (10, 10, 10))
        place = text_Game_Over.get_rect(center = (200, 500))
        
        

        for c in collides:
            score += 1
            score_to_next_lvl +=1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -100, randint(50,80), randint(50,80), randint(1,1))
            monsters.add(monster)


        for c in collides_2:
            score += 10
            score_to_next_lvl +=1

            bonus = Bonuses(img_bonus, randint(80, win_width - 80), -100, randint(50,80), randint (50,80), randint(1, 3))
            bonuses.add(bonus)



        #Game Over
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True
            img = image.load(img_gameOver)
            mixer.music.stop()
            sound_gameOver.play()
            d = img.get_width() // img.get_height()
            #window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_height * d, win_height)), (-200, 0))
            window.blit(text_Game_Over, place)

        #Win
        if score >= goal:
            finish = True
            img = image.load(img_win)
            mixer.music.pause()
            sound_win.play()
            #window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))

        display.update()
        clock.tick(FPS)




