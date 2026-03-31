"""
Tudo que está aqui eu peguei da documentação oficial da biblioteca:
https://api.arcade.academy/en/stable/index.html

Esse é o arquivo main, ele é o mais simples mas o principal, sempre que quiser rodar o jogo,
troca pra esse arquivo e roda um "python main.py" no terminal
"""

import arcade
# peguei tudo que tinha naquele arquivo de constants --> https://stackoverflow.com/questions/2349991/how-do-i-import-other-python-files
from constants import *
# código da janela do jogo
from gameview import *

window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

# Create the GameView
game = GameView()
# Show GameView on f
window.show_view(game)
# Start the arcade game loop
arcade.run()