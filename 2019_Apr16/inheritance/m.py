class MusicPlayer:

    def play(self):
        print(self.name, "playing...")

    def stop(self):
        print(self.name, "stopped...")

    def buy(self):
        print("Bought a music player")
        print("Got an object belonging to ", self.__class__)
