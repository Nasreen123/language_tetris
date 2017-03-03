import pygame

#Define colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)


class Block(pygame.sprite.Sprite):
    def __init__(self, word, units):
        pygame.sprite.Sprite.__init__(self)
        #self.id = this_id
        self.x = 275
        self.y = 0
        self.word = word
        self.change_x = 0
        self.change_y = 0
        self.colors = [GREEN, BLUE, RED]
        self.color = self.colors[int(units)]
        self.test = False
        self.font_color = BLACK
        self.active = True
        self.length = units * 25 + 75
        self.image = pygame.Surface((self.length,50))
        self.rect = self.image.get_rect()
        self.collided_with = []


        ############# FIX RECTANGLES!!!
    def move(self, change_x, change_y):
        change_x = change_x * 25
        change_y = change_y * 3
        if self.x + change_x > 600:
            self.x = 600
        elif self.x + change_x < 0:
            self.x = 0
        else:
            self.x = self.x + change_x

        self.y += change_y
        self.rect.move_ip(change_x,0)
        self.rect.move_ip(0,change_y)


    def draw(self, screen):
        pygame.draw.rect(screen,self.color,[self.x,self.y,self.length,50],0)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render(self.word,True,self.font_color)
        screen.blit(text, [self.x+20, self.y+20])
