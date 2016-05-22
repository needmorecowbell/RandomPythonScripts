import spotipy

sp= spotipy.Spotify()

results= sp.search(q='3OH!', limit= 20)

for i, t in enumerate(results['tracks']['items']):
    print(' ',i+1,t['name'])

user= sp.user("amusciano")
print(user)
                  
