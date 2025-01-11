import pygame
import random
import tkinter as tk
from tkinter import ttk
from PIL import Image as PILImage, ImageTk
#from PIL import Resampling
import models.items
import models.room
import models.events
from models.events import Eventlist, Eventfunclist
from models.omens import Omenlist, Omenfunclist
from models.graphics import Image, Button, ButtonText, color, Text
from config.config import levellist, levelnow, playernow, deathlist,playerlist

totalomen = 0

class Commoncharacter:
    def __init__(self):
        self.bag=[]
        self.hurtbuttonlist=[]
        
    def Rolldice(self):   #一次掷骰子
        num=random.randint(0,2)
        return num
    #tkinter制作骰子效果尝试
        """
        dicewindow = tk.Tk()
        dicewindow.geometry("400x400")  
        dicewindow.title("掷骰子")
        image=tk.PhotoImage(file="dice0.jpeg")
        canvas = tk.Canvas(dicewindow, width=400, height=400)
        canvas.pack()
        x=100
        y=100
        dice = canvas.create_image(x,y,image,anchor='center')
        dicewindow.update()
        dicewindow.mainloop()
        for i in range(30):
            angle = randint(0, 360)
            canvas.itemconfig(dice, image=images[randint(0, 2)])
            x = 100 + randint(-20, 20)
            y = 100 + randint(-20, 20)
            canvas.coords(dice, x, y, x+50, y+50)
            dicewindow.update()
            dicewindow.after(50)
        result = randint(0,2)
        canvas.itemconfig(dice, image=images[result])
        canvas.coords(dice, 175, 175, 225, 225)
        def close_window():
            dicewindow.destroy()
        dicewindow = tk.Tk()
        dicewindow.geometry("300x200")  
        dicewindow.title("掷骰子")
        label = tk.Label(dicewindow, text="这个窗口将在5秒后自动关闭。")
        label.pack()
        dicewindow.after(2000, close_window)
        dicewindow.mainloop()"""
    def directtest(self,num):   #num表示骰子个数
        sum=0
        for i in range(num):
            sum+=self.Rolldice()
        return sum
    def test(self,type): #能力考验 type:考验类型 value:该能力属性值
        sum=0
        if type=="strength":
            for i in range(self.strength):
                sum+=self.Rolldice()
        elif type=="speed":
            for i in range(self.speed):
                sum+=self.Rolldice()
        elif type=="mind":
            for i in range(self.mind):
                sum+=self.Rolldice()
        else:
            for i in range(self.knowledge):
                sum+=self.Rolldice()
        return sum        
    def attack(self,enemy): #能力攻击 
        numself=self.test("strength")
        numenemy=enemy.test("strength")
        print(numself)
        print(numenemy)
        if numself>numenemy:
            enemy.attributechange(numenemy-numself,"strength")
        elif numself<numenemy:
            self.attributechange(numself-numenemy,"strength")
    
    def move(character,direction):#人物移动
        if direction==0:
            if (character.pos.open_to[direction] == 0) or (character.position[1]-1 < 0): 
                print("撞到墙了")
                return
            else:
                character.position[1] = character.position[1] - 1
                if(character.pos.connect_room[direction] == 0 and models.room.map[character.position[0]][character.position[1]][character.position[2]] == 0):
                    models.room.open_new_room(character,direction)
                    print("has openned a newroom!")
                elif(character.pos.connect_room[direction] == 0 and models.room.map[character.position[0]][character.position[1]][character.position[2]] != 0):
                    print("撞到墙了")
                    character.position[2] = character.position[1] + 1
                    return
                else:
                    character.pos = character.pos.connect_room[direction]
            
                print(character.pos.name)
                print("has moved!")
        elif direction==1:
            if (character.pos.open_to[direction] == 0) or (character.position[2]+1 >= 5):  
                print("撞到墙了")
                return
            else:
                character.position[2] = character.position[2] + 1
                if(character.pos.connect_room[direction] == 0 and models.room.map[character.position[0]][character.position[1]][character.position[2]] == 0):
                    models.room.open_new_room(character,direction)
                    print("has openned a newroom!")
                elif(character.pos.connect_room[direction] == 0 and models.room.map[character.position[0]][character.position[1]][character.position[2]] != 0):
                    print("撞到墙了")
                    character.position[2] = character.position[2] - 1
                    return
                else:
                    character.pos = character.pos.connect_room[direction]
                
                print(character.pos.name)
                print("has moved!")
        elif direction==2:
            if (character.pos.open_to[direction] == 0) or (character.position[1]+1 >= 4): 
                print("撞到墙了")
                return
            else:
                character.position[1] = character.position[1] + 1
                if(character.pos.connect_room[direction] == 0 and models.room.map[character.position[0]][character.position[1]][character.position[2]] == 0):
                    models.room.open_new_room(character,direction)
                    print("has openned a newroom!")
                elif(character.pos.connect_room[direction] == 0 and models.room.map[character.position[0]][character.position[1]][character.position[2]] != 0):
                    print("撞到墙了")
                    character.position[1] = character.position[1] - 1
                    return
                else:
                    character.pos = character.pos.connect_room[direction]
                print(character.pos.name)
                print("has moved!")
        elif direction == 3:
            if (character.pos.open_to[direction] == 0) or (character.position[2]-1 < 0 ): 
                print("撞到墙了")
                return
            else:
                character.position[2] = character.position[2] - 1
                if(character.pos.connect_room[direction] == 0 and models.room.map[character.position[0]][character.position[1]][character.position[2]] == 0):
                    models.room.open_new_room(character,direction)
                    print("has openned a newroom!")
                elif(character.pos.connect_room[direction] == 0 and models.room.map[character.position[0]][character.position[1]][character.position[2]] != 0):
                    print("撞到墙了")
                    character.position[2] = character.position[2] + 1
                    return
                else:
                    character.pos = character.pos.connect_room[direction]
                print(character.pos.name)
                print("has moved!")
        elif direction == 4:
            if(character.pos.connect_room[direction] == 0):
                return
            character.position = models.room.find_element(models.room.map,character.pos.connect_room[direction])
            character.pos = character.pos.connect_room[direction]
            print(character.pos.name)
            print("has moved!")
    """
    def checkbag(self): #查看人物背包中的预兆物品牌
    def show(self):
    
    
    """
    def getcards(self,type): #抽取卡牌 type:卡牌类型
        if type=="omen":
            global totalomen
            totalomen += 1
            num=random.randint(0,len(Omenlist)-1)
            self.bag.append(Omenlist[num])
            if num<6:
                Omenfunclist[num](self,self)
            #else:Omenfunclist[num](self,self)
            self.revealtruth()
            print("has omen")
        if type=="event":
            num=2
            #num=random.randint(0,len(Eventlist)-1)
            Eventfunclist[num](self,self)
            print("has event")
        if type=="item":
            if len(models.items.item) == 0:
                print("没有可获取的物品！")
                return
            get_item = models.items.item[random.randint(0, len(models.items.item) - 1)]
            self.bag.append(get_item)
            if get_item == models.items.amulet_item:
                models.items.amulet(self)
            models.items.item.remove(get_item)
            print("has gain a item")
        #if type=="room":
        
            

    def attributechange(self,value,type): #人物能力属性上升或下降 上升或下降级数用value带正负表示
        if value!=0:
            if type=="body": #肉体属性变化，根据按钮降低速度和力量值
                self.testtype="body"
                self.hurtbuttonlist=[]
                for i in range(1-value):
                    self.hurtbutton=ButtonText("降低%d力量，降低%d速度"%(i,-value-i),color.WHITE,"HYJinShi-95W.ttf",18)
                    self.hurtbuttonlist.append(self.hurtbutton)
                    self.hurtbuttonlist[i].draw(levellist[levelnow].display_surface,levellist[levelnow].hurttypepos[self.sequence][0],levellist[levelnow].hurttypepos[self.sequence][1]+i*25)
                    pygame.display.update()
            if type=="spirit": #精神属性变化，随机神志或者知识
                self.testtype="spirit"
                self.hurtbuttonlist=[]
                for i in range(1-value):
                    self.hurtbutton=ButtonText("降低%d神志，降低%d知识"%(i,-value-i),color.WHITE,"HYJinShi-95W.ttf",18)
                    self.hurtbuttonlist.append(self.hurtbutton)
                    self.hurtbuttonlist[i].draw(levellist[levelnow].display_surface,levellist[levelnow].hurttypepos[self.sequence][0],levellist[levelnow].hurttypepos[self.sequence][1]+i*25)
                    pygame.display.update()
            if type=="strength":
                self.strength_pos+=value
                if self.strength_pos>7: #防止溢出
                    self.strength_pos=7
                if self.strength_pos<0:
                    self.strength_pos=0 #防止溢出
                    if startscript==1: #如果已经作祟则人物死亡
                        global currentplayerlist
                        global deathlist
                        currentplayerlist.remove(self.sequence)
                        deathlist.append(self.sequence)
                        self.deathtext=Text("人物已死亡",color.RED,"HYJinShi-95W.ttf",25)
                self.strength=self.strengthlist[self.strength_pos]
                pygame.event.post(changestrength)
            elif type=="speed":
                self.speed_pos+=value
                if self.speed_pos>7:
                    self.speed_pos=7
                if self.speed_pos<0:
                    self.speed_pos=0
                    if startscript==1:
                        currentplayerlist.remove(self.sequence)
                        deathlist.append(self.sequence)
                        self.deathtext=Text("人物已死亡",color.RED,"HYJinShi-95W.ttf",25)
                self.speed=self.speedlist[self.speed_pos]
                pygame.event.post(changespeed)
            elif type=="mind":
                self.mind_pos+=value
                if self.mind_pos>7:
                    self.mind_pos=7
                if self.mind_pos<0:
                    self.mind_pos=0
                    if startscript==1:
                        currentplayerlist.remove(self.sequence)
                        deathlist.append(self.sequence)
                        self.deathtext=Text("人物已死亡",color.RED,"HYJinShi-95W.ttf",25)
                self.mind=self.mindlist[self.mind_pos]
                pygame.event.post(changemind)
            elif type=="knowledge":
                self.knowledge_pos+=value
                if self.knowledge_pos>7:
                    self.knowledge_pos=7
                if self.knowledge_pos<0:
                    self.knowledge_pos=0
                    if startscript==1:
                        currentplayerlist.remove(self.sequence)
                        deathlist.append(self.sequence)
                        self.deathtext=Text("人物已死亡",color.RED,"HYJinShi-95W.ttf",25)
                self.knowledge=self.knowledgelist[self.knowledge_pos]
                pygame.event.post(changeknowledge)
        
            
    def revealtruth(self):
        sum=0
        for i in range(6):
            sum+=self.Rolldice()
        if sum<totalomen:
            global startscript
            startscript=1
            return True
        return False
  
