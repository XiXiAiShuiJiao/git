import os
import time
import random
import view
import date
date.date_local()


# 1 登录
def signin():
    """登录模块,使用用户字典"""
    print("————————————————————————————")
    print("账号登录")
    print()
    global login_id
    global login_pass
    global status

    login_id = input("请输入您的账号:")
    login_pass1 = input("请输入您的密码:")
    login_pass = login_pass1.translate(date.table_t)

    # 如果用户信息字典中有该账号和密码,则登录
    try:
        if login_id == date.dicc[login_id]["id"] and login_pass == date.dicc[login_id]["password"]:
            input("登录成功，按任意键进入商城。")
            status = "online"
            return view.login_fo()
        else:
            print("账号或密码错误，请重新输入!")
            print("————————————————————————————")
            while True:
                ny = input("是否登录(Y/N)？").upper()
                if ny == "Y":
                    return signin()
                elif ny == "N":
                    break
    # 字典内没账号
    except KeyError:
        while True:
            eor = input("账号密码错误（继续Y/返回N）").upper()
            if eor == "Y":
                return signin()
            elif eor == "N":
                break
            else:
                continue
# 1.2 个人信息


def login_date():
    """
    尝试显示信息,没有则不显示
    """
    user_date = date.dicc["{}".format(login_id)]
    print("————————————————————————————")
    print("该界面是显示用户的个人信息")
    print()
    print("昵称:", user_date["name"])
    print("性别:", user_date["sex"])
    print("职业:", user_date["job"])
    print("签名:", user_date["info"])
    print()
    print("————————————————————————————")
    print("1.更新个人信息")
    print("0.返回上一级")
    a = input("请输入选项：")
    if a == "0":
        return view.login_fo()
    elif a == "1":
        sex = input("请输入性别：")
        job = input("请输入职业：")
        info = input("请输入签名：")
    date.date_save(login_id, sex, job, info)
    input("修改成功，按任意键并回车返回菜单")
    return view.login_fo()
# 1.3 修改密码


def login_change():
    print("————————————————————————————")
    print("赵氏通货商店欢迎您")
    print()
    change_choice = input("您来到的是修改密码界面，是否继续?（Y/N）:").upper()
    if change_choice == "y":
        print("您来到的是修改密码界面，请先确认身份")
        change_id = input("用户账号：")
        change_pass = input("用户密码：")
    elif change_choice == "N":
        return view.login_fo()
    else:
        print("输入错误，重新输入")
        return login_change()

    if change_id == login_id and change_pass == login_pass:
        new_pass = input("请输入新密码：")
        new2_pass = input("请重复新密码：")
    date.change_pass(change_id, new_pass, new2_pass)

    input("修改成功，请重新登录")


# 1.5 查找用户
def login_search():
    print("————————————————————————————")
    search_id = input("请输入要查询的用户账号：")
    if search_id in date.dicc:
        print("用户：" + date.dicc[search_id]["id"])
        print("昵称：" + date.dicc[search_id]["name"])
        print("性别：" + date.dicc[search_id]["sex"])
        if len(date.dicc[search_id]["info"]) > 9:
            print("个性签名：" + date.dicc[search_id]["info"][0:10])
        else:
            print("个性签名：" + date.dicc[search_id]["info"] + "......")
    a = input("详情/返回（Y/N）").upper()
    if a == "Y":
        print("未写,将返回菜单")
        time.sleep(1)
        return view.login_fo()
    elif a == "N":
        return view.login_fo()


# 注册
def register():
    os.system('cls')
    print("————————————————————————————")
    print("账号注册")
    print()
    yn = input("注册/返回（Y/N）").upper()
    while True:
        if yn == "Y":
            register_path()
            break
        elif yn == "N":
            break
        else:
            continue


def register_path():
    register_id = input("请输入您要注册的账号：").strip()
    if register_id in date.dicc.keys():
        input("该账号已存在，请重新输入")
        return register_path()
    else:
        while True:
            # 使用strip去除账号密码两端空格
            register_pass = input("请输入您的密码：").strip()
            if register_pass == "":
                print("密码不可空，请重新输入")
                print("————————————————————")
                continue
            else:
                register_pass2 = input("请再次输入您的密码：").strip()
                if register_pass != register_pass2:
                    print("密码不一致，请重新输入")
                    print("————————————————————")
                    continue
                else:
                    while True:
                        register_name = input("请输入用户昵称:")
                        if register_name == "":
                            print("昵称不可为空")
                        elif register_name in date.dicc.values():
                            print("已有该昵称")
                        else:
                            break
                    break
        date.save_reg(register_id, register_pass, register_name)

    input("注册成功,按任意键并回车返回首页")


