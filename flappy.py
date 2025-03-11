import pygame
import random
from random import randint,choice



#class 
class Flap(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        flapy= pygame.image.load("D:\python Games\\flappy\\flappy.png")
        self.image = flapy
        self.rect = self.image.get_rect(center=(100,400))
        self.gravity=0
        
        # self.game_stat= True
    def player_input(self):
        mouse =pygame.mouse.get_pressed()
        if mouse[0]:
            self.gravity=-6
    def gravityFunc(self):
        self.gravity+=0.2
        self.rect.y +=int(self.gravity)
        if self.rect.bottom>500:
            self.rect.bottom=500
            self.gravity=0
            
            
    def update(self):
        self.player_input()
        self.gravityFunc()   

class Pipe(pygame.sprite.Sprite):
    def __init__(self,x):
        super().__init__()
        
        top_p = pygame.image.load("D:\python Games\\flappy\\top_pipe.png").convert_alpha()
        down_p=pygame.image.load("D:\python Games\\flappy\\down_pipe.png").convert_alpha()
        
        self.top_image = top_p
        self.down_image = down_p
        self.bot=randint(130,280)
        self.top_rect = self.top_image.get_rect(midbottom =(x,self.bot)) 
        self.down_rect = self.down_image.get_rect(midtop =(x,self.bot+160)) 
                      
    
    def animation(self):
        self.top_rect.x-=4
        self.down_rect.x-=4
        if self.top_rect.right<-100:
            self.kill() 
        
    def draw_pipe(self, screen):
        screen.blit(self.top_image, self.top_rect)
        screen.blit(self.down_image, self.down_rect)           
    
    def update(self,screen):
        self.animation()
        self.draw_pipe(screen)
 
 
#functions
def collision():
    global gameScore
    
    if not ob_pipe:
        return True
    for pipe in ob_pipe:
        if play_bird.sprite.rect.colliderect(pipe.top_rect) or play_bird.sprite.rect.colliderect(pipe.down_rect):
            return False 
        
        if pipe not in passed_pipes and  pipe.top_rect.right < play_bird.sprite.rect.left:
            gameScore += 1
            passed_pipes.add(pipe)
            
            
    return True

    
    
           
          
#initial
pygame.init()
window = pygame.display.set_mode((800,500))
pygame.display.set_caption("flappy bird")
clock = pygame.time.Clock()
#variables
global game_stat 
game_stat= True
run = True
global gameScore
gameScore=0
passed_pipes = set()

#class calls
play_bird=pygame.sprite.GroupSingle()
play_bird.add(Flap())
ob_pipe = pygame.sprite.Group()

#texts
gameOver = pygame.font.Font(None,62)

#surfaces
sky = pygame.image.load("D:\python Games\\flappy\\back_sky.jpg")
outSurf= gameOver.render("BIRD DIED", True, (255,0,0))
out_rect= outSurf.get_rect(center = (400,250))
#user events
piper = pygame.USEREVENT +1
pygame.time.set_timer(piper,1600)

#game loop
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == piper:
            ob_pipe.add(Pipe(randint(830,900)))
        if game_stat==False:
            
            if event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_stat = True
                ob_pipe.empty()
                passed_pipes.clear()
                gameScore=0
    if game_stat:
        window.blit(sky,(0,0))
        play_bird.draw(window)
        play_bird.update()
        for pipe in ob_pipe:
            pipe.draw_pipe(window)
        # ob_pipe.draw(window)
        ob_pipe.update(window)

        #collisions
        game_stat= collision()
        # score
        
        fscore= pygame.font.Font(None, 28)
        scoreSurf=fscore.render(f"Score:{gameScore}",True,(255,255,255))
        window.blit(scoreSurf,(700,20))
    else:
        # window.blit(sky,(0,0))
        window.blit(outSurf,out_rect)
          
        
    #updates
    clock.tick(60)        
    pygame.display.update()
    