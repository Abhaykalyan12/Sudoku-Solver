import random
import pygame 

# Class representing a single song node in the linked list
class SongNode:
    def __init__(self, title, artist, file_path):
        self.title = title         # Song title
        self.artist = artist       # Artist name
        self.file_path = file_path # Path to the song file
        self.next = None           # Reference to the next song node

# Class representing the music playlist
class Playlist:
    def __init__(self):
        self.head = None                # Head of the linked list (first song)
        # In-memory song library (key: song_key, value: song details)
        self.song_library = {
            "bohemian_rhapsody": {"title": "Bohemian Rhapsody", "artist": "Queen", "file_path": "/path/to/bohemian_rhapsody.mp3"},
            "stairway_to_heaven": {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "file_path": "/path/to/stairway_to_heaven.mp3"},
            # Add more songs to your library here
        }

        pygame.mixer.init()  # Initialize the pygame mixer for audio playback

    # Method to add a song to the playlist at a specific position
    def add_song(self, song_key, position=None):
        if song_key not in self.song_library:
            print("Song not found in library.")
            return

        song_data = self.song_library[song_key]
        new_node = SongNode(song_data["title"], song_data["artist"], song_data["file_path"])

        if not self.head:
            self.head = new_node
            return

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        index = 0
        while current.next and (position is None or index < position - 1):
            current = current.next
            index += 1

        new_node.next = current.next
        current.next = new_node

    # Method to remove a song from the playlist
    def remove_song(self, target):
        if not self.head:  # If the playlist is empty, do nothing
            return

        if self.head.title == target or self.head.artist == target:  # If the target song is at the head
            self.head = self.head.next  # Update the head to the next song
            return

        current = self.head
        while current.next:  # Traverse the playlist until we find the target or reach the end
            if current.next.title == target or current.next.artist == target:
                current.next = current.next.next  # Remove the target song by skipping it
                return
            current = current.next

    # Method to play songs in the playlist sequentially (forward)
    def play_forward(self):
        current = self.head
        while current:
            print(f"Playing: {current.title} by {current.artist}")
            pygame.mixer.music.load(current.file_path)  # Load the song into the mixer
            pygame.mixer.music.play()  # Start playing the loaded song
            while pygame.mixer.music.get_busy():  # Wait until the song finishes playing
                pygame.time.Clock().tick(10)  # Keep the program responsive during playback
            current = current.next # Move to the next song

    # Method to play songs in the playlist sequentially (backward)
    def play_backward(self):
        songs = [] # Temporary list to store songs for reversing
        current = self.head
        while current:
            songs.append(current)
            current = current.next

        for song in reversed(songs): # Iterate through songs in reverse order
            print(f"Playing: {song.title} by {song.artist}")
            pygame.mixer.music.load(song.file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

    # Method to play songs in the playlist in shuffled order
    def shuffle_play(self):
        songs = []
        current = self.head
        while current:
            songs.append(current)
            current = current.next

        random.shuffle(songs) # Shuffle the list of songs
        for song in songs:
            print(f"Playing: {song.title} by {song.artist}")
            pygame.mixer.music.load(song.file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

if __name__ == "__main__":
    my_playlist = Playlist()

    # Add some songs (replace with your actual song keys from the library)
    my_playlist.add_song("bohemian_rhapsody")
    my_playlist.add_song("stairway_to_heaven", 0)  # Add at the beginning

    # You can add more songs, remove songs, and then call the playback methods
    my_playlist.play_forward()
    # my_playlist.play_backward()
    # my_playlist.shuffle_play()
