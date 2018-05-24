import pyglet
import collections
import weakref

# Creates individual key press events so only relevant objects are triggered on these events
# We should probably be using weakrefs
# Implement deregistering
class Keyboard:
    def __init__(self, window, fps=60):
        self._window = window
        self.press = {}
        self.release = {}
        self.hold = {}
        self._held = []
        self._hold_on = False
        self._fps = fps
        self._update_interval = 1/fps

    def _activate(self):
        self._window.push_handlers(on_key_press=self._on_key_press, on_key_release=self._on_key_release)

    def _deactivate(self):
        self._window.remove_handlers(on_key_press=self._on_key_press, on_key_release=self._on_key_release)


    # Hand register hold a pyglet key object or list of key and a function to trigger
    def register_hold(self, key, trigger):
        if isinstance(key, collections.Iterable):
            for i in key:
                self._register_hold(i, trigger)
        else:
            self._register_hold(key, trigger)

    def _register_hold(self, key, trigger):
        if isinstance(self.hold.get(key, None), list):
            self.hold[key].append(trigger)
        else:
            self.hold[key] = [trigger]

    # Hand register press a pyglet key object or list of key and a function to trigger
    def register_press(self, key, trigger):
        if isinstance(key, collections.Iterable):
            for i in key:
                self._register_press(i, trigger)
        else:
            self._register_press(key, trigger)

    def _register_press(self, key, trigger):
        if isinstance(self.press.get(key, None), list):
            self.press[key].append(trigger)
        else:
            self.press[key] = [trigger]

    # Hand register release a pyglet key object or list of key and a function to trigger
    def register_release(self, key, trigger):
        if isinstance(key, collections.Iterable):
            for i in key:
                self._register_release(i, trigger)
        else:
            self._register_release(key, trigger)

    def _register_release(self, key, trigger):
        if isinstance(self.release.get(key, None), list):
            self.release[key].append(trigger)
        else:
            self.release[key] = [trigger]

    def _on_key_press(self, key, modifier):
        if self.press.get(key, False):
            for i in self.press[key]:
                i(key, modifier)

        if self.hold.get(key, False):
            # if the current update list is empty reschedule the updater
            if not self._held:
                pyglet.clock.schedule_interval(self._hold_update, self._update_interval)
            self._held.append(key)
            for i in self.hold[key]:
                i(key, 1)

    def _on_key_release(self, key, modifier):
        if self.release.get(key, False):
            for i in self.release[key]:
                i(key, modifier)

        if self.hold.get(key, False):
            self._held.remove(key)
            # if the current update list is empty unschedule the updater
            if not self._held:
                pyglet.clock.unschedule(self._hold_update)

    def _hold_update(self, dt):
        for key in self._held:
            for i in self.hold[key]:
                i(key, dt * self._fps)


