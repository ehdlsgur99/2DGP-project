from pico2d import *
import random

def generateMapInfo():
    templateData = [
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

    # 파일 열기
    f = open('mapinfo.txt', 'w')

    # index 3x3 = 9 로 저장저장
    mapindex = [0, 0, 0,
                0, 0, 0,
                0, 0, 0]

    for i in range(0, 9):
        if random.randint(0, 2) != 0:
            mapindex[i] = 1

    #끊어진 길을 이어보자
    #가로 2번줄이 짤린 경우
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    for i in range(0, 9):
        if i < 3:
            if mapindex[i] == 1:
                cnt1 += 1
        elif i >5:
            if mapindex[i] == 1:
                cnt3 += 1
        else:
            if mapindex[i] == 1:
                cnt2 += 1

    if cnt1 >1 and cnt3 >1 and cnt2 == 0:
        mapindex[4] = 1

    if mapindex[0] == 0 and mapindex[2] == 0 or mapindex[2] == 0 and mapindex[6] or mapindex[2] == 0 and mapindex[8] == 0 or mapindex[6] == 0 and mapindex[8] :
        mapindex[4] = 1


    # 파일에 텍스트 쓰기
    for i in range(0, 9):
        f.write(str(mapindex[i]))

    # 파일 닫기
    f.close()

    #map9개 만들기
    count = 0
    for i in range(0, 9):
        count += 1
        f = open('map/map' + str(count) + '.txt', 'w')
        for j in templateData:
            f.write(str(j))
        f.close()





