import pyglet
import boarhat


class Layer(pyglet.graphics.Group):
    def __init__(self, name, parent):   # Does this really need a name?
        """

        :param parent: Scene or Layer this is under
        """
        # If the parent is the Scene, we don't have a group (top level)
        self.batch = parent.batch
        if isinstance(parent, boarhat.scene.Scene):
            group = None
        else:   # If not, then we need to get the batch for other objects to use
            group = parent
        super(Layer, self).__init__(group)
        self.name = name

    def _set_order(self, number):
        self._order = number

    def __lt__(self, other):
        if isinstance(other, Layer):
            return self._order < other._order
        return super(Layer, self).__lt__(other)
    
    def __repr__(self):
        return self.name


class LayerManager(list):
    def __init__(self):
        super(LayerManager, self).__init__()
        self._dict = {}

    def append(self, lr: Layer):
        super(LayerManager, self).append(lr)
        lr._set_order(len(self) - 1)

    def insert(self, index, lr: Layer):
        super(LayerManager, self).insert(index, lr)
        for i, layer in enumerate(self[index:]):
            layer._set_order(index + i)

    def __getitem__(self, item):
        if isinstance(item, str):
            return self._dict[str]
        else:
            return super(LayerManager, self).__getitem__(item)

    # def __setitem__(self, key, value):
    #     if isinstance(key, str):
    #         self._dict[key] = value
    #     else:
    #         super(LayerList, self).__setitem__(key, value)