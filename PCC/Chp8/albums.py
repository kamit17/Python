"""
8-7. Album: Write a function called make_album() that builds a dictionary describing a
music album . The function should take in an artist name and an album title, and it should
return a dictionary containing these two pieces of information . Use the function to make
three dictionaries representing different albums . Print each return value to show that the
dictionaries are storing the album information correctly .
Add an optional parameter to make_album() that allows you to store the number of tracks on an
album . If the calling line includes a value for the num- ber of tracks, add that value to the
album’s dictionary . Make at least one new function call that includes the number of tracks on
an album .
"""

def make_album(artist_name,album_title,number_tracks=''):
    album = {'artist':artist_name,'album_name':album_title}
    if number_tracks:
        album['tracks']=number_tracks
        
    return album

album1 = make_album('MJ','Thriller')
album2= make_album('Bob Dylan','Slow Train Coming')
album3= make_album('The Beatles','Revolver')
album4=make_album('Pink Floyd','Dark side of moon',10)
print("\n")
print(album1)
print(album2)
print(album3)
print(album4)


"""intial part of the program

def make_album(artist_name,album_title,):
    album = {'artist':artist_name,'album_name':album_title}
    return album
album1 = make_album('MJ','Thriller')
album2= make_album('Bob Dylan','Slow Train Coming')
album3= make_album('The Beatles','Revolver')
album4=make_album('Pink Floyd','Dark side of moon')
print("\n")
print(album1)
print(album2)
print(album3)
print(album4)

"""
