from ursina import *

app = Ursina()

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
                # Place a block on top of the current one
                Block(position=self.position + (0,1,0))
            if key == 'right mouse down':
                # Remove this block
                destroy(self)

# Create flat terrain
for z in range(10):
    for x in range(10):
        Block(position=(x,0,z))

player = FirstPersonController()

app.run()
