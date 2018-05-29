# BoarHat

![alt text](https://github.com/pmdevita/BoarHat/raw/master/docs/boarhatdiagram.png "An analogy for BoarHat's design")

BoarHat is a companion library for pyglet that provides implementations of commonly 
used objects. It supports pyglet 1.3 and Python 3.

BoarHat ~~can~~ will do

* Scene and layer management
* Layer translations that are useful for sidescrollers and overworlds
* Import and use [Tiled](https://www.mapeditor.org/) tile maps
* Efficiently manage keyboard input
* Provide utilities like automatic anchor placement on images

and more!

BoarHat is in very early development. Check back before the next 
PyWeek (as we are writing it for that).

## Setup/Installation

Make sure you have pyglet

    pip install pyglet==1.3.2
    
Then download this repo and run setup.py

    python setup.py install
    
## Usage

This will be explained in the wiki. For now, check tests/__init__.py 
to get an idea of what you can do.

## Todo:

Right now, we are assembling the core part of BoarHat, it's scene manager. This will determine how we organize objects 
and display them on screen. 

* Create a full prototype of the scene-layer-object paradigm
* Discuss needs for flexibility (Do we need to be able to transplant layers and objects?)
* Clean and unify its UI

## Other Information

Named "BoarHat" because it sits on top of pyglet (like a hat!) and 
because some of my consulting team was watching "The Seven Deadly Sins".
    

