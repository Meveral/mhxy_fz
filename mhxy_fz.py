#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import threading
from builtins import filter
from pydoc import text

import win32con
import win32api, win32gui
import random
import time
import tkinter as tk
# from memory_pic import *
# from my_memory_pic import *
from PIL import ImageGrab, Image
import base64

#someValue
Width = 834
Height = 652
RenwuStep=77
BeibaoStep=80

#somePos
DadituPos=[30,65]
XiaodituPos = [120, 70]
DianxiaoerPos = [707,442 ]
DuiwuPos = [785, 135]
BaotuPos = [725, 190]
RenwuchuansongPos=[800,665]
CloserenwuPos=[931,137]
BeibaoPos=[993,678]
ZhengliPos=[840,675]
ShimenrenwuPos=[850,520]
GoumaiPos=[835,677]
YaodiangoumaiPos=[800,610]
SomePos = [870,384]
#1.野猪精：有话好好说 2.太白金星，师门任务
ShimenduihuaPos=[[847,548],[756,332]]


#someArea
RenwuArea = [820,136,907,175]
HuodongArea = [293,44,346,98]
ChangguirenwuArea=[254,207,285,233]
FirstRenwuArea=[140,284,190,307]
MashangchuansongArea=[749,647,873,681]
CangbaotushiyongArea =[830,655,902,687]
ShimencijiaoArea = [750, 556, 968, 589]

image_path = "Resource/"

# 从.py文件获取图片
def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(base64.b64decode(pic_code))
    image.close()


# 导入图片
if 0:
    get_pic(bangpai_jpg, 'bangpai_jpg')
    get_pic(bangpai_renwu_jpg, 'bangpai_renwu_jpg')
    get_pic(bangpai_renwu2_jpg, 'bangpai_renwu2_jpg')
    get_pic(goumai_cw_jpg, 'goumai_cw_jpg')
    get_pic(goumai_sc_jpg, 'goumai_sc_jpg')
    get_pic(goumai_yp_jpg, 'goumai_yp_jpg')
    get_pic(shangjiao_cw_jpg, 'shangjiao_cw_jpg')
    get_pic(shangjiao_yp_jpg, 'shangjiao_yp_jpg')
    get_pic(shimen_jpg, 'shimen_jpg')
    get_pic(shimen_songxin_jpg, 'shimen_songxin_jpg')
    get_pic(shiyong_jpg, 'shiyong_jpg')
    get_pic(qiecuo_jpg, 'qiecuo_jpg')
    get_pic(qiecuo_yulin_jpg, 'qiecuo_yulin_jpg')

    get_pic(renwuweizhankai_an_jpg,'renwuweizhankai_an_jpg')
    get_pic(renwuweizhankai_liang_jpg,'renwuweizhankai_liang_jpg')


def move_click(x, y, t=0):  # 移动鼠标并点击左键

    win32api.SetCursorPos((x, y))  # 设置鼠标位置(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)  # 点击鼠标左键
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 点击鼠标左键
    if t == 0:
        time.sleep(random.random() * 2 + 1)  # sleep一下
    else:
        time.sleep(random.random()*2+t)
    return 0


# 测试
# move_click(300, 300)

def resolution():  # 获取屏幕分辨率
    return win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)


# screen_resolution = resolution()

# 获取梦幻西游窗口信息吗，返回一个矩形窗口四个坐标
def get_window_info():
    wdname = u'《梦幻西游》手游'
    handle = win32gui.FindWindow(0, wdname)  # 获取窗口句柄
    if handle == 0:
        # text.insert('end', '提示：请打开梦幻西游\n')
        # text.see('end')  # 自动显示底部
        return None
    else:
        return win32gui.GetWindowRect(handle)


# window_size = get_window_info()
# 返回x相对坐标
def get_posx(x, window_size):
    return int((window_size[2] - window_size[0]) * x / 804)


# 返回y相对坐标
def get_posy(y, window_size):
    return int((window_size[3] - window_size[1]) * y / 630)



def click_renwu(window_size,taskName):
    topx, topy = window_size[0], window_size[1]
    window_shift=[topx,topy,topx,topy]
    # 1.点开任务栏
    move_click(topx + RenwuArea[0], topy + RenwuArea[1])
    move_click(topx + RenwuArea[0], topy + RenwuArea[1])


    # 2.展开任务栏
    img_tmp = ImageGrab.grab(i + j for i, j in zip(window_shift, ChangguirenwuArea))
    img_tmp_hashed = get_hash(img_tmp)
    if (hamming(get_hash(Image.open(image_path + "renwuweizhankai_an.jpg")), img_tmp_hashed) or
            hamming(get_hash(Image.open(image_path + "renwuweizhankai_liang.jpg")), img_tmp_hashed)):
        move_click(topx + ChangguirenwuArea[0], topy + ChangguirenwuArea[1])

    # 3.选中任务
    step=-1
    FirstRenwuArea_jueduiweizhi = [i + j for i, j in zip(window_shift, FirstRenwuArea)]
    img_task_an = Image.open(image_path + taskName+"_an.jpg")
    img_task_liang= Image.open(image_path + taskName+"_liang.jpg")
    img_task_an_hashed = get_hash(img_task_an)
    img_task_liang_hashed = get_hash(img_task_liang)
    for i in range(3):
        x1, y1, x2, y2 = FirstRenwuArea_jueduiweizhi[0], FirstRenwuArea_jueduiweizhi[1] + i * RenwuStep, \
                         FirstRenwuArea_jueduiweizhi[2], FirstRenwuArea_jueduiweizhi[3] + i * RenwuStep
        img_tmp = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        # img_tmp.show()
        # img_tmp.save("test"+str(i)+".jpg")
        img_tmp_hashed = get_hash(img_tmp)

        if (hamming(img_task_an_hashed, img_tmp_hashed) or hamming(img_task_liang_hashed, img_tmp_hashed)):
            step= i
            move_click(x1, y1)
            break
    return step


