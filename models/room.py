from models.graphics import Image
import pygame
class room:
    roomlist = []
    def __init__(self,ID,name,floor,room_type,known,direct,open_to,obj_name):
        self.ID = ID   #没用的东西
        self.name = name   
        self.floor = floor
        self.room_type = room_type
        self.known = known
        self.direct = direct    #没用的东西
        self.open_to = open_to
        self.roomlist.append(self)
        self.had_done = 0
        self.obj_name = obj_name
        self.image = Image(fr"图片\房间\{obj_name}.jpg",0.35)
        self.connect_room = [0,0,0,0,0]
    def trigger(self,character):
        character.getcards(self.room_type)
        print("has triggered!")
    def direct_change(self):
            self.open_to = [self.open_to[-1]] + self.open_to[:-1]
    def special(self,character):
        pass
    def specialdown(self,character):
        pass
    def specialmove(self,character):
        pass
    def handle_event(self):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            return True
        return False


class vauit_room(room):#special room?
    def __init__(self, ID, name, floor, room_type, known, direct, open_to, obj_name):
        super().__init__(ID, name, floor, room_type, known, direct, open_to, obj_name)
        room.roomlist.append(self)
        self.have_items = 1
    def get_items(self,character):
        if(character.test("knowledge") >= 6 and self.have_items):
            character.getcards("item")
            character.getcards("item")
            self.have_items = 0      
Vauit = vauit_room(100,"保险库",[1,0,1],"event",0,0,[1,0,0,0],"Vauit")

class larder_room(room):
    def __init__(self, ID, name, floor, room_type, known, direct, open_to, obj_name):
        super().__init__(ID, name, floor, room_type, known, direct, open_to, obj_name)
        room.roomlist.append(self)
        self.have_items = 1
        self.had_gain = []
    def special(self,character):
        if self.have_items:
            character.getcards(self.room_type)
            self.have_items = 0
    def specialdown(self,character):
        for e in self.had_gain:
            if character == e:
                return
        character.attributechange(1,"strength")
        self.had_gain.append(character)
Larder = larder_room(101,"食品储藏室",[0,0,1],"item",0,0,[1,0,1,0],"Larder")

class graveyard_room(room):
    def __init__(self, ID, name, floor, room_type, known, direct, open_to, obj_name):
        super().__init__(ID, name, floor, room_type, known, direct, open_to, obj_name)
        room.roomlist.append(self)
    def special(self,character):
        if character.test("mind") <= 4:
            character.attributechange(-1,"knowledge")
Graveyard = graveyard_room(103,"墓园",[0,1,0],"event",0,0,[0,0,1,0],"Graveyard")

class attic_room(room):
    def __init__(self, ID, name, floor, room_type, known, direct, open_to, obj_name):
        super().__init__(ID, name, floor, room_type, known, direct, open_to, obj_name)
        room.roomlist.append(self)
    def special(self,character):
        if character.test("speed") <= 3:
            character.attributechange(-1,"strength")
Attic = attic_room(104,"阁楼",[0,0,1],"event",0,0,[0,0,1,0],"Attic")

class pentagram_chamber_room(room):
    def __init__(self, ID, name, floor, room_type, known, direct, open_to, obj_name):
        super().__init__(ID, name, floor, room_type, known, direct, open_to, obj_name)
        room.roomlist.append(self)
    def special(self,character):
        if character.test("knowledge") <= 4:
            character.attributechange(-1,"mind")
Gpentagram_chamber = pentagram_chamber_room(105,"五芒星堂",[1,0,0],"omen",0,0,[0,1,0,0],"Gpentagram_chamber")

class dungeon_room(room):
    def __init__(self, ID, name, floor, room_type, known, direct, open_to, obj_name):
        super().__init__(ID, name, floor, room_type, known, direct, open_to, obj_name)
        room.roomlist.append(self)
    def special(self,character):
        if character.test("mind") <= 6:
            character.attributechange(-1,"mind")
