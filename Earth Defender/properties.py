from pygame import *
 


#title
display.set_caption("Шутер")

win_width, win_height = 1200 , 700
FPS = 70

clock = time.Clock()


#⚙️properties/свойства⚙️
amount_enemy = 3    #amount enemy from maps

speed_player = 8
level_player = 1    #player shooting styles 
ammunition_player = 500 #ammo

score = 0   # сбито кораблей/score
goal = 100  # столько кораблей нужно сбить для победы

lost = 0 # пропущено кораблей
max_lost = 7 # проиграли, если пропустили столько
# инвертировать если нужно на убывание


score_to_next_lvl = 0