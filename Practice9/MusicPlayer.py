import pygame
import os
import sys

def main():
    pygame.init()
    pygame.mixer.init()
    
    WIDTH, HEIGHT = 600, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Modern Music Player + Seeker")
    
    font_main = pygame.font.SysFont("Segoe UI", 24, bold=True)
    font_sub = pygame.font.SysFont("Segoe UI", 16)
    
    music_dir = "assets"
    songs = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
    if not songs: sys.exit()

    
    try:
        
        bg_image = pygame.image.load("assets/music_box.png").convert()
        bg_image = pygame.transform.smoothscale(bg_image, (WIDTH, HEIGHT))
    except:
        bg_image = None

    current_idx = 0
    is_playing = False
    volume = 0.5
    pygame.mixer.music.set_volume(volume)

    
    song_pos_pct = 0.0  
    ESTIMATED_LENGTH = 300 

    
    prog_x, prog_y, prog_w, prog_h = 100, 350, 400, 6  
    vol_x, vol_y, vol_w, vol_h = 150, 430, 300, 6      
    
    knob_vol_x = vol_x + int(volume * vol_w)
    knob_prog_x = prog_x

    def play_song(start_time=0):
        pygame.mixer.music.load(os.path.join(music_dir, songs[current_idx]))
        
        pygame.mixer.music.play(0, start_time)

    clock = pygame.time.Clock()
    running = True
    while running:
        
        if bg_image:
            screen.blit(bg_image, (0, 0))
            
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 160)) 
            screen.blit(overlay, (0, 0))
        else:
            screen.fill((20, 20, 30))

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if not is_playing:
                        play_song()
                        is_playing = True
                    else:
                        pygame.mixer.music.unpause()
                elif event.key == pygame.K_s:
                    pygame.mixer.music.pause()
                elif event.key == pygame.K_n:
                    current_idx = (current_idx + 1) % len(songs)
                    play_song()
                    is_playing = True
                elif event.key == pygame.K_b:
                    current_idx = (current_idx - 1) % len(songs)
                    play_song()
                    is_playing = True

        
        if mouse_click[0]:
            
            if vol_x <= mouse_pos[0] <= vol_x + vol_w and vol_y - 10 <= mouse_pos[1] <= vol_y + 10:
                knob_vol_x = mouse_pos[0]
                volume = (knob_vol_x - vol_x) / vol_w
                pygame.mixer.music.set_volume(volume)
        
    
            if prog_x <= mouse_pos[0] <= prog_x + prog_w and prog_y - 10 <= mouse_pos[1] <= prog_y + 10:
                knob_prog_x = mouse_pos[0]
                song_pos_pct = (knob_prog_x - prog_x) / prog_w
                
                seek_time = song_pos_pct * ESTIMATED_LENGTH
                play_song(start_time=int(seek_time))
                is_playing = True

        
        title = font_main.render(songs[current_idx], True, (255, 255, 255))
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))

        
        pygame.draw.rect(screen, (80, 80, 80), (prog_x, prog_y, prog_w, prog_h), border_radius=10)
        pygame.draw.rect(screen, (0, 255, 150), (prog_x, prog_y, knob_prog_x - prog_x, prog_h), border_radius=10)
        pygame.draw.circle(screen, (255, 255, 255), (knob_prog_x, prog_y + prog_h//2), 8)
        
        prog_label = font_sub.render("Seek", True, (200, 200, 200))
        screen.blit(prog_label, (prog_x - 50, prog_y - 8))

        
        pygame.draw.rect(screen, (60, 60, 60), (vol_x, vol_y, vol_w, vol_h), border_radius=10)
        pygame.draw.rect(screen, (0, 150, 255), (vol_x, vol_y, knob_vol_x - vol_x, vol_h), border_radius=10)
        pygame.draw.circle(screen, (255, 255, 255), (knob_vol_x, vol_y + vol_h//2), 8)
        
        vol_label = font_sub.render(f"Vol: {int(volume * 100)}%", True, (200, 200, 200))
        screen.blit(vol_label, (vol_x + vol_w + 15, vol_y - 8))

        
        hint = font_sub.render("P: Play | S: Pause | N: Next | B: Back", True, (180, 180, 180))
        screen.blit(hint, (WIDTH//2 - hint.get_width()//2, 250))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()