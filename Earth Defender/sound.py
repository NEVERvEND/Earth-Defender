from pygame import *

#🐍 SOUND 🐍
mixer.init()
#backgaraund_sound
mixer.music.load('Sounds\sounds_backgraund.mp3')
mixer.music.set_volume(1)
mixer.music.play()

sound_win = mixer.Sound('Sounds\sounds_win.mp3')
sound_kick = mixer.Sound('Sounds\sounds_bullet.mp3') #bullet
sound_kick.set_volume(0.2)
sound_gameOver = mixer.Sound('Sounds\sounds_gameOver.mp3')

from pygame import *
mixer.init()
sound_win = mixer.Sound('Sounds\sounds_win.mp3')
sound_game_o = mixer.Sound('Sounds\sounds_win.mp3')

mixer.music.play()