"""
Esse arquivo é responsável simplesmente por renderizar as coisas na tela, 
tudo que for aparecer e for desenhado vem aqui
"""

import arcade
from constants import *
from arcade.types import LRBT

class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class to set up the window
        super().__init__()

        self.background_color = arcade.csscolor.CORNFLOWER_BLUE
        
        self.camera = arcade.Camera2D(
            position=(0, 0),
            projection=LRBT(left=0, right=WINDOW_WIDTH, bottom=0, top=WINDOW_HEIGHT),
            viewport=self.window.rect
        )
        
        # Texto que está escrito na tela
        # criamos um objeto de texto e colocamos as características desse texto ao chamar a classe arcade.text
        start_x = 0
        start_y = 0
        self.title = arcade.Text(
            "Pressione F para entrar/sair do modo tela cheia \n pressione esc para sair",
            start_x,
            start_y,
            arcade.color.BLACK,
            DEFAULT_FONT_SIZE * 2,
            align="center",
        )

    def on_resize(self, width, height):
        super().on_resize(width, height)
        
        # centralizando o texto quando ele fica em fullscreen
        if hasattr(self, 'title'):
            self.title.x = 0
            self.title.y = height/2
            
            self.title.width = width
    
    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""
        
        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.

        # Code to draw other things will go here
        self.clear()
        
        self.camera.use()
        
        self.title.draw()

        
    def on_key_press(self, key, modifiers):
        """Define o que apertar cada botão vai fazer"""
        
        if key == arcade.key.F:
            # User hits f. Flip between full and not full screen.
            self.window.set_fullscreen(not self.window.fullscreen)

            # Get the window coordinates. Match viewport to window coordinates
            # so there is a one-to-one mapping.
            self.camera.viewport = self.window.rect
            self.camera.projection = arcade.LRBT(0.0, self.window.width, 0.0, self.window.height)
            
        self.camera.viewport = self.window.rect
        
        if key == arcade.key.ESCAPE:
            self.window.close()

