import pygame as pg # pygame 모듈 import
import random # rendom 모듈 import

def 당근초기화():
    global 랜덤당근, 랜덤당근좌표 # global type 랜덤당근, 랜덤당근좌표 변수 선언
    랜덤당근 = [당근] * 4 + [상한당근] * 5 # 랜덤당근 = 9 ([1] * 4 + [1] * 5)
    랜덤당근좌표 = [(170 + x * 260, 190 + y * 220)for x in range(3) for y in range(3)] 
    # 랜덤당근좌표에 게임판 크기에 맞는 좌표 설정(위와 같은 식으로 당근 랜덤 위치 설정)
    # 리스트 컴프리헨션 [ <표현,식> for <변수명> in <시퀀스> ]
    random.shuffle(랜덤당근) # shuffle 시퀀스를 뒤죽박죽으로 섞어놓는 함수 - shuffle(시퀀스)

pg.init() # pg(pygame) 초기화 (init)

화면가로길이, 화면세로길이 = (980, 940)
화면 = pg.display.set_mode([화면가로길이, 화면세로길이]) # pygame으로 생성할 창의 크기를 설정
pg.display.set_caption('상한 당근을 싱싱한 당근으로! By 인피니티 스톤') # GUI 창이 켜질 때, 창 이름을 설정 - set_caption('이름')

#글꼴설정
글꼴 = pg.font.SysFont('malgungothic', 35)

#이미지 초기화
배경이미지 = pg.image.load('img/당근_배경.png') #해당 주소에 있는 이미지 로드(호출). 이 과정에서 Surface라는 파이게임에서 사용되는 이미지를 표현할 수 있는 객체로 반환.
배경이미지 = pg.transform.scale(배경이미지, (화면가로길이, 화면세로길이)) #새 해상도로 크기 조정 - scale(Surface, (width, height)
화면.blit(배경이미지, (0, 0))

# 시간바
시간바 = pg.image.load('img/시간바.png') #해당 주소에 있는 이미지 로드(호출). 이 과정에서 Surface라는 파이게임에서 사용되는 이미지를 표현할 수 있는 객체로 반환.
시간바 = pg.transform.scale(시간바, (400, 100)) #새 해상도로 크기 조정 - scale(Surface, (width, height)
화면.blit(시간바, (520, 20))

# 당근
당근 = pg.image.load('img/당근.png') #해당 주소에 있는 이미지 로드(호출). 이 과정에서 Surface라는 파이게임에서 사용되는 이미지를 표현할 수 있는 객체로 반환.
당근 = pg.transform.scale(당근, (130, 220)) #새 해상도로 크기 조정 - scale(Surface, (width, height)

# 상한당근
상한당근 = pg.image.load('img/상한당근.png') #해당 주소에 있는 이미지 로드(호출). 이 과정에서 Surface라는 파이게임에서 사용되는 이미지를 표현할 수 있는 객체로 반환.
상한당근 = pg.transform.scale(상한당근, (130, 220)) #새 해상도로 크기 조정 - scale(Surface, (width, height)

pg.display.update() #화면 업데이트 (display update)

당근초기화()


경과시간 = 0
당근생성시간 = 0
당근인덱스 = 0
시계 = pg.time.Clock()
현재챕터 = 1
최종챕터 = 3

while True:
    if 현재챕터 <= 최종챕터:
        화면.blit(배경이미지, (0, 0))
        화면.blit(시간바, (520, 20))

        흐른시간 = 시계.tick(60) / 1000
        경과시간 += 흐른시간

        if 경과시간 <= 60:
            시간문자열 = f'{round(경과시간, 1)} 초'
        else:
            시간문자열 = f'{int(경과시간 // 60)} 분 {int(경과시간 % 60)}초'

        시간 = 글꼴.render(시간문자열, True, (0, 0, 0))
        화면.blit(시간, (700, 50))

        챕터글자 = 글꼴.render(f'챕터 : {현재챕터} / {최종챕터}', True, (255, 255, 255))
        화면.blit(챕터글자, (80, 20))

        당근글자 = 글꼴.render(f'남은 상한당근 갯수 : {len(랜덤당근) - 랜덤당근.count(당근)}개', True, (255, 255, 255))
        화면.blit(당근글자, (80, 90))

        당근생성시간 += 흐른시간
        if 당근생성시간 >= 1:
            당근생성시간 = 0
            당근인덱스 = random.randrange(len(랜덤당근))

        현재당근 = 화면.blit(랜덤당근[당근인덱스], 랜덤당근좌표[당근인덱스])
    else:
        화면.fill((255, 255, 255))
        종료멘트 = 글꼴.render(f'경과시간은 {경과시간//60}분 {round(경과시간%60)}초입니다.', True, (0, 0, 0))
        화면.blit(종료멘트, (화면가로길이 / 2 - 230, 화면세로길이 / 2 - 80))
    pg.display.update()

    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            pg.display.quit()
        elif 이벤트.type == pg.MOUSEBUTTONDOWN:
            클릭위치 = pg.mouse.get_pos()
            if 당근인덱스 != -1 and 현재당근.collidepoint(클릭위치):
                if 랜덤당근[당근인덱스] == 상한당근:
                    랜덤당근[당근인덱스] = 당근

                    if len(랜덤당근) - 랜덤당근.count(당근) == 0:
                        현재챕터 += 1
                        당근초기화()