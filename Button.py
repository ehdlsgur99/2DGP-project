from pico2d import *
import object
import KeyManager

class button(object.obj):
    def __init__(self,path1, path2, x, y, width, height, frame, func): # 버튼 이미지 path 두개를 받아옴
        super().__init__(path1, x, y, width, height, frame)
        self.isOn = False
        self.path1 = path1
        self.path2 = path2
        self.callbackfunc = func()

    def update(self):
        if KeyManager.mouseDown == True:
            self.checkPos()
        if KeyManager.mouseDown == False and  self.isOn == True:
            self.callbackfunc()

    def checkPos(self):
        if KeyManager.mouseXPos > self.x and KeyManager.mouseXPos <self.x + self.width and KeyManager.mouseYPos > self.y and \
                KeyManager.mouseYPos < self.y + self.height:
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