class ProfessorLongfellow(Commoncharacter):
    def __init__(self):
        super().__init__()
        self.strength_pos=2
        self.speed_pos=3
        self.mind_pos=2
        self.knowledge_pos=4
        self.strengthlist=[1,2,3,4,5,5,6,6]
        self.speedlist=[2,2,4,4,5,5,6,6]
        self.mindlist=[1,3,3,4,5,5,6,7]
        self.knowledgelist=[4,5,5,5,5,6,7,8]
        self.strength=self.strengthlist[self.strength_pos]
        self.speed=self.speedlist[self.speed_pos]
        self.mind=self.mindlist[self.mind_pos]
        self.knowledge=self.knowledgelist[self.knowledge_pos]
        self.image=Image(r"图片\人物五边形\ProfessorLongfellow.png",0.2)
        self.circleimage=Image(r"图片\人物圆形标记\ProfessorLongfellowcircle.png",0.2)
        self.pos = models.room.Entrancehall
        self.position = [1,0,2]
professorLongfellow=ProfessorLongfellow()


class ZoeIngstrom(Commoncharacter):
    def __init__(self):
        super().__init__()
        self.strength_pos=3
        self.speed_pos=3
        self.mind_pos=2
        self.knowledge_pos=2
        self.strengthlist=[2,2,3,3,4,4,6,7]
        self.speedlist=[4,4,4,4,5,6,8,8]
        self.mindlist=[3,4,5,5,6,6,7,8]
        self.knowledgelist=[1,2,3,4,4,5,5,5]
        self.bag=[]
        self.strength=self.strengthlist[self.strength_pos]
        self.speed=self.speedlist[self.speed_pos]
        self.mind=self.mindlist[self.mind_pos]
        self.knowledge=self.knowledgelist[self.knowledge_pos]
        self.image=Image(r"图片\人物五边形\ZoeIngstrom.png",0.2)
        self.circleimage=Image(r"图片\人物圆形标记\ZoeIngstromcircle.png",0.2)
        self.pos = models.room.Entrancehall
        self.position = [1,0,2]

zoeIngstrom=ZoeIngstrom()
class HeatherGranville(Commoncharacter):
    def __init__(self):
        super().__init__()
        self.strength_pos=2
        self.speed_pos=2
        self.mind_pos=2
        self.knowledge_pos=4
        self.strengthlist=[3,3,3,4,5,6,7,8]
        self.speedlist=[3,3,4,5,6,6,7,8]
        self.mindlist=[3,3,3,4,5,6,6,6]
        self.knowledgelist=[2,3,3,4,5,6,7,8]
        self.strength=self.strengthlist[self.strength_pos]
        self.speed=self.speedlist[self.speed_pos]
        self.mind=self.mindlist[self.mind_pos]
        self.knowledge=self.knowledgelist[self.knowledge_pos]
        self.image=Image(r"图片\人物五边形\HeatherGranville.png",0.2)
        self.circleimage=Image(r"图片\人物圆形标记\HeatherGranvillecircle.png",0.2)
        self.pos = models.room.Entrancehall
        self.position = [1,0,2]

