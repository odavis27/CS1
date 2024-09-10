# postage class to store all info of inputed postage info
class postage:
    def __init__(self,length,thick, height):
        self.length = length
        self.thick = thick
        self.height = height
        self.type = None
        #set_postage_type()

    def set_postage_type(self):
        # check if postage is any of the following:
        #    regular post card, large post card, or envelope
        if self.length <= 6.125 and self.thick >= 0.007 :
            # check for regular post card
            if self.length >= 3.5 and self.length <= 4.25 and self.thick <= 0.016:
                pass



        regular_card = {'length':(3.5,4.25),'width':(3.5,6),'tickness':(0.007,0.016), 'inclusive':True}
        large_card = {'length':(4.25),'width':(6,11.5),'tickness':(0.007,0.016), 'inclusive':False}
        postage_type_restrictions = [regular_card,large_card]
        for i in postage_type_restrictions:
            

    def get_zones(self):
        pass


