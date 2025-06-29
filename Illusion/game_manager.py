import pygame

from Illusion.scenes import MainMenuSc, LoadSc
from Illusion.text_renderer import TextRenderer
from importer import Importer, Assets
from frame_data_f import FrameData
from scene_menager import SceneManager


class GameManager:
    def __init__(self):
        self.__scene_manager = SceneManager()
        self.__importer = Importer()
        self.__assets = Assets()

        self.__importer.set_img_prefix("../assets/textures")
        self.__importer.set_animated_sprite_prefix("../assets/textures/animated/")
        self.__importer.set_sound_prefix("../assets/sounds/")

        self.__importer.import_animated_sprite("logo","logo.png",13,(64,192))

        self.__importer.import_sound("successful_select","effects/select_successful.wav")
        self.__importer.import_sound("denied","effects/select_denied.wav")

        self.__importer.import_sound("logo_sound","music/logo_sound.wav")

        self.__scene_manager.add_scene(LoadSc(self.__importer,self.__assets))
        self.__scene_manager.add_scene(MainMenuSc(self.__importer, self.__assets))

    def update_and_draw(self,frame_data: FrameData,surface: pygame.Surface):
        self.__scene_manager.update_and_draw(frame_data,surface)