import pyglet
window = pyglet.window.Window(width=1000, height=700)


obrazek = pyglet.image.load("./obrazky/had.png")
had = pyglet.sprite.Sprite(obrazek)
had.x = window.width / 2 - 40
had.y = window.height / 2 - 40
had.rotation = 30
def vykresli():
    window.clear()
    had.draw()

window.push_handlers(on_draw=vykresli)
pyglet.app.run()