# # 抓取游戏指定坐标的图像
# img_ready = ImageGrab.grab((topx + get_posx(500, window_size), topy + get_posy(480, window_size),
#                             topx + get_posx(540, window_size), topy + get_posy(500, window_size)))
# # 查看图片
# img_ready.show()

# 获得图像的hash值
def get_hash(img):
    img = img.resize((16, 16), Image.ANTIALIAS).convert('L')  # 抗锯齿 灰度
    avg = sum(list(img.getdata())) / 256  # 计算像素平均值
    s = ''.join(map(lambda i: '0' if i < avg else '1', img.getdata()))  # 每个像素进行比对,大于avg为1,反之为0
    return ''.join(map(lambda j: '%x' % int(s[j:j + 4], 2), range(0, 256, 4)))


# 计算两个图像的汉明距离
def hamming(hash1, hash2, n=10):
    b = False
    assert len(hash1) == len(hash2)
    tmp_ = sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2))
    if sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2)) < n:
        b = True
    return b


# 抓鬼
def zhua_gui(window_size):
    global is_start
    is_start = True
    topx, topy = window_size[0], window_size[1]

    # 是否继续
    isContinue = Image.open("shimen_songxin.jpg")
    isContinue_hash = get_hash(isContinue)

    # 是否使用
    shiyong = Image.open("shiyong.jpg")
    shiyong_hash = get_hash(shiyong)
    # 开始
    while is_start:
        time.sleep(1)
        # 是否继续抓鬼/是否自动加入匹配
        img_isContinue = ImageGrab.grab((topx + get_posx(750, window_size), topy + get_posy(465, window_size),
                                         topx + get_posx(840, window_size), topy + get_posy(500, window_size)))

        if hamming(get_hash(img_isContinue), isContinue_hash, 10):
            move_click(topx + get_posx(740, window_size), topy + get_posy(380, window_size))
            time.sleep(3)
            continue

        # 使用按钮
        img_shiyong = ImageGrab.grab((topx + get_posx(635, window_size), topy + get_posy(510, window_size),
                                      topx + get_posx(710, window_size), topy + get_posy(540, window_size)))
        if hamming(get_hash(img_shiyong), shiyong_hash, 20):
            move_click(topx + get_posx(670, window_size), topy + get_posy(525, window_size))
            print("点击使用")
            time.sleep(3)
            continue


