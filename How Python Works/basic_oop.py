""" Make a class
    Each instance of the class has a heat level
    The goal of the game is to reduce the heat level of each class to less than 30 / 100 """

class oven():
    def __init__(self, target=15):
        self.__heat_level = 100
        self.reduce_val = 3
        self.heat_target = target
    
    ''' Making setter and getter functions '''
    """ Heat Value Get & Set """
    @property
    def heat(self):
        return self.__heat_level
    @heat.setter
    def heat(self, val):
        ''' Taking care of edge cases '''
        if val > 100 or val < 15:
            print("Stop doing that bozo")
            return
        else:
            self.__heat_level = val
            print("Setter")
        return

    """ Value Reduction Get & Set"""
    @property
    def reduce_val_ctrl(self):
        return self.reduce_val
    @reduce_val_ctrl.setter
    def reduce_val_ctrl(self, val):
        self.reduce_val = val

    ''' Making the reducing function '''
    def reducer(self):
        self.__heat_level -= self.reduce_val
    def reduce_other(self, other_oven):
        if other_oven.__heat_level > other_oven.heat_target:
            other_oven.reducer()
            other_oven.reduce_other(self) # ???
        else:
            return
            print("It's cool enough")

if __name__ == "__main__":
    oven1 = oven(34)
    oven2 = oven(2)
    print("\n[Beginning Heat Levels]" + " Oven 1: " + str(oven1.heat) + ", Oven 2: " + str(oven2.heat))
    oven1.reduce_other(oven2)
    print("[Ending Heat Levels]" + " Oven 1: " + str(oven1.heat) + ", Oven 2: " + str(oven2.heat) + "\n")