heatherGranville=HeatherGranville()
class BrandonJaspers(Commoncharacter):
    def __init__(self):
        super().__init__()
        self.strength_pos=3
        self.speed_pos=2
        self.mind_pos=3
        self.knowledge_pos=2
        self.strengthlist=[2,3,3,4,5,6,6,7]
        self.speedlist=[3,4,4,4,5,6,7,8]
        self.mindlist=[3,3,3,4,5,6,6,6]
        self.knowledgelist=[1,3,3,5,5,6,6,7]
        self.strength=self.strengthlist[self.strength_pos]
        self.speed=self.speedlist[self.speed_pos]
        self.mind=self.mindlist[self.mind_pos]
        self.knowledge=self.knowledgelist[self.knowledge_pos]
        self.image=Image(r"图片\人物五边形\BrandonJaspers.png",0.2)
        self.circleimage=Image(r"图片\人物圆形标记\BrandonJasperscircle.png",0.2)
        self.pos = models.room.Entrancehall
        self.position = [1,0,2]

brandonJaspers=BrandonJaspers()
class DarrinWilliams(Commoncharacter):
    def __init__(self):
        super().__init__()
        self.strength_pos=2
        self.speed_pos=4
        self.mind_pos=2
        self.knowledge_pos=2
        self.strengthlist=[2,3,3,4,5,6,6,7]
        self.speedlist=[4,4,4,5,6,7,7,8]
        self.mindlist=[1,2,3,4,5,5,5,7]
        self.knowledgelist=[2,3,3,4,5,5,5,7]
        self.strength=self.strengthlist[self.strength_pos]
        self.speed=self.speedlist[self.speed_pos]
        self.mind=self.mindlist[self.mind_pos]
        self.knowledge=self.knowledgelist[self.knowledge_pos]
        self.image=Image(r"图片\人物五边形\DarrinWilliams.png",0.2)
        self.circleimage=Image(r"图片\人物圆形标记\DarrinWilliamscircle.png",0.2)
        self.pos = models.room.Entrancehall
        self.position = [1,0,2]

darrinWilliams=DarrinWilliams()
class MadameZostra(Commoncharacter):
    def __init__(self):
        super().__init__()
        self.strength_pos=3
        self.speed_pos=2
        self.mind_pos=2
        self.knowledge_pos=3
        self.strengthlist=[2,3,3,4,5,5,5,6]
        self.speedlist=[2,3,3,5,5,6,6,7]
        self.mindlist=[4,4,4,5,6,7,8,8]
        self.knowledgelist=[1,3,4,4,4,5,6,6]
        self.strength=self.strengthlist[self.strength_pos]
        self.speed=self.speedlist[self.speed_pos]
        self.mind=self.mindlist[self.mind_pos]
        self.knowledge=self.knowledgelist[self.knowledge_pos]
        self.image=Image(r"图片\人物五边形\MadameZostra.png",0.2)
        self.circleimage=Image(r"图片\人物圆形标记\MadameZostracircle.png",0.2)
       
        self.pos = models.room.Entrancehall
        self.position = [1,0,2]
madameZostra=MadameZostra()
class MissyDubourde(Commoncharacter):
    def __init__(self):
        super().__init__()
        self.strength_pos=3
        self.speed_pos=2
        self.mind_pos=2
        self.knowledge_pos=3
        self.strengthlist=[2,3,3,3,4,5,6,7]
        self.speedlist=[3,4,5,6,6,6,7,7]
        self.mindlist=[1,2,3,4,5,5,6,7]
        self.knowledgelist=[2,3,4,4,5,6,6,6]
        self.strength=self.strengthlist[self.strength_pos]
        self.speed=self.speedlist[self.speed_pos]
        self.mind=self.mindlist[self.mind_pos]
        self.knowledge=self.knowledgelist[self.knowledge_pos]
        self.image=Image(r"图片\人物五边形\MissyDubourde.png",0.2)
        self.circleimage=Image(r"图片\人物圆形标记\MissyDubourdecircle.png",0.2)
        
        self.pos = models.room.Entrancehall
        self.position = [1,0,2]
missyDubourde=MissyDubourde()
class JennyLeclerc(Commoncharacter):
    def __init__(self):
        super().__init__()
        self.strength_pos=2
        self.speed_pos=3
        self.mind_pos=4
        self.knowledge_pos=2
        self.strengthlist=[3,4,4,4,4,5,6,8]
        self.speedlist=[2,3,4,4,4,5,6,8]
        self.mindlist=[1,1,2,4,4,4,5,6]
        self.knowledgelist=[2,3,3,4,4,5,6,8]
        self.strength=self.strengthlist[self.strength_pos]
        self.speed=self.speedlist[self.speed_pos]
        self.mind=self.mindlist[self.mind_pos]
        self.knowledge=self.knowledgelist[self.knowledge_pos]
        self.image=Image(r"图片\人物五边形\JennyLeclerc.png",0.2)
        self.circleimage=Image(r"图片\人物圆形标记\JennyLeclerccircle.png",0.2)
      
        self.pos = models.room.Entrancehall
        self.position = [1,0,2]
jennyLeclerc=JennyLeclerc()
class FatherRhinehardt(Commoncharacter):
    def __init__(self):
        super().__init__()
        self.strength_pos=2 #表示在四个属性列表中所在的位置
        self.speed_pos=2
        self.mind_pos=4
        self.knowledge_pos=3
        self.strengthlist=[1,2,2,4,4,5,5,7]
        self.speedlist=[2,3,3,4,5,6,7,7]
        self.mindlist=[3,4,5,5,6,7,7,8]
        self.knowledgelist=[1,3,3,4,5,6,6,8]
        self.strength=self.strengthlist[self.strength_pos]
        self.speed=self.speedlist[self.speed_pos]
        self.mind=self.mindlist[self.mind_pos]
        self.knowledge=self.knowledgelist[self.knowledge_pos]
        self.image=Image(r"图片\人物五边形\FatherRhinehardt.png",0.2)
        self.circleimage=Image(r"图片\人物圆形标记\FatherRhinehardtcircle.png",0.2)
        
        self.pos = models.room.Entrancehall
        self.position = [1,0,2]
fatherRhinehardt=FatherRhinehardt()
class PeterAkimoto(Commoncharacter):
    def __init__(self):
        super().__init__()
        self.strength_pos=2
        self.speed_pos=3
        self.mind_pos=3
        self.knowledge_pos=2
        self.strengthlist=[2,3,3,4,5,5,6,8]
        self.speedlist=[3,3,3,4,6,6,7,7]
        self.mindlist=[3,4,4,4,5,6,6,7]
        self.knowledgelist=[3,4,4,5,6,7,7,8]
        self.strength=self.strengthlist[self.strength_pos]
        self.speed=self.speedlist[self.speed_pos]
        self.mind=self.mindlist[self.mind_pos]
        self.knowledge=self.knowledgelist[self.knowledge_pos]
        self.image=Image(r"图片\人物五边形\PeterAkimoto.png",0.2)
        self.circleimage=Image(r"图片\人物圆形标记\PeterAkimotocircle.png",0.2)
      
        self.pos = models.room.Entrancehall
        self.position = [1,0,2]
