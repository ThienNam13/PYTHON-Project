import pygame

pygame.mixer.init()

def play_background_music():
    """Chạy nhạc nền"""
    pygame.mixer.init()
    pygame.mixer.music.load("assets/background.mp3")
    pygame.mixer.music.play(-1)  # Lặp vô hạn

def stop_background_music():
    pygame.mixer.music.stop()

# Phát âm thanh hiệu ứng
def play_sound(name):
    if name == "win":
        stop_background_music()
        sound = pygame.mixer.Sound("assets/win.wav")
        sound.play()
    elif name == "lose":
        stop_background_music()
        sound = pygame.mixer.Sound("assets/lose.wav")
        sound.play()
    elif name == "click":
        sound = pygame.mixer.Sound("assets/click.wav")
        sound.play()

def stop_all_sounds():
    pygame.mixer.stop()