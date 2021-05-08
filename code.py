from pygame import*
w=1365
h=767
win = display.set_mode((w,h))
class Alfa(sprite.Sprite):
    def __init__(self,x,y,h,w,image_name,speed)
        super().__init__()
        self.image = image.load(image_name)
        self.rect = Rect(w,h,y,x)
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
ball = Alfa(0,0,100,100,'мяч.jpg',0)

while True:
    for e in event.get():
      if e.type==12:
          exit()
    win.fill((88,79,164))
    display.update()
