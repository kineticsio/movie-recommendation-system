def show_movies(movies):
    print("\nMovies Available:")

    for genre in movies:
        print("\n" + genre + ":")

        for movie in movies[genre]:
            print("- " + movie)


def recommend_movies(movies):
    print("\n1. Action")
    print("2. Comedy")
    print("3. Sci-Fi")

    pick = input("Enter number: ")

    if pick == "1":
        for movie in movies["Action"]:
            print("- " + movie)

    elif pick == "2":
        for movie in movies["Comedy"]:
            print("- " + movie)

    elif pick == "3":
        for movie in movies["Sci-Fi"]:
            print("- " + movie)

    else:
        print("Wrong number!")