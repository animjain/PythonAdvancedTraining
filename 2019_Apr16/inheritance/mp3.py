from e import ElectronicDevice
from m import MusicPlayer

class MP3Player(MusicPlayer, ElectronicDevice):
    pass
    #def buy(self):
    #    MusicPlayer.buy(self)

if __name__ == '__main__':
    m = MP3Player()
    m.name = "iPod"

    m.poweron()
    m.play()
    m.stop()
    m.poweroff()
    m.buy()


