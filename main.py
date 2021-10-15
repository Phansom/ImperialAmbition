import pygame as pg
import pygame_gui
from game.game import Game



def main():
    pg.init()

    pg.display.set_caption('quick start')
    window_surface = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    background = pg.Surface((0,0), pg.FULLSCREEN)
    background.fill(pg.Color('#000000'))
    clock = pg.time.Clock()

    game = Game(window_surface, background, clock)

    running = True
    playing = True


    while running:

        time_delta = clock.tick(60)/1000

        # menus go here

        while playing:

            game.run(time_delta)

if __name__ == "__main__":
    main()
