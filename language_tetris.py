import pygame
import networkx as nx
import graph_stuff
import word_logic
import block_builder
import block_tracker
import game_functions

pygame.init()

#Open window for game
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Language-Tetris")

#####Declare game variable:#####
game_over = False #Runs until closed
clock = pygame.time.Clock() ##Manage speed
tracker = block_tracker.Tracker()
sentences = word_logic.sentences
graph = nx.MultiGraph()#graph to store block collision info
#Define colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

change_y = 1
change_x = 0

###### MAIN LOOP #####
while not game_over:

    #####Main event loop: (ALL USER EVENTS SHOULD GO HERE)
    for event in pygame.event.get(): #user does something
        if event.type == pygame.QUIT: #if user closes:
            print 'quit pressed'
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_x = -1
            if event.key == pygame.K_RIGHT:
                change_x = 1
            if event.key == pygame.K_DOWN:
                change_y = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                change_x = 0
            elif event.key == pygame.K_DOWN:
                change_y = 1

    ###### Game logic goes here: ######

    #~~Add new block when there are no active blocks
    if len(tracker.blocks) <1 or tracker.blocks[len(tracker.blocks)-1].active == False:
        word, units = word_logic.get_word()
        block = block_builder.Block(word,units,(GREEN, BLUE, RED),BLACK)
        tracker.blocks.append(block)
        graph = graph_stuff.add_node(graph, block) #add block to graph
        #print 'graph ', graph.nodes()
        #for block in tracker.blocks:
        #    print block.active


    #~~Draw new screen:
    screen.fill(WHITE)

    #iterate through blocks
    for block in tracker.blocks:
        #tracker.check takes a block, and compares it against self.landed_blocks
        #it returns block, block it collided with (none if none)
        #***Later this needs to handle more than one collisions

        if block.active:
            block, collided_with = tracker.check(block)

            if collided_with: #if block collided with other blocks:
                print block.word, 'collided with ',
                for each in collided_with:
                    print each.word,
                print '\n'

                for each_block in collided_with:
                    graph = graph_stuff.add_collision(graph, block, each_block) #add collision edges to graph
                    sentence_forming_blocks = graph_stuff.search_graph(graph, sentences) #check if sentences formed

                    if sentence_forming_blocks:
                        graph = graph_stuff.remove_nodes(graph, sentence_forming_blocks) #so no longer count to making sentences
                        for block in sentence_forming_blocks:
                            block.color = WHITE # white blocks will fall off the screen
                            tracker.remove_block_from_landed_sprites(block) #so no longer detect collisions while they are falling


        #move block
        if block.active == True: #if it didn't collide it should keep falling
            block.move(change_x, change_y)
        elif block.color == WHITE: #it has been used to form a sentence so it should fall off screen
            block.move(0, 1)

        # draw block
        block.draw(screen)

    game_over = game_over or game_functions.is_game_done(block)

    pygame.display.update()

    clock.tick(30) #limit to 60 frames per second


pygame.quit() #End game properly
