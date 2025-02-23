import pygame

pygame.init()

BLACK = (0, 0, 0)
BROWN = (165, 42, 42)
RED = (255, 0 , 0)

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
table_rect = image_table1.get_rect(topleft=(10, -20))

big_image_table = pygame.image.load("big_table.png")

draw_big_table = False

btn_exit = pygame.Rect(670, 85, 50, 50)

class FishCreater(pygame.sprite.Sprite):
    def __init__(self, name, image, kg_info, x, y, w, h):
        super().__init__()
        self.name = name
        self.kg_info = kg_info
        self.image = pygame.transform.scale(pygame.image.load(image),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw_image(self):
        screen.blit(self.image, (self.rect.x - 10, self.rect.y))

    def draw_text(self):
        info1 = small_font.render(self.name, True, BLACK)
        screen.blit(info1, (self.rect.x + 10, self.rect.y + 55))
        info2 = small_font.render(self.kg_info, True, BLACK)
        screen.blit(info2, (self.rect.x + 10, self.rect.y + 75))

fish1 = FishCreater("Петя", "fish_1.png", "3 kg", 75, 130, 150, 70)

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        if table_rect.collidepoint(event.pos):
            draw_big_table = True

    if event.type == pygame.MOUSEBUTTONDOWN:
        if btn_exit.collidepoint(event.pos):
            draw_big_table = False

    if draw_big_table == True:
        screen.blit(big_image_table, (20, -75))
        pygame.draw.rect(screen, BROWN, (75, 130, 130, 175))
        fish1.draw_image()
        fish1.draw_text()
        pygame.draw.rect(screen, RED, btn_exit)

    pygame.display.flip()
    screen.blit(image_table1, table_rect.topleft)
    screen.blit(image_fon, image_fon_rect)
    screen.blit(image_table1, (10, -20))
    screen.blit(text_for_collection, (30, 49))

# Замість червоного квадрата додать чорний хресік
# Normal image for fishs
# Механіка ловлі риби ви натискаєте кнопку і зявляється !!!перемикач!!! якщо попасти почервоному квадрату ви виграли і отримуєте рибу