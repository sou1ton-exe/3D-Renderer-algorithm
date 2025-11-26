import os
from vector import Vector
from polygon import Polygon


def PolygonsAndVectorsLists():
    explore = os.path.dirname(__file__)
    explore = os.path.join(explore, "3D-Objects/cube3.obj")

    vector_cords = Vector(0, 0, 0)
    polygon_nums = Polygon(0, 0, 0)

    wave = open(explore, "r")

    list_of_vertices = []
    list_of_polygons = []

    for el in wave: 
        replaced_el = el.replace("\n", "")
        list_of_v = replaced_el.split(" ")

        if list_of_v[0] == "v":
            vector_cords = Vector(float(list_of_v[1]), float(list_of_v[2]), float(list_of_v[3]))
            list_of_vertices.append(vector_cords)

        replaced_el = el.replace("\n", "")
        list_of_f = replaced_el.split(" ")

        if list_of_f[0] == "f":
            polygon_nums = Polygon(int(list_of_f[1][0]), int(list_of_f[2][0]), int(list_of_f[3][0]))
            list_of_polygons.append(polygon_nums)

    wave.close()

    return (list_of_vertices, list_of_polygons)