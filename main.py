import pygame
from game_logic.core import GameLogic
from menus.main_menu import MenuManager
from common.constants import *


pygame.init()

def main():
    clock = pygame.time.Clock()
    FPS = 60 

    state = "menu"  # Keep track of the game state (default: menu)
    menu = MenuManager()
    pass_n_play = None  # Initialize pass_n_play only when a number of players has been selected
    
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT: 
                running = False
       
        if state == "menu":
            temp_state, pl_info = menu.run(events)
           
            if temp_state == pygame.QUIT:
                running = False
            elif temp_state == "pass_n_play":
                state = "pass_n_play"
                pass_n_play = GameLogic(pl_info)  # pl_info is an int in this instance
        elif state == "pass_n_play": 
            if pass_n_play.gameplay(events) == "menu":
                state = "menu"
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()  # Close the pygame module


if __name__ == "__main__":  
    main()
    