Dungeon = dungeon_room(106,"地牢",[1,0,0],"omen",0,0,[1,0,1,0],"Dungeon")

class junk_room(room):
    def __init__(self, ID, name, floor, room_type, known, direct, open_to, obj_name):
        super().__init__(ID, name, floor, room_type, known, direct, open_to, obj_name)
        room.roomlist.append(self)
    def special(self,character):
        if character.test("strength") <= 3:
            character.attributechange(-1,"speed")
Junkroom = junk_room(107,"破烂的房间",[1,1,1],"omen",0,0,[1,1,1,1],"Junkroom")

class furnace_room(room):
    def __init__(self, ID, name, floor, room_type, known, direct, open_to, obj_name):
        super().__init__(ID, name, floor, room_type, known, direct, open_to, obj_name)
        room.roomlist.append(self)
    def specialdown(self,character):
        character.attributechange(-1,"strength")
Furnaceroom = furnace_room(108,"暖炉房",[1,0,0],"omen",0,0,[1,0,1,1],"Furnaceroom")

class crypt_room(room):
    def __init__(self, ID, name, floor, room_type, known, direct, open_to, obj_name):
        super().__init__(ID, name, floor, room_type, known, direct, open_to, obj_name)
        room.roomlist.append(self)
    def specialdown(self,character):
        character.attributechange(-1,"mind")
Crypt = crypt_room(109,"地窖",[1,0,0],"event",0,0,[1,0,0,0],"Crypt")

class gymnasium_room(room):
    def __init__(self, ID, name, floor, room_type, known, direct, open_to, obj_name):
        super().__init__(ID, name, floor, room_type, known, direct, open_to, obj_name)
        room.roomlist.append(self)
        self.had_gain = []
    def specialdown(self,character):
        for e in self.had_gain:
            if character == e:
                return
        character.attributechange(1,"speed")
        self.had_gain.append(character)
Gymnasium = gymnasium_room(110,"健身房",[1,0,1],"omen",0,0,[0,1,1,0],"Gymnasium")

class chapel_room(room):
    def __init__(self, ID, name, floor, room_type, known, direct, open_to, obj_name):
        super().__init__(ID, name, floor, room_type, known, direct, open_to, obj_name)
        room.roomlist.append(self)
        self.had_gain = []
    def specialdown(self,character):
        for e in self.had_gain:
            if character == e:
                return
        character.attributechange(1,"mind")
        self.had_gain.append(character)
Chapel = chapel_room(111,"礼拜堂",[0,1,1],"event",0,0,[1,0,0,0],"Chapel")

class library_room(room):
    def __init__(self, ID, name, floor, room_type, known, direct, open_to, obj_name):
        super().__init__(ID, name, floor, room_type, known, direct, open_to, obj_name)
        room.roomlist.append(self)
        self.had_gain = []
    def specialdown(self,character):
        for e in self.had_gain:
            if character == e:
                return
        character.attributechange(1,"knowledge")
        self.had_gain.append(character)
Library = library_room(112,"图书馆",[0,1,1],"event",0,0,[0,0,1,1],"Library")



