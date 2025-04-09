import pygame
import time
import sys

def show_treasure_animation():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Kho báu đã mở!")

    # Màu sắc
    pink = (255, 182, 193)
    gold = (255, 215, 0)
    brown = (139, 69, 19)

    # Rương ban đầu (đóng)
    chest_rect = pygame.Rect(150, 120, 100, 60)

    # Vòng lặp mở hiệu ứng
    running = True
    open_lid = False
    clock = pygame.time.Clock()
    animation_start = time.time()

    while running:
        screen.fill(pink)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mở nắp rương sau 1s
        if time.time() - animation_start > 1 and not open_lid:
            open_lid = True

        # Vẽ rương
        pygame.draw.rect(screen, brown, chest_rect)  # thân rương
        if not open_lid:
            pygame.draw.rect(screen, brown, (150, 90, 100, 30))  # nắp đóng
        else:
            pygame.draw.polygon(screen, brown, [(150, 90), (250, 90), (240, 60), (160, 60)])  # nắp mở
            pygame.draw.circle(screen, gold, (200, 120), 10)  # vàng bên trong

        pygame.display.flip()
        clock.tick(30)

        # Thoát tự động sau 3s
        if time.time() - animation_start > 3:
            running = False

    pygame.quit()
    sys.exit()
