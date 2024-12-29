startscript=0 #是否已经作祟
totalomen=0 #统计目前预兆个数
Omenlist=[]
Omenfunclist=[]
class Bookomen:
    def Book(self,character):
        character.attributechange(2,"knowledge")
book=Bookomen()
Omenfunclist.append(Bookomen.Book)
Omenlist.append(book)
class Girlomen:
    def Girl(self,character):
        character.attributechange(1,"knowledge")
        character.attributechange(1,"mind")
girl=Girlomen()
Omenfunclist.append(Girlomen.Girl)
Omenlist.append(girl)
class Dogomen:
    def Dog(self,character):
        character.attributechange(1,"strength")
        character.attributechange(1,"mind")
dog=Dogomen()
Omenfunclist.append(Dogomen.Dog)
Omenlist.append(dog)
class Madmanomen:
    def Madman(self,character):
        character.attributechange(2,"strength")
        character.attributechange(-1,"mind")
madman=Madmanomen()
Omenfunclist.append(Madmanomen.Madman)
Omenlist.append(madman)
class Holysymbolomen:
    def Holysymbol(self,character):
        character.attributechange(2,"mind")
holysymbol=Holysymbolomen()
Omenfunclist.append(Holysymbolomen.Holysymbol)
Omenlist.append(holysymbol)
class Biteomen:
    def Bite(self,character):
        numenemy=character.directtest(4)
        numself=character.test("strength")
        print("numenemy:%d"%numenemy)
        print("numself:%d"%numself)
        if numenemy>numself:
            character.attributechange(numself-numenemy,"body")
bite=Biteomen()
Omenfunclist.append(Biteomen.Bite)
Omenlist.append(bite)
class Ringomen:
    def Ring(self,character,enemy): #能力攻击  value:该能力属性值
        numself=character.test("mind")
        numenemy=enemy.test("mind")
        if numself>numenemy:
            enemy.attributechange(numenemy-numself,"spirit")
        elif numself<numenemy:
            character.attributechange(numself-numenemy,"spirit")
ring=Ringomen()
Omenfunclist.append(Ringomen.Ring)
Omenlist.append(ring)
class Spearomen:
    def Spear(self,attacker,enemy): #能力攻击 
        numself=attacker.test("strength")
        numself+=attacker.directtest(2)
        numenemy=enemy.test("strength")
        print(numself)
        print(numenemy)
        if numself>numenemy:
            enemy.attributechange(numenemy-numself,"body")
        elif numself<numenemy:
            self.attributechange(numself-numenemy,"body")
spear=Spearomen()
Omenfunclist.append(Spearomen.Spear)
Omenlist.append(spear)
