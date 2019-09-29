import pyglet
import boarhat
import weakref
import boarhat.keyboard
from boarhat.layer import Layer, LayerManager
from boarhat.image import load_resource
from boarhat.sprite import Sprite
from boarhat.scene import Scene
from pyglet.window import key as Keys
from random import randrange


class LayerScene(Scene):
    def build_scene(self):
        layer_imgs = []
        for num in range(4):
            layer_imgs.append(load_resource(str(num)+'.png', 'center'))
        self.layers = []
        self.sprites = []
        for num in range(4):
            self.layers.append(Layer(self, 4 - num))
            self.sprites.append(Sprite(layer_imgs[num], num * 50 - 200, 0, parent=self.layers[num]))
        self.sprites.append(Sprite(layer_imgs[3], 5 * 50 - 200, 0, parent=self.layers[2]))


class App(boarhat.window.Window):
    def __init__(self):
        super(App, self).__init__(centered=True)
        self.scenemanager.create(LayerScene)
        self.scenemanager.next_scene()

        # Global keyboard stuff
        # Fullscreen
        self.keyboard.register_release(Keys.F11, self.go_fullscreen)

    def go_fullscreen(self, key, modifier):
        self.fullscreen = not self.fullscreen


if __name__ == '__main__':
    pyglet.resource.path = [".", "images", ".."]
    pyglet.resource.reindex()
    a = App()
    pyglet.app.run()
