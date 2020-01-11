tags = "concrete, table ,wood, furniture, accessorizes, metal"
video_1_title = "Concrete Candle Holder How To Make"
video_1_link = "Z_8Ss94fgZc"

video_2_title = "How To Make a Concrete Fire Bowl"
video_2_link = "uSSp3X07Vls"

video_3_title = "Diy LED Desk Lamp With Concrete Base"
video_3_link = "a5yiMhJaGCo"
playlist_1_title = "Работа по дереву"
playlist_2_title = "Литье"
playlist_3_title = "Оборудование мастерской"
print("""Приложение в разработке.
Введите "videos" чтобы посмотреть список видео. 
Введите "tags" чтобы посмотреть список тегов. 
Введите "playlists" чтобы посмотреть список тегов. 
Введите "about" чтобы получить информацию.""")
a = input()
if a == "videos":
    print("""У нас есть 3 видео:
Concrete Candle Holder How To Make: youtu.be/Z_8Ss94fgZc
How To Make a Concrete Fire Bowl: youtu.be/uSSp3X07Vls
Diy LED Desk Lamp With Concrete Base: youtu.be/a5yiMhJaGCo""")
elif a =="tags":
    print("У нас есть 6 тегов: concrete, table ,wood, furniture, accessorizes, metal")
elif a == "playlists":
    print("У нас есть 3 плейлиста: Работа по дереву, Литье, Оборудование мастерской")
elif a == "about":
    print("Stepik Media – О приложении. Это – кинотеатр полезных  видео про DYI")
else:
    print("""К сожалению, по вашему запросу ничего не нашли.
Выберите из предлагаемого списка""")