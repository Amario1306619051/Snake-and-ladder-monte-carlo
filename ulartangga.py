import pygame,sys
from pygame.locals import*

pygame.init()
#Menggunakan fungsi clock pada pygame
clock = pygame.time.Clock()

#Mengatur ukuran layar menjadi 500 x 500 pixel
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Snake and ladder')
#mendefinisikan warna dalam kode RGB
hitam = (0,0,0)
biru = (0,0,255)
putih = (255,255,255)
hijau = (0,255,0)
merah = (255,0,0)

#Menginisiasikan random Number
k = 65
q = 2*(31) - 1
p = 7**5
himpunan1 = [1,467]
n = 1


screen.fill(merah)# mengatur warna dasar warna merah

#menggambar objek kotak dan garis pada  ular tangga
pygame.draw.rect(screen,biru,(400,75,75,300))#kotak dari 1 - 4
for i in range(75,450,75):#Menggambar garis tepi
    pygame.draw.line(screen,hitam,(400,i),(475,i),2)
pygame.draw.rect(screen,biru,(175,150,225,75))#kotak dari 5 - 7
for i in range(175,401,75):
    pygame.draw.line(screen,hitam,(i,225-75),(i,300-75),2)#garis
pygame.draw.line(screen,hitam,(175,150),(400,150),2)
pygame.draw.line(screen,hitam,(175,225),(400,225),2)
pygame.draw.line(screen,hitam,(475,75),(475,375),2)
pygame.draw.line(screen,hitam,(400,75),(400,375),2)
pygame.draw.rect(screen,biru,(175,0,75,225))#kotak dari 7-9
pygame.draw.line(screen,hitam,(175,0),(175,225),2)
pygame.draw.line(screen,hitam,(250,0),(250,225),2)
for i in range(0,151,75):
     pygame.draw.line(screen,hitam,(175,i),(250,i),2)
     
#untuk menampilkan urutan
himpunan = ['1','2','3','4','5','6','7','8','9']
font1 = pygame.font.Font(None,30)#ukuran tulisan 1
font2 = pygame.font.Font(None,20)#ukuran tulisan 2

#menampilakn urutan
s = 0
for i in range(0,4):#urutan 1 sampai 4
    text1 = font1.render(himpunan[i],True,putih)
    screen.blit(text1,[460,305-s])
    s += 75
s = 75
for i in range(4,7):#urutan 5 samapai 7
    text1 = font1.render(himpunan[i],True,putih)
    screen.blit(text1,[460-s,155])
    s += 75
s = 75
for i in range(7,9):#urutan 7 sampai 9
    text1 = font1.render(himpunan[i],True,putih)
    screen.blit(text1,[240,155-s])
    s += 75

#menggambar tangga 
pygame.draw.line(screen,putih,(400,254),(310,225),4)
pygame.draw.line(screen,putih,(400,275),(300,240),4)
for i in range(0,7):
    pygame.draw.line(screen,putih,(390-15*i,270-5*i),(400-15*i,250-5*i),4)
text2 = font2.render('Finish',True,putih)
screen.blit(text2,[180,50])

#pygame.draw.line(screen,putih,(0,490),(500,490),4)
#menginisiasikan kondisi awal
bb = 0 #urutan awal listing
posisi = 1 #posisi awal 
lokasi = 1 #posisi akhir
x1 = 420 #lokasi awal dalam sumbu x
y1 = 320 #lokasi akhir dalam sumbu y
#list gambar dadu
himpunan3 = ['dadu.jpg','dadu1.jpg','dadu2.jpg','dadu3.jpg','dadu4.png','dadu5.jpg','dadu6.png']
pridan = 0

#memproses pygame
while True:
    
    #nmemanggil pion 
    gambar = pygame.image.load("boruto.jpg")
    gambar = pygame.transform.scale(gambar,(40,40))
    screen.blit(gambar,(x1,y1))
    for event in pygame.event.get():
        if event.type == QUIT:  
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:#apabila klik mouse
            k = p*k % q #random
            r = k/q
            y = 6*r + 1
            s = int(y) #dibulatkan
            k += himpunan1[bb]*himpunan1[bb]
            n += 1
            himpunan1.append(n)
            bb += 1
            pygame.draw.rect(screen,merah,(0,300,200,300))
            lokasi += s
            #memanggil gambar dadu berdasarkan list
            gambar2 = pygame.image.load(himpunan3[s])
            gambar2 = pygame.transform.scale(gambar2,(40,40))
            screen.blit(gambar2,(50,400))

    print(posisi,lokasi,pridan)
    pygame.draw.rect(screen,biru,(x1,y1,40,40))
    font1 = pygame.font.Font(None,50)
    if posisi > 9:
        pridan += 1
    #koordinat dari 1 sampai 4
    for i in range(1,5):
        if posisi == i and lokasi != 2:
            x1 = 420
            y1 = 320 - 75*(i-1)
            #apabila mendapat dadu dengan jumlah satu
        if posisi == i and lokasi == 2:
            clock.tick(0.1)
            x1 = 420
            y1 = 320 - 75
    #koordinat dari 5 sampai 7
    for i in range(5,8):
        if posisi == i:
            x1 = 345 - (i-5)*75
            y1 = 170
    #koordinat 7 sampai 9            
    for i in range(8,10):
        if posisi == i:
            x1 = 195
            y1 = 95 - (i-8)*75
    #untuk penetrasi 7 - 9
    if (posisi // 2)%2 == 0 and pridan > 0 and (posisi%2) != 0:
        x1 = 195
        y1 = 20
    if (posisi // 2)%2 != 0 and  pridan > 0:
        x1 = 195
        y1 = 170
    if (posisi)%2 == 0  and pridan > 0:
        x1 = 195
        y1 = 95
 

    if posisi < lokasi:
        posisi += 1
    if lokasi == 2:
        posisi = 6
        lokasi = 6
    clock.tick(1)#fps
    gambar = pygame.image.load("boruto.jpg")
    gambar = pygame.transform.scale(gambar,(40,40))
    screen.blit(gambar,(x1,y1))
    pygame.display.update()
sys.quit()