peterAkimoto=PeterAkimoto()

class OxBellows(Commoncharacter):
    def __init__(self):
        super().__init__()
        self.strength_pos=2
        self.speed_pos=4
        self.mind_pos=2
        self.knowledge_pos=2
        self.strengthlist=[4,5,5,6,6,7,8,8]
        self.speedlist=[2,2,2,3,4,5,5,6]
        self.mindlist=[2,2,3,4,5,5,6,7]
        self.knowledgelist=[2,2,3,3,5,5,6,6]
        self.strength=self.strengthlist[self.strength_pos]
        self.speed=self.speedlist[self.speed_pos]
        self.mind=self.mindlist[self.mind_pos]
        self.knowledge=self.knowledgelist[self.knowledge_pos]
        self.image=Image(r"图片\人物五边形\OxBellows.png",0.2)
        self.circleimage=Image(r"图片\人物圆形标记\OxBellowscircle.png",0.2)
      
        self.pos = models.room.Entrancehall
        self.position = [1,0,2]
oxBellows=OxBellows()
class VivianLopez(Commoncharacter):
    def __init__(self):
        super().__init__()
        self.strength_pos=2
        self.speed_pos=3
        self.mind_pos=2
        self.knowledge_pos=3
        self.strengthlist=[2,2,2,4,4,5,6,6]
        self.speedlist=[3,4,4,4,4,6,7,8]
        self.mindlist=[4,4,4,5,6,7,8,8]
        self.knowledgelist=[4,5,5,5,5,6,6,7]
        self.strength=self.strengthlist[self.strength_pos]
        self.speed=self.speedlist[self.speed_pos]
        self.mind=self.mindlist[self.mind_pos]
        self.knowledge=self.knowledgelist[self.knowledge_pos]
        self.image=Image(r"图片\人物五边形\VivianLopez.png",0.2)
        self.circleimage=Image(r"图片\人物圆形标记\VivianLopezcircle.png",0.2)
        
        self.pos = models.room.Entrancehall
        self.position = [1,0,2]
vivianLopez=VivianLopez()

characterlist=[peterAkimoto,brandonJaspers,missyDubourde,zoeIngstrom,darrinWilliams,oxBellows,heatherGranville,jennyLeclerc,fatherRhinehardt,professorLongfellow,madameZostra,vivianLopez]

    
#人物属性变化就发布相应事件，让pygame修改页面中相应属性的值
CHANGEATTRIBUTE = pygame.USEREVENT
changestrength= pygame.event.Event(CHANGEATTRIBUTE,{"message":"strength"})
changespeed= pygame.event.Event(CHANGEATTRIBUTE,{"message":"speed"})
changemind= pygame.event.Event(CHANGEATTRIBUTE,{"message":"mind"})
changeknowledge= pygame.event.Event(CHANGEATTRIBUTE,{"message":"knowledge"})

class Start_interface:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH=1200
        self.WINDOW_HEIGHT=900
        self.display_surface=pygame.display.set_mode((self.WINDOW_WIDTH,self.WINDOW_HEIGHT))
        self.display_surface.fill(color.WHITE)
        pygame.display.set_caption("山中小屋")
        self.background_image = pygame.image.load(r"图片/山中小屋背景.jpg")
        self.display_surface.blit(self.background_image, (0, 0))
        self.buttonstart=ButtonText("start",color.BLACK,"HYJinShi-95W.ttf",50)
        self.buttonstart.draw(self.display_surface,400,600)
        self.buttonhelp=ButtonText("help",color.BLACK,"HYJinShi-95W.ttf",50)
        self.buttonhelp.draw(self.display_surface,800,600)
        pygame.display.update()
    def run(self):
        self.running=True
        while self.running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
                if event.type == pygame.MOUSEBUTTONDOWN: #如果点击在开始按钮区域就跳转界面
                    print(self.buttonstart.handle_event())
                    print(self.buttonhelp.handle_event())
                    if self.buttonstart.handle_event():
                        self.running=False                                    
                        choose_interface=Choose_interface()
                        choose_interface.run()
         #如果点击在帮助按钮区域就跳转帮助文档弹窗
                    if self.buttonhelp.handle_event():
                        self.running=True
                        newpopup=helpdocument() 
        pygame.quit()
"""
PeterAkimoto,BrandonJaspers,MissyDubourde,ZoeIngstrom,DarrinWilliams,OxBellows,HeatherGranville,JennyLeclerc,FatherRhinehardt,ProfessorLongfellow,MadameZostra,VivianLopez
"""

class Choose_interface:#人物角色选择界面 
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH=1200
        self.WINDOW_HEIGHT=900
        self.display_surface=pygame.display.set_mode((self.WINDOW_WIDTH,self.WINDOW_HEIGHT))
        self.background_image = pygame.image.load(r"图片/山中小屋背景.jpg")
        self.display_surface.blit(self.background_image, (0, 0))
        pygame.display.set_caption("人物角色选择")
        self.text=Text("请选择四个角色",color.WHITE,"HYJinShi-95W.ttf",50)
        self.text.draw(self.display_surface,600,45)
        self.PeterAkimotoimage=Button(r"图片\人物五边形\PeterAkimoto.png",0.28)
        self.PeterAkimotoimage.draw(self.display_surface,150,210)
        self.BrandonJaspersimage=Button(r"图片\人物五边形\BrandonJaspers.png",0.28)
        self.BrandonJaspersimage.draw(self.display_surface,450,210)
        self.MissyDubourdeimage=Button(r"图片\人物五边形\MissyDubourde.png",0.28)
        self.MissyDubourdeimage.draw(self.display_surface,750,210)
        self.ZoeIngstromimage=Button(r"图片\人物五边形\ZoeIngstrom.png",0.28)
        self.ZoeIngstromimage.draw(self.display_surface,1050,210)
        self.DarrinWilliamsimage=Button(r"图片\人物五边形\DarrinWilliams.png",0.28)
        self.DarrinWilliamsimage.draw(self.display_surface,150,490)
        self.OxBellowsimage=Button(r"图片\人物五边形\OxBellows.png",0.28)
        self.OxBellowsimage.draw(self.display_surface,450,490)
        self.HeatherGranvilleimage=Button(r"图片\人物五边形\HeatherGranville.png",0.28)
        self.HeatherGranvilleimage.draw(self.display_surface,750,490)
        self.JennyLeclercimage=Button(r"图片\人物五边形\JennyLeclerc.png",0.28)
        self.JennyLeclercimage.draw(self.display_surface,1050,490)
        self.FatherRhinehardtimage=Button(r"图片\人物五边形\FatherRhinehardt.png",0.28)
        self.FatherRhinehardtimage.draw(self.display_surface,150,770)
                                        
        self.ProfessorLongfellowimage=Button(r"图片\人物五边形\ProfessorLongfellow.png",0.28)
        self.ProfessorLongfellowimage.draw(self.display_surface,450,770)
        self.MadameZostraimage=Button(r"图片\人物五边形\MadameZostra.png",0.28)
        self.MadameZostraimage.draw(self.display_surface,750,770)
        self.VivianLopezimage=Button(r"图片\人物五边形\VivianLopez.png",0.28)
        self.VivianLopezimage.draw(self.display_surface,1050,770)
        self.buttonlist=[self.PeterAkimotoimage,self.BrandonJaspersimage,self.MissyDubourdeimage,self.ZoeIngstromimage,self.DarrinWilliamsimage,self.OxBellowsimage,self.HeatherGranvilleimage,self.JennyLeclercimage,self.FatherRhinehardtimage,self.ProfessorLongfellowimage,self.MadameZostraimage,self.VivianLopezimage]
        pygame.display.update()
    def run(self):
        self.count=0
        self.running=True
        downstairs_interface = Downstairs_interface()
        levellist.append(downstairs_interface)
        ground_interface = Ground_interface()
        levellist.append(ground_interface)
        upstairs_interface = Upstairs_interface()
        levellist.append(upstairs_interface)
        while self.running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(12):
                        if self.buttonlist[i].handle_event():
                            characterlist[i].sequence=self.count
                            self.count+=1
                            playerlist.append(characterlist[i])
                if self.count==4:
                    self.running=False
                    levellist[1].run()
                    
        pygame.quit()

        

