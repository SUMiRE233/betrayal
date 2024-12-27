import pygame
import random
import tkinter as tk
class Color:
    ORANGE = (220, 160, 87)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)
    PURPLE = (102, 0,153)
    TRANSPARENT = (255, 255, 255, 0)
    LIGHTBLUE=(173, 216, 230)
    YELLOW=(255,255,0)
color=Color()
class Text:
    def __init__(self, text: str, text_color: Color, font_type: str, font_size: int):
        """
        text: 文本内容，如'大学生模拟器'，注意是字符串形式
        text_color: 字体颜色，如Color.WHITE、COLOR.BLACK
        font_type: 字体文件(.ttc)，如'msyh.ttc'，注意是字符串形式
        font_size: 字体大小，如20、10
        """
        self.text = text
        self.text_color = text_color
        self.font_type = font_type
        self.font_size = font_size
 
        font = pygame.font.Font(font_type, self.font_size)
        self.text_image = font.render(self.text, True, self.text_color).convert_alpha()
 
        self.text_width = self.text_image.get_width()
        self.text_height = self.text_image.get_height()
 
    def draw(self, surface: pygame.Surface, center_x, center_y):
        """
        surface: 文本放置的表面
        center_x, center_y: 文本放置在表面的<中心坐标>
        """
        upperleft_x = center_x - self.text_width / 2
        upperleft_y = center_y - self.text_height / 2
        surface.blit(self.text_image, (upperleft_x, upperleft_y))
class Image:
    def __init__(self, img_name: str, ratio=0.4):
        """
        img_name: 图片文件名，如'background.jpg'、'ink.png',注意为字符串
        ratio: 图片缩放比例，与主屏幕相适应，默认值为0.4
        """
        self.img_name = img_name
        self.ratio = ratio
 
        self.picture = pygame.image.load(img_name)
        self.img_width = self.picture.get_width()
        self.img_height = self.picture.get_height()
 
        self.size_scaled = self.img_width * self.ratio, self.img_height * self.ratio
 
        self.image_scaled = pygame.transform.smoothscale(self.picture, self.size_scaled)
        self.img_width_scaled = self.image_scaled.get_width()
        self.img_height_scaled = self.image_scaled.get_height()
        self.rect = self.image_scaled.get_rect()
    def draw(self, surface: pygame.Surface, center_x, center_y):
        """
        surface: 图片放置的表面
        center_x, center_y: 图片放置在表面的<中心坐标>
        """
        self.upperleft_x = center_x - self.img_width_scaled / 2
        self.upperleft_y = center_y - self.img_height_scaled / 2
        surface.blit(self.image_scaled, (self.upperleft_x, self.upperleft_y))
class ButtonText(Text):
    def __init__(self, text: str, text_color: Color, font_type: str, font_size: int):
        super().__init__(text, text_color, font_type, font_size)
        self.rect = self.text_image.get_rect()
 
    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y
 
    def handle_event_interface(self,command): #跳转其他界面
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            newinterface=command() #初始化
            newinterface.run()  #运行界面
    def handle_event_popup(self,command): #打开tkinter弹窗
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            newpopup=command()

class Button(Image):
    def __init__(self, img_name: str, ratio=0.4):
        super().__init__(img_name, ratio)
        self.rect = self.image_scaled.get_rect()
 
    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y
 
    def handle_event_interface(self,command):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            newinterface=command()
            newinterface.run()
    def handle_event_popup(self,command):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            newpopup=command()
