import sys

import pygame
import serial # pyserial
import time
import math

pygame.init()

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
sc = pygame.display.set_mode((900,500))
pygame.display.set_caption('Arduino Radar Viewer')
font = pygame.font.Font('font.ttf',20)

logo = pygame.image.load('tf_dot_text_logo.png')
size = logo.get_size()
scale = 2
logo = pygame.transform.scale(logo,(size[0]/scale,size[1]/scale))
logoR = logo.get_rect()

size = sc.get_size()
def toInt(x) -> int:
    try: return int(x)
    except: return 0

lines = {}

while True:
    try:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        sc.fill((0,0,0))
        data = arduino.readline().decode('utf8') \
            .replace('\r', '') \
            .replace('\n', '').split(' ')
        data[0] = toInt(data[0])
        data[1] = toInt(data[1])
        lines[data[0]] = {'d': data[1], 't': time.time(), 'a':255}
        result = data[1]
        logoR.x = 10
        logoR.y = size[1]-logoR.h-10
        sc.blit(logo,logoR)

        if result >= 60:
            result = f'{int(result/60)}m {result-(60*int(result/60))}'

        text = font.render(f'D: {result}cm',True, (255,255,255))
        textR = text.get_rect()
        textR.y = (size[1]/2)+230
        textR.centerx = size[0]/2
        sc.blit(text,textR)

        for i in lines.keys():
            d = lines[i]['d']
            t = lines[i]['t']
            a = lines[i]['a']

            print(a)

            x = (size[0]/2) + math.cos(math.radians(-i)) * 200
            y = (size[1]/2) + math.sin(math.radians(-i)) * 200
            if a>255: a = 255
            if a < 0: a = 0
            pygame.draw.line(sc,(0,a,0),(size[0]/2,size[1]/2),(x,y),3)
            x2 = (size[0] / 2) + math.cos(math.radians(-i)) * (200*((d/60)/2))
            y2 = (size[1] / 2) + math.sin(math.radians(-i)) * (200*((d/60)/2))
            pygame.draw.line(sc, (a,0,0), (x2, y2), (x, y), 3)

            lines[i]['a'] = a-5
        pygame.draw.circle(sc, (255, 255, 255), (size[0] / 2, size[1] / 2), 200, 2)
        pygame.draw.circle(sc, (100, 100, 100), (size[0] / 2, size[1] / 2), 200-((200/4)*1), 2)
        pygame.draw.circle(sc, (100, 100, 100), (size[0] / 2, size[1] / 2), 200-((200/4)*2), 2)
        pygame.draw.circle(sc, (100, 100, 100), (size[0] / 2, size[1] / 2), 200-((200/4)*3), 2)

        pygame.display.flip()
    except Exception as e: print(e)