import pyglet
import pyglet.gl as gl
from pyglet.event import EventDispatcher, EVENT_UNHANDLED, EVENT_HANDLED
import boarhat.keyboard
import boarhat.scene


class Window(pyglet.window.Window):
    def __init__(self, widthheight=(800, 600), title="BoarHat", resizable=True, visible=True, centered=False):
        super(Window, self).__init__(width=widthheight[0], height=widthheight[1], resizable=resizable,
                                     caption=title, visible=visible)
        self.batch = pyglet.graphics.Batch()
        self.scenemanager = boarhat.scene.SceneManager(self)

        if centered:
            self.on_draw = self._on_draw_centered
            self.on_resize = self._on_resize_centered
        else:
            self.on_draw = self._on_draw_default

    @property
    def fullscreen(self):
        return self._fullscreen

    @fullscreen.setter
    def fullscreen(self, value):
        self.set_fullscreen(value)

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
        gl.glPushMatrix()
        gl.glTranslatef(self._center_x, self._center_y, 0)
        self.scenemanager.active_scene.batch.draw()
        gl.glPopMatrix()

    """
    In order to let scenes have different EventManagers, we need to only run events of the active scene's EventManger. 
    This requires a couple changes to switch from the Window's EventManager to the Scene's. 
    """

    def _dispatch_event(self, event_type, *args):
        '''
        Borrowed from pyglet.event.EventDispatcher 1.3.2 THIS WILL NEED TO BE UPDATED
        In the version, we search the handler stack of the scene's EventManager and then check the window for an
        event handler function.


        Dispatch a single event to the attached handlers.

        The event is propagated to all handlers from from the top of the stack
        until one returns `EVENT_HANDLED`.  This method should be used only by
        :py:class:`~pyglet.event.EventDispatcher` implementors; applications should call
        the ``dispatch_events`` method.

        Since pyglet 1.2, the method returns `EVENT_HANDLED` if an event
        handler returned `EVENT_HANDLED` or `EVENT_UNHANDLED` if all events
        returned `EVENT_UNHANDLED`.  If no matching event handlers are in the
        stack, ``False`` is returned.

        :Parameters:
            `event_type` : str
                Name of the event.
            `args` : sequence
                Arguments to pass to the event handler.

        :rtype: bool or None
        :return: (Since pyglet 1.2) `EVENT_HANDLED` if an event handler
            returned `EVENT_HANDLED`; `EVENT_UNHANDLED` if one or more event
            handlers were invoked but returned only `EVENT_UNHANDLED`;
            otherwise ``False``.  In pyglet 1.1 and earler, the return value
            is always ``None``.

        '''
        assert event_type in self.event_types, "%r not found in %r.event_types == %r" % (event_type, self,
                                                                                         self.event_types)

        invoked = False

        # Search handler stack for matching event handlers
        for frame in list(self.scenemanager.active_scene.events._event_stack):
            handler = frame.get(event_type, None)
            if handler:
                try:
                    invoked = True
                    if handler(*args):
                        return EVENT_HANDLED
                except TypeError:
                    self.scenemanager.active_scene.events._raise_dispatch_exception(event_type, args, handler)


        # Check instance for an event handler
        if hasattr(self, event_type):
            try:
                invoked = True
                if getattr(self, event_type)(*args):
                    return EVENT_HANDLED
            except TypeError:
                self._raise_dispatch_exception(
                    event_type, args, getattr(self, event_type))

        if invoked:
            return EVENT_UNHANDLED

        return False

    def dispatch_event(self, *args):
        """Borrowed from pyglet.window.Window 1.3.2 THIS WILL NEED TO BE UPDATED
        Small change to use our modified dispatch_event function"""
        if not self._enable_event_queue or self._allow_dispatch_event:
            if not self._dispatch_event(*args):
                self._legacy_invalid = True
        else:
            self._event_queue.append(args)


