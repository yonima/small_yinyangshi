# -*- coding: utf-8 -*-

import time


class Yinyangshi:
    """
         定义阴阳师类:
         包括阴阳师人物（属性）和游戏场景（方法）
    """
    def __init__(self,name, gender, shishen, boss, attack, life):
        ''' 定义属性：游戏人物的属性 '''
        self.name = name
        self.gender = gender
        self.shishen = shishen
        self.boss = boss
        self.attack = attack
        self.life = life

        # 添加两个新的属性，保存最初的生命力和攻击力
        # 也可以写成方法
        self.init_vale(attack, life)
        # self.attack_init = attack
        # self.life_init = life

    def init_vale(self, attack, life):
        """
        回城以后，恢复攻击力和生命力
        :param attack:
        :param life:
        :return: none
        """
        self.attack_init = attack
        self.life_init = life

    def get_information(self):
        """
            描述游戏人物信息
        :return:
        """
        # print('阴阳师人物介绍:')
        information = '  {n}、{g}、式神:{s}、主人：{b}、攻击力{a}、生命值{l}'
        mess = information.format(n = self.name,
                                  g = self.gender,
                                  s = self.shishen,
                                  b = self.boss,
                                  a = self.attack,
                                  l = self.life)
        print(mess)

    def game_scene(self, name,  consume_attack, consume_life):
        """
            定义方法：游戏场景
        :return:
        """
        print()
        print(f'您已经进入{name} 战场')
        print("敌人还有五秒达到战场")
        time.sleep(2)
        print(f'开始{name}游戏')
        print()
        if self.attack < consume_attack or self.life < consume_life:
            print('您的生命力或者攻击力已耗尽')
            print('   游戏失败！请回城!!!!!!!!!  ')
            self.return_home()
        else:
            self.attack = int(self.attack) - int(consume_attack)
            self.life = self.life - consume_life
            print(f'恭喜您成功通过{name}！')
            print(f'目前攻击力为{self.attack}、生命值为{self.life}')

    def return_home(self):
        """
            回城
        :return:
        """
        information = '{n}已回城，恢复攻击力{a}、生命值{l}'
        mess = information.format(n=self.name,
                                  a=self.attack_init,
                                  l=self.life_init)
        print(mess)
