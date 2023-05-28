from objects import *
import display

earth = Body(*[0,0,0], *[0,0,0], 1e4, 1e5)
moon = Body(*[3,0,0], *[0,0,0], 1e2, 1e2)

earth_moon = System()

earth_moon.add_body(earth)
earth_moon.add_body(moon)

display.draw(earth_moon)
