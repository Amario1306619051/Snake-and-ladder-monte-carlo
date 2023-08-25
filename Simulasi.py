# Import a library of functions called 'pygame'
import pygame
import random
import matplotlib.pyplot as plt

pygame.init()

black = [ 0, 0, 0]
white = [255,255,255]
blue = [0,0,255]


screen=pygame.display.set_mode([400,500])
pygame.display.set_caption("Snow Animation")

# Create an empty array
star_list=[]
intensity = 600
# Loop 50 times and add a star in a random x,y position
for i in range(intensity):
    x = random.randint(0,400)
    y = random.randint(0,400)
    star_list.append([x,y])
    
vx = 1
clock = pygame.time.Clock()
titik = 0
ll = 0
if intensity == 50:
    m = 0.0000000186
if intensity == 300:
    m = 0.000000004
if intensity == 600:
    m = 0.0000000045
g = 9.8
h = 2.5

energi = 0
hewan = 0
#Loop until the user clicks the close button.
himpunan = []
done=False
while done==False:

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(white)
    for i in range(len(star_list)):
        pygame.draw.circle(screen,blue,star_list[i],1)
        star_list[i][1] += vx
        
        if star_list[i][1] > 500:
            x=random.randrange(0,400)
            y = 0
            star_list[i][0] = x
            star_list[i][1] = y
            vx = 1
        if (star_list[i][0] > 150 and star_list[i][0] < 225) and star_list[i][1] > 475:
            x=random.randrange(0,400)
            y = 0
            star_list[i][0] = x
            star_list[i][1] = y
            vx = 1
            hewan = titik
            titik += 1
            energi += m*g*h
        

        vx += 1
    himpunan.append(energi)
    if ll == 300:
        done = True
    ll += 1
    pygame.draw.rect(screen,black,[150,475,75,25])
    pygame.display.flip()
    clock.tick(30)
pygame.quit ()

def fungsi(x):
    if intensity == 50:
        f = 0.0000001448*x - 0.000001871
    if intensity == 300:
        f = 0.0000001731*x - 0.0000006671
    if intensity == 600:
        f = 0.000000394*x - 0.00000396
    return f

waktu = []
hasil = []
for i in range(301):
    waktu.append(i)
    hasil.append(fungsi(i))
plt.plot(waktu,hasil)
plt.scatter(waktu,himpunan,c = 'red')
plt.show()