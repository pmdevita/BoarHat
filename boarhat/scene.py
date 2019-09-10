import pyglet
import boarhat.keyboard


class SceneManager:
    def __init__(self, window):
        self.window = window
        # self.batch = window.batch
        self.scene_stack = []
        self.active_scene = None

    def create(self, scene):
        self.scene_stack.append(scene(self))

    def next_scene(self):
        self._deactivate()
        self.active_scene = self.scene_stack.pop(0)
        self._activate()

    def _activate(self):
        """Intiate a scene's setup"""
        self.active_scene._activate()

    def _deactivate(self):
        """Initiate a scene's teardown"""
        if self.active_scene:
            self.active_scene._deactivate()


class Scene:
    """
    Subclass and build your scene under the function `build_scene()`.
    Usually also contains logic for scene-wide things like mouse control

    """
    def __init__(self, scenemanager):
        self.scenemanager = scenemanager
        self.events = boarhat.event.EventManager(scenemanager.window.event_types)
        self.batch = pyglet.graphics.Batch()
        self.keyboard = boarhat.keyboard.Keyboard(self.events)
        self.layers = boarhat.layer.LayerManager()
        self.build_scene()

    def build_scene(self):
        raise NotImplemented

    def _activate(self):
        """Setup when this scene becomes the active scene"""
        pass

    def _deactivate(self):
        """Teardown when this scene is no longer the active scene"""
        pass

    def __repr__(self):
        return self.__class__.__name__