Gameroom = room(1, "游戏室", [1, 1, 1], "event", 0, 0, [1, 1, 1, 0], "Gameroom")
Organroom = room(2, "风琴室", [1, 1, 1], "event", 0, 0, [0, 0, 1, 1], "Organroom")
Ballroom = room(3, "舞厅", [0, 1, 0], "event", 0, 0, [1, 1, 1, 1], "Ballroom")
Researchlab = room(4, "研究室", [1, 0, 1], "event", 0, 0, [1, 0, 1, 0], "Researchlab")
Garden = room(5, "庭院", [0, 1, 0], "event", 0, 0, [1, 0, 1, 0], "Garden")
Bedroom = room(6, "寝室", [0, 0, 1], "event", 0, 0, [0, 1, 0, 1], "Bedroom")
Operatinglab = room(8, "手术室", [1, 0, 1], "event", 0, 0, [0, 1, 1, 0], "Operatinglab")
Bathroom = room(9, "浴室", [0, 1, 1], "event", 0, 0, [0, 0, 1, 0], "Bathroom")
Statuarycorridor = room(10, "雕塑长廊", [1, 1, 1], "event", 0, 0, [1, 0, 1, 0], "Statuarycorridor")
Undergroundlake = room(11, "地下湖", [1, 0, 0], "event", 0, 0, [1, 1, 0, 0], "Undergroundlake")
Conservatory = room(12, "温室", [0, 1, 1], "event", 0, 0, [1, 0, 0, 0], "Conservatory")
Patio = room(13, "天井", [0, 1, 0], "event", 0, 0, [1, 0, 1, 1], "Patio")
Master_bedroom = room(14, "主人房", [0, 0, 1], "omen", 0, 0, [1, 0, 0, 1], "Master_bedroom")
Charredroom = room(15, "熏黑的房间", [0, 1, 1], "omen", 0, 0, [1, 1, 1, 1], "Charredroom")
Diningroom = room(16, "餐厅", [0, 1, 0], "omen", 0, 0, [1, 1, 0, 0], "Diningroom")
Serventquarters = room(17, "佣人房", [1, 0, 1], "omen", 0, 0, [1, 1, 1, 1], "Serventquarters")
Abandonedroom = room(18, "荒废的房间", [1, 1, 0], "omen", 0, 0, [1, 1, 1, 1], "Abandonedroom")
Balcony = room(19, "露台", [0, 0, 1], "omen", 0, 0, [1, 0, 1, 0], "Balcony")
Theater = room(20, "剧院", [0, 1, 1], "omen", 0, 0, [0, 1, 0, 1], "Theater")
Bloodroom = room(21, "沾血的房间", [0, 1, 1], "item", 0, 0, [1, 1, 1, 1], "Bloodroom")
Storeroom = room(22, "储物室", [1, 0, 1], "item", 0, 0, [1, 0, 0, 0], "Storeroom")
Winecellar = room(23, "酒窖", [1, 0, 0], "item", 0, 0, [1, 0, 1, 0], "Winecellar")
Dustyhallway = room(24, "尘封的门廊", [1, 1, 1], "void", 0, 0, [1, 1, 1, 1], "Dustyhallway")
Creakyhallway = room(25, "老修的门廊", [1, 1, 1], "void", 0, 0, [1, 1, 1, 1], "Creakyhallway")
Entrancehall = room(26, "入口大堂", [0, 1, 0], "void", 1, 1, [0, 1, 1, 1], "Entrancehall")
Foyer = room(27, "门廊", [0, 1, 0], "void", 1, 1, [1, 1, 1, 1], "Foyer")
Grandstaircase = room(28, "梯间", [0, 1, 0], "void", 1, 1, [1, 0, 0, 0], "Grandstaircase")
Upperlanding = room(30, "上台阶", [0, 0, 1], "void", 1, 1, [1, 1, 1, 1], "Upperlanding")
Basementlanding = room(29, "下台阶", [1, 0, 0], "void", 1, 1, [1, 1, 1, 1], "Basementlanding")
Upstairs = room(32,"地下室楼梯",[1,0,0],"void",0,0,[1,0,1,0],"Upstairs")
Entrancehall.connect_room[2] = Foyer
Foyer.connect_room[0] = Entrancehall
Grandstaircase.connect_room[0] = Foyer
Foyer.connect_room[2] = Grandstaircase
Upstairs.connect_room[4] = Foyer
Grandstaircase.connect_room[4] = Upperlanding
Upperlanding.connect_room[4] = Grandstaircase
Kitchen = room(33,"厨房",[0,1,1],"omen",0,0,[1,1,0,0],"Kitchen")
class Coalchute_room(room):
    def __init__(self, ID, name, floor, room_type, known, direct, open_to, obj_name):
        super().__init__(ID, name, floor, room_type, known, direct, open_to, obj_name)
        room.roomlist.append(self)
    def specialmove(self,character):
        character.pos = Basementlanding
        character.position = [0,1,2]
