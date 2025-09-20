
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
    
    with open("music_sorted.txt", "w") as m:
        m.writelines(songs)
    
    print(f"\n Sorted songs saved in 'music_sorted.txt'")
    
    return songs

if __name__ == "__main__":
    resultado = create_music_file()
   