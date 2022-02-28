import pygame
from drawing import Board, Player, start_menu

pygame.init()

with open(input('введите номер уровня(число от 1 до 3)  ') + '.txt', encoding='utf-8') as map_file:
    map = [list(map(int, list(i.strip()))) for i in map_file.readlines()]


if __name__ == '__main__':
    running = True
    scr = pygame.display.set_mode((700, 700))
    world = Board(len(map), len(map))
    world.board = map
    world.cell_size = 80
    player = Player(world.cell_size)
    clock = pygame.time.Clock()
    game_moment = 'start'
    textures = {0: pygame.transform.scale(pygame.image.load('data/0.png').convert(), (world.cell_size, world.cell_size)),
                1: pygame.transform.scale(pygame.image.load('data/1.png').convert(), (world.cell_size, world.cell_size)),
                'player': pygame.transform.scale(pygame.image.load('data/player.png').convert_alpha(), (world.cell_size, world.cell_size)),
                'start_menu': pygame.image.load('data/start.png').convert(),
                'background': pygame.image.load('data/background.jpg').convert()}
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                player.pos = [player.pos[0], player.pos[1] - 1 if map[player.pos[1] - 1][player.pos[0]] != 0 else player.pos[1]]
            if keys[pygame.K_DOWN]:
                player.pos = [player.pos[0], player.pos[1] + 1 if map[player.pos[1] + 1][player.pos[0]] != 0 else player.pos[1]]
            if keys[pygame.K_LEFT]:
                player.pos = [player.pos[0] - 1 if map[player.pos[1]][player.pos[0] - 1] != 0 else player.pos[0], player.pos[1]]
            if keys[pygame.K_RIGHT]:
                player.pos = [player.pos[0] + 1 if map[player.pos[1]][player.pos[0] + 1] != 0 else player.pos[0], player.pos[1]]
            if keys[pygame.K_SPACE] and game_moment == 'start':
                game_moment = 'game'
        scr.blit(textures['background'], (0, 0))
        if game_moment == 'game':
            world.render(scr, textures)
            player.render(scr, textures)
        elif game_moment == 'start':
            start_menu(scr, textures['start_menu'])
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()