Coalchute = Coalchute_room(31,"煤导槽",[0,1,1],"void",0,0,[1,0,0,0],"Coalchute")
class Cooapsedroom_room(room):
    def __init__(self, ID, name, floor, room_type, known, direct, open_to, obj_name):
        super().__init__(ID, name, floor, room_type, known, direct, open_to, obj_name)
        room.roomlist.append(self)
    def specialmove(self,character):
        character.pos = Basementlanding
        character.position = [0,1,2]
        #soecial_check_and_down
Cooapsedroom = Cooapsedroom_room(32,"崩塌的房间",[0,1,1],"void",0,0,[1,1,1,1],"Cooapsedroom")
Cooapsedroom.connect_room[4] = Basementlanding
Coalchute.connect_room[4] = Basementlanding
"""
class Tower_room(room)()
class Chims_room(room)()
"""
map = [[[0 for i in range(5)] for j in range(4)] for i in range(3)]
map[0][1][2] = Basementlanding
Basementlanding.image.picture = pygame.transform.rotate(Basementlanding.image.picture, 90)
Basementlanding.image.image_scaled = pygame.transform.smoothscale(Basementlanding.image.picture, Basementlanding.image.size_scaled)
Basementlanding.image.img_width_scaled = Basementlanding.image.image_scaled.get_width()
Basementlanding.image.img_height_scaled = Basementlanding.image.image_scaled.get_height()
Basementlanding.image.rect = Basementlanding.image.image_scaled.get_rect()
map[1][0][2] = Entrancehall
Entrancehall.image.picture = pygame.transform.rotate(Entrancehall.image.picture, 90)
Entrancehall.image.image_scaled = pygame.transform.smoothscale(Entrancehall.image.picture, Entrancehall.image.size_scaled)
Entrancehall.image.img_width_scaled = Entrancehall.image.image_scaled.get_width()
Entrancehall.image.img_height_scaled = Entrancehall.image.image_scaled.get_height()
Entrancehall.image.rect = Entrancehall.image.image_scaled.get_rect()
map[1][1][2] = Foyer
Foyer.image.picture = pygame.transform.rotate(Foyer.image.picture, 90)
Foyer.image.image_scaled = pygame.transform.smoothscale(Foyer.image.picture, Foyer.image.size_scaled)
Foyer.image.img_width_scaled = Foyer.image.image_scaled.get_width()
Foyer.image.img_height_scaled = Foyer.image.image_scaled.get_height()
Foyer.image.rect = Foyer.image.image_scaled.get_rect()
map[1][2][2] = Grandstaircase
Grandstaircase.image.picture = pygame.transform.rotate(Grandstaircase.image.picture, 90)
Grandstaircase.image.image_scaled = pygame.transform.smoothscale(Grandstaircase.image.picture, Grandstaircase.image.size_scaled)
Grandstaircase.image.img_width_scaled = Grandstaircase.image.image_scaled.get_width()
Grandstaircase.image.img_height_scaled = Grandstaircase.image.image_scaled.get_height()
Grandstaircase.image.rect = Grandstaircase.image.image_scaled.get_rect()
map[2][1][2] = Upperlanding
Upperlanding.image.picture = pygame.transform.rotate(Upperlanding.image.picture, 90)
Upperlanding.image.image_scaled = pygame.transform.smoothscale(Upperlanding.image.picture, Upperlanding.image.size_scaled)
Upperlanding.image.img_width_scaled = Upperlanding.image.image_scaled.get_width()
Upperlanding.image.img_height_scaled = Upperlanding.image.image_scaled.get_height()
Upperlanding.image.rect = Upperlanding.image.image_scaled.get_rect()
import random