class Basicbackground:
    def __init__(self):
        self.WINDOW_WIDTH=1200 #游戏主页面宽高
        self.WINDOW_HEIGHT=800
        self.ratio=1
        self.playertextpos=[[55,200],[1145,200],[1145,570],[55,570]] #人物四个属性文本的摆放位置
        self.playerimagepos=[[75,75],[1125,75],[1125,725],[75,725]] #人物五边形摆放位置
        self.hurttypepos=[[275,40],[925,40],[925,740],[275,740]] #肉体精神损伤分配情况按钮/四个属性选择按钮摆放的位置
        self.width=52 #四个属性文本的宽和高
        self.height=16
        self.hurtwidth=177
        self.hurtheight=19
        self.leftrightpos=[[1,3],[2,0],[3,1],[0,2]]
        self.bagpos=[[50,270],[1150,270],[1150,540],[50,540]]
    def Draw(self):
        self.display_surface=pygame.display.set_mode((self.WINDOW_WIDTH,self.WINDOW_HEIGHT))
        pygame.display.set_caption("游戏界面")
        self.background_color = self.display_surface.get_at((0, 0))
        for i in range(4):
            playerlist[i].image.draw(self.display_surface,self.playerimagepos[i][0],self.playerimagepos[i][1])
        for i in range(4):  #初始化用户选择四个属性选择按钮
            playerlist[i].strengthbutton=ButtonText("力量",color.WHITE,"HYJinShi-95W.ttf",20)
            playerlist[i].speedbutton=ButtonText("速度",color.WHITE,"HYJinShi-95W.ttf",20)
            playerlist[i].mindbutton=ButtonText("神志",color.WHITE,"HYJinShi-95W.ttf",20)
            playerlist[i].knowledgebutton=ButtonText("知识",color.WHITE,"HYJinShi-95W.ttf",20)
        for i in range(4):
            playerlist[i].textstrength=Text("力量：%d"%playerlist[i].strength,color.WHITE,"HYJinShi-95W.ttf",15)
            playerlist[i].textspeed=Text("速度：%d"%playerlist[i].speed,color.WHITE,"HYJinShi-95W.ttf",15)
            playerlist[i].textmind=Text("神志：%d"%playerlist[i].mind,color.WHITE,"HYJinShi-95W.ttf",15)
            playerlist[i].textknowledge=Text("知识：%d"%playerlist[i].knowledge,color.WHITE,"HYJinShi-95W.ttf",15)
            playerlist[i].textbag=ButtonText("背包",color.WHITE,"HYJinShi-95W.ttf",20)
        for i in range(4): #绘制显示人物四个属性的文本和背包按钮
            playerlist[i].textstrength.draw(self.display_surface,self.playertextpos[i][0],self.playertextpos[i][1])
            playerlist[i].textspeed.draw(self.display_surface,self.playertextpos[i][0],self.playertextpos[i][1]+16)
            playerlist[i].textmind.draw(self.display_surface,self.playertextpos[i][0],self.playertextpos[i][1]+32)
            playerlist[i].textknowledge.draw(self.display_surface,self.playertextpos[i][0],self.playertextpos[i][1]+48)
            playerlist[i].textbag.draw(self.display_surface,self.bagpos[i][0],self.bagpos[i][1])
        self.levelbuttonlist=[] #初始化楼层按钮
        self.levelbuttonpos=[[500,40],[600,40],[700,40]]
        self.downstairsbutton=ButtonText("地下",color.WHITE,"HYJinShi-95W.ttf",30)
        self.levelbuttonlist.append(self.downstairsbutton)
        self.groundbutton=ButtonText("地面",color.WHITE,"HYJinShi-95W.ttf",30)
        self.levelbuttonlist.append(self.groundbutton)
        self.upstairsbutton=ButtonText("楼上",color.WHITE,"HYJinShi-95W.ttf",30)
        self.levelbuttonlist.append(self.upstairsbutton)
        for i in range(3):
            self.levelbuttonlist[i].draw(self.display_surface,self.levelbuttonpos[i][0],self.levelbuttonpos[i][1])
        self.roomlength=175 #房间卡牌宽度/高度
        self.bigroomscale=0.7 #放大房间倍率
        self.startpos=[250,150] #可摆放的最左上角房间的位置
        pygame.display.update()

