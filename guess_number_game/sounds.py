import pygame

def play_background_music():
    """Chạy nhạc nền"""
    pygame.mixer.init()
    pygame.mixer.music.load("assets/background.mp3")
    pygame.mixer.music.play(-1)  # Lặp vô hạn

def play_sound(effect):
    """Chạy âm thanh khi thắng/thua."""
    pygame.mixer.Sound(f"assets/{effect}.wav").play()
