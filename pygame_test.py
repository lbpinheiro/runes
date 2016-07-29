import pygame, sys,os
from pygame.locals import * 
import rune
import grid
import player

pygame.init() 
columns = 10
lines = 10
window = pygame.display.set_mode((columns * 15, lines * 15)) 
pygame.display.set_caption('Runes') 
screen = pygame.display.get_surface() 

r = rune.Rune()
g = grid.Grid(lines, columns)
print str(g)

i_offset = 0
for i in range(g._y):
	for j in range(g._x):
		screen.blit(g._column[i][j].get_image(), (i_offset, j * 15)) 		
	i_offset += 15		

pygame.display.flip()
p = player.Player('lucas', 20)

def input(events): 
	for event in events: 
		if event.type == QUIT: 
			sys.exit(0)
		elif event.type == MOUSEBUTTONUP:
			j = event.pos[0]/15
			print 'clicl j=' + str(j) + ' _x=' + str(g._x)
			if j > g._y -1:
				continue
			i = event.pos[1]/15
			print 'clicl i=' + str(i) + ' _x=' + str(g._x)			
			if i > g._x -1:
				continue	
			print 'j=' + str(j)
			print 'i=' + str(i)
			print str(g._column[j][i])
			g.change_state(j, i, p)

			#screen.blit(g._column[j][i]._image_hl, (j * 15, i * 15))
			i_offset = 0
			for _i in range(g._y):
				for _j in range(g._x):
					screen.blit(g._column[_i][_j].get_image(), (i_offset, _j * 15)) 		
				i_offset += 15	

			print str(g)
			pygame.display.flip()
			pygame.time.delay(200)
			print str(p)
 
while True: 
   input(pygame.event.get()) 

