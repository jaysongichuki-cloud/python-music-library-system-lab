class Song:
    # --- Class Attributes ---
    total_songs = 0
    unique_artists = set()
    unique_genres = set()
    genre_counts = {}
    artist_counts = {}

    def __init__(self, name, artist, genre):
        # Assigning instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Track global stats
        Song.total_songs += 1
        Song.unique_artists.add(artist)
        Song.unique_genres.add(genre)

        # Increment counts
        Song.genre_counts[genre] = Song.genre_counts.get(genre, 0) + 1
        Song.artist_counts[artist] = Song.artist_counts.get(artist, 0) + 1

    @classmethod
    def get_total_songs(cls):
        return cls.total_songs

    @classmethod
    def get_unique_artists(cls):
        return cls.unique_artists

    @classmethod
    def get_unique_genres(cls):
        return cls.unique_genres

    @classmethod
    def get_genre_count(cls, genre):
        return cls.genre_counts.get(genre, 0)

    @classmethod
    def get_artist_count(cls, artist):
        return cls.artist_counts.get(artist, 0)