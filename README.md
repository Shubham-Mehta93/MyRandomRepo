# MyRandomRepo
README FILE: 
      Created By : Shubham Mehta 
		  mehta.shubham250@gmail.com
		  13 Oct 2017
      Developed a custom random number generation algo which is 73% biased to the higher number.
      Like if I want a random number between 1 to 10 100 times then it gives number more than 5
      73 times and less than 5 27 times.

Solution:

Created a class named MyRandom that contains five methods namely:
    def __init__(self, **kwargs)
                This function initializes the keyword arguements that are passed through to the method when the object is created.

    def get_seed(self)
	        This function generates and returns two randomly generated values to be used as seeds.
	        I have used time() of the time module, that returns time since epoch in terms of a float value.
	        Extracted the decimal part from it and used its last two digits as seeds.

    def validate_seed(self, mod, inc)
		This function validates the value of generated seeds by get_seed() and returns them.
		The value of one of the seeds used as a multiplier to generate actual random number in get_random() method must be either 1,3,7 or 9.
		The value of other seed must be in range [0,10).

    def get_random(self, mod, inc)
		This function generates a psuedo random number using previously generated seed values and returns it.
		It uses a list to perform computations on the generated seeds and store the results of those computations.
		The last element from the list is returned then as a randomly generated number.

    def print_randoms(self)
		This function generates a list of biased randomly generated numbers and prints them.
		As per the scenario, of the number of randomly generated numbers that user wants, it gets 73% (rounded of to nearest integer)
		numbers whose value is higher than 5 and 27% numbers with value less than 5.

   
 The main section is enclosed under "if __name__ == '__main__': " block to make sure that the statements within this block are only executed when
 this module is run as a main module and not when it is imported by some other module. 
