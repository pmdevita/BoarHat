import pyglet

def _anchor(img, anchor):
    if anchor == "center":
        return (round(img.width / 2), round(img.height / 2))
    elif anchor == "bottomright":
        return (img.width, 0)
    elif anchor == "topleft":
        return (0, img.height)

def load(filename, anchor=None):
    img = pyglet.image.load(filename)
    if anchor:
        img.anchor_x, img.anchor_y = _anchor(img, anchor)
    return img

def load_resource(filename, anchor=None):
    img = pyglet.resource.image(filename)
    if anchor:
        img.anchor_x, img.anchor_y = _anchor(img, anchor)
    return img
