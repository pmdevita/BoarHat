import pyglet

class Sprite:
    def __init__(self,
                 img, x=0, y=0,
                 blend_src=GL_SRC_ALPHA,
                 blend_dest=GL_ONE_MINUS_SRC_ALPHA,
                 layer=None,
                 usage='dynamic',
                 subpixel=False):
        super(Sprite, self).__init__()