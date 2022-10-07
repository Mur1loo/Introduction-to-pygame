import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('CinZelda by PitbullsDoAgreste')
clock = pygame.time.Clock()  #OBJETO QUE AJUDA O CONTROLE DE FPS DO PROGRAMA (CEIL)
game_active = True

#TESTE DE TEXTOS
test_font = pygame.font.Font('../UltimatePygameIntro/font/Pixeltype.ttf',50)

#SURFACE

sky_surface = pygame.image.load('../UltimatePygameIntro/graphics/Sky.png').convert()          #IMAGEM
ground_surface = pygame.image.load('../UltimatePygameIntro/graphics/ground.png').convert()    #IMAGEM


text_surf = test_font.render('We are gigachad', False, 'Black')         #TEXTO
text_rect = text_surf.get_rect(center= (400, 50))

#ANIMATIONS
snail_surface = pygame.image.load('../UltimatePygameIntro/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom= (790,300))

#JOGADOR
player_surface =pygame.image.load('../UltimatePygameIntro/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom= (80, 300))
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #       IDENTIFICAR O CLICK DO MOUSE

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if player_rect.collidepoint(event.pos) == True:
        #         player_gravity = -15

        #       IDENTIFICAR A TECLA QUE FOI CLICADA
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                player_gravity = -16

    if game_active == True:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        pygame.draw.rect(screen, '#c0e8ec', text_rect)
        pygame.draw.rect(screen, 'Black', text_rect, 1)
        screen.blit(text_surf, text_rect)
        screen.blit(snail_surface, (snail_rect))
        snail_rect.left -= 10
        if snail_rect.left < -50: snail_rect.right = 800


        #PLAYER
        screen.blit(player_surface, player_rect)
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300

        #GAMER_OVER/GAME_ACTIVE
        if player_rect.colliderect(snail_rect):
            game_active = False
    else:
        screen.blit(pygame.image.load('../GRAPHICS/chuu.png'), (0, 0))
        screen.blit(test_font.render('PRESS SPACE TO CONTINUE', True, 'Black'), (0,0))
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    game_active = True



    pygame.display.update()
    clock.tick(60)
