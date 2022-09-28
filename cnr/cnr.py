import math
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

#한꺼번에 많이 작성하고 실행하지 않기, 실행 자주잦주 하기

def render_all(x,y):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.02)


#원 위의 점이 있을 때 반지름을 r, 각도를 세타라고 한다면
#x 좌표는 r cos세타, y좌표는 r sin 세
def run_circle():
    print('circle')

    cx, cy, r = 400, 300, 200
    for deg in range(0, 360, 5):     # while도 가능하지만, 직관적으로 for가 더 가독성이 좋을 수도 있음.
        x = cx + r * math.cos(deg/360*2*math.pi)
        y = cy + r * math.sin(deg/360*2*math.pi)
        render_all(x,y)

def run_rectangle():
    print('rectangle')

    #bottom line
    for x in range(50,750+1,10):
        render_all(x,90)
    #right side
    for y in range(90, 550+1, 10):
        render_all(750, y)
    #top line
    for x in range(750, 50-1, -10):     # 자잘한 것들은 idle에서 시험해봐도 괜찮음.
        render_all(x,550)
    #left side
    for y in range(550, 90-1, -10):
        render_all(50,y)


while True:
    run_circle()
    run_rectangle()
    break

close_canvas()
