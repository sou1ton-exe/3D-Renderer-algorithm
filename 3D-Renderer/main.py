"    @Telegram Channel: https://t.me/s_lowcode_w                                                          "
"    @Author's support: https://dalink.to/sou1toon                                                        "
"    |----------------------------------------- by sou1toon ---------------------------------------------|"
"    |                                                                                                   |"                                                                                                   
"    |       ██████╗░██████╗░░░░░██████╗░███████╗███╗░░██╗██████╗░███████╗██████╗░███████╗██████╗░       |"
"    |       ╚════██╗██╔══██╗░░░░██╔══██╗██╔════╝████╗░██║██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗       |"
"    |       ░█████╔╝██║░░██║░░░░██████╔╝█████╗░░██╔██╗██║██║░░██║█████╗░░██████╔╝█████╗░░██████╔╝       |"
"    |       ░╚═══██╗██║░░██║░░░░██╔══██╗██╔══╝░░██║╚████║██║░░██║██╔══╝░░██╔══██╗██╔══╝░░██╔══██╗       |"
"    |       ██████╔╝██████╔╝░░░░██║░░██║███████╗██║░╚███║██████╔╝███████╗██║░░██║███████╗██║░░██║       |"
"    |       ╚═════╝░╚═════╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝       |"
"    |                                                                                                   |"
"    |------------------------------------------- v.1.0.0 -----------------------------------------------|"
"    Algorithm for rendering a 3D model using the pygame module.                                          "
"                                                                                                         "
"                                                                                                         "
"    Open source code to explore                                                                          "





from pygame import *
import read_current_model
from vector import Vector


SIZE = (400,400)
FPS = 60

BLACK = (0,0,0)
WHITE = (255, 255, 255)

Light = Vector(1, 1, -1)


timer = time.Clock()
screen = display.set_mode(SIZE)
name = display.set_caption("3D Renderer")
list_of_vertices, list_of_polygons = read_current_model.PolygonsAndVectorsLists()

matrix_of_z = [[-1000 for _ in range(400)] for _ in range(400)]

game_over = False

def sign(a):
    if a > 0: return 1
    elif a < 0: return -1
    else: return 0

def DrawLine(x1,y1,x2,y2, color:tuple):
    delta_x = x2 - x1
    delta_y = y2 - y1

    if delta_x == delta_y == 0: 
        screen.set_at((int(x1), int(y1)), color)
        return None

    if abs(delta_x) >= abs(delta_y): 
        step_x = 1
        step_y = abs(delta_y)/abs(delta_x)

        for i in range(0, abs(delta_x)):
            x = x1 + step_x * i * sign(delta_x)
            y = y1 + step_y * i * sign(delta_y)
            screen.set_at((int(x), int(y)), color)

    elif abs(delta_y) >= abs(delta_x):
        step_y = 1
        step_x = abs(delta_x) / abs(delta_y)

        for i in range(0, abs(delta_y)):
            x = x1 + step_x * i * sign(delta_x)
            y = y1 + step_y * i * sign(delta_y)
            screen.set_at((int(x), int(y)), color)
                       
def DrawHorizontalLine(a:Vector, b:Vector, color:tuple):
    if int(a.x - b.x) == 0:
        z_i = a.z + (b.z - a.z)
        
        if z_i > matrix_of_z[int(a.y)][int(a.x)]:
            matrix_of_z[int(a.y)][int(a.x)] = z_i
            screen.set_at((int(a.x), int(a.y)), color)
            
    
    elif a.x <= b.x:
        n = int(b.x - a.x)
        
        for i in range(n+1):
            z_i = a.z + (b.z - a.z) * i/n
            
            if z_i > matrix_of_z[int(a.y)][int(a.x)+i]:
                matrix_of_z[int(a.y)][int(a.x)+i] = z_i
                screen.set_at((int(a.x + i), int(a.y)), color)
            
    else:
        n = int(a.x - b.x)
        
        for i in range(n+1):
            z_i = a.z + (b.z - a.z) * i/n
            
            if z_i > matrix_of_z[int(b.y)][int(b.x)+i]:
                matrix_of_z[int(b.y)][int(b.x)+i] = z_i
                screen.set_at((int(b.x + i), int(a.y)), color)


def linear_interpolation(a:float | int, b:float | int, t:float) -> float:
    interpolation = a + (b - a) * t
    
    return interpolation

def vector_interpolation(a:Vector, b:Vector, t:float) -> Vector:
    interpolation = a + (b - a) * t
    
    return interpolation

def KeySort(vector:Vector) -> Vector: return vector.y

def DrawPolygon(a:Vector, b:Vector, c:Vector, color:tuple):
    list_1 = [a,b,c]
    list_1.sort(key=KeySort, reverse=True)
    A,B,C = list_1
    
    p_1_y = B.y
    t = (p_1_y - C.y) / (A.y - C.y)
    
    p_1 = linear_interpolation(C, A, t)

    for i in range(int(p_1_y - C.y)):
        k = ((p_1_y - i) - C.y) / (B.y - C.y) 
        p_0_i = (B - C) * k + C
        p_1_i = (p_1 - C) * k + C
        
        DrawHorizontalLine(p_0_i, p_1_i, color)
        
    t = (A.y - B.y) / (A.y - C.y)
    p_1_up = A + (C - A) * t
    
    for i in range(int(A.y - p_1_up.y)):
        k = (A.y - (p_1_up.y + i)) / (A.y - B.y)
        p_0_i = (B - A) * k + A
        p_1_i = (p_1_up - A) * k + A

        DrawHorizontalLine(p_0_i, p_1_i, color)

def scalar(a:Vector, b:Vector): return a.x * b.x + a.y * b.y + a.z * b.z

def vector_mul(a:Vector, b:Vector):
    x = (a.y * b.z - a.z * b.y)
    y = (a.z * b.x - a.x * b.z)
    z = (a.x * b.y - a.y * b.x)
    
    return Vector(x,y,z)

def lighting(a:Vector, b:Vector):
    n_l = scalar(vector_mul(a,b).normalized(), Light.normalized())

    if n_l > 0: L = 0
    if n_l < 0: L = n_l * (-1)
    
    new_light = Vector(WHITE[0], WHITE[1], WHITE[-1]) * L
    new_color = (new_light.x, new_light.y, new_light.z)
    
    return new_color
    
while not game_over:
    for evnt in event.get():
        if evnt.type == QUIT:
            game_over = True
            break

    screen.fill(BLACK)

    matrix_of_z = [[-1000 for _ in range(400)] for _ in range(400)]
    
    for i in range(len(list_of_polygons)):
        a = list_of_vertices[list_of_polygons[i].first_vertice-1]
        b = list_of_vertices[list_of_polygons[i].second_vertice-1]
        c = list_of_vertices[list_of_polygons[i].third_vertice-1]

        a = (a + 2) * 100
        b = (b + 2) * 100
        c = (c + 2) * 100
        
        DrawPolygon(a, b, c, lighting(b-a, c-a))

    display.update()

    timer.tick(FPS)

quit()