# Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. When user presses Up, Down, Left,
# Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed key. The ball should
# not leave the screen, i.e. user input that leads the ball to leave of the screen should be ignored
import pygame

pygame.init()
screen = pygame.display.set_mode(size=(200, 200))
clock = pygame.time.Clock()
running = True

time_since_last_frame = 0

circle_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    speed = 20 * time_since_last_frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        width, height = screen.get_size()
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP:
                    next_y = circle_position.y - speed

                    if (next_y - 25) > 0:
                        circle_position.y = next_y
                case pygame.K_DOWN:
                    next_y = circle_position.y + speed

                    if (next_y + 25) < heigh:
                        circle_position.y = next_y
                case pygame.K_LEFT:
                    next_x = circle_position.x - speed

                    if (next_x - 25) > 0:
                        circle_position.x = next_x
                case pygame.K_RIGHT:
                    next_x = circle_position.x + speed

                    if (next_x + 25) < width:
                        circle_position.x = next_x

    screen.fill("white")

    pygame.draw.circle(surface=screen, color="red", center=circle_position, radius=25)

    pygame.display.flip()
    time_since_last_frame = clock.tick(100) / 100

pygame.quit()
