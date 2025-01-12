import pygame

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
        self.center_x=center_x
        self.center_y=center_y
        self.upperleft_x = self.center_x - self.img_width_scaled / 2
        self.upperleft_y = self.center_y - self.img_height_scaled / 2
        surface.blit(self.image_scaled, (self.upperleft_x, self.upperleft_y))
    def scalechange(self,surface,changescale):
        self.size_scaled = self.img_width * changescale, self.img_height * changescale
        self.image_scaled = pygame.transform.smoothscale(self.picture, self.size_scaled)
        self.img_width_scaled = self.image_scaled.get_width()
        self.img_height_scaled = self.image_scaled.get_height()
        self.draw(surface,self.center_x, self.center_y)
        
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
        pygame.font.init()
        font = pygame.font.Font(font_type, self.font_size)
        self.text_image = font.render(self.text, True, self.text_color).convert_alpha()
 
        self.text_width = self.text_image.get_width()
        self.text_height = self.text_image.get_height()
        
 
    def draw(self, surface: pygame.Surface, center_x, center_y):
        """
        surface: 文本放置的表面
        center_x, center_y: 文本放置在表面的<中心坐标>
        """
        self.upperleft_x = center_x - self.text_width / 2
        self.upperleft_y = center_y - self.text_height / 2
        surface.blit(self.text_image, (self.upperleft_x,self.upperleft_y))



class ButtonText(Text):
    def __init__(self, text: str, text_color: Color, font_type: str, font_size: int):
        super().__init__(text, text_color, font_type, font_size)
        self.rect = self.text_image.get_rect()
        self.whether=0
 
    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y
    def handle_event(self):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            return True
        return False

class Button(Image):
    def __init__(self, img_name: str, ratio=0.4):
        super().__init__(img_name, ratio)
        self.rect = self.image_scaled.get_rect()
        self.scalenow = 0

    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y
 
    def handle_event(self):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            return True
        return False