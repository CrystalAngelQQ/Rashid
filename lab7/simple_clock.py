import pygame, time


# Работает только с квадратными спрайтами.
def rot_center(image: pygame.Surface, angle: float):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


display_size = [1400, 1050]

display_half_size = [i / 2 for i in display_size]

pygame.init()
screen = pygame.display.set_mode(size=display_size)

running = True

mickey_clock_image = pygame.image.load("mickeyclock.jpg")
left_arrow_image = pygame.image.load("mickey_left_arrow.png")
right_arrow_image = pygame.image.load("mickey_right_arrow.png")

mickey_clock = pygame.transform.scale(mickey_clock_image, display_size)
left_arrow = pygame.transform.scale(left_arrow_image, (240, 115))
right_arrow = pygame.transform.scale(right_arrow_image, (301, 83))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    screen.blit(mickey_clock, (0, 0))

    # localtime
    localtime = time.localtime()

    # left arrow - seconds
    seconds = localtime.tm_sec
    seconds_as_angle = (seconds * 6) + 90
    rotated_left_arrow = rot_center(image=left_arrow_image, angle=-seconds_as_angle)
    screen.blit(rotated_left_arrow, display_half_size)

    # right arrow - minutes
    minutes = localtime.tm_min
    minutes_as_angle = minutes * 6 + 90
    rotated_right_arrow = rot_center(image=right_arrow_image, angle=-seconds_as_angle)
    screen.blit(rotated_right_arrow, display_half_size)

    pygame.display.flip()

pygame.quit()
