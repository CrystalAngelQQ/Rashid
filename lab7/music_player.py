import os, pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(size=(1280, 720))
clock = pygame.time.Clock()
running = True

default_font = pygame.font.Font(None, 48)

floating_text = "Keys: h for play, j for stop, k for next and l for previous"
status_text = "Status: music player started"

music_dir = os.listdir("музыка")
num_tracks = len(music_dir)

music_i = 0

while running:
    current_song_name = music_dir[music_i]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status_text = "Status: exiting..."
            running = False
        if event.type == pygame.KEYDOWN:
            match event.key:
                # Keys: h for play, j for stop, k for next and l for previous
                case pygame.K_h:
                    pygame.mixer.music.play()
                    status_text = "Status: started"
                case pygame.K_j:
                    pygame.mixer.music.stop()
                    status_text = "Status: stopped"
                case pygame.K_k:
                    music_i = (music_i + 1) % num_tracks
                    pygame.mixer.music.play()
                case pygame.K_l:
                    music_i = (music_i - 1) % num_tracks
                    pygame.mixer.music.play()

    floating_text_rendered = default_font.render(floating_text, True, "black")
    status_text_rendered = default_font.render(status_text, True, "black")
    current_song_name_text_rendered = default_font.render(
        current_song_name, True, "black"
    )

    pygame.mixer.music.load(os.path.join("music", current_song_name))

    screen.fill("orange")
    screen.blit(floating_text_rendered, (0, 0))
    screen.blit(status_text_rendered, (0, 50))
    screen.blit(current_song_name_text_rendered, (0, 100))
    pygame.display.flip()

pygame.quit()
