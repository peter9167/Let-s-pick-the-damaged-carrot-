import pygame as pg

pg.init()

화면가로길이, 화면세로길이 = (980, 940)
화면 = pg.display.set_mode([화면가로길이, 화면세로길이])
pg.display.set_caption('상한 당근을 싱싱한 당근으로! By 인피니티 스톤')

#글꼴설정
글꼴 = pg.font.SysFont('malgungothic', 35)

#이미지 초기화
배경이미지 = pg.image.load('img/당근_배경.png')
배경이미지 = pg.transform.scale(배경이미지, (화면가로길이, 화면세로길이))
화면.blit(배경이미지, (0, 0))

# 시간바
시간바 = pg.image.load('img/시간바.png')
시간바 = pg.transform.scale(시간바, (400, 100))
화면.blit(시간바, (520, 20))

# 당근
당근 = pg.image.load('img/당근.png')
당근 = pg.transform.scale(당근, (130, 220))
# 화면.blit(당근, (200, 200))

# 상한당근
상한당근 = pg.image.load('img/상한당근.png')
상한당근 = pg.transform.scale(상한당근, (130, 220))
# 화면.blit(상한당근, (300, 250))

pg.display.update()

while True:
    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            pg.display.quit()