"""
This module contains the menu functions, and a MenuManager class to handle them.
"""

from common.button import *
from common.constants import *
from menus.credits import Credits
from menus.settings import Settings
from common.text_handler import display_text


"""Game states."""
MAIN_MENU = "main_menu"
PASS_N_PLAY_MENU = "pass_n_play_menu"
PASS_N_PLAY = "pass_n_play"
SETTINGS = "settings"
CREDITS = "credits"
QUIT = "quit"

current_state = MAIN_MENU  # Global variable

"""Button callback function to navigate the menus."""
def change_menu_state(state):
    global current_state
    current_state = state

    if current_state == QUIT:
        print("Quitting the game")
    else:
        print(f"Menu state changed to: {current_state}")


class MenuManager:
    """
    Manages the creation and interaction of buttons for different menus.
    """
    def __init__(self):
        self.menu_buttons = {}  # Dictionary to store menu buttons as {"current page": buttons[]}
        self.pl_count = 2 
        self.pl_prev = 2  # Keep track if the player number has been changed

        # Initialize title and buttons for the main menu
        self.main_menu_surf = LARGE_FONT.render("I Don't Know!", True, BLACK)
        self.main_menu_rect = self.main_menu_surf.get_rect(center=(HALF_WIDTH, SCREEN_HEIGHT * 0.2))
        menu_func_args = [PASS_N_PLAY_MENU, SETTINGS, CREDITS, QUIT]  
        self.menu_buttons[MAIN_MENU] = load_main_menu_btns(change_menu_state, menu_func_args)

        # Initialize title and buttons for pass and play settings
        self.pass_n_play_surf = LARGE_FONT.render("Pass And Play", True, BLACK)
        self.pass_n_play_rect = self.pass_n_play_surf.get_rect(center=(HALF_WIDTH, SCREEN_HEIGHT * 0.2))
        self.menu_buttons[PASS_N_PLAY_MENU] = load_pass_settings_btns(self.add_player, self.remove_player, self.confirm_players, change_menu_state, MAIN_MENU)
        
        # Initialize title and buttons for online play
        self.settings = Settings()
        self.settings_surf = LARGE_FONT.render("Settings", True, BLACK)
        self.settings_rect = self.settings_surf.get_rect(center=(HALF_WIDTH, SCREEN_HEIGHT * 0.2))
        self.menu_buttons[SETTINGS] = load_settings_btns(change_menu_state, MAIN_MENU)
         
        # Initialize the credits page
        self.credits_page = Credits()
        self.credits_surf = LARGE_FONT.render("Thanks to:", True, BLACK)
        self.credits_rect = self.credits_surf.get_rect(center=(HALF_WIDTH, SCREEN_HEIGHT * 0.2))

        # To blit the number of players on the pass and play settings menu
        self.pl_count_surf = LARGE_FONT.render(str(self.pl_count), True, BLACK)
        self.pl_count_rect = self.pl_count_surf.get_rect(center=((HALF_WIDTH, HALF_HEIGHT - 10)))
    

    """Callback functions for pass and play settings."""
    def add_player(self):
        if self.pl_count < 8:
            self.pl_count += 1
    
    def remove_player(self):
        if self.pl_count > 2:
            self.pl_count -= 1
        
    def confirm_players(self):
        global current_state, selected_player_count
        selected_player_count = self.pl_count
        current_state = PASS_N_PLAY

    
    def draw_menu(self, state):
        """Function to draw the different menus based on the current state."""
        SCREEN.blit(TABLE_BACKGROUND, (0, 0))
        
        if state == MAIN_MENU:
            SCREEN.blit(self.main_menu_surf, self.main_menu_rect)
        elif state == PASS_N_PLAY_MENU:
            display_text(False, "Number of players:", MEDIUM_FONT, BLACK, (HALF_WIDTH, SCREEN_HEIGHT * 0.4))
            if self.pl_prev != self.pl_count:
                self.pl_count_surf = LARGE_FONT.render(str(self.pl_count), True, BLACK)
                self.pl_prev = self.pl_count

            SCREEN.blit(self.pass_n_play_surf, self.pass_n_play_rect)
            SCREEN.blit(self.pl_count_surf, self.pl_count_rect)  # Blit the number of players
        elif state == SETTINGS:
            SCREEN.blit(self.settings_surf, self.settings_rect)
        elif state == CREDITS:
            SCREEN.blit(self.credits_surf, self.credits_rect)
        else: 
            return 
        

    def run(self, events): 
        """
        Function to run all the menu states. It also returns arguments to "main.py" when needed,
        for example when the amount of players has been selected.
        """
        global current_state, selected_player_count 
        
        if current_state == MAIN_MENU:
            self.draw_menu(MAIN_MENU)
            handle_buttons(self.menu_buttons[MAIN_MENU], events)
            return "menu", None
        elif current_state == PASS_N_PLAY_MENU:
            self.draw_menu(PASS_N_PLAY_MENU)
            handle_buttons(self.menu_buttons[PASS_N_PLAY_MENU], events)
            return "menu", None
        elif current_state == PASS_N_PLAY:
            SCREEN.blit(TABLE_BACKGROUND, (0, 0))
            display_text(True, "Ready?", LARGE_FONT, BLACK, (HALF_WIDTH, HALF_HEIGHT)) 
            pygame.display.update() 
            pygame.time.wait(1000)
            current_state = PASS_N_PLAY_MENU
            return "pass_n_play", self.pl_count
        elif current_state == SETTINGS:
            self.draw_menu(SETTINGS)
            handle_buttons(self.menu_buttons[SETTINGS], events)
            self.settings.run(events)
            return "menu", None
        elif current_state == CREDITS:
            self.draw_menu(CREDITS)
            self.credits_page.show_credits()
            handle_buttons(self.menu_buttons[SETTINGS], events)
            return "menu", None
        elif current_state == QUIT:
            return pygame.QUIT, None
        