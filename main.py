import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
running = True
dt = 0
movement_speed = 1000

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
other_pos = pygame.Vector2(player_pos.x, player_pos.y - 100)
swtch = 1
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    pygame.draw.circle(screen, "green", player_pos, 40)
    pygame.draw.circle(screen, "red", other_pos, 40)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
       player_pos.y -= movement_speed * dt    
    if keys[pygame.K_s]:
        player_pos.y += movement_speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= movement_speed * dt
    if keys[pygame.K_d]:
        player_pos.x += movement_speed * dt
    if keys[pygame.K_SPACE]:
        movement_speed = 500
    else:
        movement_speed = 1000
    # print(player_pos)
    # swtch = 1
        
    if other_pos.x <= 43 or other_pos.x >= 750:
        print("run")
        swtch *= -1
    other_pos.x += (swtch*50)*dt
    print(swtch)

    dst = math.sqrt((player_pos.x - other_pos.x)**2 + (player_pos.y - other_pos.y)**2)
    
    if dst < 70:
        print("Game Over")
        running = False
            
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
