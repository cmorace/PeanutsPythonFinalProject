from pycat.core import Window, Sprite
from pycat.experimental.ldtk_level_entities import get_levels_entities, LevelData, Entity

ldtk_file = "/Users/ccm/Desktop/PeanutsPythonFinalProject/platformer_example/platformer.ldtk"
w = Window(width=256, height=256)

class Level(Sprite):
    def on_create(self):
        self.image = "platformer/png/Level_0.png"
        self.position = w.center


level_entities: list[LevelData] = get_levels_entities(ldtk_file)
for level in level_entities:
    for entity in level.entities:
        print(entity)

w.create_sprite(Level)
w.run()
