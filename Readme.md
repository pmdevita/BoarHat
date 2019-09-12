# BoarHat

![alt text](https://github.com/pmdevita/BoarHat/raw/master/docs/boarhatdiagram.png "An analogy for BoarHat's design")

BoarHat is a companion library for [pyglet](https://github.com/pyglet/pyglet) that provides implementations of commonly 
used objects. It supports pyglet 1.3+ and Python 3+.

BoarHat itself is not a full game/graphics engine. Rather, it gives you structures to help manage your pyglet 
application and utilities to make common tasks easier.

BoarHat ~~can~~ will do

* Scene and layer management
* Layer translations that are useful for sidescrollers and overworlds
* Support [Tiled](https://www.mapeditor.org/) tile maps
* Provide utilities like automatic anchor placement on images, a better keyboard input manager

and more!

BoarHat is in very early development. It's being written for PyWeek (provided I'll actually have time to participate).

## Setup/Installation

Make sure you have pyglet

    pip install pyglet
    
Then download this repo and run setup.py

    python setup.py install
    
## Usage

This will be explained in the wiki. For now, check `tests/__init__.py`
to get an idea of what you can do.

## To Do

Right now, we are assembling the core part of BoarHat, it's scene manager. This will determine how we organize objects 
and display them on screen. 

* Create a full prototype showcasing all of the abilities of Scenes, Layers, and Objects
* Discuss needs for flexibility (Do we need to be able to transplant layers and objects after creation?)
* Clean and unify its API

## Other Information

Named "BoarHat" because it sits on top of pyglet (like a hat!) and 
because some of my consulting team was watching "The Seven Deadly Sins".
    

