# I Don't Know!
#### Disclaimer: 
This repository is just used to showcase the code, I can't include the assets used because they are copywrighted.


La seguente repository è solo per mostrare il codice, non posso includere gli asset usati poichè protetti da copywright.
#### Description:

This project is game, entirely written in Python using the Pygame module to handle the UI. It is currently a pass and play game, but I'd like to make it multiplayer in the future. 
I'm unsure about the origin of this game and its name; I've played it with many friends and each one told me a different name for it, so I decided to pick the most approriate one: "I Don't Know!".
The rules are simple: from 2 to 8 players, it uses a deck of French playing cards. Each player gets 5 cards, then 4, 3 and so on based on the current turn. Each player makes a call, which is how many points they think will be won on that specific round. The sum of the player's calls cannot be equal to the amount of cards drawn on that turn.
Points are assigned using this hierarchy(higher to lower):  
 - suits = hearts, diamonds, clubs, spades
 - values = ace, 3, king, queen, jack, 7, 6, 5, 4, 2

So, for example, a 2 of hearts will win against any diamond, clubs or spades. The ace of hearts is the jolly, and it can count as the highest or lowest card played(declared by the player).
If the player's call does not match the points taken, that player will lose 1 life, until there's a single player standing.


## Code description

First we have the core of the project: main.py. I've kept it simple, it mostly relies on other files; the main function is to initialize pygame and switch between game states using a if-elif statement and a status flag. It also sets the FPS to 60 and closes the program by quitting the pygame module when necessary.


### The "common" folder

 - constants.py: this module contains constants used in all of the other files of the project. The most important ones are: the current screen dimensions, the SCREEN costant which is the surface used to draw all the pygame objects, a scaler function to adapt all of the object's sizes and dimensions(suggested by ChatGPT), the loaded game assets(from the "assets" folder) and finally some standard constants such as colors, font sizes and button width/height.

 - text_handler.py: this module contains a very simple function to display a given string of text on the screen. It also has the option to mark the "to_update" variable to True, if that part of the screen needs to be updated with each interaction.

 - button.py: this module contains a Button class to create buttons. It takes the button informations as arguments such as width, height, (x, y) position, text and so on.
 It has several methods:
    * draw(self): it draws the button along with the text.
    * check_hover(self): it's used to determine whether the mouse cursor is colliding with the button's background; it uses pygame's masks to have a pixel-perfect collision.
    * handle_event(self, events): using the pygame events queue, it determines if the mouse has been clicked on the button or not; if it is, it executes the button's function.
 
    handle_buttons(buttons, events): a simple function to be used in other files; when creating a list of buttons, this function can take care of making each button work using the button's built in methods I've previously described.

    The remaining functions are just button initializations used in other modules to keep other files clean.


### The "menus" folder

 - credits.py: a very simple module to display the people who made this project possible, using a Credits class. Thanks to each and everyone one of them(see the "Credits" chapter).

 - main_menu.py: the first file that gets used in the project. It displays the main menu of the game using the MenuManager class. It uses status flags to change between the different menu pages.
 The class contains:
    * The buttons of each page, the page's class, such as Settings and Credits and three callback functions for the buttons to decide the player count.
    * The draw_menu(self, state) method to display the current page based on the state status flag.
    * The run(self, events) method used in main.py, which also returns arguments to "main.py" when needed, for example when the amount of players has been selected.

 - settings.py: this module handles the settings using a Settings class.
    * It contains three methods which are used as callback function for the buttons, two to increase and decrease the volume and the other turn SFX on and off.
    * The run method simply draws the settings title, the buttons, the current volume level and handles the mouse clicks.


