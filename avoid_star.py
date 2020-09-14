import pygame
import random

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("별 피하기 게임")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/thgml/OneDrive/바탕 화면/mygame/background2.png")

# 캐릭터 불러오기
character = pygame.image.load("C:/Users/thgml/OneDrive/바탕 화면/mygame/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0

# 이동 속도
character_speed = 0.3
enemy_speed = 0.5

# 적 불러오기
enemy = pygame.image.load("C:/Users/thgml/OneDrive/바탕 화면/mygame/star.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randrange(screen_width - enemy_width)
enemy_y_pos = -enemy_height

# 폰트 정의
font_size = 50
game_font = pygame.font.Font(None, font_size)

# 게임 시작 시간
start_ticks = pygame.time.get_ticks()

# 이벤트 루프
running = True
while (running):
    # FPS
    dt = clock.tick(30)

    # 이벤트 처리
    for event in pygame.event.get():

        # 게임 종료
        if event.type == pygame.QUIT:
            running = False

        # 방향키 이동
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    
    # 캐릭터 위치 업데이트
    character_x_pos += to_x * dt

    # 경계값 처리
    if character_x_pos <= 0:
        character_x_pos = 0
    elif character_x_pos >= screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 적 위치
    enemy_y_pos += enemy_speed * dt

    # 경계값 처리
    if enemy_y_pos >= screen_height:
        enemy_x_pos = random.randrange(screen_width - enemy_width)
        enemy_y_pos = -enemy_height

    # 충돌 처리를 위한 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 처리
    if character_rect.colliderect(enemy_rect):
        print("Collide")
        running = False

    # 게임 경과 시간
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(float(elapsed_time)), True, pygame.Color("White"))

    # 화면에 불러오기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(timer, ((screen_width - font_size * 2) / 2, 0))

    pygame.display.update()

# 게임 종료
pygame.quit()