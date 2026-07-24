"""
=========================================
Day 3 : Personal Movie Tracker
=========================================

A CLI-based movie tracker that stores movie
information permanently in a JSON file.

Features:
✔ Add a movie
✔ View all movies
✔ Search by title or genre
✔ Prevent duplicate movie titles
✔ Validate movie ratings
✔ Store data permanently in movies.json

Concepts Covered:
✔ JSON File Handling
✔ Lists
✔ Dictionaries
✔ Functions
✔ Loops
✔ List Comprehension
✔ Exception Handling
✔ Data Validation
✔ match-case
"""


import json
import os


MOVIE_FILE = "movies.json"


def load_movies():
    """
    Load movie data from the JSON file.

    If the file does not exist,
    return an empty list.
    """

    if not os.path.exists(MOVIE_FILE):
        return []

    try:
        with open(MOVIE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("⚠️ Movie file is corrupted or empty.")
        return []


def save_movies(movies):
    """
    Save the current movie list
    into the JSON file.
    """

    with open(MOVIE_FILE, "w", encoding="utf-8") as file:

        json.dump(
            movies,
            file,
            indent=4
        )


def add_movie(movies):
    """Add a new movie to the movie database."""

    title = input(
        "\nEnter movie title: "
    ).strip()

    # Prevent empty movie titles.
    if not title:
        print("❌ Movie title cannot be empty.")
        return

    # Prevent duplicate movie titles.
    if any(
        movie["title"].lower() == title.lower()
        for movie in movies
    ):
        print("❌ This movie already exists.")
        return

    genre = input(
        "Enter movie genre: "
    ).strip()

    if not genre:
        print("❌ Genre cannot be empty.")
        return

    # Validate movie rating.
    try:

        rating = float(
            input("Enter rating (0-10): ")
        )

        if not 0 <= rating <= 10:
            print("❌ Rating must be between 0 and 10.")
            return

    except ValueError:

        print("❌ Please enter a valid number.")
        return

    # Create a dictionary for the new movie.
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    # Add the movie to the list.
    movies.append(movie)

    # Save updated list to JSON.
    save_movies(movies)

    print(f"✅ '{title}' added successfully!")


def view_movies(movies):
    """Display all movies in the database."""

    if not movies:
        print("\n📭 No movies found.")
        return

    print("\n" + "=" * 60)
    print("🍿 MY MOVIE DATABASE".center(60))
    print("=" * 60)

    print(
        f"{'Title':<25}"
        f"{'Genre':<20}"
        f"{'Rating':<10}"
    )

    print("-" * 60)

    for movie in movies:

        print(
            f"{movie['title']:<25}"
            f"{movie['genre']:<20}"
            f"{movie['rating']:<10.1f}"
        )

    print("=" * 60)


def search_movies(movies):
    """Search movies by title or genre."""

    search_term = input(
        "\nSearch by title or genre: "
    ).strip().lower()

    if not search_term:
        print("❌ Search term cannot be empty.")
        return

    # Find movies where the search term
    # exists in either title or genre.
    results = [
        movie
        for movie in movies
        if (
            search_term in movie["title"].lower()
            or
            search_term in movie["genre"].lower()
        )
    ]

    if not results:
        print("❌ No matching movies found.")
        return

    print(
        f"\n🔎 Found {len(results)} movie(s):"
    )

    print("-" * 60)

    for movie in results:

        print(
            f"🎬 {movie['title']} | "
            f"Genre: {movie['genre']} | "
            f"Rating: {movie['rating']}/10"
        )

    print("-" * 60)


def run_movie_tracker():

    # Load existing movies when program starts.
    movies = load_movies()

    while True:

        print("\n🍿 MY MOVIE TRACKER")
        print("-" * 30)
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Search Movie")
        print("4. Exit")

        choice = input(
            "\nChoose an option (1-4): "
        ).strip()

        match choice:

            case "1":
                add_movie(movies)

            case "2":
                view_movies(movies)

            case "3":
                search_movies(movies)

            case "4":
                print("\n👋 Goodbye! See you next time.")
                break

            case _:
                print(
                    "❌ Invalid choice. "
                    "Please select 1-4."
                )


if __name__ == "__main__":
    run_movie_tracker()