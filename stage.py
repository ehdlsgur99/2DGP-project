from pico2d import *
import random
import sys

class Stage:
    def __init__(self):

        self.width, self.height = 20, 14
        self.map = load_image('Resource/Stage/map.png')
        self.mapData = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]

        self.portals = []
        self.portalsPos = []
        self.initPortal()
        self.getStageInfo()

        self.imageData = []
        self.loadResources()


    def initPortal(self):
        for i in range(0, 4):
            self.portals.append(load_image('Resource/Stage/portal.png'))
        self.portalsPos.append((400, 700))
        self.portalsPos.append((400, 000))
        self.portalsPos.append((100, 300))
        self.portalsPos.append((500, 300))


    def loadResources(self):
        self.imageData.append(load_image('Resource/Stage/tree1_01.png'))
        self.imageData.append(load_image('Resource/Stage/well1.png'))
        self.imageData.append(load_image('Resource/Stage/well2.png'))
        self.imageData.append(load_image('Resource/Stage/well3.png'))
        self.imageData.append(load_image('Resource/Stage/well4.png'))

        self.stageMiniMap = []
        self.stageMiniMap.append(load_image('Resource/Stage/minimapBG.png'))
        self.stageMiniMap.append(load_image('Resource/Stage/smallMap.png'))
        self.stageMiniMap.append(load_image('Resource/Stage/arrow.png'))

    def getStageInfo(self):
        # Stage 정보를 가져온다.------
        self.mapInfo = []
        f = open("mapinfo.txt", "rt")
        while True:
            c = f.read(1)
            self.mapInfo.append(c)
            if c == '':
                break
        f.close()
        for i in range(0, 9):
            if self.mapInfo[i] != '0':
                self.nowMapIndex = i
                break
        # ---------------------------

    def draw(self):
        w, h = 0, 0
        self.map.clip_composite_draw(0, 0, 1000, 700, 0.0, 'none',500, 350)
        for i in self.mapData:
            if i != 0:
                self.imageData[i].clip_composite_draw(0, 0, 50, 50, 0.0, 'none', w * 50 + 25, -25 + 700 - (h * 50), 50, 50)
            w = w + 1
            if w>=20:
                h = h + 1
                w = 0



        # 미니맵 그리기
        self.stageMiniMap[0].clip_composite_draw(0, 0, 100, 100,0.0, 'none', 100, 100, 100 ,100)
        for i in range(0, 9):
            if self.mapInfo[i] != '0':
                self.stageMiniMap[1].clip_composite_draw(0, 0, 30, 30,0.0, 'none', 65 + 35 * (i%3), 135 - (35 * int(i/3)), 20 ,20)

        self.stageMiniMap[2].clip_composite_draw(0, 0, 15, 15,0.0, 'none', 65 + 35 * (self.nowMapIndex%3), 135 - (35 * int(self.nowMapIndex/3)), 15 ,15)