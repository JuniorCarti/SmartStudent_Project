#Challenge 1: The Box Class

class Box:
    def __init__(self, length, width, height):
        """
        Initialize a Box with length, width, and height
        """
        self.length = length
        self.width = width
        self.height = height
    
    def get_volume(self):
        """
        Returns the volume of the box (length × width × height)
        """
        return self.length * self.width * self.height
    
    def is_cube(self):
        """
        Returns True if all sides are equal (it's a cube)
        """
        return self.length == self.width == self.height
    
    def bigger(self, other):
        """
        Returns the box with a larger volume
        """
        if self.get_volume() > other.get_volume():
            return self
        else:
            return other
    
    def __str__(self):
        """
        String representation of the Box
        """
        return f"Box({self.length} x {self.width} x {self.height})"

# Test the Box class
print("📦 Box Class Tests:")
box1 = Box(3, 4, 5)
box2 = Box(2, 2, 2)
box3 = Box(5, 5, 5)  # Cube

print(f"{box1} Volume: {box1.get_volume()}")  # 60
print(f"{box2} Volume: {box2.get_volume()}")  # 8
print(f"{box3} Volume: {box3.get_volume()}")  # 125

print(f"{box1} is cube: {box1.is_cube()}")    # False
print(f"{box3} is cube: {box3.is_cube()}")    # True

bigger_box = box1.bigger(box2)
print(f"Bigger between {box1} and {box2}: {bigger_box}")  # box1


#Challenge 2: The Song Class

class Song:
    def __init__(self, title, artist, duration):
        """
        Initialize a Song with title, artist, and duration in seconds
        """
        self.title = title
        self.artist = artist
        self.duration = duration
    
    def is_long(self):
        """
        Returns True if the song is over 5 minutes (300 seconds)
        """
        return self.duration > 300
    
    def same_artist(self, other):
        """
        Returns True if two songs have the same artist
        """
        return self.artist.lower() == other.artist.lower()
    
    def longer_song(self, other):
        """
        Returns the song with the longer duration
        """
        if self.duration > other.duration:
            return self
        else:
            return other
    
    def __str__(self):
        """
        String representation of the Song
        """
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"'{self.title}' by {self.artist} ({minutes}:{seconds:02d})"

# Test the Song class
print("\n🎵 Song Class Tests:")
song1 = Song("Bohemian Rhapsody", "Queen", 355)
song2 = Song("Yesterday", "The Beatles", 125)
song3 = Song("We Will Rock You", "Queen", 122)

print(song1)  # 'Bohemian Rhapsody' by Queen (5:55)
print(song2)  # 'Yesterday' by The Beatles (2:05)

print(f"'{song1.title}' is long: {song1.is_long()}")  # True
print(f"'{song2.title}' is long: {song2.is_long()}")  # False

print(f"Same artist '{song1.title}' and '{song3.title}': {song1.same_artist(song3)}")  # True
print(f"Same artist '{song1.title}' and '{song2.title}': {song1.same_artist(song2)}")  # False

longer = song1.longer_song(song2)
print(f"Longer song between '{song1.title}' and '{song2.title}': {longer.title}")  # Bohemian Rhapsody