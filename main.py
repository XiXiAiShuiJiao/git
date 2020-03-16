import time
import os
import view
import date

date.date_local()

print("正在启动请稍后")
for i in range(0, 6):
    a = "■■■"
    os.system('cls')
    print("|" + "{:<15}".format(a * i) + "|")
    time.sleep(0.35)
print("载入完成,欢迎使用")
time.sleep(0.7)
view.main_menu()
