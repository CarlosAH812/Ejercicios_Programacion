
def create_music_file():
    
    with open("music.txt", "r") as m:
        songs = m.readlines()
    
    print("\n Original list:")
    for song in songs:
        print(f"   - {song.strip()}")
    
    songs.sort()
    print("\n Sorted list:")
    for song in songs:
        print(f"   - {song.strip()}")
    
    return songs

if __name__ == "__main__":
    resultado = create_music_file()
   