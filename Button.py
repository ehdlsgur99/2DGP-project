from pico2d import *
import object



class Button(object.obj):
    def __init__(self,path1, path2, x, y, width, height, frame, func): # 버튼 이미지 path 두개를 받아옴
        super().__init__(path1, x, y, width, height, frame)
        self.isOn = False
        self.path1 = path1
        self.path2 = path2
        self.callbackfunc = func()
        pass

    def checkPos(self, mouseXPos, mouseYPos):
        if mouseXPos > self.x and mouseXPos <self.x + self.width and mouseYPos > self.y and mouseYPos < self.y + self.height:
                if self.isOn == False:
                    self.image = load_image(self.path2)
                self.isOn = True
                self.callbackfunc()
                return True
        else:
            if self.isOn == True:
                self.image = load_image(self.path1)
            self.isOn = False
            return False