import pyglet
from math import sin

window = pyglet.window.Window(width=1000, height=700, caption="Start rakety")

raketa_on = pyglet.image.load('./obrazky/raketa_on.png')
raketa_off = pyglet.image.load('./obrazky/raketa_off.png')

raketa = pyglet.sprite.Sprite(raketa_off)
raketa.x = window.width / 2
raketa.y = 0

@window.event
def vykresli():
    window.clear()
    raketa.draw()

def odstartuj(t):  # dt - zpozdeny start
    pyglet.clock.schedule_interval(let, 1/60.)

def let(t):  # dt - zpozdeny start
    if raketa.y < window.height:
        raketa.y +=4
    else:
        raketa.y = 0
    raketa.rotation = sin(raketa.y/4)

def horeni_zapni(t):
    raketa.image = raketa_on
    pyglet.clock.schedule_once(horeni_vypni, 0.01)

def horeni_vypni(t):
    raketa.image = raketa_off
    pyglet.clock.schedule_once(horeni_zapni, 0.01)

pyglet.clock.schedule_once(horeni_zapni, 0.9)
pyglet.clock.schedule_once(odstartuj, 1.3)
window.push_handlers(on_draw=vykresli)

pyglet.app.run()