# 师门任务
def shimen(window_size):#todo
    global is_start
    is_start = True
    topx, topy = window_size[0], window_size[1]
    window_shift = [topx,topy,topx,topy]

    '''
    #1.找到师门任务
    click_renwu(window_size,"shimen")
    
    #2.点击马上传送
    move_click(topx+MashangchuansongArea[0]+10,topy+MashangchuansongArea[1]+10)

    #3.点击去完成(todo)
    time.sleep(10)
    

    #4.点击“师门任务”对话
    move_click(topx+ShimenrenwuPos[0],topy+ShimenrenwuPos[1])

    img_shimencijiao= Image.open(image_path+"shimencijiao.jpg")
    img_shimencijiao_hashed= get_hash(img_shimencijiao  )
    img_tmp = ImageGrab.grab(bbox=(topx + ShimencijiaoArea[0], topy + ShimencijiaoArea[1], topx + ShimencijiaoArea[2], topy + ShimencijiaoArea[3]))
    img_tmp_hashed=get_hash(img_tmp)
    if(hamming(img_shimencijiao_hashed,img_tmp_hashed)):
        move_click(topx+ShimencijiaoArea[0],topy+ShimencijiaoArea[1])
    '''

    #5.找到师门任务
    step = click_renwu(window_size, "shimen")

    #6.点击马上传送
    FirstRenwuArea_jueduiweizhi = [i + j for i, j in zip(window_shift, FirstRenwuArea)]
    img_shimen_an = Image.open(image_path +  "shimen_an.jpg")
    img_shimen_liang = Image.open(image_path +  "shimen_liang.jpg")
    img_shimen_an_hashed = get_hash(img_shimen_an)
    img_shimen_liang_hashed = get_hash(img_shimen_liang)
    x1, y1, x2, y2 = FirstRenwuArea_jueduiweizhi[0], FirstRenwuArea_jueduiweizhi[1] + step * RenwuStep, \
                     FirstRenwuArea_jueduiweizhi[2], FirstRenwuArea_jueduiweizhi[3] + step * RenwuStep
    img_tmp = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    img_tmp_hashed = get_hash(img_tmp)
    while hamming(img_shimen_an_hashed, img_tmp_hashed) or hamming(img_shimen_liang_hashed, img_tmp_hashed):
        move_click(topx + MashangchuansongArea[0] + 10, topy + MashangchuansongArea[1] + 10,1)
        move_click(topx+CloserenwuPos[0],topy+CloserenwuPos[1],10)
        move_click(topx + GoumaiPos[0] + 30, topy + GoumaiPos[1] + 30)
        for pos in ShimenduihuaPos:
            move_click(topx+pos[0],topy+pos[1])
        move_click(topx + SomePos[0] + 10, topy + SomePos[1] + 10,1)
        move_click(topx + SomePos[0] + 10, topy + SomePos[1] + 10,1)
        move_click(topx + SomePos[0] + 10, topy + SomePos[1] + 10,1)
        move_click(topx + SomePos[0] + 10, topy + SomePos[1] + 10,1)
        time.sleep(60)

        move_click(topx+CloserenwuPos[0],topy+CloserenwuPos[1])
        step = click_renwu(window_size, "shimen")
        img_tmp = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        img_tmp.show()
        img_tmp_hashed = get_hash(img_tmp)



    # 使用按钮（比如是x1,y1,x2,y2）
    shiyong = Image.open("shiyong_jpg")
    shiyong_hash = get_hash(shiyong)
    # shiyong.show()
    # print(shiyong_hash)
    # 购买宠物（比如是x1,y1,x2,y2）
    goumai_cw = Image.open("goumai_cw_jpg")
    goumai_cw_hash = get_hash(goumai_cw)
    # 上交药品按钮（比如是x1,y1,x2,y2）
    shangjiao_yp = Image.open("shangjiao_yp_jpg")
    shangjiao_yp_hash = get_hash(shangjiao_yp)
    # 上交宠物按钮
    shangjiao_cw = Image.open("shangjiao_cw_jpg")
    shangjiao_cw_hash = get_hash(shangjiao_cw)
    # 师门任务栏
    shimen = Image.open("shimen_jpg")
    shimen_hash = get_hash(shimen)

    # 师门任务栏
    shimen_songxin = Image.open("shimen_songxin_jpg")
    shimen_songxin_hash = get_hash(shimen_songxin)

    # 药店购买
    goumai_yp = Image.open("goumai_yp_jpg")
    goumai_yp_hash = get_hash(goumai_yp)
    # 商城购买
    goumai_sc = Image.open("goumai_sc_jpg")
    goumai_sc_hash = get_hash(goumai_sc)
    i = 0
    count = 0
    while is_start:
        time.sleep(2)
        i = i + 1
        print("第%i次循环" % i)
        # 使用按钮（635 ，510 ，710 ，540）
        img_shiyong = ImageGrab.grab((topx + get_posx(635, window_size), topy + get_posy(510, window_size),
                                      topx + get_posx(710, window_size), topy + get_posy(540, window_size)))
        # img_shiyong.show()
        # img_shiyong.save("shiyong.jpg")
        # print("显示图片")
        # print(get_hash(img_shiyong))
        # print(hamming(get_hash(img_shiyong), shiyong_hash, 20))
        if hamming(get_hash(img_shiyong), shiyong_hash, 30):
            move_click(topx + get_posx(670, window_size), topy + get_posy(525, window_size))
            print("点击使用")
            time.sleep(3)
            continue

        # 购买宠物610，505，740，540
        img_goumai_cw = ImageGrab.grab((topx + get_posx(610, window_size), topy + get_posy(505, window_size),
                                        topx + get_posx(740, window_size), topy + get_posy(540, window_size)))
        # img_goumai_cw.save("goumai_cw.jpg")
        if hamming(get_hash(img_goumai_cw), goumai_cw_hash, 20):
            move_click(topx + get_posx(680, window_size), topy + get_posy(520, window_size))
            print("点击购买宠物")
            time.sleep(3)
            continue

        # 药店购买 570，470，700，505
        img_goumai_yp = ImageGrab.grab((topx + get_posx(560, window_size), topy + get_posy(460, window_size),
                                        topx + get_posx(690, window_size), topy + get_posy(500, window_size)))
        # img_goumai_yp.save("goumai_yp.jpg")
        if hamming(get_hash(img_goumai_yp), goumai_yp_hash, 20):
            move_click(topx + get_posx(620, window_size), topy + get_posy(480, window_size))
            print("点击购买药")
            time.sleep(3)
            continue

        # 商城购买 520，520，715，550
        img_goumai_sc = ImageGrab.grab((topx + get_posx(580, window_size), topy + get_posy(515, window_size),
                                        topx + get_posx(715, window_size), topy + get_posy(550, window_size)))
        # img_goumai_sc.save("goumai_sc.jpg")
        if hamming(get_hash(img_goumai_sc), goumai_sc_hash, 20):
            move_click(topx + get_posx(650, window_size), topy + get_posy(530, window_size))
            print("点击商城购买")
            time.sleep(3)
            continue

        # 上交药品按钮 600，470，700，500
        img_shangjiao_yp = ImageGrab.grab((topx + get_posx(590, window_size), topy + get_posy(465, window_size),
                                           topx + get_posx(695, window_size), topy + get_posy(490, window_size)))
        # img_shangjiao_yp .save("shangjiao_yp.jpg")
        if hamming(get_hash(img_shangjiao_yp), shangjiao_yp_hash, 20):
            move_click(topx + get_posx(640, window_size), topy + get_posy(478, window_size))
            print("点击药品上交")
            time.sleep(3)
            continue

        # 上交宠物按钮
        img_shangjiao_cw = ImageGrab.grab((topx + get_posx(500, window_size), topy + get_posy(460, window_size),
                                           topx + get_posx(600, window_size), topy + get_posy(500, window_size)))
        # img_shangjiao_cw.save("shangjiao_cw.jpg")
        if hamming(get_hash(img_shangjiao_cw), shangjiao_cw_hash, 20):
            move_click(topx + get_posx(550, window_size), topy + get_posy(480, window_size))
            print("点击宠物上交")
            time.sleep(3)
            continue

        # 师门送信按钮
        img_shimen_songxin1 = ImageGrab.grab((topx + get_posx(620, window_size), topy + get_posy(290, window_size),
                                              topx + get_posx(700, window_size), topy + get_posy(325, window_size)))
        # img_shimen_songxin1 .save("shimen_songxin1.jpg")
        # img_shimen_songxin1.show()
        if hamming(get_hash(img_shimen_songxin1), shimen_songxin_hash, 30):
            move_click(topx + get_posx(660, window_size), topy + get_posy(310, window_size))
            print("点击师门任务1")
            time.sleep(3)
            continue

        # 师门任务按钮
        img_shimen_songxin = ImageGrab.grab((topx + get_posx(620, window_size), topy + get_posy(345, window_size),
                                             topx + get_posx(700, window_size), topy + get_posy(370, window_size)))
        # img_shimen_songxin .save("shimen_songxin1.jpg")

        if hamming(get_hash(img_shimen_songxin), shimen_songxin_hash, 30):
            move_click(topx + get_posx(660, window_size), topy + get_posy(360, window_size))
            print("点击师门任务")
            time.sleep(3)
            continue

        # # 师门任务栏 630，150，665，175
        img_shimen = ImageGrab.grab((topx + get_posx(630, window_size), topy + get_posy(160, window_size),
                                     topx + get_posx(670, window_size), topy + get_posy(180, window_size)))
        # img_shimen.save("shimen.jpg")
        if hamming(get_hash(img_shimen), shimen_hash, 50):
            move_click(topx + get_posx(650, window_size), topy + get_posy(170, window_size))
            print("点击师门任务栏")
            time.sleep(3)
            continue

        # 结束师门任务
        # img_finish = ImageGrab.grab((topx + get_posx(630, window_size), topy + get_posy(160, window_size),
        #                              topx + get_posx(670, window_size), topy + get_posy(180, window_size)))
        # # img_finish.save("finish.jpg")
        # if hamming(get_hash(img_finish), finish_hash, 20):
        #     move_click(topx + get_posx(650, window_size), topy + get_posy(170, window_size))
        #     print("师门任务完成")
        #     break