class Ground_interface(Basicbackground):
    def __init__(self):
        pygame.init()
        super().__init__()
    def run(self):
        global levelnow
        levelnow = 1
        self.running = True
        super().Draw()
        self.groundbutton = ButtonText("地面", color.RED, "HYJinShi-95W.ttf", 30)
        self.groundbutton.draw(self.display_surface, 600, 40)
        self.roomlist = [[0 for i in range(5)] for j in range(4)]
        playerlist[0].getcards("item")


        while self.running:
            for i in range(4):
                for j in range(5):
                    if models.room.map[1][i][j] == 0:
                        continue
                    else:
                        models.room.map[1][i][j].image.draw(self.display_surface, 250 + j * 175, 150 + i * 175)
            for i in range(4):
                if playerlist[i].position[0] == 1:
                    if i == 0:
                        a = 1
                        b = 0
                    elif i == 1:
                        a = 0
                        b = 1
                    elif i == 2:
                        a = -1
                        b = 0
                    elif i == 3:
                        a = 0
                        b = -1
                    playerlist[i].circleimage.draw(self.display_surface, playerlist[i].position[2] * 175 + 250 + a * 30,
                                                   playerlist[i].position[1] * 175 + 150 + b * 30)
            for i in deathlist:
                playerlist[deathlist[i]].deathtext.draw(self.display_surface, self.playerimagepos[deathlist[i]][0],
                                                       self.playerimagepos[deathlist[i]][1])
            for event in pygame.event.get():
                if event.type == CHANGEATTRIBUTE:
                    if event.message == "strength":
                        for i in range(4):
                            playerlist[i].textstrength = Text("力量：%d" % playerlist[i].strength, color.WHITE,
                                                              "HYJinShi-95W.ttf", 15)
                            pygame.draw.rect(self.display_surface, self.background_color,
                                             (self.playertextpos[i][0] - self.width / 2,
                                              self.playertextpos[i][1] - self.height / 2, self.width, self.height))
                            playerlist[i].textstrength.draw(self.display_surface, self.playertextpos[i][0],
                                                            self.playertextpos[i][1])
                    elif event.message == "speed":
                        for i in range(4):
                            playerlist[i].textspeed = Text("速度：%d" % playerlist[i].speed, color.WHITE,
                                                           "HYJinShi-95W.ttf", 15)
                            pygame.draw.rect(self.display_surface, self.background_color,
                                             (self.playertextpos[i][0] - self.width / 2,
                                              self.playertextpos[i][1] + 16 - self.height / 2, self.width, self.height))
                            playerlist[i].textspeed.draw(self.display_surface, self.playertextpos[i][0],
                                                         self.playertextpos[i][1] + 16)
                    elif event.message == "mind":
                        for i in range(4):
                            playerlist[i].textmind = Text("神志：%d" % playerlist[i].mind, color.WHITE,
                                                          "HYJinShi-95W.ttf", 15)
                            pygame.draw.rect(self.display_surface, self.background_color,
                                             (self.playertextpos[i][0] - self.width / 2,
                                              self.playertextpos[i][1] + 32 - self.height / 2, self.width, self.height))
                            playerlist[i].textmind.draw(self.display_surface, self.playertextpos[i][0],
                                                        self.playertextpos[i][1] + 32)
                    else:
                        for i in range(4):
                            playerlist[i].textknowledge = Text("知识：%d" % playerlist[i].knowledge, color.WHITE,
                                                               "HYJinShi-95W.ttf", 15)
                            pygame.draw.rect(self.display_surface, self.background_color,
                                             (self.playertextpos[i][0] - self.width / 2,
                                              self.playertextpos[i][1] + 48 - self.height / 2, self.width, self.height))
                            playerlist[i].textknowledge.draw(self.display_surface, self.playertextpos[i][0],
                                                             self.playertextpos[i][1] + 48)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(4):
                        x, y = 20, 20
                        if playerlist[i].textbag.handle_event():
                            bag = tk.Tk()
                            bag.geometry('1200x600')
                            bag.title(f"玩家{i}的背包")
                            
                            item_width = 250
                            item_height = 500
                            photolist = []
                            labellist = []
                            for thing in playerlist[i].bag:
                                if isinstance(thing, models.items.Items):
                                    try:
                                        img = PILImage.open(thing.image.img_name)
                                        img = img.resize((item_width, item_height))
                                        photo = ImageTk.PhotoImage(img)
                                        photolist.append(photo)
                                        
                                        label = tk.Label(bag, image=photo)
                                        label.image = photo
                                        label.place(x=x, y=y)
                                        labellist.append(label)
                                        x += 250
                                    except:
                                        pass
                            bag.mainloop()
                    for i in range(len(playerlist[playernow].hurtbuttonlist)):
                        if playerlist[playernow].hurtbuttonlist[i].handle_event():
                            for j in range(len(playerlist[playernow].hurtbuttonlist)):
                                pygame.draw.rect(self.display_surface, self.background_color,
                                                 (self.hurttypepos[playernow][0] - self.hurtwidth / 2,
                                                  self.hurttypepos[playernow][1] - self.hurtheight / 2 + j * 25,
                                                  self.hurtwidth, self.hurtheight))
                            if playerlist[playernow].testtype == "body":
                                playerlist[playernow].attributechange(-i, "strength")
                                playerlist[playernow].attributechange(i - len(playerlist[playernow].hurtbuttonlist) + 1,
                                                                      "speed")
                            else:
                                playerlist[playernow].attributechange(-i, "mind")
                                playerlist[playernow].attributechange(i - len(playerlist[playernow].hurtbuttonlist) + 1,
                                                                      "knowledge")
                            playerlist[playernow].hurtbuttonlist = []
                            break
                    for i in range(3):
                        if self.levelbuttonlist[i].handle_event():
                            self.running = False
                            levellist[i].run()
                    for i in range(4):
                        for j in range(5):
                            if self.roomlist[i][j]!= 0:
                                if self.roomlist[i][j].handle_event():
                                    if self.roomlist[i][j].scalenow == 0:
                                        self.roomlist[i][j].scalechange(self.display_surface, self.bigroomscale)
                                        self.roomlist[i][j].scalenow = 1
                                    else:
                                        pygame.draw.rect(self.display_surface, self.background_color,
                                                         (self.roomlist[i][j].upperleft_x, self.roomlist[i][j].upperleft_y,
                                                          self.roomlist[i][j].img_width_scaled,
                                                          self.roomlist[i][j].img_height_scaled))
                                        self.roomlist[i][j].scalenow = 0
                                        if (i == 0 and j == 0) or (i == 0 and j == 4) or (i == 3 and j == 0) or (
                                                i == 3 and j == 4):
                                            for i in range(4):
                                                playerlist[i].image.draw(self.display_surface, self.playerimagepos[i][0],
                                                                         self.playerimagepos[i][1])
                                        if i == 0:
                                            for i in range(3):
                                                self.levelbuttonlist[i].draw(self.display_surface,
                                                                             self.levelbuttonpos[i][0],
                                                                             self.levelbuttonpos[i][1])
                                            self.levelbuttonlist[1] = ButtonText("地面", color.RED, "HYJinShi-95W.ttf", 30)
                                            self.levelbuttonlist[1].draw(self.display_surface, 600, 40)
                                        for i in range(4):
                                            for j in range(5):
                                                self.room.draw(self.display_surface, self.startpos[0] + j * self.roomlength,
                                                               self.startpos[1] + i * self.roomlength)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("空格键被按下")
                        playerlist[0].move(4)
                    if event.key == pygame.K_RETURN:
                        print("Enter键被按下")
                    if event.key == pygame.K_UP:
                        print("上方向键被按下")
                        playerlist[0].move(0)
                    if event.key == pygame.K_DOWN:
                        print("下方向键被按下")
                        playerlist[0].move(2)
                    if event.key == pygame.K_LEFT:
                        print("左方向键被按下")
                        playerlist[0].move(3)
                    if event.key == pygame.K_RIGHT:
                        print("右方向键被按下")
                        playerlist[0].move(1)
                elif event.type == pygame.QUIT:
                    self.running = False
            pygame.display.update()


        pygame.quit()
