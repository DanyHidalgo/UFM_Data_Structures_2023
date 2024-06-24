from LinkedListPlaylist import Node, LinkedListPlaylist

song1 = Node(10001,"Arrancarmelo", "Wos", "Oscuro extasis")
song2 = Node(15820,"Past Lives", "Sapientdream", "Past Lives")
song3 = Node(20841,"If I can dream", "Elvis", "68' Comeback Special")
song4 = Node(95051,"Pensamos", "Nicki Nicole", "Parte de mí")
song5 = Node(84102, "Quereme", "Wos", "Oscuro Extasis")
song6 = Node(48052, "Alma Dinamita", "Wos", "Tres puntos suspensivos")


ll = LinkedListPlaylist()

ll.append(song1)
ll.append(song2)
ll.append(song4)
ll.append(song5)
ll.append(song6)

ll.current_node = ll.head
ll.Play()


ll.Previous()
ll.Play

#Move to the next song
ll.Next()
ll.Play()

ll.Next()
ll.Play()

ll.Next()
ll.Play()

ll.Next()
ll.Play()

ll.Next()
ll.Play()

ll.Next()
ll.Play()

ll.Next()
ll.Play()

#Move to the previous song
ll.Previous()
ll.Play()

#Search by song's name
ll.SearchByName("Pensamos")
ll.SearchByName("Arrancarmelo")
ll.SearchByName("Dakiti")

#Search by artist's songs
print(ll.SearchByArtist("Wos"))
print(ll.SearchByArtist("Nicki Nicole"))
print(ll.SearchByArtist("Chino y Nacho"))

#Playlist len
print(ll.PlaylistLen())

ll.append(song3)

print(ll.PlaylistLen())


ll.Play()

#Random song
ll.PlayShuffle()