def open_new_room(character,direction):#这个direction是人物移动的方向
    while True:
        newroom = random.choice(room.roomlist)
        if newroom.floor[character.position[0]] and (newroom.known == 0): #楼层合适与未被发现
            character.pos.connect_room[direction] = newroom #角色当前所在的房间与新房项链
            direction = (direction + 2) % 4   #这个是新房间连接口的方向
            for i in range(4):  #转
                if newroom.open_to[direction] == 1:
                    newroom.connect_room[direction] = character.pos
                    for j in range(3):  #探测剩余方向的连接情况
                        direction = (direction + 1) % 4#方向加一
                        if newroom.open_to[direction]:
                            if direction==0:
                                if character.position[1] - 1 > 0 and map[character.position[0]][character.position[1] - 1][character.position[2]] != 0: #如果旁边房间不为空
                                    directionA = (direction + 2) % 4 #旁边房间的连接口方向
                                    nearroom = map[character.position[0]][character.position[1] - 1][character.position[2]] 
                                    if nearroom.open_to[directionA]: #如果旁边房间开口
                                        nearroom.connect_room[directionA] = newroom
                                        newroom.connect_room[direction] = nearroom #加上对方的连接
                            elif direction==1:
                                if character.position[2] + 1 < 5 and map[character.position[0]][character.position[1]][character.position[2] + 1] != 0:
                                    directionA = (direction + 2) % 4
                                    nearroom = map[character.position[0]][character.position[1]][character.position[2] + 1]
                                    if nearroom.open_to[directionA]:
                                        nearroom.connect_room[directionA] = newroom
                                        newroom.connect_room[direction] = nearroom
                            elif direction==2:
                                if character.position[1] + 1 < 4 and map[character.position[0]][character.position[1] + 1][character.position[2]] != 0:
                                    directionA = (direction + 2) % 4
                                    nearroom = map[character.position[0]][character.position[1] + 1][character.position[2]]
                                    if nearroom.open_to[directionA]:
                                        nearroom.connect_room[directionA] = newroom
                                        newroom.connect_room[direction] = nearroom
                            elif direction == 3:
                               if character.position[2] - 1 > 0 and map[character.position[0]][character.position[1]][character.position[2] - 1] != 0:
                                    directionA = (direction + 2) % 4
                                    nearroom = map[character.position[0]][character.position[1]][character.position[2] - 1]
                                    if nearroom.open_to[directionA]:
                                        nearroom.connect_room[directionA] = newroom
                                        newroom.connect_room[direction] = nearroom
                
                    break
                newroom.image.picture = pygame.transform.rotate(newroom.image.picture, -90)
                newroom.image.image_scaled = pygame.transform.smoothscale(newroom.image.picture, newroom.image.size_scaled)
                newroom.image.img_width_scaled = newroom.image.image_scaled.get_width()
                newroom.image.img_height_scaled = newroom.image.image_scaled.get_height()
                newroom.image.rect = newroom.image.image_scaled.get_rect()
                newroom.direct_change() #如果没有对上就转动新房
                print("转了")
            print("trigger!")
            newroom.trigger(character)
            newroom.special(character)
            newroom.specialdown(character)  #翻开新房后各种检查
            map[character.position[0]][character.position[1]][character.position[2]] = newroom
            character.pos = newroom
            newroom.specialmove(character)
            newroom.known = 1
            print(newroom.name) 
             
            break
def find_element(lst, target):
    for i, layer in enumerate(lst):  # 遍历最外层
        for j, row in enumerate(layer):  # 遍历每一层中的每一行
            for k, element in enumerate(row):  # 遍历每一行中的每一个元素
                if element == target:
                    return [i, j, k]  # 返回元素的索引位置
    return None