class Song:
    # --- Class Attributes ---
    # These track global metrics across all instances of Song
    total_songs = 0
    unique_artists = set()
    unique_genres = set()
    genre_counts = {}
    artist_counts = {}

    def __init__(self, name, artist, genre):
        # --- Instance Attributes ---
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment total song count
        Song.total_songs += 1

        # Track unique items using sets
        Song.unique_artists.add(artist)
        Song.unique_genres.add(genre)

        # Update global count for this specific genre
        if genre in Song.genre_counts:
            Song.genre_counts[genre] += 1
        else:
            Song.genre_counts[genre] = 1

        # Update global count for this specific artist
        if artist in Song.artist_counts:
            Song.artist_counts[artist] += 1
        else:
            Song.artist_counts[artist] = 1

    # --- Class Methods ---
    @classmethod
    def get_total_songs(cls):
        """Returns the total number of songs created."""
        return cls.total_songs

    @classmethod
    def get_unique_artists(cls):
        """Returns a list or set of all unique artists."""
        return cls.unique_artists

    @classmethod
    def get_unique_genres(cls):
        """Returns a list or set of all unique genres."""
        return cls.unique_genres

    @classmethod
    def get_genre_count(cls, genre):
        """Returns the count of songs for a specific genre (defaults to 0 if not found)."""
        return cls.genre_counts.get(genre, 0)

    @classmethod
    def get_artist_count(cls, artist):
        """Returns the count of songs for a specific artist (defaults to 0 if not found)."""
        return cls.artist_counts.get(artist, 0)