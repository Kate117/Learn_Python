#-*- coding:utf-8 -*-
#!/usr/bin/env python3

"""
Function: lucky draw app

Description:
Step1: implement lucky_draw function.
    using random module to choose 3 persons for No.3 award, 2 persons for No.2 award, and 1 person for No.1 awrd from
    give name_list. The effect is as below:
    >> Participants of this lucky draw are [...]
    >> Are you ready to choose No.3 award?(Y/N): Y
    >> The lucky ones for third prize are:
        ========== Third prize =========
                        A
                        B
                        C
        ================================
    >> Are you ready to choose No.2 prize?(Y/N): Y
    >> The lucky ones for second prize are:
        ========== Second prize ========
                        D
                        E
        ================================
    >> The lucky ones for first prize is:
        ========== First prize =========
                        F
        ================================
    >> End

Step2: increase yourself possibility of luck :)
Step3: TODO

Author: Liu, Kate

Date: 2/22/2019 ~ 2/28/2019
"""

import random



def lucky_draw(name_list=None):
    """
    this is your code area
    :param name_list:
    :return:
    """
    print('Participants of the lucky draw are:',name_list)

    round_1 = input('Are you ready to select the 3rd prize?(Y/N) \n>')
    answer = ('Y','y')
    if round_1 in answer:
        name1 = random.sample(name_list, 3)
        print(name1)
        for name in name1:
            name_list.remove(name)
        print('Now there are remaining lucky ones:', name_list)

    round_2 = input ('Ready for the 2nd prize?(Y/N) \n>')
    if round_2 in answer:
        name2 = random.sample(name_list, 2)
        print(name2)
        for r_name in name2:
            name_list.remove(r_name)
    round_3 = input ('Now is the most exciting time, 1st prize! Ready?(Y/N) \n>')
    if round_3 in answer:
        name3 = random.sample(name_list, 1)
        print(name3)


def main():
    name_list = ['Anna', 'kate', 'Liangchun', 'Tina', 'tim', 'Turen','Shoujiang','Sarah','Tingting','Jingjing']
    lucky_draw(name_list)

if __name__ == '__main__':
    main()