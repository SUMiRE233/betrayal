#有修改 spider,funeral
Eventlist=[]
Eventfunclist=[]
whethereventopen=[]
class Contractevent:
    def __init__(self):
        #self.image=Image(r"图片\事件\contract.jpg",0.75)
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
    def Nightshadow(self,character):
        if character.test("knowledge")>=5:character.attributechange(1,"knowledge")
nightshadow=Nightshadowevent()
Eventlist.append(nightshadow)
Eventfunclist.append(Nightshadowevent.Nightshadow)
class Spiderevent:
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