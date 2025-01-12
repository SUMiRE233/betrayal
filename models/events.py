from config.config import currentplayerlist,playerlist
from config.config import totalomen
from models.graphics import Image

#有修改 spider,funeral
Eventlist=[]
Eventfunclist=[]
whethereventopen=[]
class Contractevent:
    def __init__(self):
        self.image=Image(r"图片\事件\contract.jpg",0.3)
        self.name="contract"
        pass
    def Contract(self,character):
        result=character.test("knowledge")
        if result<=1:character.attributechange(-1,"mind")
        elif result<=3:
            character.attributechange(-1,"mind")
            character.getcards("item")
        elif result==4:character.getcards("item")
        else:
            character.attributechange(1,"mind") 
            character.getcards("item")
contract=Contractevent()
Eventlist.append(contract)
Eventfunclist.append(Contractevent.Contract)
class Nightshadowevent:
    def __init__(self):
        self.image=Image(r"图片\事件\nightshadow.jpg",0.3)
        self.name="nightshadow"
        pass
    def Nightshadow(self,character):
        if character.test("knowledge")>=5:character.attributechange(1,"knowledge")
nightshadow=Nightshadowevent()
Eventlist.append(nightshadow)
Eventfunclist.append(Nightshadowevent.Nightshadow)
class Spiderevent:
    def __init__(self):
        self.image=Image(r"图片\事件\spider.jpg",0.3)
        self.name="spider"
        pass
    def Spider(self,character):
        result=character.test("speed")
        if result>=4:
            character.attributechange(1,"speed")
        elif result>=1:
            hurt=character.directtest(1)
            print(hurt)
            character.attributechange(-hurt,"body")
        else:
            hurt=character.directtest(2)
            print(hurt)
            character.attributechange(-hurt,"body")
spider=Spiderevent()
Eventlist.append(spider)
Eventfunclist.append(Spiderevent.Spider)
class Funeralevent:
    def __init__(self):
        self.image=Image(r"图片\事件\funeral.jpg",0.3)
        self.name="funeral"
        pass
    def Funeral(self,character):
        result=character.test("mind")
        if result>4:
            character.attributechange(1,"mind")
        elif result>=2:
            character.attributechange(-1,"mind")
        else:
            character.attributechange(-1,"mind")
            character.attributechange(-1,"strength")
            #goto地下室
funeral=Funeralevent()
Eventlist.append(funeral)
Eventfunclist.append(Funeralevent.Funeral)
class Wormevent:
    def __init__(self):
        self.image=Image(r"图片\事件\worm.jpg",0.3)
        self.name="worm"
        pass
    def Worm(self,character):
        result=character.test("mind")
        if result>=5:
            character.attributechange(1,"mind")
        elif result>=1:
            character.attributechange(-1,"mind")
        else:
            character.attributechange(-2,"mind")
worm=Wormevent()
Eventlist.append(worm)
Eventfunclist.append(Wormevent.Worm)
class Uneasynoiseevent:
    def __init__(self):
        self.image=Image(r"图片\事件\uneasynoise.jpg",0.3)
        self.name="uneasynoise"
        pass
    def Uneasynoise(self,character):
        result=character.directtest(6)
        if result>=totalomen:
            character.attributechange(1,"mind")
        else:
            hurt=character.directtest(1)
            character.attributechange(-hurt,"spirit")
uneasynoise=Uneasynoiseevent()
Eventlist.append(uneasynoise)
Eventfunclist.append(Uneasynoiseevent.Uneasynoise)
class Mirrorimageevent:
    def __init__(self):
        self.image=Image(r"图片\事件\mirrorimage.jpg",0.3)
        self.name="mirrorimage"
        pass
    def Mirrorimage(self,character):
        character.getcards("item")
mirrorimage=Mirrorimageevent()
Eventlist.append(mirrorimage)
Eventfunclist.append(Mirrorimageevent.Mirrorimage)

class Telephoneringevent:
    def __init__(self):
        self.image=Image(r"图片\事件\telephonering.jpg",0.3)
        self.name="telephonering"
        pass
    def Telephonering(self,character):
        result=character.directtest(2)
        if result==4:
            character.attributechange(1,"mind")
        elif result==3:
            character.attributechange(1,"knowledge")
        elif result>=1:
            hurt=character.directtest(1)
            character.attributechange(-hurt,"spirit")
        else:
            hurt=character.directtest(2)
            character.attributechange(-hurt,"body")
telephonering=Telephoneringevent()
Eventlist.append(telephonering)
Eventfunclist.append(Telephoneringevent.Telephonering)
class Rotevent:
    def __init__(self):
        self.image=Image(r"图片\事件\rot.jpg",0.3)
        self.name="rot"
        pass
    def Rot(self,character):
        result=character.test("mind")
        if result>=5:
            character.attributechange(1,"mind")
        elif result>=2:
            character.attributechange(-1,"strength")
        elif result==1:
            character.attributechange(-1,"strength")
            character.attributechange(-1,"speed")
        else:
            character.attributechange(-character.strength_pos,"strength")
            character.attributechange(-character.speed_pos,"speed")
            character.attributechange(-character.mind_pos,"mind")
            character.attributechange(-character.knowledge_pos,"knowledge")
