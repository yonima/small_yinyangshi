# -*- coding: utf-8 -*-
"""
    阴阳师主程序
    1、创建一个SSR、一个SR以及R 游戏人物，分别是：
    大天狗，男，式神：是，主人：黑晴明，攻击力3136、生命10026
    雪女，女，式神：是，主人：黑晴明，攻击力 3048、生命 10634
    九命猫，女，式神：否；主人：黑晴明，攻击力2968、生命力 9905
    2、游戏场景，分别：
    请在每一个场景里输出（“敌人还有五秒到达战场”）
    如果生命或者攻击力没有这么多，则失败，回程
    阴界裂缝，消耗220攻击力、2000生命。。
    鬼王封印，消耗3100攻击力、3000生命力
    回城，    回复原来的攻击力和生命力

    知识点：
        代码重构
"""

from yinyangshi import *
import game_select as gs
import time

# 进入游戏场景
while True:

    # 游戏欢迎界面
    gs.welcome()
    time.sleep(3)

    # 游戏人物介绍
    gs.introduction_game_character()
    gs.please_select_game_character()

    input_figure = int(input('请输入您使用的游戏人物'))
    game_figure = gs.select_figure(input_figure)
    time.sleep(2)

    # 游戏场景介绍以及选择
    gs.introduction_game_scene()
    gs.please_select_scene()
    time.sleep(2)
    select_game = int(input('请输入您要进入的游戏场景'))

    # 开始游戏
    gs.enter_scene(game_figure, select_game)

    # 是否进入下一轮游戏
    print()
    end_game = input(" 是否接着开始下一次挑战（Y/N）")
    if end_game == 'N':
        print()
        print("游戏结束！")
        break
    elif end_game == 'Y':
        print()
        print("接着开始")



