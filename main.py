import pygame
from core.performs import Start_interface
from config.config import levellist

def main():
    # 初始化游戏
    pygame.init()

    # 显示开始界面并获取用户选择
    start_interface = Start_interface()
    start_interface.run()

    # 游戏主循环
    game_loop()

    # 退出游戏
    pygame.quit()



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