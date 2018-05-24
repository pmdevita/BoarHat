import pyglet
import pyglet.gl as gl
import boarhat.keyboard
import boarhat.scene


class Window(pyglet.window.Window):
    def __init__(self, widthxheight=(800, 600), title="BoarHat", resizable=True, visible=True):
        super(Window, self).__init__(width=widthxheight[0], height=widthxheight[1], resizable=resizable,
                                     caption=title, visible=visible)
        self.batch = pyglet.graphics.Batch()
        self.scenemanager = boarhat.scene.SceneManager(self)

    @property
    def fullscreen(self):
        return self._fullscreen

    @fullscreen.setter
    def fullscreen(self, value):
        self.set_fullscreen(value)

    # Drawing and layer stuffs

    def on_resize(self, width, height):
        super(Window, self).on_resize(width, height)
        # Useful to have on hand since some platforms require
        # a window API call to get this info
        self._center_x = width / 2
        self._center_y = height / 2

    def on_draw(self):
        self.clear()
        gl.glPushMatrix()
        gl.glTranslatef(self.width/2, self.height/2, 0)
        self.batch.draw()
        gl.glPopMatrix()


