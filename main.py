# class Book:
#
#     def __init__(self, name, author, isbn):
#         self.__name = name
#         self.__author = author
#         self.__isbn = isbn
#
#     def get_author(self):
#         return self.__author
#
#     def set_author(self, author):
#         self.__author = author
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_isbn(self):
#         return self.__isbn
#
#     def set_isbn(self, isbn):
#         self.__author = isbn
#
#
# b = Book('name', 'author1', '1234543736472')
# print(b.get_author())
# b.set_author('fnndbk')
# print(b.get_author())

#
# class Figure:
#     def __init__(self, coords, width, color):
#         self.coords = coords
#         self.width = width
#         self.color = color
#
#     def draw(self):
#         print(f'рисуем фигуру цветом {self.color} и шириной {self.width}')
#
#
# class Line(Figure):
#     def draw(self):
#         print(f'рисуем линию цветом {self.color} и шириной {self.width}')
#
#
# class Rect(Figure):
#     def __init__(self, coords, width, color, right):
#         super().__init__(coords, width, color)
#         self.right = right
#
#     def draw(self):
#         print(f'рисуем прямоугольник цветом {self.color} и шириной {self.width}. Прямоугольник {self.right}')
#
#
# class Ellips(Figure):
#     def draw(self):
#         print(f'рисуем эллипс цветом {self.color} и шириной {self.width}')
#
#
# f = Figure([1, 2, 3, 4, 5, 6], 2, 'black')
# f.draw()
# l = Line([1, 2, 3], 4, 'white')
# class Publication:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def display(self):
#         print('Название:', self.title)
#         print('Автор:', self.author)
#         print('Год выпуска:', self.year)
#
#
# class Book(Publication):
#     def __init__(self, title, author, year, isbn):
#         super().__init__(title, author, year)
#         self.isbn = isbn
#
#     def display(self):
#         super().display()
#         print(f'ISBN: {self.isbn}')
#
#
# class Magazine(Publication):
#     def __init__(self, title, author, year, issue_number):
#         super().__init__(title, author, year)
#         self.issue_number = issue_number
#
#     def display(self):
#         super().display()
#         print(f'Номер журнала: {self.issue_number}')
#
#
# def info(obj):
#     obj.display()
#
#
# p = Publication('Название1','Автор1',2015)
# b = Book('Название2','Автор2',2021,2003939300)
# m = Magazine('Автор3','Название3',2023,5)

import random
class MusicAlbum:

    def __init__(self,title,artist,release_year,genre,tracklist):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist

    def get_info(self):
        print(f'''
Название:{self.title}
Исполгнитель:{self.artist}
Год выпуска:{self.release_year}
Жанр:{self.genre}
Список треков:{self.tracklist}
''')

    def play_random_track(self):
        return random.choice(self.tracklist)

album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte",
                    ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex",
                     "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo",
                     "Hallomann"])
print("Название:", album4.title)
print("Исполнитель:", album4.artist)
print("Год:", album4.release_year)
print("Жанр:", album4.genre)
print("Треки:", album4.tracklist)
album4.play_random_track()


album4.get_info()
print(album4.play_random_track())



