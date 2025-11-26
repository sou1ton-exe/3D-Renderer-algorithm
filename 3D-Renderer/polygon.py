class Polygon:
    def __init__(self, first_vertice, second_vertice, third_vertice):
        self.first_vertice = first_vertice
        self.second_vertice = second_vertice
        self.third_vertice = third_vertice

    def __str__(self) -> str:
        return f"{self.first_vertice}, {self.second_vertice}, {self.third_vertice}"