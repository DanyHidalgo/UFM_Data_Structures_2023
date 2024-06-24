import random
class Node:

    def __init__(self, id: int, name: str, artist: str, album: str, prev=None, next=None):

        self.id = id
        self.name = name
        self.artist = artist
        self.album = album
        self.prev = prev
        self.next = next


class LinkedListPlaylist:

    def __init__(self):
        self.current_node = None
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


    def __len__(self):
        return self.length


    def __next__(self):
        if node is None:
            raise StopIteration
        else:
            node = current_node
            current_node = node.next
            yield node
    

    def append(self, new_node: Node):
        if self.head is None:
            self.head = new_node
            self.tail = self.head

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1


    def delete(self, name):

        self.current_node = self.head

        while self.current_node:

            if self.current_node.name == name:

                if self.current_node == self.head and self.current_node == self.tail:
                    self.head = None
                    self.tail = None

                elif self.current_node == self.head:
                    self.head = self.head.next
                    self.head.prev = None

                elif self.current_node == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None

                else:
                    self.current_node.prev.next = self.current_node.next
                    self.current_node.next.prev = self.current_node.prev

                self.length -= 1

            self.current_node = self.current_node.next
            
    
    def Show_Details(self):
        if self.current_node is not None:
            print(f"| ID: {self.current_node.id} | Name: {self.current_node.name} | Album: {self.current_node.album} | Artist: {self.current_node.artist}")
        
        else:
            print("There is no song in the playlist")
    

    def Next(self):
        if self.current_node is None:
            print("There is no song in the playlist")

        elif self.current_node.next is None:
            print("This is the last song in the playlist")

        else:
            self.current_node = self.current_node.next


    def Previous(self):
        if self.current_node is None:
            print("There is no song in the playlist")

        elif self.current_node.prev is None:
            print("This is the first song in the playlist")
        
        else:
            self.current_node = self.current_node.prev

    
    def Play(self):
        self.Show_Details()

    def SearchByName(self, name: str):

        for current_node in self:
            if current_node.name == name:
                self.current_node = current_node
                self.Play()
                return
        print (f"There is no song named {name}")


    def SearchByArtist(self, artist: str):

        songs = []

        for current_node in self:
            if current_node.artist == artist:
                songs.append(current_node.name)
        
        if songs:
            print(f"Songs of {artist} in the playlist")
            return(songs)
        
        else:
            return(f"There are no songs of {artist} in the playlist")
        
    
    def PlaylistLen(self):
        count = 0

        for current_node in self:
            count +=1
        return(f"There is {count} songs in the playlist")
    
    def PlayShuffle(self):
        if self.head is None:
            return ("There is not song to choose")
        
        rand = random.randint(0, len(self)-1)

        current_node = self.head

        for element in range(rand):
            current_node = current_node.next

        self.current_node = current_node
        self.Play()