### The "card_handling" folder

 - deck.py: this is where the cards and deck get created. 
 
    First, there's the Card class:
     * It tries to load a given card from the assets folder with a try-except block and keeps track of the value and suit. It also has the __repr__(self) and __str__(self) methods to represent the card as a string(for example, Ace of Clubs) and be able to make comparisons between two cards(such as card_1 == card_2).

    Then, the Deck class:
     * It tries to load the card's back image first and then the 40 cards using the create_deck(self) method.
     * The shuffle(self) method uses the random library to randomly shuffle the deck.
     * The draw_card(self) method returns a random cards from the deck, if it is not empty.

    Finally, the AnimatedCard class: 
     * It takes all the parameters necessary to animate a card such as the start and end position, animation duration and so on.
     * The method get_current_pos(self) gets the current position of the card in the instant t of time and changes its position based on the elapsed time.

 - card_manager.py: this file handles the card animations and the interactions with the players, using the CardManager class.    
    The main methods are:
     * see_hand(self): to reveal the current player's hand.
     * handle_input(self, hand, player_pos, events): that checks if a card has been clicked, along with the check_hover(self, hand, player_pos) method.
     * draw_deck(self): simply draws the deck at center of the screen, represented as a single rotated card. It also rotates the deck when distributing cards.
     * draw_player_hands(self, players, pl_num, player_pos): draws the current player's hand if the "reveal" button has been clicked, other players are represented by a single rotated card.
     * single_card_round(self, players, PLAYER_POS, current_player): draws other player's cards(the rules change when a single card is drawn).
     * draw_played_cards(self, players, PLAYER_POS): draws the played cards in front of each player.
     * animation(self, anim_c, player_pos): animates a given card using the AnimatedCard class and also rotates the it based on the player's position.

Almost all of these methods rely on the player_positions.py module, found in the "game_logic" folder, containing each player's position on the screen, based on how many players are currently in the game.


### The "game_logic" folder

This is the heart of the game, and has a number of different modules. I've talked about the player_positions.py module, let's now focus on the others.

 - core.py: this is the core of the game, and similarly to main.py, it greatly relies on other modules. It is the "union" of the other game phases. It initializes the Player objects, keeps track of the current turn, sets the card animation speed and so on.
 Its methods are:
    * initialize_players(self): uses the player.py module.
    * cards_to_draw(self): calculates the number of cards to draw on each turn.
    * winner_found(self): checks if there's a single player in the self.players list.
    * gameplay(self, events): used in main.py, it makes the game run, drawing the background, deck, players information, buttons and switching between the different game phases.

 - player.py: it contains the Player class, which keeps track of all the information about a specific player, as well as drawing the information on the screen, adding points, removing player lives and resetting the variables.

 #### The "phases" folder

Here all of the different game phases are divided in a dedicated module to make the program clear and easier to navigate. At first, everything was written in the core.py module, but it was messy and difficult to understand.
All of the phases are classes and contain an execute method to be used in core.py.

 - draw_phase.py: this it where the cards get distributed to each player, based on the round number.
 It uses the previously described modules found in card_handling to animate the cards moving from the deck to each player's hand. It also has a check_full_hands(self, to_draw) method to move to the next phase.

 - call_phase.py: in this phase, players make their call. It uses the Button class and has three unique methods to change the player's call and confirm it. If the last player's call is not correct, it will move to the recall_phase

 - recall_phase.py: it uses the methods of call_phase.py, but only moves on if the last player makes a different call.

 - single_call_phase: when players have one card, they need to guess if they'll lose or win by looking at the other player's cards, but not their own. 

 - play_phase: this is the most complex phase. Here are its methods:
      * check_highest_card(self, played_cards): given a list of played cards, it returns the highest one based on the hierarchy seen in the rules of the game. 
      * assign_point(self, played_cards): assigns the point to the player who played the highest card, it also accounts for the jolly being played and displays a message.
      * everyone_played(self, current_player): checks if all players have played a card.
      * move_to_end_phase(self): checks if all players have an empty hand. If that's the case, it moves to next phase.
      * is_jolly(self, current_player): if the jolly has been played, it moves to the jolly phase.

 - jolly_phase.py: allows the player to decide if the jolly is lower or higher and saves the decision in the player's "jolly_val" variable, found in the Player class.

 - end_phase.py: resets the turn by using the Player class built-in reset method and also accounts for draws by making players have another round until there's only one left.

This was my project for CS50x, thanks to all of the staff and to Harvard University for making this course available to the World.
This is CS50!


## Credits 
I would like to thank all the people who made this project possible.
 - Francesco Vinci: helped me with the game animations module.
 - ZentropyArt: created the table background art.
 - SofuAssets: created the cards used in the project. They're available for purchase on itch.io.
 - Zakiro: created the music used in the project. It's available for free on itch.io.
 - Khurasan: created the font used in the project. 
 - SnowyPandas: created the icons used in the project. Also available for purchase on itch.io.
      