class Upstairs_interface(Basicbackground):
    def __init__(self):
        pygame.init()
        super().__init__()
    def run(self):
        global levelnow
        levelnow=2
        self.running=True
        super().Draw()
        self.upstairsbutton=ButtonText("楼上",color.RED,"HYJinShi-95W.ttf",30)
        self.upstairsbutton.draw(self.display_surface,700,40)
        self.roomlist=[[0 for i in range(5)] for j in range(4)]
        while self.running:
            for i in range(4):
                for j in range(5):
                    if models.room.map[2][i][j] == 0:
                        continue
                    else:
                        models.room.map[2][i][j].image.draw(self.display_surface,250+j*175,150+i*175)
            for i in range(4):
                if playerlist[i].position[0] == 2:
                    if i == 0:
                        a = 1
                        b = 0
                    elif i == 1: 
                        a = 0
                        b = 1
                    elif i == 2:
                        a = -1
                        b = 0
                    elif i == 3: 
                        a = 0
                        b = -1
                    playerlist[i].circleimage.draw(self.display_surface,playerlist[i].position[2]*175+250+a*30,playerlist[i].position[1]*175+150+b*30)
            for i in deathlist:
                playerlist[deathlist[i]].deathtext.draw(self.display_surface,self.playerimagepos[deathlist[i]][0],self.playerimagepos[deathlist[i]][1])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running=False
               
                if event.type == CHANGEATTRIBUTE:#检测到有角色属性变化，更新相应文本
                    if event.message=="strength":
                        for i in range(4):
                            playerlist[i].textstrength=Text("力量：%d"%playerlist[i].strength,color.WHITE,"HYJinShi-95W.ttf",15)
                            pygame.draw.rect(self.display_surface, self.background_color,(self.playertextpos[i][0]-self.width/2,self.playertextpos[i][1]-self.height/2,self.width,self.height))
                            playerlist[i].textstrength.draw(self.display_surface,self.playertextpos[i][0],self.playertextpos[i][1])
                    elif event.message=="speed":
                        for i in range(4):
                            playerlist[i].textspeed=Text("速度：%d"%playerlist[i].speed,color.WHITE,"HYJinShi-95W.ttf",15)
                            pygame.draw.rect(self.display_surface, self.background_color,(self.playertextpos[i][0]-self.width/2,self.playertextpos[i][1]+16-self.height/2,self.width,self.height))
                            playerlist[i].textspeed.draw(self.display_surface,self.playertextpos[i][0],self.playertextpos[i][1]+16)
                    elif event.message=="mind":
                        for i in range(4):
                            playerlist[i].textmind=Text("神志：%d"%playerlist[i].mind,color.WHITE,"HYJinShi-95W.ttf",15)
                            pygame.draw.rect(self.display_surface, self.background_color,(self.playertextpos[i][0]-self.width/2,self.playertextpos[i][1]+32-self.height/2,self.width,self.height))
                            playerlist[i].textmind.draw(self.display_surface,self.playertextpos[i][0],self.playertextpos[i][1]+32)
                    else:
                        for i in range(4):
                            playerlist[i].textknowledge=Text("知识：%d"%playerlist[i].knowledge,color.WHITE,"HYJinShi-95W.ttf",15)
                            pygame.draw.rect(self.display_surface, self.background_color,(self.playertextpos[i][0]-self.width/2,self.playertextpos[i][1]+48-self.height/2,self.width,self.height))
                            playerlist[i].textknowledge.draw(self.display_surface,self.playertextpos[i][0],self.playertextpos[i][1]+48)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(4):
                        if playerlist[i].textbag.handle_event():
                            print(f"玩家{i}的背包按钮被点击")
                    for i in range(len(playerlist[playernow].hurtbuttonlist)):
                        if playerlist[playernow].hurtbuttonlist[i].handle_event():
                            if playerlist[playernow].testtype=="body":
                                playerlist[playernow].attributechange(-i,"strength")
                                playerlist[playernow].attributechange(i-len(playerlist[playernow].hurtbuttonlist)+1,"speed")
                            else:
                                playerlist[playernow].attributechange(-i,"mind")
                                playerlist[playernow].attributechange(i-len(playerlist[playernow].hurtbuttonlist)+1,"knowledge")
                            playerlist[playernow].hurtbuttonlist=[]
                            break
                    for i in range(3):
                        if self.levelbuttonlist[i].handle_event():
                            self.running=False
                            levellist[i].run()
                    for i in range(4): #点击房间图片就放大缩小房间
                        for j in range(5):
                            if self.roomlist[i][j]!=0:
                                if self.roomlist[i][j].handle_event():
                                    if self.roomlist[i][j].scalenow==0:
                                        self.roomlist[i][j].scalechange(self.display_surface,self.bigroomscale)
                                        self.roomlist[i][j].scalenow=1
                                    else:
                                        pygame.draw.rect(self.display_surface, self.background_color,(self.roomlist[i][j].upperleft_x, self.roomlist[i][j].upperleft_y, self.roomlist[i][j].img_width_scaled, self.roomlist[i][j].img_height_scaled))
                                        self.roomlist[i][j].scalenow=0
                                        if (i==0 and j==0) or (i==0 and j==4) or(i==3 and j==0) or (i==3 and j==4):
                                            for i in range(4):
                                                playerlist[i].image.draw(self.display_surface,self.playerimagepos[i][0],self.playerimagepos[i][1])
                                        if i==0:
                                            for i in range(3):
                                                self.levelbuttonlist[i].draw(self.display_surface,self.levelbuttonpos[i][0],self.levelbuttonpos[i][1])
                                            self.levelbuttonlist[1]=ButtonText("地面",color.RED,"HYJinShi-95W.ttf",30)
                                            self.levelbuttonlist[1].draw(self.display_surface,600,40)
                                        for i in range(4): 
                                            for j in range(5):
                                                self.room.draw(self.display_surface,self.startpos[0]+j*self.roomlength,self.startpos[1]+i*self.roomlength)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # 检测到空格键被按下
                        print("空格键被按下")
                        playerlist[0].move(4)
                    if event.key == pygame.K_RETURN:
                        print("Enter键被按下")

                        # 检测上下左右方向键
                    if event.key == pygame.K_UP:
                        print("上方向键被按下")
                        playerlist[0].move(0)
                           
                    if event.key == pygame.K_DOWN:
                        print("下方向键被按下")
                        playerlist[0].move(2)
                            
                    if event.key == pygame.K_LEFT:
                        print("左方向键被按下")
                        playerlist[0].move(3)
                           
                    if event.key == pygame.K_RIGHT:
                        print("右方向键被按下") 
                        playerlist[0].move(1)      
                elif event.type == pygame.QUIT:
                    self.running=False
            
                        
            
            pygame.display.update()
