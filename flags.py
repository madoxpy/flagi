from pygame import *
from random import choice

WIDTH, HEIGHT = 800,600

init()
screen = display.set_mode((WIDTH,HEIGHT))
clock = time.Clock()
Font=font.SysFont("arial",16)

tryb = "menu"

class Przycisk(object):
    def __init__(self, napis, x, y, szer, wys):
        self.napis = napis
        self.x = x
        self.y = y
        self.szer = szer
        self.wys = wys
        self.color = (100,100,100)
    def rysuj(self):
        draw.rect(screen, self.color,Rect(self.x,self.y,self.szer, self.wys),0)
        text = Font.render(self.napis,True,(0,0,0))
        screen.blit(text,(self.x+self.szer//2-4*len(self.napis),self.y+15))

    def wew(self,x,y):
        if self.x<x<self.x+self.szer and self.y<y<self.y+self.wys:
            return True
        else:
            return False

def losuj(tab):
    return choice(tab)

def clean(napis):
    napis = napis[0:-4]
    napis = napis.replace("_"," ")
    return napis


peasy = Przycisk("Easy",300,150,200,50)
pmedium = Przycisk("Medium",300,300,200,50)
phard = Przycisk("Hard",300,450,200,50)

punkty = 0
pytan = 0

panstwa = []

end = False
while not end:
    screen.fill((0, 0, 0))
    for z in event.get():
        if z.type == QUIT:
            end = True
    if tryb == "menu":
        peasy.rysuj()
        pmedium.rysuj()
        phard.rysuj()
        if mouse.get_pressed()[0]:
            x, y = mouse.get_pos()
            if peasy.wew(x,y):
                tryb="easy"
            if pmedium.wew(x,y):
                tryb="medium"
            if phard.wew(x,y):
                tryb="hard"
            if tryb != "menu":
                plik=open(tryb+"/lista.txt")
                for linia in plik:
                    panstwa.append(linia[0:-1])
                odp = [losuj(panstwa)]
                while len(odp)<4:
                    n = losuj(panstwa)
                    if n not in odp:
                        odp.append(n)
                pop = choice(odp)
                p1 = Przycisk(clean(odp[0]),100,400,200,50)
                p2 = Przycisk(clean(odp[1]),500,400,200,50)
                p3 = Przycisk(clean(odp[2]),100,500,200,50)
                p4 = Przycisk(clean(odp[3]),500,500,200,50)
                nowa = Przycisk("Reset",10,10,50,50)
                nasza = ""
                flaga = image.load(tryb+"/"+pop)
                pop = clean(pop)
                flaga=transform.scale(flaga,(600,250))
                screen.blit(flaga,(100,50))
    else:
        text = Font.render(str(punkty)+"/"+str(pytan),True,(255,255,255))
        screen.blit(text,(750,10))
        p1.rysuj()
        p2.rysuj()
        p3.rysuj()
        p4.rysuj()
        nowa.rysuj()
        screen.blit(flaga,(100,50))
        if mouse.get_pressed()[0]:
            x,y = mouse.get_pos()
            if p1.wew(x,y):
                nasza = p1.napis
                if nasza == pop:
                    p1.color=(0,255,0)
                else:
                    p1.color=(255,0,0)
                p1.rysuj()
            if p2.wew(x,y):
                nasza = p2.napis
                if nasza == pop:
                    p2.color=(0,255,0)
                else:
                    p2.color=(255,0,0)
                p2.rysuj()
            if p3.wew(x,y):
                nasza = p3.napis
                if nasza == pop:
                    p3.color=(0,255,0)
                else:
                    p3.color=(255,0,0)
                p3.rysuj()
            if p4.wew(x,y):
                nasza = p4.napis
                if nasza == pop:
                    p4.color=(0,255,0)
                else:
                    p4.color=(255,0,0)
                p4.rysuj()
            if nasza != "":
                if nasza == pop:
                    print("OK")
                    punkty += 1
                else:
                    print("Fail")
                pytan += 1
                display.flip()
                time.wait(1000)
                odp = [losuj(panstwa)]
                while len(odp)<4:
                    n = losuj(panstwa)
                    if n not in odp:
                        odp.append(n)
                pop = choice(odp)
                p1 = Przycisk(clean(odp[0]),100,400,200,50)
                p2 = Przycisk(clean(odp[1]),500,400,200,50)
                p3 = Przycisk(clean(odp[2]),100,500,200,50)
                p4 = Przycisk(clean(odp[3]),500,500,200,50)
                nasza = ""
                flaga = image.load(tryb+"/"+pop)
                pop = clean(pop)
                flaga=transform.scale(flaga,(600,250))
                screen.blit(flaga,(100,50))
            if nowa.wew(x,y):
                tryb = "menu"
                punkty = 0
                pytan = 0
                panstwa = []

    display.flip()
    clock.tick(25)



