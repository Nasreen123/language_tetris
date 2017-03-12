import pygame

class Tracker():
    def __init__(self):
        self.blocks = [] #keeps active landed and falling off blocks
        self.landed_blocks = pygame.sprite.Group()

    def check(self,block):
        collided_list = []
        if block.y >= (445): #block hit floor
            print 'hit bottom'
            self.landed_blocks.add(block)
            block.active = False
        elif pygame.sprite.spritecollideany(block, self.landed_blocks, False):
            print 'collided'
            collided_list = pygame.sprite.spritecollide(block, self.landed_blocks, False)
            self.landed_blocks.add(block)
            block.active = False

        return block, collided_list

    def remove_block_from_landed_sprites(self, block):
        self.landed_blocks.remove(block)
