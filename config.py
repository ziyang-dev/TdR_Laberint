class Color:
    background=         (245, 247, 250)     #black
    wall=               (24, 28, 36)        #white
    line=               (50, 220, 120)      #fluorescent green
    error=              (255, 0, 0)         #fluorescent red
    exit=               (255, 160, 170)     #light red
    star=               (140, 210, 255)     #light gleu


    gren=               (180, 245, 205)     #light green
    yellow=             (255, 230, 150)     #light yellow
    blue=               (40, 60, 95)        #deep blue
    purple=             (185, 130, 255)     #purple


class Maze_size:
    small=              5
    medium=             25
    large=              50
    extra=              500

#research
direction=((1,0), (0,1), (-1,0), (0,-1))
start_pos=(1,1)
exit_pos=(-2,-2)

#main
windowsCaptionText="Debug"  #Nom de finestres
windows_size=600 # tamany de la pantalla, quadrat

with_auxiliary_line=True

animation_type="off"  #["off","click","atuo"]

ticks=30
