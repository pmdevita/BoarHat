import pyglet
import boarhat
import boarhat.keyboard
from boarhat.layer import Layer
from boarhat.image import load_resource
from boarhat.sprite import Sprite
from pyglet.window import key as Keys


class SecondScene(boarhat.scene.Scene):
    def build_scene(self):
        self.layers.append(Layer("mainlayer", self))  # This is quite long and verbose to init a layer
        testimg = load_resource("docs/boarhatdiagram.png", "center")
        self.bh = Sprite(testimg, 0, 0, parent=self.layers[0])
        self.keyboard.register_release(pyglet.window.key.SPACE, self.switch)

    def switch(self, key, modifiers):
        print("second")
        self.scenemanager.next_scene()
        self.scenemanager.scene_stack.append(self)


class MenuScene(boarhat.scene.Scene):
    def build_scene(self):
        self.x, self.y = 0, 0
        self.layers.append(Layer("mainlayer", self))  # This is quite long and verbose to init a layer
        testimg = load_resource("docs/boarhat.png", "center")
        self.bh = Sprite(testimg, 0, 0, parent=self.layers[0])
        self.keyboard.register_release(pyglet.window.key.SPACE, self.switch)
        self.keyboard.register_hold([Keys.W, Keys.A, Keys.S, Keys.D], self.move)

    def switch(self, key, modifiers):
        print("menu")
        self.scenemanager.next_scene()
        self.scenemanager.scene_stack.append(self)
        print(self.scenemanager.scene_stack, self.scenemanager.active_scene)

    def move(self, key, modifiers):
        if key == Keys.W:
            self.y += 2
        elif key == Keys.S:
            self.y -= 2
        elif key == Keys.A:
            self.x -= 2
        elif key == Keys.D:
            self.x += 2

        self.bh.y = self.y
        self.bh.x = self.x


class App(boarhat.window.Window):
    def __init__(self):
        super(App, self).__init__(centered=True)
        self.scenemanager.create(MenuScene)
        self.scenemanager.create(SecondScene)
        self.scenemanager.next_scene()

        # Global keyboard stuff
        # Fullscreen
        self.keyboard.register_release(Keys.F11, self.go_fullscreen)

    def go_fullscreen(self, key, modifier):
        self.fullscreen = not self.fullscreen


if __name__ == '__main__':
    pyglet.resource.path = [".."]
    pyglet.resource.reindex()
    a = App()
    pyglet.app.run()
