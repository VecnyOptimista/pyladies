import pyglet

window = pyglet.window.Window(width=1000, height=700)
micek = pyglet.image.load("./obrazky/micek.png")

objekty = []
objekty.append({'objekt': pyglet.sprite.Sprite(micek), 'smer': 4})

def vykresli():
    window.clear()
    objekty[0]['objekt'].draw()

def pohyb(t):
    objekty[0]['objekt'].y += objekty[0]['smer']
    if objekty[0]['objekt'].y > window.height - objekty[0]['objekt'].height or objekty[0]['objekt'].y < 0 :
        objekty[0]['smer'] = - objekty[0]['smer']

pyglet.clock.schedule_interval(pohyb, 1/60)
window.push_handlers(on_draw=vykresli)
pyglet.app.run()
