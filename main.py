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


class FishCreater(pygame.sprite.Sprite):
    def __init__(self, name, image, kg_info, x, y, w, h): # info
        super().__init__()
        self.name = name
        self.kg_info = kg_info
        self.image = pygame.transform.scale(
            pygame.image.load(image),
            (w, h)
        )
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self): # draw
        pygame.draw.rect(screen, BROWN, (self.rect.x, self.rect.y, 75, 120))
        screen.blit(self.image, (self.rect.x, self.rect.y))
        info = small_font.render(self.name + " " + self.kg_info, True, BLACK)
        screen.blit(info, (self.rect.x + 10, self.rect.y + 60))


fish1 = FishCreater("Петя", "fish_1.png", "3 kg", 20, 10, 25, 15)


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.display.flip()

    screen.blit(image_fon, image_fon_rect)
    screen.blit(image_table1, (10, -20))
    screen.blit(text_for_collection, (30, 49))
    fish1.draw()

# image fishs
# Механіка ловлі риби ви натискаєте кнопку і зявляється !!!перемикач!!! якщо попасти почервоному квадрату ви виграли і отримуєте рибу
