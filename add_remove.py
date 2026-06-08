import difflib

def add_movie(movies):
    print("\n1. Action")
    print("2. Comedy")
    print("3. Sci-Fi")

    pick = input("Enter genre number: ")
    movie = input("Enter movie name: ").title()

    if pick == "1":
        movies["Action"].append(movie)

    elif pick == "2":
        movies["Comedy"].append(movie)

    elif pick == "3":
        movies["Sci-Fi"].append(movie)

    else:
        print("Wrong number!")
        return

    print("Movie added!")


def remove_movie(movies):
    movie = input("Enter movie name to remove: ").title()

    found = False

    for genre in movies:
        if movie in movies[genre]:
            movies[genre].remove(movie)
            print("Movie removed!")
            found = True
            break

    if not found:
        all_movies = []

        for genre in movies:
            for m in movies[genre]:
                all_movies.append(m)

        match = difflib.get_close_matches(movie, all_movies, n=1, cutoff=0.4)

        if match:
            answer = input("Did you mean " + match[0] + "? (yes/no): ")

            if answer.lower() == "yes":
                for genre in movies:
                    if match[0] in movies[genre]:
                        movies[genre].remove(match[0])
                        print(match[0] + " removed from " + genre)
                        break
        else:
            print("Movie not found!")