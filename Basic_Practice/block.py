import pygame as pg

def main():
    pg.init()
    wn = pg.display.set_mode((500, 500))

    pg.display.set_caption('Block')

    x = 250
    y = 250
    width = 20
    height = 20
    speed = 5

    run = True

    while run:
        pg.time.delay(10)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            x -= speed
        if keys[pg.K_RIGHT]:
            x += speed
        if keys[pg.K_DOWN]:
            y += speed
        if keys[pg.K_UP]:
            y -= speed

        wn.fill((0, 0, 0))
        pg.draw.rect(wn, (255, 0, 0), (x, y, width, height))
        pg.display.update()
    
    pg.quit()


if __name__ == '__main__':
    main()