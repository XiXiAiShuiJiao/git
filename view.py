import os
import func
import view
import date
import random
from date import date_local
date_local()
# 1.0 登陆成功后的菜单


def main_menu():
    while True:
        os.system('cls')
        print("————————————————————————————")
        print("赵氏通货商店欢迎您")
        print()
        print("1.登录商城")
        print("2.注册账号")
        print("3.娱乐功能")
        print("*.敬请期待")
        print("0.退出商城")
        print("————————————————————————————")
        choice = input("请选择功能：")
        os.system('cls')
        eval(date.menu_choice["main_menu"].get(choice, "main_menu()"))


def login_fo():
    """登陆成功后的菜单,做跳转,无其他功能"""
    if func.status == "online":
        os.system('cls')
        print("————————————————————————————")
        print("欢迎回来", date.dicc[func.login_id]["name"])  # 显示用户昵称
        print()
        print("1.通货商城")
        print("2.个人信息")
        print("3.查找用户")
        print("0.退出账号")
        print("————————————————————————————")
        choice = input("请选择:")
        if choice == "0":
            func.status = 0
        else:
            return eval(date.menu_choice["login_fo"].get(choice, "login_fo()"))


# 1.1 通货商城
def login_currency():
    """仅菜单,没功能"""
    os.system('cls')
    date.date_local
    print("————————————————————————————")
    print("欢迎来到通货商城", date.dicc[func.login_id]["name"])
    wallet = date.dicc[func.login_id]["wallet"]
    print(f"我的余额{wallet}")
    print()
    print("1.崇高石")
    print("2.神圣石")
    print("3.剥离石")
    print("4.远古石")
    print("5.我的背包")
    print("0.返回上级")
    print("————————————————————————————")
    choice = input("我想：")
    if choice == "0":
        return login_fo()
    elif choice == "1":
        goods = "崇高石"
        cost = random.randint(170, 200)
        print(f"崇高石价格为:{cost}")
    elif choice == "2":
        goods = "神圣石"
        cost = random.randint(70, 90)
        print(f"神圣石价格为:{cost}")
    elif choice == "3":
        goods = "剥离石"
        cost = random.randint(120, 150)
        print(f"剥离石价格为:{cost}")
    elif choice == "4":
        goods = "远古石"
        cost = random.randint(50, 55)
        print(f"远古石价格为:{cost}")
    elif choice == "5":
        print("————————————————————————————")
        print("崇高石:", date.dicc[func.login_id]["崇高石"])
        print("神圣石:", date.dicc[func.login_id]["神圣石"])
        print("剥离石:", date.dicc[func.login_id]["剥离石"])
        print("远古石:", date.dicc[func.login_id]["远古石"])
        input("按任意键返回商城")
        return login_currency()
    else:
        return login_currency()
    price = int(cost)
    while True:
        print(f"您要购买的是{goods},价格为:{price}")
        print(f"您的余额为:{wallet}")
        num = input("请输入想要购买的数量:")
        if num.isdigit():
            num = int(num)
            print("总价为:", price*num)
            coin = wallet - price*num
            print(f"购买后剩余{coin}")
            if coin < 0:
                print("余额不足,无法购买")
            else:
                a = input("是否购买(Y/N):").upper()
                if a == "Y":
                    wallet = coin
                    date.dicc[func.login_id]["wallet"] = wallet
                    date.dicc[func.login_id][f"{goods}"] = num
                    dicc_txt = open("dir.txt", "w+")
                    dicc_txt.write(str(date.dicc))
                    dicc_txt.close()
                    return login_currency()
                elif a == "N":
                    return login_currency()
                else:
                    continue
        else:
            print("输入错误")


# 3.游戏菜单
def game():
    os.system('cls')
    print("————————————————————————————")
    print("赵氏GAME欢迎您")
    print()
    print("1.猜数字")
    print("2.CRAPS赌博游戏")
    print("3.石头剪刀布")
    print("*.敬请期待")
    print("0.返回首页")
    print("————————————————————————————")
    game_choice = input("请选择功能：")

    if game_choice == "1":
        return func.game_guess()
    elif game_choice == "2":
        return func.game_CRAPS()
    elif game_choice == "3":
        return func.game_stj()
    elif game_choice == "0":
        pass
    else:
        input("系统升级中，按任意键并回车重新输入")
    return view.game()
