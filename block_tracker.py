import pygame

class Tracker():
    def __init__(self):
        self.blocks = []
        self.all_blocks = pygame.sprite.Group()
        self.landed_blocks = pygame.sprite.Group()

    def check(self,block):
        collided_list = []
        if block.active == True:
            if block.y >= (445):
                print 'hit bottom'
                #block.test = True
                self.landed_blocks.add(block)
                block.active = False
            elif pygame.sprite.spritecollideany(block, self.landed_blocks, False):
                print 'collided'
                collided_list = pygame.sprite.spritecollide(block, self.landed_blocks, False)
                self.landed_blocks.add(block)
                block.active = False
        """if len(collided_list) > 0:
            collided = collided_list[0]
        else:
            collided = None"""
        return block, collided_list

    """    def check(self,block):
        collided_list = []
        if block.active == True:
            if pygame.sprite.spritecollideany(block, self.landed_blocks, False): #check for collisions
                print 'collided'
                #collided_list = pygame.sprite.spritecollide(block, self.landed_blocks, False)
                block.collided_with = pygame.sprite.spritecollide(block, self.landed_blocks, False)
                self.landed_blocks.add(block)
                block.active = False
            elif block.y >= (445): #if not collisions check if landed at bottom
                print 'hit bottom'
                #block.test = True
                self.landed_blocks.add(block)
                block.active = False
        #if len(collided_list) > 0:
        #    collided = collided_list[0]
        #else:
        #    collided = None
        return block #, collided_list"""



    def check_aligned(self,block1,block2):
        if block2:
            if abs(block1.x - block2.x) < 26 or (block1.x + block1.length) == block2.x:
                return True, block1, block2
        return False, block1, block2