# 帮派任务
def bang_pai(window_size):
    global is_start
    is_start = True
    topx, topy = window_size[0], window_size[1]
    # 使用按钮（比如是x1,y1,x2,y2）
    shiyong = Image.open("shiyong_jpg")
    shiyong_hash = get_hash(shiyong)
    # shiyong.show()
    # print(shiyong_hash)
    # 购买宠物（比如是x1,y1,x2,y2）
    goumai_cw = Image.open("goumai_cw_jpg")
    goumai_cw_hash = get_hash(goumai_cw)
    # 上交药品按钮（比如是x1,y1,x2,y2）
    shangjiao_yp = Image.open("shangjiao_yp_jpg")
    shangjiao_yp_hash = get_hash(shangjiao_yp)
    # 上交宠物按钮
    shangjiao_cw = Image.open("shangjiao_cw_jpg")
    shangjiao_cw_hash = get_hash(shangjiao_cw)
    # 帮派任务栏
    bangpai = Image.open("bangpai_jpg")
    bangpai_hash = get_hash(bangpai)

    # 门派切磋
    qiecuo = Image.open("qiecuo_jpg")
    qiecuo_hash = get_hash(qiecuo)
    # 御林军切磋
    qiecuo_yulin = Image.open("qiecuo_yulin_jpg")
    qiecuo_yulin_hash = get_hash(qiecuo_yulin)

    # 帮派任务按钮
    bangpai_renwu = Image.open("bangpai_renwu_jpg")
    bangpai_renwu_hash = get_hash(bangpai_renwu)

    # 帮派任务按钮2
    bangpai_renwu2 = Image.open("bangpai_renwu2_jpg")
    bangpai_renwu2_hash = get_hash(bangpai_renwu2)

    # 药店购买
    goumai_yp = Image.open("goumai_yp_jpg")
    goumai_yp_hash = get_hash(goumai_yp)
    # 商城购买
    goumai_sc = Image.open("goumai_sc_jpg")
    goumai_sc_hash = get_hash(goumai_sc)
    i = 0
    count = 0
    while is_start:
        time.sleep(2)
        i = i + 1
        print("第%i次循环" % i)
        # 使用按钮（635 ，510 ，710 ，540）
        img_shiyong = ImageGrab.grab((topx + get_posx(635, window_size), topy + get_posy(510, window_size),
                                      topx + get_posx(710, window_size), topy + get_posy(540, window_size)))
        # img_shiyong.show()
        #  img_shiyong.save("shiyong.jpg")

        if hamming(get_hash(img_shiyong), shiyong_hash, 20):
            move_click(topx + get_posx(670, window_size), topy + get_posy(525, window_size))
            print("点击使用")
            time.sleep(3)
            continue

        img_qiecuo_yulin = ImageGrab.grab((topx + get_posx(620, window_size), topy + get_posy(200, window_size),
                                           topx + get_posx(710, window_size), topy + get_posy(230, window_size)))
        # img_shiyong.show()
        # img_qiecuo_yulin.save("qiecuo_yulin.jpg")
        # break
        if hamming(get_hash(img_qiecuo_yulin), qiecuo_yulin_hash, 20):
            move_click(topx + get_posx(670, window_size), topy + get_posy(215, window_size))
            print("点击切磋")
            time.sleep(3)
            continue

        # 购买宠物610，505，740，540
        img_goumai_cw = ImageGrab.grab((topx + get_posx(610, window_size), topy + get_posy(505, window_size),
                                        topx + get_posx(740, window_size), topy + get_posy(540, window_size)))
        # img_goumai_cw.save("goumai_cw.jpg")
        if hamming(get_hash(img_goumai_cw), goumai_cw_hash, 20):
            move_click(topx + get_posx(680, window_size), topy + get_posy(520, window_size))
            print("点击购买宠物")
            time.sleep(3)
            continue

        # 药店购买 570，470，700，505
        img_goumai_yp = ImageGrab.grab((topx + get_posx(560, window_size), topy + get_posy(460, window_size),
                                        topx + get_posx(690, window_size), topy + get_posy(500, window_size)))
        # img_goumai_yp.save("goumai_yp.jpg")
        if hamming(get_hash(img_goumai_yp), goumai_yp_hash, 20):
            move_click(topx + get_posx(620, window_size), topy + get_posy(480, window_size))
            print("点击购买药")
            time.sleep(3)
            continue

        # 商城购买 520，520，715，550
        img_goumai_sc = ImageGrab.grab((topx + get_posx(580, window_size), topy + get_posy(515, window_size),
                                        topx + get_posx(715, window_size), topy + get_posy(550, window_size)))
        # img_goumai_sc.save("goumai_sc.jpg")
        if hamming(get_hash(img_goumai_sc), goumai_sc_hash, 20):
            move_click(topx + get_posx(650, window_size), topy + get_posy(530, window_size))
            print("点击商城购买")
            time.sleep(3)
            continue

        # 上交药品按钮 600，470，700，500
        img_shangjiao_yp = ImageGrab.grab((topx + get_posx(590, window_size), topy + get_posy(465, window_size),
                                           topx + get_posx(695, window_size), topy + get_posy(490, window_size)))
        # img_shangjiao_yp .save("shangjiao_yp.jpg")
        if hamming(get_hash(img_shangjiao_yp), shangjiao_yp_hash, 20):
            move_click(topx + get_posx(640, window_size), topy + get_posy(478, window_size))
            print("点击药品上交")
            time.sleep(3)
            continue

        # 上交宠物按钮
        # img_shangjiao_cw = ImageGrab.grab((topx + get_posx(500, window_size), topy + get_posy(460, window_size),
        #                                    topx + get_posx(600, window_size), topy + get_posy(500, window_size)))
        # # img_shangjiao_cw.save("shangjiao_cw.jpg")
        # if hamming(get_hash(img_shangjiao_cw), shangjiao_cw_hash, 20):
        #     move_click(topx + get_posx(550, window_size), topy + get_posy(480, window_size))
        #     print("点击宠物上交")
        #     time.sleep(5)
        #     continue

        # 帮派任务按钮
        img_bangpai_renwu = ImageGrab.grab((topx + get_posx(620, window_size), topy + get_posy(300, window_size),
                                            topx + get_posx(700, window_size), topy + get_posy(330, window_size)))
        # img_bangpai_renwu .save("bangpai_renwu.jpg")
        if hamming(get_hash(img_bangpai_renwu), bangpai_renwu_hash, 20):
            move_click(topx + get_posx(660, window_size), topy + get_posy(315, window_size))
            print("点击帮派任务提交按钮")
            time.sleep(3)
            continue

        # 帮派任务按钮2
        img_bangpai_renwu2 = ImageGrab.grab((topx + get_posx(620, window_size), topy + get_posy(250, window_size),
                                             topx + get_posx(700, window_size), topy + get_posy(280, window_size)))
        # img_bangpai_renwu2 .save("bangpai_renwu2.jpg")
        if hamming(get_hash(img_bangpai_renwu2), bangpai_renwu2_hash, 20):
            move_click(topx + get_posx(660, window_size), topy + get_posy(265, window_size))
            print("点击帮派任务提交按钮2")
            time.sleep(3)
            continue

        # #切磋
        img_qiecuo = ImageGrab.grab((topx + get_posx(625, window_size), topy + get_posy(431, window_size),
                                     topx + get_posx(710, window_size), topy + get_posy(468, window_size)))
        # img_shiyong.show()
        # img_qiecuo.save("qiecuo.jpg")
        if hamming(get_hash(img_qiecuo), qiecuo_hash, 20):
            move_click(topx + get_posx(670, window_size), topy + get_posy(450, window_size))
            print("点击切磋")
            time.sleep(3)
            continue

        # # # 帮派任务栏
        img_bangpai = ImageGrab.grab((topx + get_posx(630, window_size), topy + get_posy(160, window_size),
                                      topx + get_posx(670, window_size), topy + get_posy(180, window_size)))
        # img_bangpai.save("bangpai.jpg")
        if hamming(get_hash(img_bangpai), bangpai_hash, 40):
            move_click(topx + get_posx(650, window_size), topy + get_posy(170, window_size))
            print("点击帮派任务栏")
            time.sleep(3)
            continue
        # break
    # print("帮派任务停止...")


