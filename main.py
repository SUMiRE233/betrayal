import pygame
from core.performs import Start_interface, Downstairs_interface, Ground_interface, Upstairs_interface

def main():
    # 初始化游戏
    pygame.init()
    initialize_game()

    # 显示开始界面并获取用户选择
    start_interface = Start_interface()
    start_interface.run()

    # 游戏主循环
    game_loop()

    # 退出游戏
    pygame.quit()


def initialize_game():
    global currentplayerlist, deathlist, levelnow, playernow, levellist
    currentplayerlist = [0, 1, 2, 3]
    deathlist = []
    levelnow = 1
    playernow = 0
    levellist = []
    downstairs_interface = Downstairs_interface()
    levellist.append(downstairs_interface)
    ground_interface = Ground_interface()
    levellist.append(ground_interface)
    upstairs_interface = Upstairs_interface()
    levellist.append(upstairs_interface)


def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 在这里可以添加更多的事件处理逻辑，如按键按下、鼠标点击等
            # 根据不同的事件调用相应的业务逻辑层函数
        # 在这里可以添加游戏状态更新逻辑，如角色行动、事件触发等
        pygame.display.update()


if __name__ == "__main__":
    main()