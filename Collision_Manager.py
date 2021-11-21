from pico2d import *
import object

class CollisionManager:
    _sing = None

    def __new__(self, *args, **kwargs):
        if not self._sing:
            self._sing = super(CollisionManager, self).__new__(self, *args, **kwargs)
            return self._sing

    def checkBoxColiision(self,x1, y1, sizeX1, sizeY1, x2, y2, sizeX2, sizeY2):
         left1 = x1 - sizeX1/2
         right1 = x1 + sizeX1/2
         top1 = y1 - sizeY1/2
         bottom1 = y1 + sizeY1/2

         left2 = x2 - sizeX2 / 2
         right2 = x2 + sizeX2 / 2
         top2 = y2 - sizeY2 / 2
         bottom2 = y2 + sizeY2 / 2

         if left1 < right2 and top1 < bottom2 and right1 < left2 and bottom1 < top2:
             return True
         else:
             return False

    def checkCircleCollision(x1, y1, x2, y2, size):
        if ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) <= size * size):
            return True
        else:
            return False
