"""
This module contains a Button class to dynamically create buttons.
It also contains functions to initialize buttons in other files: 
- menu.py
- game_logic.py
"""

from common.constants import *
import os


class Button: 
    """
    A class to create buttons.
    """
    def __init__(self, x: int, y: int, width: int, height: int, font_size: int, 
                 btn_background: pygame.Surface | None, cursor_img: pygame.Surface | None, 
                 text: str = '', text_color: tuple[int, int, int] = DEFAULT_TEXT_COLOR,
                 hover_text_color: tuple[int, int, int] = HOVER_TEXT_COLOR,
                 on_click_callback=None, args=None): 
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size    
        self.text = text
        self.text_color = text_color
        self.hover_text_color = hover_text_color
        self.on_click_callback = on_click_callback
        self.args = args  # callback function arguments
        
        self.sfx_on = True

        # Load the button image background
        self.btn_background = pygame.transform.scale(btn_background, (width, height)) 
        self.rect = self.btn_background.get_rect(center=(x, y)) 
        self.btn_mask = pygame.mask.from_surface(self.btn_background)

        # Load the cursor image (if there is one, otherwise skip this step)
        self.cursor_img = None
        if cursor_img:
            self.cursor_img = pygame.transform.scale(cursor_img, (CURSOR_WIDTH, CURSOR_HEIGHT))
            self.cursor_rect = self.cursor_img.get_rect(midright=(self.rect.left - 10, self.rect.centery))# Cursor positioning

        FONTS_DIR = os.path.join(ASSETS_DIR, "fonts", "catways.ttf")
        self.font = pygame.font.Font(FONTS_DIR, font_size) # Specify a different font here

        self.is_hovered = False
        self.is_pressed = False  # New variable to track button press


    def draw(self):
        """
        Draws the button and its text.
        """
        SCREEN.blit(self.btn_background, self.rect)

        current_text_color = self.hover_text_color if self.is_hovered else self.text_color  # Change color when hovering
        
        if self.text:
            text_surface = self.font.render(self.text, True, current_text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            SCREEN.blit(text_surface, text_rect)
            
        if self.is_hovered and self.cursor_img:
            SCREEN.blit(self.cursor_img, self.cursor_rect) 


    def check_hover(self):
        """
        Checks if the mouse is on the button.
        It uses a mask for the button image for pixel-perfect collision.
        """
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            # Calculates the relative position of the mouse compared to the top left corner
            relative_mouse_pos = (mouse_pos[0] - self.rect.x, mouse_pos[1] - self.rect.y)
            
            # Checks the collision between mouse and mask
            if 0 <= relative_mouse_pos[0] < self.btn_mask.get_size()[0] and \
               0 <= relative_mouse_pos[1] < self.btn_mask.get_size()[1]: 
                self.is_hovered = self.btn_mask.get_at(relative_mouse_pos) != 0
            else:
                self.is_hovered = False
        else:
            self.is_hovered = False
        
        
    def handle_event(self, events):
        """
        Handles pygame events for the buttons.
        """
        for event in events:
            # Step 1: Check for mouse button press
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                if self.is_hovered:
                    if sfx_on[0]:
                        CLICK_SOUND.play()
                    self.is_pressed = True
                    return True  # Indicates the button has been pressed

            # Step 2: Check for mouse button release (change suggested by ChatGPT to avoid double clicks)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.is_pressed and self.is_hovered:
                    if self.on_click_callback:
                        if self.args:
                            self.on_click_callback(self.args)
                        else:
                            self.on_click_callback()
                    self.is_pressed = False  # Reset the flag
                    return True  # Indicates a successful click

                self.is_pressed = False  # Reset the flag if the mouse is released outside the button

        return False
    
    
def handle_buttons(buttons, events):
    """Function to handle buttons in other parts of the program."""
    for button in buttons:  
        button.check_hover()
        button.draw()
        button.handle_event(events)


"""Initialization of buttons used in menu.py"""
def load_main_menu_btns(change_menu_state, menu_func_args):
    buttons = []
    button_spacing = [0.35, 0.5, 0.65, 0.8]
    btn_names = ["Pass 'n Play", "Settings", "Credits", "Quit"]

    for spacing, name, arg in zip(button_spacing, btn_names, menu_func_args):
        buttons.append(
            Button(
                HALF_WIDTH, (SCREEN_HEIGHT * spacing), BUTTON_WIDTH, BUTTON_HEIGHT, 
                BUTTON_TEXT_SIZE, BUTTON_BACKGROUND, CURSOR_IMAGE, 
                text=name, on_click_callback=change_menu_state, args=arg
            )
        )
    
    return buttons 

def load_settings_btns(change_menu_state, MAIN_MENU):
    buttons = [
        Button(
            HALF_WIDTH, (SCREEN_HEIGHT * 0.8), BUTTON_WIDTH, BUTTON_HEIGHT, 
            BUTTON_TEXT_SIZE, BUTTON_BACKGROUND, CURSOR_IMAGE, 
            text="Back", on_click_callback=change_menu_state, args=MAIN_MENU
        )
    ]

    return buttons

def load_pass_settings_btns(add_player, remove_player, confirm_players, change_menu_state, MAIN_MENU):
    buttons = [
        Button(
            (SCREEN_WIDTH * 0.53), SCREEN_HEIGHT * 0.57, BUTTON_WIDTH * 0.4, BUTTON_HEIGHT * 0.8, 
            BUTTON_TEXT_SIZE, ALT_BTN_BACKGROUND, None, 
            text="+", on_click_callback=add_player
        ),
        
        Button(
            (SCREEN_WIDTH * 0.47), SCREEN_HEIGHT * 0.57, BUTTON_WIDTH * 0.4, BUTTON_HEIGHT * 0.8, 
            BUTTON_TEXT_SIZE, ALT_BTN_BACKGROUND, None, 
            text="-", on_click_callback=remove_player
        ),

        Button(
            HALF_WIDTH, (SCREEN_HEIGHT * 0.65), BUTTON_WIDTH, BUTTON_HEIGHT,
            BUTTON_TEXT_SIZE, BUTTON_BACKGROUND, CURSOR_IMAGE, 
            text="Ready!", on_click_callback=confirm_players
        ),

        Button(
            HALF_WIDTH, (SCREEN_HEIGHT * 0.8), BUTTON_WIDTH, BUTTON_HEIGHT,
            BUTTON_TEXT_SIZE, BUTTON_BACKGROUND, CURSOR_IMAGE, 
            text="Back", on_click_callback=change_menu_state, args=MAIN_MENU
        ) 
    ]

    return buttons


"""Initialization of buttons used in game_logic."""
def normal_round_btns(increase_call, decrease_call, confirm_call):
    btn_width = scaler_func(70)
    btn_height = scaler_func(50)

    buttons = [ 
        Button(
            (SCREEN_WIDTH * 0.53), SCREEN_HEIGHT * 0.65, btn_width, btn_height, 
            BUTTON_TEXT_SIZE, BUTTON_BACKGROUND, None, 
            text="+", on_click_callback=increase_call
        ),

        Button(
            (SCREEN_WIDTH * 0.47), SCREEN_HEIGHT * 0.65, btn_width, btn_height,
            BUTTON_TEXT_SIZE, BUTTON_BACKGROUND, None, 
            text="-", on_click_callback=decrease_call
        ),
        
        Button(
            HALF_WIDTH, SCREEN_HEIGHT * 0.7, BUTTON_WIDTH * 0.7, BUTTON_HEIGHT * 0.7,
            BUTTON_TEXT_SIZE, BUTTON_BACKGROUND, None, 
            text="confirm!", on_click_callback=confirm_call
        )
    ]

    return buttons 

def one_card_btns(win_call, lose_call):     
    buttons = [
        Button(
            (SCREEN_WIDTH * 0.6), SCREEN_HEIGHT * 0.65, BUTTON_WIDTH * 0.6, BUTTON_HEIGHT * 0.8,
            BUTTON_TEXT_SIZE, BUTTON_BACKGROUND, None, 
            text="Win", on_click_callback=win_call
        ),
        
        Button(
            (SCREEN_WIDTH * 0.4), SCREEN_HEIGHT * 0.65, BUTTON_WIDTH * 0.6, BUTTON_HEIGHT * 0.8,
            BUTTON_TEXT_SIZE,BUTTON_BACKGROUND, None, 
            text="Lose", on_click_callback=lose_call
        )   
    ] 

    return buttons

def jolly_btns(jolly_high, jolly_low):     
    buttons = [
        Button(
            (SCREEN_WIDTH * 0.6), SCREEN_HEIGHT * 0.65, BUTTON_WIDTH * 0.6, BUTTON_HEIGHT * 0.8,
            BUTTON_TEXT_SIZE, BUTTON_BACKGROUND, None, 
            text="High", on_click_callback=jolly_high
        ),

        Button(
            (SCREEN_WIDTH * 0.4), SCREEN_HEIGHT * 0.65, BUTTON_WIDTH * 0.6, BUTTON_HEIGHT * 0.8,
            BUTTON_TEXT_SIZE,BUTTON_BACKGROUND, None, 
            text="Low", on_click_callback=jolly_low
        )   
    ] 

    return buttons
