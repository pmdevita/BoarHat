import pyglet
import boarhat
import weakref
import boarhat.keyboard
from boarhat.layer import Layer, LayerManager
from boarhat.image import load_resource
from boarhat.sprite import Sprite
from pyglet.window import key as Keys
from pyglet import clock
from random import randrange

CROWD_LIMIT = 1
DISTANCE = 4


class CrowdScene(boarhat.scene.Scene):
    def build_scene(self):
        self.crowd_men = []
        self.background = Layer(self, 0)
        self.background_sprite = Sprite(load_resource("boarhat.png", 'center'), 0, 0, parent=self.background)
        self.foreground = Layer(self, 1)
        self.layers = []
        self.crowd_img = load_resource("man.png", "center")
        for i in range(DISTANCE):
            self.layers.append(Layer(self.foreground, DISTANCE - i - 1))

        pyglet.clock.schedule_interval(self.tick, 1/60)

    def tick(self, dt):
        # print(dt)
        if len(self.crowd_men) < CROWD_LIMIT and randrange(10) == 0:
            dist = randrange(DISTANCE)
            man = CrowdMan(self.crowd_img, self.window.width/2, dist, randrange(5, 20), self.layers[dist])
            self.crowd_men.append(man)
        delete_list = []
        for i, man in enumerate(self.crowd_men):
            if man.tick() < -1 * self.window.width/2:
                delete_list.append(i)
        for i in reversed(delete_list):
            self.crowd_men.pop(i)


class CrowdMan(Sprite):
    def __init__(self, img, startx, distance, speed, layer):
        super(CrowdMan, self).__init__(img, startx, -20, parent=layer)
        self.scale = 1/(distance + 1)
        self.speed = speed * 1/(distance + 1)

    def tick(self):
        self.x = self.x - self.speed
        return self.x


class App(boarhat.window.Window):
    def __init__(self):
        super(App, self).__init__(centered=True, show_fps=True)
        self.scenemanager.create(CrowdScene)
        self.scenemanager.next_scene()

        # Global keyboard stuff
        # Fullscreen
        self.keyboard.register_release(Keys.F11, self.go_fullscreen)
        # pyglet.clock.schedule_interval(self.exit, 10)

    def go_fullscreen(self, key, modifier):
        self.fullscreen = not self.fullscreen

    def exit(self, dt):
        pyglet.app.exit()


if __name__ == '__main__':
    pyglet.resource.path = ["images"]
    pyglet.resource.reindex()
    a = App()
    pyglet.app.run()
