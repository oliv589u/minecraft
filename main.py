from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

# Initialize Ursina app
app = Ursina()

# Block class with placing and destroying behavior
class Block(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture='white_cube',
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=1
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                print(f'Placing block on top of {self.position}')
                Block(position=self.position + Vec3(0, 1, 0))
            elif key == 'right mouse down':
                print(f'Removing block at {self.position}')
                destroy(self)

# Create a flat grid of blocks (10x10)
for z in range(10):
    for x in range(10):
        Block(position=(x, 0, z))

# Add a player with basic movement and gravity
player = FirstPersonController()
player.gravity = 0.5
player.jump_height = 1
player.cursor.visible = True

# Add a sky for a better visual experience
Sky()

# Run the Ursina app
app.run()
