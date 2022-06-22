""" Make a class
    Each instance of the class has a heat level
    The goal of the game is to reduce the heat level of each class to less than 30 / 100 """

class oven:
    def __init__(self, target=15):
        self.heat_level = 100
        self.reduce_val = 1
        self.heat_target = target
        self.target_oven
    
    ''' Making setter and getter functions '''
    """ Heat Value Get & Set """
    @property
    def heat(self):
        return self.heat_level

    @heat.setter
    def heat(self, val):
        ''' Taking care of edge cases '''
        if val > 100 or val < 15:
            print("Stop doing that bozo")
            return
        else:
            self.heat_level = val
            print("Setter")
        return

    """ Value Reduction Get & Set"""
    @property
    def reduce_val_ctrl(self):
        return self.reduce_val
    
    @reduce_val_ctrl.setter
    def reduce_val_ctrl(self, val):
        self.reduce_val = val

    """ Target Oven Get & Set """
    @property
    def targ_ov(self):
        return self.target_oven

    def targ_ov(self, targ_oven):
        self.target_oven = targ_oven

    ''' Making the reducing function '''
    def reducer(self):
        if self.target_oven.heat_level > self.heat_target:
            self.target_oven.heat_level -= 1