rot=Rotevent()
Eventlist.append(rot)
Eventfunclist.append(Rotevent.Rot)
class Stickyevent:
    def __init__(self):
        self.image=Image(r"图片\事件\sticky.jpg",0.3)
        self.name="sticky"
        pass
    def Sticky(self,character):
        result=character.test("speed")
        if result>=4:
            character.attributechange(1,"speed")
        elif result>=1:
            character.attributechange(-1,"strength")
        else:
            character.attributechange(-1,"strength")
            character.attributechange(-1,"speed")
sticky=Stickyevent()
Eventlist.append(sticky)
Eventfunclist.append(Stickyevent.Sticky)
class Soundevent:
    def __init__(self):
        self.image=Image(r"图片\事件\sound.jpg",0.3)
        self.name="sound"
        pass
    def Sound(self,character):
        result=character.test("knowledge")
        if result>=4:
            character.getcards("item")
sound=Soundevent()
Eventlist.append(sound)
Eventfunclist.append(Soundevent.Sound)
class Acupunctureevent:
    def __init__(self):
        self.image=Image(r"图片\事件\acupuncture.jpg",0.3)
        self.name="acupuncture"
        pass
    def Acupuncture(self,character):
        result=character.test("strength")
        if result>=5:
            character.attributechange(1,"strength")
            character.attributechange(1,"speed")
            character.attributechange(1,"mind")
        elif result>=3:
            character.attributechange(1,"strength")
            character.attributechange(1,"speed")
        else:
            character.attributechange(-1,"strength")
            character.attributechange(-1,"speed")
acupuncture=Acupunctureevent()
Eventlist.append(acupuncture)
Eventfunclist.append(Acupunctureevent.Acupuncture)
class Gardenerevent:
    def __init__(self):
        self.image=Image(r"图片\事件\gardener.jpg",0.3)
        self.name="gardener"
        pass
    def Gardener(self,character):
        result=character.test("knowledge")
        if result>=4:
            character.getcards("item")
        else:
            numenemy=character.directtest(4)
            numself=character.test("strength")
            if numenemy>numself:
                character.attributechange(numself-numenemy,"body")
gardener=Gardenerevent()
Eventlist.append(gardener)
Eventfunclist.append(Gardenerevent.Gardener)
class Angrycreaturesevent:
    def __init__(self):
        self.image=Image(r"图片\事件\angrycreature.jpg",0.3)
        self.name="angrycreature"
        pass
    def Angrycreatures(self,character):
        result=character.test("speed")
        if result>=5:
            character.attributechange(1,"speed")
        elif result>=2:
            hurt=character.directtest(1)
            character.attributechange(-hurt,"spirit")
        else:
            hurt=character.directtest(1)
            character.attributechange(-hurt,"spirit")
            hurt=character.directtest(1)
            character.attributechange(-hurt,"body")
angrycreatures=Angrycreaturesevent()
Eventlist.append(angrycreatures)
Eventfunclist.append(Angrycreaturesevent.Angrycreatures)
class Mutantpetsevent:
    def __init__(self):
        self.image=Image(r"图片\事件\mutantpets.jpg",0.3)
        self.name="mutantpets"
        pass
    def Mutantpets(self,character):
        result=character.test("speed")
        if result>=4:
            character.attributechange(1,"speed")
            character.attributechange(1,"mind")
        else:
            character.attributechange(-1,"body")
mutantpets=Mutantpetsevent()
Eventlist.append(mutantpets)
Eventfunclist.append(Mutantpetsevent.Mutantpets)
class Screamevent:
    def __init__(self):
        self.image=Image(r"图片\事件\scream.jpg",0.3)
        self.name="scream"
        pass
    def Scream(self):
        for i in currentplayerlist:
            result=playerlist[i].test("mind")
            if result<=3 and result>0:
                hurt=playerlist[i].directtest(1)
                playerlist[i].attributechange(-hurt,"spirit")
            elif result==0:
                hurt=playerlist[i].directtest(2)
                playerlist[i].attributechange(-hurt,"spirit")
scream=Screamevent()
Eventlist.append(scream)
Eventfunclist.append(Screamevent.Scream)
class Silenceevent:
    def __init__(self):
        self.image=Image(r"图片\事件\silence.jpg",0.3)
        self.name="silence"
        pass
    def Silence(self):
        for i in currentplayerlist:
            if playerlist[i].position[0]==0:
                result=playerlist[i].test("mind")
                if result<=3 and result>=1:
                    hurt=playerlist[i].directtest(1)
                    playerlist[i].attributechange(-hurt,"spirit")
                elif result==0:
                    hurt=playerlist[i].directtest(2)
                    playerlist[i].attributechange(-hurt,"spirit")
silence=Silenceevent()
Eventlist.append(silence)
Eventfunclist.append(Silenceevent.Silence)
whethereventopen=[0 for i in range(len(Eventlist))]
print(len(Eventlist)) 
