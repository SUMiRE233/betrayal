import pygame
import random
from models.graphics import Image
from config.config import playerlist, playernow

class Items:
    def __init__(self, name, description, effect, image, discard_after_use, can_be_stolen):
        self.name = name
        self.description = description
        self.effect = effect
        self.image = Image(img_name = image)
        self.discard_after_use = discard_after_use
        self.can_be_stolen = can_be_stolen
        self.type = "items"

#肾上腺素
def Adrenaline(dice_index):
    return dice_index + 4

#上古护符
import random


def amulet(character):
    character.attributechange(1, "strength")
    character.attributechange(1, "speed")
    character.attributechange(1, "knowledge")
    character.attributechange(1, "mind")


def lose_amulet(character):
    character.attributechange(-3, "strength")
    character.attributechange(-3, "speed")
    character.attributechange(-3, "knowledge")
    character.attributechange(-3, "mind")


# 天使羽毛
def feather():
    dice_index = int(input("需要的点数"))
    while (True):
        if (0 <= dice_index <= 8):
            return dice_index
        print("请选择0到8间的数值！")


# 盔甲
def armor(damage):
    return damage - 1


# 斧头
def axe(character):
    if (character.strength < 8):
        return character.strength + 1
    return 8


# 铃铛
# def bell(character):
#     character."mind" += 1
#
#
# def lose_bell(character):
#     character."mind" -= 1
#
#
# def use_bell(dice_index):
#     if (dice_index >= 5):


# 血棘
def knife_of_blood(character):
    character.attributechange(-1, "speed")
    if (character.strength < 6):
        dice_index = 0
        for i in range(character.strength + 3):
            dice_index += character.character.Rolldice()
        return dice_index
    else:
        for i in range(8):
            dice_index += character.Rolldice()
        return dice_index


# 瓶子
def bottle(character):
    dice_index = 0
    for i in range(3):
        dice_index += character.Rolldice()
    if (dice_index == 0):
        character.attributechange(-2, "strength")
        character.attributechange(-2, "speed")
        character.attributechange(-2, "mind")
        character.attributechange(-2, "knowledge")
    elif (dice_index == 1):
        character.attributechange(-2, "strength")
        character.attributechange(-2, "speed")
    elif (dice_index == 2):
        character.attributechange(-2, "mind")
        character.attributechange(-2, "knowledge")
    elif (dice_index == 3):
        character.attributechange(-1, "strength")
        character.attributechange(1, "knowledge")
    elif (dice_index == 4):
        character.attributechange(2, "mind")
        character.attributechange(2, "knowledge")
    elif (dice_index == 5):
        character.attributechange(2, "strength")
        character.attributechange(2, "speed")
    else:
        # 移动到任意房间
        pass


# 蜡烛
# def candle():


# 黑暗骰子
def dark_dice():
    character = playerlist[playernow]
    dice_index = 0
    for i in range(3):
        dice_index += character.Rolldice()
    if (dice_index == 0):
        character.attributechange(-(character.strength - 1), "strength")
        character.attributechange(-(character.speed - 1), "speed")
        character.attributechange(-(character.mind - 1), "mind")
        character.attributechange(-(character.knowledge - 1), "knowledge")
    elif (dice_index == 1):
        # 抽取事件
        pass
    elif (dice_index == 2):
        index = random.randint(1, 3)
        if (index == 1):
            character.attributechange(1, "mind")
        else:
            character.attributechange(1, "knowledge")
    elif (dice_index == 3):
        # 移动到相邻房间
        pass
    elif (dice_index == 4):
        index = random.randint(1, 3)
        if (index == 1):
            character.attributechange(1, "strength")
        else:
            character.attributechange(1, "speed")
    elif (dice_index == 5):
        # 所有人移动到相邻房间
        pass
    else:
        # 移动到队友房间
        pass


#
# def dynamite():


# 治疗药膏
def healing_ointment(character, choice):
    if (choice == "strength"):
        if (character.strength < 8):
            character.attributechange(1, "strength")
    if (choice == "speed"):
        if (character.speed < 8):
            character.attributechange(1, "speed")


