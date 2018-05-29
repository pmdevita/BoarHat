import pyglet
from pyglet.event import EVENT_HANDLED, EVENT_UNHANDLED

"""
BoarHat's EventManager manages all events for a scene. It only passes events through if the scene it is attached to is 
active. 
"""

class EventManager(pyglet.event.EventDispatcher):
    def __init__(self, event_types):
        self._event_stack = ()
        self.event_types = event_types  # Event types from Window so we can register them

