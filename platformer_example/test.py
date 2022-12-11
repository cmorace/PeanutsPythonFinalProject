from pycat.core import Sprite, Window, Color
from pycat.experimental.ldtk_level_entities import (Entity, LevelData,
                                                    get_levels_entities)

ldtk_dir = "/Users/ccm/Desktop/PeanutsPythonFinalProject/platformer_example"
ldtk_file = ldtk_dir + "/platformer.ldtk"
w = Window(width=256, height=256)


class Level(Sprite):
    def on_create(self):
        self.image = "platformer/png/Level_0.png"
        self.position = w.center
        level_data: list[LevelData] = get_levels_entities(ldtk_file)
        for ld in level_data:
            for e in ld.entities:
                self.create_entity(e)

    def create_entity(self, e: Entity):
        w.create_sprite(x=e.x, y=e.y, scale_x=e.width, scale_y=e.height,
                        opacity=100, tag=e.id, layer=2, color=Color.PURPLE)


level = w.create_sprite(Level)
w.run()
