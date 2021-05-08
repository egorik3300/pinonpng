from pygame import*
w=1365
h=767
win = display.set_mode((w,h))
while True:
   
    for e in event.get():
      if e.type==12:
          exit()
    win.fill((88,79,164))
    display.update()