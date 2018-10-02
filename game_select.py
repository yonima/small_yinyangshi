# -*- coding: utf-8 -*-
from yinyangshi import *
import time

# 创建游戏人物
datiangou = Yinyangshi('大天狗', '男', '是', '黑晴明', 3136, 10026)
xuenv = Yinyangshi('雪女', '女', '是', '黑晴明', 3048, 10634)
niumingbao = Yinyangshi('九命猫', '女', '否', '黑晴明', 2698, 9905)


def welcome ():
    """
        欢迎界面
    :return:
    """
    print('++++++++++++++++++++')
    print()
    print('欢迎进入阴阳师游戏世界')
    print()
    print('++++++++++++++++++++')


def introduction_game_character():
    """
        游戏人物介绍
    :return:
    """
    print('阴阳师人物介绍')
    datiangou.get_information()
    xuenv.get_information()
    niumingbao.get_information()


def please_select_game_character():
    """
         选择人物界面
    :return:
    """
    print()
    print('-------------------')
    print('请根据游戏人物介绍，选择喜欢的人物')
    print('1 大天狗')
    print('2 雪女')
    print('3 九命猫')


def select_figure(value):
    if value == 1:
        print()
        print('您选择的游戏人物是')
        datiangou.get_information()
        print()
        return datiangou
    elif value == 2:
        print()
        print('您选择的游戏人物是')
        xuenv.get_information()
        print()
        return xuenv
    elif value == 3:
        print()
        print('您选择的游戏人物是')
        niumingbao.get_information()
        print()
        return niumingbao
    else:
        print('请输入正确的选择数字')

def please_select_scene():
    """
        游戏场景
    :return:
    """
    print()
    print("===================")
    print('请选择游戏场景')
    print('4 阴界裂缝')
    print('5 鬼王封印')
    print("===================")

def introduction_game_scene():
    """
        介绍游戏场景
    :return:
    """
    print()
    print("您将进入游戏场景选择\n")
    print("此版本阴阳师，共设置两个游戏场景")

    print(" 阴界裂缝，消耗220攻击力、2000 生命。。")
    print(" 鬼王封印，消耗3100攻击力、3000 生命力..")

    print(" 在每一个场景里，如果生命或者攻击力没有这么多，则失败.")
    print(" 回城恢复原来的攻击力和生命力")

def enter_scene(game_figure, select_game):
    """
        进入游戏场景，开始游戏
    :param game_figure:
    :param select_game:
    :return:
    """
    if select_game == 4:
        print()
        print(F'欢迎 {game_figure.name} 来到 阴界裂缝，请开始您的游戏')

        game_figure.game_scene('阴界裂缝', 220, 2000)
        time.sleep(5)

    elif select_game ==5:
        print(f'欢迎{game_figure.name}来到 鬼王封印，请开始您的游戏')
        game_figure.game_scene('鬼王封印', 3100, 3000)
        time.sleep(5)


