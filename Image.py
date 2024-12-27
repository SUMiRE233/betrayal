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