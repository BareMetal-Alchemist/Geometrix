import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
running = True
dt = 0
movement_speed = 1000
other_speed = 1
radius = 20
grid_size = 100
line_color = ("white")



player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
other_pos = pygame.Vector2(player_pos.x, player_pos.y - 600)
swtch = 1

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    
    for x in range(0, screen.get_width(), grid_size):
        pygame.draw.line(screen, line_color, (x,0), (x, screen.get_height()))

    for y in range(0, screen.get_height(), grid_size):
        pygame.draw.line(screen, line_color, (0, y), (screen.get_width(), y))

    pygame.draw.circle(screen, "green", player_pos, radius)
    pygame.draw.circle(screen, "red", other_pos, radius)
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_w]:
       player_pos.y -= movement_speed * dt
    if keys[pygame.K_s]:
        player_pos.y += movement_speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= movement_speed * dt
    if keys[pygame.K_d]:
        player_pos.x += movement_speed * dt

    
        
    #if other_pos.x <= 43 or other_pos.x >= 750:
    #    swtch *= -1
    other_pos.x += ((player_pos.x-other_pos.x)/0.1)*dt
    other_pos.y += ((player_pos.y-other_pos.y)/0.1)*dt
    
    dst = math.sqrt((player_pos.x - other_pos.x)**2 + (player_pos.y - other_pos.y)**2)
    
    if dst < (radius*2)-1:
        screen.fill("white")
        print("Game Over")
        running = False
        
    pygame.display.flip()

    dt = clock.tick(120) / 1000

pygame.quit()
