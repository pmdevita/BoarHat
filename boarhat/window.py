import pyglet
import pyglet.gl as gl
from pyglet.event import EventDispatcher, EVENT_UNHANDLED, EVENT_HANDLED
import boarhat.keyboard
import boarhat.scene


class Window(pyglet.window.Window):
    def __init__(self, widthheight=(800, 600), title="BoarHat", resizable=True, visible=True, centered=False, show_fps=False):
        self._window_event_stack = []
        super(Window, self).__init__(width=widthheight[0], height=widthheight[1], resizable=resizable,
                                     caption=title, visible=visible)
        self.scenemanager = boarhat.scene.SceneManager(self)
        self.keyboard = boarhat.keyboard.Keyboard(self)

        if centered:
            self.on_draw = self._on_draw_centered
            self.on_resize = self._on_resize_centered
        else:
            self.on_draw = self._on_draw_default
        self.show_fps = pyglet.window.FPSDisplay(self) if show_fps else False

    @property
    def fullscreen(self):
        return self._fullscreen

    @fullscreen.setter
    def fullscreen(self, value):
        self.set_fullscreen(value)

    # Use the active scene's event stack instead of our own
    @property
    def _event_stack(self):
        if self.scenemanager.active_scene:
            return self._window_event_stack + self.scenemanager.active_scene.events._event_stack
        return self._window_event_stack

    @_event_stack.setter
    def _event_stack(self, value):
        self._window_event_stack = value

    # Drawing and layer stuffs

    def _on_resize_centered(self, width, height):
        super(Window, self).on_resize(width, height)
        # Useful to have on hand since some platforms require
        # a window API call to get this info
        self._center_x = width / 2
        self._center_y = height / 2

    def _on_draw_default(self):
        self.clear()
        self.scenemanager.active_scene.batch.draw()

    def _on_draw_centered(self):
        self.clear()
        if self.show_fps:
            self.show_fps.draw()
        gl.glPushMatrix()
        gl.glTranslatef(self._center_x, self._center_y, 0)
        self.scenemanager.active_scene.batch.draw()
        gl.glPopMatrix()

