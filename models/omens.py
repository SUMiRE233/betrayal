from models.graphics import Image

Omenlist=[]
Omenfunclist=[]
class Bookomen:
    def __init__(self, image):
        self.image = Image(img_name = image)
    def Book(self,character):
        character.attributechange(2,"knowledge")
book=Bookomen(image = r"图片/预兆/book.jpg")
Omenfunclist.append(Bookomen.Book)
Omenlist.append(book)
class Girlomen:
    def __init__(self, image):
        self.image = Image(img_name = image)
    def Girl(self,character):
        character.attributechange(1,"knowledge")
        character.attributechange(1,"mind")
girl=Girlomen(image = r"图片/预兆/girl.jpg")
Omenfunclist.append(Girlomen.Girl)
Omenlist.append(girl)
class Dogomen:
    def __init__(self, image):
        self.image = Image(img_name = image)
    def Dog(self,character):
        character.attributechange(1,"strength")
        character.attributechange(1,"mind")
dog=Dogomen(image = r"图片/预兆/dog.jpg")
Omenfunclist.append(Dogomen.Dog)
Omenlist.append(dog)
class Madmanomen:
    def __init__(self, image):
        self.image = Image(img_name = image)
    def Madman(self,character):
        character.attributechange(2,"strength")
        character.attributechange(-1,"mind")
madman=Madmanomen(image = r"图片/预兆/madman.jpg")
Omenfunclist.append(Madmanomen.Madman)
Omenlist.append(madman)
class Holysymbolomen:
    def __init__(self, image):
        self.image = Image(img_name = image)
    def Holysymbol(self,character):
        character.attributechange(2,"mind")
holysymbol=Holysymbolomen(image = r"图片/预兆/holysymbol.jpg")
Omenfunclist.append(Holysymbolomen.Holysymbol)
Omenlist.append(holysymbol)
class Biteomen:
    def __init__(self, image):
        self.image = Image(img_name = image)
    def Bite(self,character):
        numenemy=character.directtest(4)
        numself=character.test("strength")
        print("numenemy:%d"%numenemy)
        print("numself:%d"%numself)
        if numenemy>numself:
            character.attributechange(numself-numenemy,"body")
bite=Biteomen(image = r"图片/预兆/bite.jpg")
Omenfunclist.append(Biteomen.Bite)
Omenlist.append(bite)
class Ringomen:
    def __init__(self, image):
        self.image = Image(img_name = image)
ring=Ringomen(image = r"图片/预兆/ring.jpg")
Omenlist.append(ring)
class Spearomen:
    def __init__(self, image):
        self.image = Image(img_name = image)
spear=Spearomen(image = r"图片/预兆/spear.jpg")
Omenlist.append(spear)

whetheromenopen=[0 for i in range(len(Omenlist))]