def my_bang_pai(window_size):
    topx,topy=window_size[0],window_size[1]

    global is_start
    is_start =True

    #some pos
    BangpairenwuduihuaPos1=[850,510]#"帮派任务":首席弟子切磋,上交任务
    BangpairenwuduihuaPos2=[750,270]#"帮派任务":1.御林军
    ShangjiaoPos = [830,610]

    #some area
    # RenwuName4Area=[352,204,509,228]
    RenwuNameArea=[352,204,460,228]
    ShouxiArea=[750,500,950,530]
    YunleyouArea=[780,317,933,352]
    YuanshouchengArea = [790,260,920,290]
    ZhengbiaotouArea = [775,436,930,470]
    BaixiaoxianziArea=[790,380,915,411]
    BangzhuArea = [780,560,914,589]
    CloserenwuArea = [916,124,948,153]
    CloseyaodianArea = [950,124,985,153]

    #some images

    img_closerenwu= Image.open(image_path+"closerenwu.jpg")#关闭任务区域
    img_closerenwu_hashed= get_hash(img_closerenwu)

    img_closeyaodian= Image.open(image_path+"closeyaodian.jpg")#关闭药店区域
    img_closeyaodian_hashed= get_hash(img_closeyaodian)

    img_jiayuanxunluo = Image.open(image_path+"jiayuanxunluo.jpg")#玄武-家园巡逻
    img_jiayuanxunluo_hashed = get_hash(img_jiayuanxunluo)

    img_zhanbei= Image.open(image_path+"zhanbei.jpg")#玄武-战备
    img_zhanbei_hashed= get_hash(img_zhanbei)

    img_chumo= Image.open(image_path+"chumo.jpg")#玄武-除魔
    img_chumo_hashed= get_hash(img_chumo)

    img_bangpaixunluo= Image.open(image_path+"bangpaixunluo.jpg")#玄武-帮派巡逻
    img_bangpaixunluo_hashed= get_hash(img_bangpaixunluo)

    img_xuandugonggao= Image.open(image_path+"xuandugonggao.jpg")#朱雀-宣读公告
    img_xuandugonggao_hashed= get_hash(img_xuandugonggao)

    img_liangcao= Image.open(image_path+"liangcao.jpg")#朱雀-粮草
    img_liangcao_hashed= get_hash(img_liangcao)

    img_qiecuo= Image.open(image_path+"qiecuo.jpg")#朱雀-切磋
    img_qiecuo_hashed= get_hash(img_qiecuo)

    img_tiaozhan= Image.open(image_path+"tiaozhan.jpg")#朱雀-挑战帮主
    img_tiaozhan_hashed= get_hash(img_tiaozhan)

    img_baifang= Image.open(image_path+"baifang.jpg")#青龙-拜访
    img_baifang_hashed= get_hash(img_baifang)

    img_yaocai =Image.open(image_path+"yaocai.jpg")#青龙-药材
    img_yaocai_hashed = get_hash(img_yaocai)

    img_wuzi=Image.open(image_path+"wuzi.jpg")#青龙-物资
    img_wuzi_hashed = get_hash(img_wuzi)

    #切磋对话框
    img_shouxi = Image.open(image_path + "shouxi.jpg")  # 切磋首席弟子
    img_shouxi_hashed = get_hash(img_shouxi)

    #拜访对话框
    img_yunleyou= Image.open(image_path + "baifang_yunleyou.jpg")  # 拜访云乐游
    img_yunleyou_hashed = get_hash(img_yunleyou)

    img_yuanshoucheng= Image.open(image_path + "baifang_yuanshoucheng.jpg")  #拜访袁守诚
    img_yuanshoucheng_hashed= get_hash(img_yuanshoucheng)

    img_zhengbiaotou= Image.open(image_path + "baifang_zhengbiaotou.jpg")  #拜访袁守诚
    img_zhengbiaotou_hashed= get_hash(img_zhengbiaotou)

    img_baixiaoxianzi= Image.open(image_path + "baifang_baixiaoxianzi.jpg")  #拜访袁守诚
    img_baixiaoxianzi_hashed= get_hash(img_baixiaoxianzi)

    img_tiaozhanbangzhu= Image.open(image_path + "tiaozhanbangzhu.jpg")  #拜访袁守诚
    img_tiaozhanbangzhu_hashed= get_hash(img_tiaozhanbangzhu)

    # img_tmp = ImageGrab.grab(bbox=(topx+FirstRenwuArea[0],topy+FirstRenwuArea[1]+RenwuStep,topx+FirstRenwuArea[2],topy+FirstRenwuArea[3]+RenwuStep))
    # img_tmp.show()
    # img_tmp.save("test.jpg")