# 猜拳计分装饰器
def Scoring(fn):

    def inner():

        global login_id
        while True:
            try:
                with open("{}.txt".format(login_id), "r") as filename:
                    count1 = filename.read()
                    filename.close()
            except FileNotFoundError:
                count1 = "100"
            finally:
                count = int(count1)
            print("---------")
            print("您的积分:{}".format(count))
            print("---------")
            fn()
            with open("{}.txt".format(login_id), "w") as filename:
                if win == 1:
                    count = count + 2
                    filename.write(str(count))
                elif win == 0:
                    count = count - 1
                    filename.write(str(count))
                else:
                    filename.write(str(count))
                filename.close()
            choice = input("继续/返回(Y/N):").upper()
            if choice == "Y":
                continue
            elif choice == "N":
                break
        return view.game()
    return inner
# 3.1 猜数字


def game_guess():
    os.system('cls')
    print("————————————————————————————")
    print("赵氏GAME欢迎您")
    print()
    shuzi = random.randint(1, 100)
    cishu = 0

    while True:
        cishu = cishu + 1
        nu = input("请输入100以内整数(Q退出)：").upper()

        if nu.isdigit():
            guess_num = int(nu)

            if 1 <= guess_num <= 100:
                if guess_num > shuzi:
                    print("大了")
                elif guess_num < shuzi:
                    print("小了")
                elif guess_num == shuzi:
                    print("猜对了")
                    print("你一共猜了：" + str(cishu) + "次")
                    guess_choice = input("是否继续（Y/N）").upper()

                    if guess_choice == "y":
                        game_guess()
                    elif guess_choice == "N":
                        view.game()
            else:
                print("输入错误")
                continue
        elif nu == "Q":
            view.game()
        else:
            input("输入错误，按任意键重新输入")


# 3.2 CRAPS游戏
def game_CRAPS():
    os.system('cls')
    print(
        '''CRAPS赌博游戏。
        玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
        玩家第一次如果摇出2点、3点或12点，庄家胜；
        其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
        如果玩家摇出了第一次摇的点数，玩家胜；
        其他点数，玩家继续要骰子，直到分出胜负''')
    shu = 0
    ying = 0

    while True:
        print("—————————————————")
        print("赌博有害，不要赌博")
        peo = input("是否开始/继续？：（Y/N）").upper()

        if peo == "Y":
            one = random.randint(1, 6)
            two = random.randint(1, 6)
            first = one + two
            print("玩家摇出了%d,%d点数，共%d点" % (one, two, one + two))

            if first == 7 or first == 1:
                print("您赢了")
                ying += 1
            elif first in [2, 3, 12]:
                print("您输了")
                shu += 1
            else:
                while True:
                    one = random.randint(1, 6)
                    two = random.randint(1, 6)
                    zong = one + two
                    print("玩家摇出了%d,%d点数，共%d点" % (one, two, zong))

                    if zong == 7:
                        print("您输了")
                        shu += 1
                        break
                    elif zong == first:
                        print("您赢了")
                        ying += 1
                        break
        elif peo == "N":
            print("您本次游玩共计游玩%d次，输了%d次，赢了%d次" % (shu + ying, shu, ying))
            print("希望您玩得愉快，以后远离赌博😊")
            break
    input("按任意键并回车返回游戏菜单")
    view.game()
    print("————————————————————————————")


@Scoring
# 3.3 猜拳
def game_stj():
    global win
    a = random.choice(["石头", "剪刀", "布"])
    b = input("请出拳（1-石头/2-剪刀/3-布）：")

    if (b == "1" and a == "剪刀") or (b == "2" and a == "布") or (b == "3" and a == "石头"):
        print("你的对手出了" + a, "，结果为：胜利")
        win = 1
    elif (a == "石头" and b == "2") or (a == "剪刀" and b == "3") or (a == "布" and b == "1"):
        print("你的对手出了" + a, "，结果为：失败")
        win = 0
    elif b not in ["石头", "剪刀", "布", "1", "2", "3"]:
        print("输入错误重新输入")
    else:
        print("你的对手出了" + a, "，结果为：平局")
        win = 2
