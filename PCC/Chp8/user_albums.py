"""
8-8. User Albums: Start with your program from Exercise 8-7 . Write a while loop that allows
users to enter an album’s artist and title . Once you have that information, call make_album()
with the user’s input and print the dictionary that’s created . Be sure to include a quit value
in the while loop .
"""
def make_album(artist_name,album_title,number_tracks=''):
    album = {'artist':artist_name,'album_name':album_title}
    if number_tracks:
        album['tracks']=number_tracks
    return album

while True:
    print('Please enter the details of the album: ')
    print("(enter 'q' at any time to quit)")
    a_name = input('Enter artist name: ')
    if a_name == 'q':
        break
    a_title = input('Enter the album name: ')
    if a_title == 'q':
        break
    n_tracks = int(input('Enter the number of tracks in the album: '))
    if n_tracks == 'q':
        break

    album_details = make_album(a_name,a_title,n_tracks)

    print(album_details)