#some func
    def reset():
        img_tmp = ImageGrab.grab(
            bbox=(topx + CloserenwuArea[0], topy + CloserenwuArea[1], topx + CloserenwuArea[2], topy + CloserenwuArea[3]))
        img_tmp_hashed = get_hash(img_tmp)
        if (hamming(img_tmp_hashed, img_closerenwu_hashed)):
            move_click(topx + CloserenwuPos[0], topy + CloserenwuPos[1])
            return

        img_tmp = ImageGrab.grab(
            bbox=(topx + CloseyaodianArea[0], topy + CloseyaodianArea[1], topx + CloseyaodianArea[2], topy + CloseyaodianArea[3]))
        img_tmp_hashed = get_hash(img_tmp)
        if (hamming(img_tmp_hashed, img_closeyaodian_hashed)):
            move_click(topx + CloseyaodianArea[0], topy + CloseyaodianArea[1])
            return


    def goumai(pos=GoumaiPos):
        move_click(topx + MashangchuansongArea[0], topy + MashangchuansongArea[1], 15)
        move_click(topx + pos[0], topy + pos[1], 5)
        move_click(topx + CloserenwuPos[0], topy + CloserenwuPos[1])
        move_click(topx + BangpairenwuduihuaPos1[0], topy + BangpairenwuduihuaPos1[1])
        move_click(topx + ShangjiaoPos[0], topy + ShangjiaoPos[1])
    def xunluo():
        move_click(topx + MashangchuansongArea[0], topy + MashangchuansongArea[1], 60)
        move_click(topx + CloserenwuPos[0], topy + CloserenwuPos[1])
    def is_this_type(topx,topy,area,img_target_hashed):
        img_tmp = ImageGrab.grab(bbox=(topx+area[0],topy+area[1],topx+area[2],topy+area[3]))
        # img_tmp.show()
        # img_tmp.save(image_path+"tiaozhanbangzhu.jpg")
        img_tmp_hashed = get_hash(img_tmp)
        if(hamming(img_tmp_hashed,img_target_hashed)):
            return True
        else:
            return False

    def duihua():
        move_click(topx + MashangchuansongArea[0], topy + MashangchuansongArea[1], 20)
        move_click(topx + CloserenwuPos[0], topy + CloserenwuPos[1])

        if(is_this_type(topx,topy,ShouxiArea,img_shouxi_hashed)):#首席切磋
            move_click(topx+ShouxiArea[0],topy+ShouxiArea[1],60)
        elif(is_this_type(topx, topy, YunleyouArea, img_yunleyou_hashed)):  # 拜访云乐游
            move_click(topx + YunleyouArea[0], topy + YunleyouArea[1])
        elif(is_this_type(topx, topy, YuanshouchengArea,img_yuanshoucheng_hashed)):  # 拜访袁守诚
            move_click(topx + YuanshouchengArea[0], topy + YuanshouchengArea[1])
        elif(is_this_type(topx, topy, ZhengbiaotouArea,img_zhengbiaotou_hashed)):  # 拜访郑镖头
            move_click(topx + ZhengbiaotouArea[0], topy + ZhengbiaotouArea[1])
        elif(is_this_type(topx, topy, BaixiaoxianziArea,img_baixiaoxianzi_hashed)):  # 拜访百晓仙子
            move_click(topx + BaixiaoxianziArea[0], topy + BaixiaoxianziArea[1])
        elif(is_this_type(topx, topy, BangzhuArea,img_tiaozhanbangzhu_hashed)):  # 挑战帮主
            move_click(topx + BangzhuArea[0], topy + BangzhuArea[1],60)
        # else:#挑战帮主
        #     move_click(topx+800,topy+570,45)

    miss_hit = 0
    while miss_hit<60 and is_start:

        reset()

        click_renwu(window_size,"bangpai")

        img_renwu = ImageGrab.grab( bbox=(topx + RenwuNameArea[0], topy + RenwuNameArea[1], topx + RenwuNameArea[2], topy + RenwuNameArea[3]))
        # img_renwu.show()
        # img_renwu.save(image_path+"wuzi.jpg")
        img_renwu_hashed = get_hash(img_renwu)

        if(hamming(img_renwu_hashed,img_zhanbei_hashed)):#玄武-战备
            goumai(GoumaiPos)
        elif hamming(img_renwu_hashed,img_chumo_hashed):#玄武-除魔
            xunluo()
        elif hamming(img_renwu_hashed,img_bangpaixunluo_hashed):#玄武-帮派巡逻
            xunluo()
        elif hamming(img_renwu_hashed,img_jiayuanxunluo_hashed):#玄武-家园巡逻
            xunluo()
        elif hamming(img_renwu_hashed,img_xuandugonggao_hashed):#朱雀-宣读公告
            move_click(topx+MashangchuansongArea[0],topy+MashangchuansongArea[1],15)
            move_click(topx+CloserenwuPos[0],topy+CloserenwuPos[1])
            move_click(topx+CangbaotushiyongArea[0],topy+CangbaotushiyongArea[1],4)
            click_renwu(window_size,"bangpai")
        elif hamming(img_renwu_hashed,img_liangcao_hashed):#朱雀-粮草
            goumai(GoumaiPos)
        elif hamming(img_renwu_hashed,img_qiecuo_hashed):#朱雀-切磋
            duihua()
        elif hamming(img_renwu_hashed,img_tiaozhan_hashed):#朱雀-挑战
            duihua()
        elif hamming(img_renwu_hashed,img_baifang_hashed):#青龙-拜访
            duihua()
        elif hamming(img_renwu_hashed,img_yaocai_hashed):#青龙-药材
            goumai(YaodiangoumaiPos)
        elif hamming(img_renwu_hashed,img_wuzi_hashed):#青龙-物资
            goumai()
        else:
            miss_hit+=1
            time.sleep(10)



    a = 1;








