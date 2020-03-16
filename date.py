import string
import os

# 真密码
password_t = string.ascii_letters + string.digits
# 假密码
password_f = string.digits + string.ascii_letters
# 真-->假
table_t = str.maketrans(password_t, password_f)
# 假-->真
table_f = str.maketrans(password_f, password_t)
# 菜单选项表
menu_choice = {
    "main_menu": {"1": "func.signin()", "2": "func.register()", "3": "game()", "0": "exit()"},
    "game": {"1": "view.game_guess()", "2": "view.game_CRAPS()", "3": "view.game_stj()", "0": "foomain_menu()"},
    "login_fo": {"1": "view.login_currency()", "2": "func.login_date()", "3": "func.login_search()", "0": "pass"}
}


# 个人资料更新
def date_save(id, sex, job, info):
    dicc["{}".format(id)].update(
        {"sex": sex, "job": job, "info": info})

    # 打开字典txt,把更新的信息存进去
    dicc_txt = open("dir.txt", "w+")
    dicc_txt.write(str(dicc))
    dicc_txt.close()


# 修改密码
def change_pass(id, new1, new2):
    while True:  # 读取用户信息,检测旧密码所在位置,替换为新密码
        if new1 == new2:
            global table_t
            new_pass = new1.translate(table_t)
            with open("user.txt", "r") as e:
                lines = e.readlines()
            with open("user.txt", "w") as f:
                for line in lines:
                    if id + "," + change_pass in line:
                        f.write(id + "," + new_pass)
                        f.write("\n")
                        continue
                    f.write(line)
                f.close()
        else:
            print("输入错误，重新输入")


# 保存注册信息
def save_reg(id, password, name):
    global dicc
    password = password.translate(table_t)

    # 使用用户信息创建用户账户为名的字典
    dicc["{}".format(id)] = {"id": id, "password": password, "name": name,
                             "sex": "保密", "job": " ", "info": "尚未填写个人签名",
                             "wallet": 1000, "崇高石": 0, "神圣石": 0, "剥离石": 0, "远古石": 0}

    # 写入字典txt
    dict_txt = open("dir.txt", "w+")
    dict_txt.write(str(dicc))
    dict_txt.close()


# 读取用户所有信息
def date_local():
    '''读取用户所有信息(登录,注册,显示所有信息)'''
    try:
        global dicc
        dicc = {}
        with open("dir.txt", "r+") as dict_txt:
            # dict_txt = open("dir.txt", "r+")
            dicc = eval(dict_txt.read())
            dict_txt.close()
    except FileNotFoundError:
        pass
    finally:
        os.system('cls')
