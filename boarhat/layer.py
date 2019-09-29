import pyglet
import boarhat
import bisect


class Layer(pyglet.graphics.OrderedGroup):
    def __init__(self, parent, order=0, name=None):   # Does this really need a name?
        """

        :param parent: Scene or Layer this is under
        """
        # If the parent is the Scene, we don't have a group (top level)
        self.batch = parent.batch
        if isinstance(parent, boarhat.scene.Scene):
            group = None
        else:   # If not, then we need to get the batch for other objects to use
            group = parent
        super(Layer, self).__init__(order, group)
        if not name:
            name = self.__class__.__name__
        self.name = name
        self.parent_layer = parent
        self.build_layer()

    def build_layer(self):
        pass
    
    def __repr__(self):
        return self.name


class LayerManager(list):
    """Hold all the layers and update their order as needed"""
    def __init__(self):
        super(LayerManager, self).__init__()
        # Store them by name in this dictionary
        self._dict = {}

    def append(self, lr: Layer):
        super(LayerManager, self).append([lr])
        lr.order(len(self) - 1)

    def insert(self, index, lr: Layer):
        super(LayerManager, self).insert(index, lr)
        for i, layer in enumerate(self[index:]):
            layer.order(index + i)

    def _update_order(self, start=0):
        for i, layer in enumerate(self[start:]):
            for j in layer:
                j.order(i + i)

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