# 挖宝图
'''
1.点开地图
2.找到店小二
3.点开任务栏（todo）
4.点击宝图任务
5.自动挖图（todo）

Positions：
地图：

'''


def baotu(window_size):
    global is_start
    is_start = True
    topx, topy = window_size[0], window_size[1]
    window_shift=[topx,topy,topx,topy]

    # 1.点开地图
    move_click(topx + XiaodituPos[0], topy + XiaodituPos[1])

    # 2.找到店小二
    move_click(topx + DianxiaoerPos[0], topy + DianxiaoerPos[1])
    time.sleep(10)
    move_click(topx + 850, topy + 570)#ting ting wu fang pos

    # 3.点开任务栏
    move_click(topx + RenwuArea[0], topy + RenwuArea[1])

    # 4.展开任务栏
    img_tmp=ImageGrab.grab(i+j for i,j in zip(window_shift,ChangguirenwuArea))
    img_tmp_hashed=get_hash(img_tmp)
    if(hamming(get_hash(Image.open(image_path+"renwuweizhankai_an.jpg")),img_tmp_hashed) or
            hamming(get_hash(Image.open(image_path+"renwuweizhankai_liang.jpg")),img_tmp_hashed)):
        move_click(topx + ChangguirenwuArea[0], topy + ChangguirenwuArea[1])

    # 5.选中宝图任务
    location = 0
    FirstRenwuArea_jueduiweizhi = [i+j for i,j in zip(window_shift,FirstRenwuArea)]
    img_baotu_an = Image.open(image_path+"baotu_an.jpg")
    img_baotu_liang= Image.open(image_path+"baotu_liang.jpg")
    img_baotu_an_hashed=get_hash(img_baotu_an)
    img_baotu_liang_hashed=get_hash(img_baotu_liang)
    for i in range(3):
        x1,y1,x2,y2=FirstRenwuArea_jueduiweizhi[0],FirstRenwuArea_jueduiweizhi[1]+i*RenwuStep,FirstRenwuArea_jueduiweizhi[2],FirstRenwuArea_jueduiweizhi[3]+i*RenwuStep
        img_tmp = ImageGrab.grab(bbox=(x1,y1,x2,y2))
        # img_tmp.show()
        img_tmp_hashed=get_hash(img_tmp)

        if(hamming(img_baotu_an_hashed,img_tmp_hashed) or hamming(img_baotu_liang_hashed,img_tmp_hashed)):
            location=i
            move_click(x1,y1)
            break

    # 6.点击马上传送
    move_click(topx+MashangchuansongArea[0]+10,topy+MashangchuansongArea[1]+10)

    x1, y1, x2, y2 = FirstRenwuArea_jueduiweizhi[0], FirstRenwuArea_jueduiweizhi[1] + location * RenwuStep, \
                     FirstRenwuArea_jueduiweizhi[2], FirstRenwuArea_jueduiweizhi[3] + location * RenwuStep
    img_tmp = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    img_tmp_hashed=get_hash(img_tmp)
    while(hamming(img_baotu_an_hashed,img_tmp_hashed) or hamming(img_baotu_liang_hashed,img_tmp_hashed)):
        time.sleep(10)
        img_tmp = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        img_tmp_hashed=get_hash(img_tmp)

    # 7.关闭任务界面，打开背包，寻找藏宝图位置
    move_click(topx+CloserenwuPos[0],topy+CloserenwuPos[1])
    move_click(topx+BeibaoPos[0],topy+BeibaoPos[1])
    move_click(topx+ZhengliPos[0],topy+ZhengliPos[1])

    img_cangbaotu = Image.open(image_path+"cangbaotu.jpg")
    img_cangbaotu_hashed=get_hash(img_cangbaotu)
    cangbaotuPos_first = [i+j for i,j in zip(window_shift,[527,241,589,303])]

    for i in range(5):
        x1,y1,x2,y2=cangbaotuPos_first[0],cangbaotuPos_first[1]+BeibaoStep*i,cangbaotuPos_first[2],cangbaotuPos_first[3]+BeibaoStep*i
        img_tmp = ImageGrab.grab(bbox=(x1,y1,x2,y2))
        # img_tmp.show()
        # img_tmp.save("testImg"+str(i)+".jpg")
        img_tmp_hashed = get_hash(img_tmp)
        if(hamming(img_cangbaotu_hashed,img_tmp_hashed)):
            move_click(int((x1+x2)/2),int((y1+y2)/2))
            break
    #使用藏宝图
    move_click(topx+400,topy+500)
    img_shiyongcangbaotu = Image.open(image_path+"shiyongcangbaotu.jpg")
    img_shiyongcangbaotu_hashed = get_hash(img_shiyongcangbaotu)
    wait_count = 0
    while wait_count<10:
        img_tmp = ImageGrab.grab(bbox=(topx+CangbaotushiyongArea[0],topy+CangbaotushiyongArea[1],topx+CangbaotushiyongArea[2],topy+CangbaotushiyongArea[3]))
        img_tmp_hashed = get_hash(img_tmp)
        if(hamming(img_tmp_hashed,img_shiyongcangbaotu_hashed)):
            move_click(topx+CangbaotushiyongArea[0],topy+CangbaotushiyongArea[1])
            wait_count=0
        else:
            time.sleep(10)



