from data import movies
from search import search_movie
from add_remove import add_movie, remove_movie
from display import show_movies, recommend_movies

while True:
    print("\n===== MOVIE RECOMMENDATION SYSTEM =====")
    print("1. View All Movies")
    print("2. Recommend Movies by Genre")
    print("3. Add Movie")
    print("4. Remove Movie")
    print("5. Search Movie")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_movies(movies)

    elif choice == "2":
        recommend_movies(movies)

    elif choice == "3":
        add_movie(movies)

    elif choice == "4":
        remove_movie(movies)

    elif choice == "5":
        search_movie(movies)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Wrong choice!")