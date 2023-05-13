# PABUNA, KATRINA B. 

# Create class TV
class TV:
    # constructor
    def __init__(self, channel, volume_level, on):
        '''Create a TV instance where
        channel = int(channel of TV)
        volume_level = int(volume level of TV)
        on = bool(if the TV is on or not)'''

        # instance variables
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
    
    def get_channel(self):
        return self.channel
