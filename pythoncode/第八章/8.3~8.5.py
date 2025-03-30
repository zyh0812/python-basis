# def make_shirt(size,str):
#     print(f"This shirt's size is {size}, word is {str}")

# make_shirt("M","hero")
# make_shirt("S","red") 

# def make_shirt(size="X",str="I love  Python"):
#     print(f"This shirt's size is {size}, word is {str}")

# make_shirt()
# make_shirt(size="M")
# make_shirt(str='I hate you')

# def describe_city(cityname="Reykjavik",country="Iceland"):
#     print(f"{cityname.title()} is in {country.title()}")

# describe_city(cityname="nanchang",country="china")
# describe_city(cityname="jiujinshan",country="usa")

# def city_country(city,country):
#     c_c = f"{city},{country}"
#     return c_c.title()

# print(city_country("wuhan","china"))
# print(city_country("nanchang","china"))

# def make_album(singer,name,time=''):
#     if time:
#         album = {"singer":singer,'s_name':'name','time':time}
#     else:
#         album = {"singer":singer,'s_name':name}
#     return album

# album1 = make_album('周杰伦','双截棍','2006')
# print(album1)
# album2 = make_album('陈奕迅','富士山下')
# print(album2)

# def make_album(singer,name):
#     album = {'singer':singer,'name':name}
#     return album

# while True:
#     singer = input("singer name: ")
#     if (singer == 'q'):
#         break
#     name = input("album name: ")
#     if name == 'q':
#         break
#     album = make_album(singer,name)
#     print(album)
