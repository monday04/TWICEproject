from masterlist_songs import songlist
from masterlist_genre import genrelist, genreMenu
"""
TWICE has a lot of songs which can be divided into different genres.
This program helps you recommend a twice song based on a genre they liked or
based on a TWICE song they like with a similar feel
1. Search by song
2. Search by genre
"""


def search_by_song():
    song = ""
    while True:
        for index, (title, genre) in enumerate(songlist):
            if song == title:
                print(f"Track: {title}\nGenre: {genre}.\nSimilar songs:\n")
                songs_by_genre(genre)
                break
            # print(">> No songs of the same genre found. Try again.")
        song = input("\n\nEnter a TWICE song or '.' to quit: ")
        if song == ".":                     # exit song search
            return "-"


def songs_by_genre(genre):
    if genre in genrelist:
        tracks = genrelist[genre]
        for track in tracks:
            print(f"\t{track}")


def search_by_genre():
    while True:
        print("\n\nPlease choose your genre:")
        for index, (genre, subgenre) in enumerate(genreMenu):
            print("{}. {}".format(index + 1, genre))
        print(f"{len(genreMenu)+1}. Quit / Back")
        gen_option = int(input(": ")) - 1

        if gen_option == len(genreMenu):      # exit search
            return "-"
        if gen_option > len(genreMenu)+1:
            return "2"

        genre, subgenre = genreMenu[gen_option]

        if len(subgenre) != 0:                  # choose from subgenre if it exist
            for idx, i in enumerate(subgenre):  # display subgenre
                print(f"{idx+1} - {i}")
            print(f"{len(subgenre)+1} - Display all songs.\nChoose subgenre.\n\n")

            sub_option = int(input(": "))
            if sub_option == len(subgenre)+1:   # Display all songs
                print(f"\n\nDisplaying all songs under {genre}:")
                songs_by_genre(genre)
                for sub in subgenre:            # iterate from subgenre list
                    songs_by_genre(sub)

            if sub_option <= len(subgenre):     # Display songs from subgenre
                sub = subgenre[sub_option-1]
                songs_by_genre(sub)

        else:   # display all songs from the master genre
            songs_by_genre(genre)


option = "-"
while option != "3":
    if option == "1":
        option = search_by_song()
    elif option == "2":
        option = search_by_genre()   # option = search_by_genre()
    else:
        print("Search Menu\n\t1. Search by song\n\t2. Search by genre\n\t3. Quit")
        option = str(input(": "))
