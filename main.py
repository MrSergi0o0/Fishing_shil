import pygame

pygame.init()

BLACK = (0, 0, 0)
BROWN = (165, 42, 42)

W = 750
H = 500

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("fishing shil")

image_fon = pygame.image.load("boss_fon.jpg")
image_fon = pygame.transform.scale(image_fon, (750, 500))
image_fon_rect = image_fon.get_rect(center=(W // 2, H // 2))

small_font = pygame.font.Font(None, 35)

text_for_collection = small_font.render("Collection", True, BLACK)  
    
image_table1 = pygame.image.load("table.png")

###################big_image_table = pygame.image.load("")

class Fish_creater:
    def __init__(self, name, image, kg_info, x_for_rect, y_for_rect, x_for_image, y_for_image): # info
        self.name = name
        self.image = image
        self.kg_info = kg_info
        self.x_for_rect = x_for_rect
        self.y_for_rect = y_for_rect
        self.x_for_image = x_for_image
        self.y_for_image = y_for_image
        #self.info = info

    def draw_cart(self, x_for_rect, y_for_rect, image, x_for_image, y_for_image, name, kg_info): # info
        pygame.draw.rect(screen, BROWN, (x_for_rect, y_for_rect, 75, 120))
        screen.blit(image, (x_for_image, y_for_image))
        info = small_font.render(name + " " + kg_info, True, BLACK)  
        screen.blit(info, (x_for_image + 10, y_for_image + 60))


fish1 = Fish_creater("Петя", "fish_1.png", "3 kg", 20, 10, 25, 15)

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.display.flip()

    screen.blit(image_fon, image_fon_rect)
    screen.blit(image_table1, (10, -20))
    screen.blit(text_for_collection, (30, 49))
    fish1.draw_cart(20, 10, "fish_1.png", 25, 15, "Петя", "3 kg")

# image fishs
# Механіка ловлі риби ви натискаєте кнопку і зявляється !!!перемикач!!! якщо попасти почервоному квадрату ви виграли і отримуєте рибу