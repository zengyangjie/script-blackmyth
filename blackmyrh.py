import pyautogui as pag
import keyboard
import time
import threading

# 通过键盘输入设置参数值
def get_input(prompt, default):
    user_input = input(prompt)
    return user_input if user_input else default

# 获取用户输入或使用默认值
load_time = int(get_input("请输入等待加载的时间（默认18秒）：", "18"))
start_key = get_input("请输入开始运行快捷键（默认home）：", "home")
pause_key = get_input("请输入暂停运行快捷键（默认end）：", "end")
stop_key = get_input("请输入停止程序快捷键（默认delete）：", "delete")

# 全局变量，用于控制自动化脚本是否运行
running = False
print(f'-----------------------------------------')
print(f'配置参数已通过键盘输入设置完成')
print(f'点击【{start_key}】键运行，点击【{pause_key}】键暂停，点击【{stop_key}】键结束程序')
print(f'提醒：如果是笔记本电脑或带fn的键盘，若按下以上三个按键无反应，需要在键盘上找到【fn】键')
print(f'提醒：同时按【fn】键和对应按键，如：同时按下【fn】+【{start_key}】')
print(f'提醒：运行此脚本后，需将画面切至游戏窗口，否则无法运行。')
print(f'尽量调整分辨率：1920*1080，显示模式：窗口模式，从土地庙缩地至：盘丝洞-碎玉池，将视角对准到土地庙直至出现【E 上香】')
print(f'在背包中将【缩地青符】放置【1号位】，将变身切换为【鼠】')
print(f'按下【{start_key}】即可开始娱乐，祝您旅途愉快')
print(f'-----------------------------------------')

def sleep(duration=0.2):
    print('等待' + str(duration) + '秒')
    time.sleep(duration)

def press(key, duration=0.1):
    print('按下' + key)
    pag.keyDown(key)
    sleep(duration)
    pag.keyUp(key)

def press2(key1, key2, duration=0.1):
    print('按下' + key1 + '和' + key2)
    pag.keyDown(key1)
    pag.keyDown(key2)
    sleep(duration)
    pag.keyUp(key2)
    pag.keyUp(key1)

def press3(key1, key2, key3, duration=0.1):
    print('按下' + key1 + '和' + key2 + '和' + key3)
    pag.keyDown(key1)
    pag.keyDown(key2)
    pag.keyDown(key3)
    sleep(duration)
    pag.keyUp(key3)
    pag.keyUp(key2)
    pag.keyUp(key1)

def multi_press(key, num=3, duration=0.1):
    print('按下' + key + '键' + str(num) + '次')
    for i in range(num):
        press(key, duration)

def click(button='left', duration=0.1):
    pag.mouseDown(button=button)
    sleep(duration)
    pag.mouseUp(button=button)

def brush_lingyun():
    multi_press('e')
    sleep(2)
    press('esc')
    sleep(2)

    press('s', 0.5)
    press('d', 2.8)
    press2('w', 'd', 3.3)
    press('w', 5.5)
    multi_press('4', 8)
    sleep(3)
    multi_press('q', 5)
    sleep(load_time)

def is_finished():
    return False

def automate_script():
    while True:
        if running:
            brush_lingyun()
        else:
            time.sleep(0.1)  # 如果不运行，稍微休眠一下以减少CPU占用

def start_automation():
    global running
    running = True
    print("自动化脚本已启动")
    time.sleep(0.1)  # 添加短暂延迟

def stop_automation():
    global running
    running = False
    print("自动化脚本已暂停")
    time.sleep(0.1)  # 添加短暂延迟

# 监听键盘事件
keyboard.add_hotkey(start_key, start_automation)
keyboard.add_hotkey(pause_key, stop_automation)

# 启动自动化线程
thread = threading.Thread(target=automate_script, daemon=True)
thread.start()

# 保持主线程运行
keyboard.wait(stop_key)  # 按下“stop_key”退出程序
