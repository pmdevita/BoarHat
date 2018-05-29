import pyglet
from pyglet.gl import GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA
import boarhat


class Sprite(pyglet.sprite.Sprite):
    def __init__(self,
                 img, x=0, y=0,
                 blend_src=GL_SRC_ALPHA,
                 blend_dest=GL_ONE_MINUS_SRC_ALPHA,
                 parent=None,
                 usage='dynamic',
                 subpixel=False):
        if isinstance(parent, boarhat.scene.Scene):
            group = None
        else:   # If not, then we need to get the batch for other objects to use
            group = parent
        super(Sprite, self).__init__(img, x, y, blend_src, blend_dest, parent.batch, group, usage, subpixel)