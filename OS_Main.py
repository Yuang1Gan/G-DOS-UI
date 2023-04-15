import pgzrun, easygui, datetime, OS_information
import image
#窗口高度
WIDTH = 1700
HEIGHT = 860
now = 0  #系统状态
name = 'bilibili2023拜年纪1'  #标准背景
#图标定义
IMVI = Actor('imvi')
c = Actor('change')
off = Actor('关机')
ifor = Actor('系统信息')
#图标位置
c.y = 200
off.x = 900
off.y = 835
ifor.y = 300
#绘制
def draw():
    global now, name
    if now == 0:
        easygui.msgbox("加载完成，即将进入系统，\nCopyright：Tony Gan Studio", 'G-DOS-UI')
        now = 1
    elif now == 1:
        screen.clear()
        screen.blit(name, pos=(0, 0))
        IMVI.draw()
        c.draw()
        a = datetime.datetime.now()
        screen.draw.text(a.strftime('%Y-%m-%d %A %B %H:%M:%S'), (1422, 833), fontsize = 25)
        off.draw()
        ifor.draw()
def update():
    pass

#背景切换程序
def change():
    choice = easygui.choicebox("请选择壁纸", "壁纸切换工具", ["bilibili2023拜年纪1", "bilibili2023拜年纪2", "草神1"])
    return choice
#鼠标事件
def on_mouse_down(pos, button):
    global now, name
    if IMVI.collidepoint(pos) and button == mouse.LEFT and now == 1:
        image.open_image()
    if c.collidepoint(pos) and button == mouse.LEFT and now == 1:
        name = change()
    if off.collidepoint(pos) and button == mouse.LEFT and now == 1:
        easygui.msgbox('G-DOS-UI正在关闭', 'G-DOS-UI')
        exit()
    if ifor.collidepoint(pos) and button == mouse.LEFT and now == 1:
        OS_information.window()

pgzrun.go()

