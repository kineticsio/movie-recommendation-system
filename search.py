import difflib

def search_movie(movies):
    movie = input("Enter movie name to search: ").title()

    found = False

    for genre in movies:
        if movie in movies[genre]:
            print(movie + " is in " + genre)
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
                        print(match[0] + " is in " + genre)
                        break
            else:
                print("Movie not found!")

        else:
            print("Movie not found!")