class Downstairs_interface(Basicbackground):
    def __init__(self):
        pygame.init()
        super().__init__()
    def run(self):
        global levelnow
        levelnow=0
        self.running=True
        super().Draw()
        self.downstairsbutton=ButtonText("地下",color.RED,"HYJinShi-95W.ttf",30)
        self.downstairsbutton.draw(self.display_surface,500,40)
        self.roomlist=[[0 for i in range(5)] for j in range(4)]
        while self.running:
            for i in range(4):
                for j in range(5):
                    if models.room.map[0][i][j] == 0:
                        continue
                    else:
                        models.room.map[0][i][j].image.draw(self.display_surface,250+j*175,150+i*175)
            for i in range(4):
                if playerlist[i].position[0] == 0:
                    if i == 0:
                        a = 1
                        b = 0
                    elif i == 1: 
                        a = 0
                        b = 1
                    elif i == 2:
                        a = -1
                        b = 0
                    elif i == 3: 
                        a = 0
                        b = -1
                    playerlist[i].circleimage.draw(self.display_surface,playerlist[i].position[2]*175+250+a*30,playerlist[i].position[1]*175+150+b*30)
            for i in deathlist:
                playerlist[deathlist[i]].deathtext.draw(self.display_surface,self.playerimagepos[deathlist[i]][0],self.playerimagepos[deathlist[i]][1])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running=False
               
                if event.type == CHANGEATTRIBUTE:#检测到有角色属性变化，更新相应文本
                    if event.message=="strength":
                        for i in range(4):
                            playerlist[i].textstrength=Text("力量：%d"%playerlist[i].strength,color.WHITE,"HYJinShi-95W.ttf",15)
                            pygame.draw.rect(self.display_surface, self.background_color,(self.playertextpos[i][0]-self.width/2,self.playertextpos[i][1]-self.height/2,self.width,self.height))
                            playerlist[i].textstrength.draw(self.display_surface,self.playertextpos[i][0],self.playertextpos[i][1])
                    elif event.message=="speed":
                        for i in range(4):
                            playerlist[i].textspeed=Text("速度：%d"%playerlist[i].speed,color.WHITE,"HYJinShi-95W.ttf",15)
                            pygame.draw.rect(self.display_surface, self.background_color,(self.playertextpos[i][0]-self.width/2,self.playertextpos[i][1]+16-self.height/2,self.width,self.height))
                            playerlist[i].textspeed.draw(self.display_surface,self.playertextpos[i][0],self.playertextpos[i][1]+16)
                    elif event.message=="mind":
                        for i in range(4):
                            playerlist[i].textmind=Text("神志：%d"%playerlist[i].mind,color.WHITE,"HYJinShi-95W.ttf",15)
                            pygame.draw.rect(self.display_surface, self.background_color,(self.playertextpos[i][0]-self.width/2,self.playertextpos[i][1]+32-self.height/2,self.width,self.height))
                            playerlist[i].textmind.draw(self.display_surface,self.playertextpos[i][0],self.playertextpos[i][1]+32)
                    else:
                        for i in range(4):
                            playerlist[i].textknowledge=Text("知识：%d"%playerlist[i].knowledge,color.WHITE,"HYJinShi-95W.ttf",15)
                            pygame.draw.rect(self.display_surface, self.background_color,(self.playertextpos[i][0]-self.width/2,self.playertextpos[i][1]+48-self.height/2,self.width,self.height))
                            playerlist[i].textknowledge.draw(self.display_surface,self.playertextpos[i][0],self.playertextpos[i][1]+48)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(4):
                        if playerlist[i].textbag.handle_event():
                            print(f"玩家{i}的背包按钮被点击")
                    for i in range(len(playerlist[playernow].hurtbuttonlist)):
                        if playerlist[playernow].hurtbuttonlist[i].handle_event():
                            if playerlist[playernow].testtype=="body":
                                playerlist[playernow].attributechange(-i,"strength")
                                playerlist[playernow].attributechange(i-len(playerlist[playernow].hurtbuttonlist)+1,"speed")
                            else:
                                playerlist[playernow].attributechange(-i,"mind")
                                playerlist[playernow].attributechange(i-len(playerlist[playernow].hurtbuttonlist)+1,"knowledge")
                            playerlist[playernow].hurtbuttonlist=[]
                            break
                    for i in range(3):
                        if self.levelbuttonlist[i].handle_event():
                            self.running=False
                            levellist[i].run()
                    for i in range(4): #点击房间图片就放大缩小房间
                        for j in range(5):
                            if self.roomlist[i][j]!=0:
                                if self.roomlist[i][j].handle_event():
                                    if self.roomlist[i][j].scalenow==0:
                                        self.roomlist[i][j].scalechange(self.display_surface,self.bigroomscale)
                                        self.roomlist[i][j].scalenow=1
                                    else:
                                        pygame.draw.rect(self.display_surface, self.background_color,(self.roomlist[i][j].upperleft_x, self.roomlist[i][j].upperleft_y, self.roomlist[i][j].img_width_scaled, self.roomlist[i][j].img_height_scaled))
                                        self.roomlist[i][j].scalenow=0
                                        if (i==0 and j==0) or (i==0 and j==4) or(i==3 and j==0) or (i==3 and j==4):
                                            for i in range(4):
                                                playerlist[i].image.draw(self.display_surface,self.playerimagepos[i][0],self.playerimagepos[i][1])
                                        if i==0:
                                            for i in range(3):
                                                self.levelbuttonlist[i].draw(self.display_surface,self.levelbuttonpos[i][0],self.levelbuttonpos[i][1])
                                            self.levelbuttonlist[1]=ButtonText("地面",color.RED,"HYJinShi-95W.ttf",30)
                                            self.levelbuttonlist[1].draw(self.display_surface,600,40)
                                        for i in range(4): 
                                            for j in range(5):
                                                self.room.draw(self.display_surface,self.startpos[0]+j*self.roomlength,self.startpos[1]+i*self.roomlength)
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # 检测到空格键被按下
                        print("空格键被按下")
                        playerlist[0].move(4)
                    if event.key == pygame.K_RETURN:
                        print("Enter键被按下")

                        # 检测上下左右方向键
                    if event.key == pygame.K_UP:
                        print("上方向键被按下")
                        playerlist[0].move(0)
                           
                    if event.key == pygame.K_DOWN:
                        print("下方向键被按下")
                        playerlist[0].move(2)
                            
                    if event.key == pygame.K_LEFT:
                        print("左方向键被按下")
                        playerlist[0].move(3)
                           
                    if event.key == pygame.K_RIGHT:
                        print("右方向键被按下") 
                        playerlist[0].move(1)      
                elif event.type == pygame.QUIT:
                    self.running=False
               
                        
            
            pygame.display.update()


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

downstairs_interface = Downstairs_interface()
levellist.append(downstairs_interface)
ground_interface = Ground_interface()
levellist.append(ground_interface)
upstairs_interface = Upstairs_interface()
levellist.append(upstairs_interface)