def stop():
    global is_start
    is_start = False
    print("停止")

def grab_images(window_size):
    global is_start
    is_start = True
    topx, topy = window_size[0], window_size[1]
    window_shift=[topx,topy,topx,topy]

    #0.test
    # img_test = ImageGrab.grab(bbox=(window_size[0],window_size[1],window_size[2],window_size[3]))
    # img_test.show()

    #1.截取任务栏
    img_renwuArea = ImageGrab.grab(bbox=(topx + RenwuArea[0], topy + RenwuArea[1], topx + RenwuArea[2], topy + RenwuArea[3]))
    # img_renwuArea.show()
    img_renwuArea.save("test_images/renwuArea.jpg")

    #2.截取活动栏
    img_huodongArea= ImageGrab.grab(bbox=(topx + HuodongArea[0], topy + HuodongArea[1], topx + HuodongArea[2], topy + HuodongArea[3]))
    # img_huodongArea.show()
    img_huodongArea.save("test_images/huodongArea.jpg")

    #3.截取常规任务栏
    img_changguirenwu= ImageGrab.grab(bbox=(topx + ChangguirenwuArea[0], topy + ChangguirenwuArea[1], topx + ChangguirenwuArea[2], topy + ChangguirenwuArea[3]))
    # img_changguirenwu.show()
    img_changguirenwu.save("test_images/cgrw.jpg")

    #4.截取多项任务栏
    for i in range(5):
        time.sleep(3)
        img_renwu= ImageGrab.grab(bbox=(topx + FirstRenwuArea[0], topy + FirstRenwuArea[1]+RenwuStep*i, topx + FirstRenwuArea[2], topy + FirstRenwuArea[3]+RenwuStep*i))
        # img_renwu.show()
        image_name="test_images/renwu"+str(i)+".jpg"
        img_renwu.save(image_name)

    #5.截取马上传送栏
    img_mashangchuansong= ImageGrab.grab(bbox=(topx + MashangchuansongArea[0], topy + MashangchuansongArea[1], topx + MashangchuansongArea[2], topy + MashangchuansongArea[3]))
    # img_mashangchuansong.show()
    img_mashangchuansong.save("test_images/mscs.jpg")

    #6.截取藏宝图图片
    img_cangbaotu = ImageGrab.grab((i+j for i,j in zip(window_shift,[769,322,831,383])))
    img_cangbaotu.show()
    img_cangbaotu.save("test_images/cangbaotu.jpg")

    return 0


class MyThread(threading.Thread):
    def __init__(self, func, *args):
        super().__init__()

        self.func = func
        self.args = args

        self.setDaemon(True)
        self.start()  # 在这里开始

    def run(self):
        self.func(*self.args)


# 启动
if __name__ == "__main__":
    screen_resolution = resolution()
    # print(screen_resolution)
    window_size = get_window_info()  # width:834 height:652
    print(window_size)
    global is_start
    global is_stop
    # shimen(window_size)
    # zhua_gui(window_size)
    # bang_pai(window_size)
    # baotu(window_size)

    # 创建主窗口
    root = tk.Tk()
    root.title("梦幻西游手游辅助")
    root.minsize(300, 300)
    root.maxsize(300, 300)
    # 创建按钮
    button_shimen = tk.Button(root, text=u"师门", command=lambda: MyThread(shimen, window_size), width=15, height=2)
    button_shimen.place(relx=0.2, rely=0.15, width=200)
    button_shimen.pack()

    button_bangpai = tk.Button(root, text="帮派", command=lambda: MyThread(my_bang_pai, window_size), width=15, height=2)
    button_bangpai.place(relx=0.2, rely=0.35, width=200)
    button_bangpai.pack()

    button_baotu = tk.Button(root, text="宝图", command=lambda: MyThread(baotu, window_size), width=15, height=2)
    button_baotu.place(relx=0.4, rely=0.55, width=200)
    button_baotu.pack()

    button_zhuagui = tk.Button(root, text="带队抓鬼", command=lambda: MyThread(zhua_gui, window_size), width=15, height=2)
    button_zhuagui.place(relx=0.4, rely=0.65, width=100)
    button_zhuagui.pack()

    button_tingzhi = tk.Button(root, text=u"停止", command=lambda: MyThread(stop), width=15, height=2)
    button_tingzhi.place(relx=0.4, rely=0.85, width=200)
    button_tingzhi.pack()

    button_test = tk.Button(root, text=u"测试", command=lambda: MyThread(grab_images,window_size), width=15, height=2)
    button_test.place(relx=0.4, rely=0.9, width=200)
    button_test.pack()

    root.mainloop()

