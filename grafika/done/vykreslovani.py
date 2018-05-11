import pyglet
window = pyglet.window.Window()

def tik(t):
    print(t)

pyglet.clock.schedule_interval(tik, 1/30)

def zpracuj_text(text):
    print(text)

obrazek = pyglet.image.load('./obrazky/had.png')
had = pyglet.sprite.Sprite(obrazek)

def vykresli():
    window.clear()
    had.draw()

window.push_handlers(
    on_text=zpracuj_text,
    on_draw=vykresli,
)

pyglet.app.run()
