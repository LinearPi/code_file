"""
生成滑动轨迹
由于极验的后台在不断的训练识别模型，所以移动轨迹可能是有实效性的，时常需要修改
轨迹要尽量的靠近人类的行为习惯
"""
import random


class SlidingTrack(object):
    def __init__(self, position):
        self.position = position
        self.set_random_params()

    def set_random_params(self):
        self.mid = random.uniform(0.5, 0.8) * self.position
        if self.position < 80:
            self.t = random.uniform(0.15, 0.4) * 0.8
            self.up_a = random.uniform(1.5, 4) * 0.8
            self.down_a = random.uniform(-3, -5) * 0.8
        elif 140 >= self.position >= 80:
            self.t = random.uniform(0.15, 0.4)
            self.up_a = random.uniform(1.5, 4)
            self.down_a = random.uniform(-3, -5)
        elif self.position > 140:
            self.t = random.uniform(0.15, 0.4) * 1.2
            self.up_a = random.uniform(1.5, 4) * 1.2
            self.down_a = random.uniform(-3, -5) * 1.2

    def get_move_list(self):
        currtent = 0
        speed = 0
        move_list = []

        while currtent < self.position:
            if currtent < self.mid:
                # 距离的计算公式
                move = speed * self.t + 0.5 * self.up_a * self.t * self.t
                # 将生成的移动距离添加到列表中
                move_list.append(round(move))
                speed += (self.up_a * self.t)
                currtent += move
            else:
                move = speed * self.t + 0.5 * self.down_a * self.t * self.t
                # 将生成的移动距离添加到列表中
                move_list.append(round(move))
                speed += (self.down_a * self.t)
                currtent += move
                if speed <= 0:
                    break

        print(speed)

        if speed < 0:
            x, y = 3, 2
        elif 5 > speed >= 0:
            x, y = 4, 2
        elif 13 > speed >= 7:
            x, y = 5, 3
        elif speed >= 13:
            x, y = 6, 4

        offset = sum(move_list) - self.position
        if offset > 0:
            end_track = [-1]*offset + [-1]*x + \
                [0]*5 + [1]*(x+y) + [0]*5 + [-1]*y
        elif offset < 0:
            end_track = [1]*abs(offset) + [1]*x + [0]*5 + \
                [-1]*(x+y) + [0]*5 + [1]*y
        else:
            end_track = [1]*x + [0]*5 + [-1]*(x+y) + [0]*5 + [1]*y

        move_list.extend(end_track)
        print(move_list)
        print(self.position)

        return move_list
