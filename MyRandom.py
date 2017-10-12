from time import time
import time as t


class MyRandom(object):

    # Initializing object with keyword arguements
    def __init__(self, **kwargs):
        """ This function initializes the keyword
            arguements that are being passed."""
        self.maxlist = kwargs["maxlist"]
        self.minlist = kwargs["minlist"]
        self.inc = kwargs["inc"]
        self.mod = kwargs["mod"]
        self.length = kwargs["length"]


    def get_seed(self):
        """ This function generates and returns two
            randomly generated values being used as seeds"""
        self.first = 0
        self.second = 0
        while not self.first and not self.second:
            try:
                self.first, self.second = int(str(time() - int(time()))[-1]), int(str(time() - int(time()))[-2])
            except ValueError:
                self.get_seed()
        return self.first, self.second


    def validate_seed(self, mod, inc):
        """ This function validates the value of
            generated seed and multiplier and returns them """
        self.mod = mod
        self.inc = inc
        temp = 0
        while not temp:
            multiplier, seed = self.get_seed()
            temp = 0 <= self.inc < self.mod and 0 <= seed < self.mod and multiplier in [1, 3, 7, 9]

        return multiplier, seed



    def get_random(self, mod, inc):
        """ This function generates a psuedo
                 random number and returns it."""
        self.mod = mod
        self.inc = inc
        multiplier, seed = self.validate_seed(self.mod, self.inc)
        result = [seed]
        current_iteration = -1
        switch = False

        while current_iteration != seed and current_iteration != 0:
            if not switch:
                current_iteration = (seed * multiplier) + self.inc
                switch = True
            else:
                current_iteration = (current_iteration * multiplier) + self.inc
                if current_iteration > self.mod:
                    current_iteration %= self.mod
                result.append(current_iteration)

        return result[-1]


    def print_randoms(self):
        """ This function generates a list of biased
            randomly generated numbers and prints them. """
        while True:
            t.sleep(0.00000000000001)
            num = self.get_random(self.mod,self.inc)
            if num >= 5:
                if len(self.maxlist) < round((73*self.length)/100):
                    self.maxlist.append(num)
            else:
                if len(self.minlist) < round((27*self.length)/100):
                    self.minlist.append(num)
            if len(self.maxlist) == round((73*self.length)/100) and len(self.minlist) == round((27*self.length)/100):
                break
        print("Randomly generated list with 27% biased to less than 5 is:\n",self.minlist)
        print("Randomly generated list with 73% biased to more than 5 is:\n",self.maxlist)

# Main Section
if __name__ == '__main__':
    while True:
        try:
            l = int(input("Enter number of elements to generate:\n"))
            break
        except ValueError:
            print("Incorrect input. !! Try Again")

    rand_obj = MyRandom(inc=0,mod=10,maxlist=[],minlist=[],length=l)
    rand_obj.print_randoms()

