# PABUNA, KATRINA B. 

# Create class TV
class TV:
    # constructor
    def __init__(self, channel, volume_level, on, off):
        '''Create a TV instance where
        channel = int(channel of TV)
        volume_level = int(volume level of TV)
        on = bool(if the TV is on or not)
        off = bool(if the TV is on or not)'''

        # instance variables
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
        self.off = off
    
tv1 = TV(30, 3, True, False)
tv2 = TV(3, 2, True, False)

