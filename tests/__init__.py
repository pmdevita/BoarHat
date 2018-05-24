import pyglet
import boarhat
import boarhat.keyboard


class SecondScene(boarhat.scene.Scene):
    def build_scene(self):
        testimg = boarhat.image.load_resource("docs/boarhatdiagram.png", "center")
        self.bh = pyglet.sprite.Sprite(testimg, 200, 200, batch=self.batch, group=self)
        self.keyboard.register_release(pyglet.window.key.SPACE, self.switch)

    def switch(self, key, modifiers):
        print("second")
        self.scenemanager.next_scene()
        self.scenemanager.scene_stack.append(self)


class MenuScene(boarhat.scene.Scene):
    def build_scene(self):
        testimg = boarhat.image.load_resource("docs/boarhat.png", "center")
        self.bh = pyglet.sprite.Sprite(testimg, -200, -200, batch=self.batch, group=self)
        self.keyboard.register_release(pyglet.window.key.SPACE, self.switch)

    def switch(self, key, modifiers):
        print("menu")
        self.scenemanager.next_scene()
        self.scenemanager.scene_stack.append(self)

        print(self.scenemanager.scene_stack, self.scenemanager.active_scene)




class App(boarhat.window.Window):
    def __init__(self):
        super(App, self).__init__()
        # # Fullscreen
        # print(self.fullscreen)
        # self.fullscreen = True
        # self.fullscreen = False

        # keyboard input should be a singleton
        # assert self.keyboard == boarhat.keyboard.Keyboard(self)

        self.scenemanager.create(MenuScene)
        self.scenemanager.create(SecondScene)
        self.scenemanager.next_scene()



if __name__ == '__main__':
    pyglet.resource.path = [".."]
    pyglet.resource.reindex()
    a = App()
    pyglet.app.run()