"""
class commoncharacter:
    def Rolldice(self,center_x,center_y):   #一次掷骰子
        self.images=[]
        self.index=random.randint(0,2)
        for num in range(3):
            img=Image(f"dice{num}.jpg",0.4)
            self.images.append(img)
        self.frame=150 #骰子动画屏幕停留时间
        count=0
        while True:
            self.images[self.index].draw(self.display_surface,center_x,center_y)
            pygame.display.update()
            if count==10:break #随机切换骰子图片10次掷骰结束
            self.changeindex=random.randint(0,2)
            while self.index==self.changeindex:
                self.changeindex=random.randint(0,2)
            self.index=self.changeindex
            pygame.time.delay(self.frame)
            count+=1
        return self.index #返回最终显示图片的骰子点数
    def test(self,type,value): #能力考验 type:考验类型 value:该能力属性值
    def attack(self,type,enemy,value): #能力攻击 type:攻击类型 value:该能力属性值
    def move(self): #人物移动
    def getcards(self,type): #抽取卡牌 type:卡牌类型
    def checkbag(self): #查看人物背包中的预兆物品牌
    def show(self): 
    def attributechange(self,value): #人物能力属性上升或下降 上升或下降级数用value带正负表示
    def revealtruth(self,num): #揭露真相
class oldman(commoncharacter):
    def __init__(self):
        super().__init__()
        self.strength=
        self.speed=
        self.mind=
        self.knowledge=
        self.strengthlist=
        self.speedlist=
        self.mindlist=
        self.knowledgelist=
        self.bag=[]
        self.pos=
""" 
#class (commoncharacter):
class Start_interface:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH=1000
        self.WINDOW_HEIGHT=900
        self.display_surface=pygame.display.set_mode((self.WINDOW_WIDTH,self.WINDOW_HEIGHT))
        self.display_surface.fill(color.WHITE)
        pygame.display.set_caption("山中小屋")
        background_image = pygame.image.load("山中小屋背景.jpg")
        self.display_surface.blit(background_image, (0, 0))
        self.buttonstart=ButtonText("start",color.BLACK,"HYJinShi-95W.ttf",50)
        self.buttonstart.draw(self.display_surface,300,600)
        self.buttonhelp=ButtonText("help",color.BLACK,"HYJinShi-95W.ttf",50)
        self.buttonhelp.draw(self.display_surface,700,600)
        pygame.display.update()
    def run(self):
        self.running=True
        while self.running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.running=False
                    self.buttonstart.handle_event_interface(Ground_interface) #如果点击在开始按钮区域就跳转界面
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.running=True
                    self.buttonhelp.handle_event_popup(helpdocument) #如果点击在帮助按钮区域就跳转帮助文档弹窗
        pygame.quit()
class Choose_interface:#人物角色选择界面
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH=1200
        self.WINDOW_HEIGHT=800
        self.display_surface=pygame.display.set_mode((self.WINDOW_WIDTH,self.WINDOW_HEIGHT))
        self.display_surface.fill(color.LIGHTBLUE)
        pygame.display.set_caption("人物角色选择")
        self.characteroneimage=Image("character1.jpg",0.3)
        self.characteroneimage.draw(self.display_surface,300,400)
        self.charactertwoimage=Image("character2.jpg",0.3)
        self.charactertwoimage.draw(self.display_surface,900,400)
        pygame.display.update()
    def run(self):
        self.running=True
        while self.running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                     self.running=False
        pygame.quit()
class Basicbackground:
    def __init__(self):
        self.WINDOW_WIDTH=1200
        self.WINDOW_HEIGHT=800
        self.display_surface=pygame.display.set_mode((self.WINDOW_WIDTH,self.WINDOW_HEIGHT))
        pygame.display.set_caption("游戏界面")
        self.display_surface.fill(color.LIGHTBLUE)
        self.ratio=1
class Ground_interface(Basicbackground):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.image = Image("山中小屋背景.jpg",0.5)  
        self.image.draw(self.display_surface,self.WINDOW_WIDTH/2,self.WINDOW_HEIGHT/2)
        self.background_color = self.display_surface.get_at((0, 0))
        pygame.display.update()
    def run(self):
        running=True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                elif event.type == pygame.MOUSEWHEEL:  #通过鼠标滚轮控制地图放大缩小
                    # 隐藏图片，通过绘制一个相同大小的矩形
                    pygame.draw.rect(self.display_surface, self.background_color,(self.image.upperleft_x, self.image.upperleft_y, self.image.img_width_scaled, self.image.img_height_scaled))
                    # 获取滚轮移动的量，event.y 表示垂直滚动量，正值向上滚动，负值向下滚动
                    self.scroll_amount = event.y
                    # 执行放大或缩小操作
                    self.ratio=self.ratio+self.scroll_amount*0.01
                    self.image = Image("山中小屋背景.jpg",self.ratio)
                    self.image.draw(self.display_surface,self.WINDOW_WIDTH/2,self.WINDOW_HEIGHT/2)
                    pygame.display.update()
                           
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # 检测到空格键被按下
                        print("空格键被按下")

                        # 检测上下左右方向键
                    if event.key == pygame.K_UP:
                        print("上方向键被按下")
                           
                    if event.key == pygame.K_DOWN:
                        print("下方向键被按下")
                            
                    if event.key == pygame.K_LEFT:
                        print("左方向键被按下")
                           
                    if event.key == pygame.K_RIGHT:
                        print("右方向键被按下")
                         
        pygame.quit()
