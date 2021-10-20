from pico2d import *
import random

def generateMapInfo():
    # 파일 열기
    f = open('mapinfo.txt', 'w')

    # index 3x3 = 9 로 저장저장
    mapindex = [0, 0, 0,
                0, 0, 0,
                0, 0, 0]

    for i in range(0, 9):
        if random.randint(0, 2) != 0:
            mapindex[i] = 1

    # 파일에 텍스트 쓰기
    for i in range(0, 9):
        f.write(str(mapindex[i]))

    # 파일 닫기
    f.close()