# 神像
def idol(character, choice):
    dice_index = 0
    if choice == "strength":
        for i in range(min(character.strength + 2, 8)):
            dice_index += character.Rolldice()
    if choice == "speed":
        for i in range(min(character.speed + 2, 8)):
            dice_index += character.Rolldice()
    if choice == "mind":
        for i in range(min(character.mind + 2, 8)):
            dice_index += character.Rolldice()
    if choice == "knowledge":
        for i in range(min(character.knowledge + 2, 8)):
            dice_index += character.Rolldice()
    character.attributechange(-1, "mind")
    return dice_index


# 盗贼手套
def gloves_of_thief(character, other):
    index = len(other.bag)
    r = random.randint(0, index - 1)
    character.bag.append(other.bag[r])
    other.bag.remove(other.bag[r])


# 魔术方块
def magic_cube(character):
    dice_index = 0
    for i in range(character.knowledge):
        dice_index += character.Rolldice()
    if (dice_index >= 6):
        # 抽取两张物品
        pass
    else:
        return "failed!"

item = []

# 创建Adrenaline物品实例
adrenaline_item = Items(
    name="Adrenaline",
    description="",
    effect=Adrenaline,
    image=r"图片/物品/Adrenaline.jpg",
    discard_after_use=True,
    can_be_stolen=True
)
item.append(adrenaline_item)

# 创建Amulet物品实例
amulet_item = Items(
    name="Amulet",
    description="",
    effect=amulet,
    image=r"图片/物品/Amulet.jpg",
    discard_after_use=False,
    can_be_stolen=True
)
item.append(amulet_item)

# 创建Feather物品实例
feather_item = Items(
    name="Feather",
    description="",
    effect=feather,
    image=r"图片/物品/Feather.jpg",
    discard_after_use=True,
    can_be_stolen=True
)
item.append(feather_item)

# 创建Armor物品实例
armor_item = Items(
    name="Armor",
    description="",
    effect=armor,
    image=r"图片/物品/Armor.jpg",
    discard_after_use=False,
    can_be_stolen=True
)
item.append(armor_item)

# 创建Axe物品实例
axe_item = Items(
    name="Axe",
    description="",
    effect=axe,
    image=r"图片/物品/Axe.jpg",
    discard_after_use=False,
    can_be_stolen=True
)
item.append(axe_item)

# 创建Knife of Blood物品实例
knife_of_blood_item = Items(
    name="Knife of Blood",
    description="",
    effect=knife_of_blood,
    image=r"图片/物品/Knife of Blood.jpg",
    discard_after_use=False,
    can_be_stolen=True
)
item.append(knife_of_blood_item)

# 创建Bottle物品实例
bottle_item = Items(
    name="Bottle",
    description="",
    effect=bottle,
    image=r"图片/物品/Bottle.jpg",
    discard_after_use=True,
    can_be_stolen=True
)
item.append(bottle_item)

# 创建Dark Dice物品实例
dark_dice_item = Items(
    name="Dark Dice",
    description="",
    effect=dark_dice,
    image=r"图片/物品/Dark Dice.jpg",
    discard_after_use=False,
    can_be_stolen=True
)
item.append(dark_dice_item)

# 创建Healing Ointment物品实例
healing_ointment_item = Items(
    name="Healing Ointment",
    description="",
    effect=healing_ointment,
    image=r"图片/物品/Healing Ointment.jpg",
    discard_after_use=True,
    can_be_stolen=True
)
item.append(healing_ointment_item)

# 创建Idol物品实例
idol_item = Items(
    name="Idol",
    description="",
    effect=idol,
    image=r"图片/物品/Idol.jpg",
    discard_after_use=False,
    can_be_stolen=True
)
item.append(idol_item)

# 创建Gloves of Thief物品实例
gloves_of_thief_item = Items(
    name="Gloves of Thief",
    description="",
    effect=gloves_of_thief,
    image=r"图片/物品/Gloves of Thief.jpg",
    discard_after_use=True,
    can_be_stolen=True
)
item.append(gloves_of_thief_item)

# 创建Magic Cube物品实例
magic_cube_item = Items(
    name="Magic Cube",
    description="",
    effect=magic_cube,
    image=r"图片/物品/Magic Cube.jpg",
    discard_after_use=False,
    can_be_stolen=True
)
item.append(magic_cube_item)