class Upstairs_interface(Basicbackground):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.image = Image("山中小屋背景.jpg",0.5)  
        self.image.draw(self.display_surface,self.WINDOW_WIDTH/2,self.WINDOW_HEIGHT/2)
        self.background_color = self.display_surface.get_at((0, 0)) # 假设左上角的像素代表背景色
        pygame.display.update()
    def run(self):
        running=True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                elif event.type == pygame.MOUSEWHEEL:  #通过鼠标滚轮控制地图放大缩小
                    # 隐藏图片，通过绘制一个相同大小的矩形
                    pygame.draw.rect(self.display_surface, self.background_color,(self.image.upperleft_x, self.image.upperleft_y, self.image.img_width_scaled, self.image.img_height_scaled))
                    # 获取滚轮移动的量，event.y 表示垂直滚动量，正值向上滚动，负值向下滚动
                    self.scroll_amount = event.y
                    # 执行放大或缩小操作
                    self.ratio=self.ratio+self.scroll_amount*0.01
                    self.image = Image("山中小屋背景.jpg",self.ratio)
                    self.image.draw(self.display_surface,self.WINDOW_WIDTH/2,self.WINDOW_HEIGHT/2)
                    pygame.display.update()
        pygame.quit()
class Downstairs_interface(Basicbackground):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.image = Image("山中小屋背景.jpg",0.5)  
        self.image.draw(self.display_surface,self.WINDOW_WIDTH/2,self.WINDOW_HEIGHT/2)
        self.background_color = self.display_surface.get_at((0, 0)) # 假设左上角的像素代表背景色
        pygame.display.update()
    def run(self):
        running=True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                elif event.type == pygame.MOUSEWHEEL:  #通过鼠标滚轮控制地图放大缩小
                    # 隐藏图片，通过绘制一个相同大小的矩形
                    pygame.draw.rect(self.display_surface, self.background_color,(self.image.upperleft_x, self.image.upperleft_y, self.image.img_width_scaled, self.image.img_height_scaled))
                    # 获取滚轮移动的量，event.y 表示垂直滚动量，正值向上滚动，负值向下滚动
                    self.scroll_amount = event.y
                    # 执行放大或缩小操作
                    self.ratio=self.ratio+self.scroll_amount*0.01
                    self.image = Image("山中小屋背景.jpg",self.ratio)
                    self.image.draw(self.display_surface,self.WINDOW_WIDTH/2,self.WINDOW_HEIGHT/2)
                    pygame.display.update()
        pygame.quit()
class helpdocument:
    def __init__(self):
        screen=tk.Tk()
        screen.title("help")
        resolution=screen.maxsize() #获取用户电脑分辨率
        resolutionw,resolutionh=resolution
        width=600
        height=800
        screen.geometry(f"{width}x{height}+{int(resolutionw*0.5)-int(width*0.5)}+{int(resolutionh*0.5)-int(height*0.5)}") #设置窗口打开位置
        screen.resizable(False,False)
        #screen.iconbitmap("") 只支持ICO
        title=tk.Label(screen,text="山中小屋游戏说明",font=("黑体",24),fg="red",bg="black")
        title.pack() #默认布局
        with open("山中小屋游戏说明.txt",'r',encoding='utf-8') as file:
            content = file.read()
        text = tk.Text(screen,font=("宋体",18))
        text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(screen, orient="vertical") #设置滚动条
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text.insert(tk.END, content) 
        screen.mainloop()
start_interface=Start_interface()
start_interface.run()


"""
    def Rolldice(self,center_x = .center_y = ):
        self.images=[]
        self.index=random.randint(0,2)
        for num in range(3):
            img=Image(f"dice{num}.jpg",0.4)
            self.images.append(img)
        self.frame=150 #骰子动画屏幕停留时间
        count=0
        while True:
            self.images[self.index].draw(self.display_surface,center_x,center_y)
            pygame.display.update()
            if count==10:break #随机切换骰子图片10次掷骰结束
            self.changeindex=random.randint(0,2)
            while self.index==self.changeindex:
                self.changeindex=random.randint(0,2)
            self.index=self.changeindex
            pygame.time.delay(self.frame)
            count+=1
        return self.index #返回最终显示图片的骰子点数
    """
