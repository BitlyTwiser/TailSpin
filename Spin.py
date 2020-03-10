import random
import operator
import time


class CoinFlip():

    def __init__(self):
        self.option1 = str(input('Heads: '))
        self.option2 = str(input('Tails: '))
        self.choices = {self.option1: 0, self.option2: 0}
        self.entropy = random.randint(100_000, 10_000_000)
        self.heads = """
        _.-'~~`~~'-._
     .'`  B   E   R  `'.
    / I               T \\
  /`       .-'~"-.       `\\
 ; L      / `-    \      Y ;
;        />  `.  -.|        ;
|       /_     '-.__)       |
|        |-  _.' \ |        |
;        `~~;     \\        ;
 ;  INGODWE /      \\)P    ;
  \  TRUST '.___.-'`"     /
   `\                   /`
     '._   1 9 9 7   _.'
        `'-..,,,..-'`
"""
        self.tails = """
        _.-'~~`~~'-._
     .'`      S      `'.
    / U               A \\
  /`                     `\\
 ;     E Pluribus Unum     ;
;       ''''''''''''''      ;
|       ''          ''      |
|       ''    \/    ''      |
;       ''    $$    ''      ;
 ;      ''    ''    ''     ;
  \     --------------    /
   `\                   /`
     '._   1 9 9 7   _.'
       `'-..,,,..-'`
"""

    def flip_coin(self, object):
        """
        --------------
        Performs final coin flip.
        --------------
        """
        print('Printing Details..!\n')
        time.sleep(1)
        if object == self.option1:
            print(f'Heads! Option {object} is the winner\n{self.heads}')
            print(f'Heads beat tails by {int(self.choices[object]-self.choices[self.option2])} points')
        else:
            print(f'Tails! Option {object} is the winner\n{self.tails}')
            print(f'Tails beat heads by {int(self.choices[object]-self.choices[self.option1])} points')
        print(f'The object which occured the most in time and space is {object} with the odds being of 1 in {int(self.choices[object]/2)}!!.\n')
        print(f'Total values of both given items: {self.choices}\n')

    def compute_entropy(self):
        """
        --------------
        Base check is performed to validate that data input is valid.
        --------------
        Performs computation to generate the coin flip data values.
        --------------
        """

        def _higher_val(object):
            """
            --------------
            Determine which value from a given hashtable is greater in value.
            --------------
            """
            # Will fail of object is not dict..
            try:
                assert isinstance(object, dict)
            except AssertionError:
                print('It appears that the object being utilized here is not a dict.. please validate this.')
            else:
                return max(object.items(), key=operator.itemgetter(1))[0] # Return item with max value.
        if len(self.option1) <= 0 or len(self.option2) <= 0 or self.option1 is None or self.option2 is None or self.option1 == '' or self.option2 == '':
            raise Exception('The given value is to damn small, try to cultivate its growth and try again give it another go!')
        else:
            print('\nPerforming coin flip and computation..Give us a few seconds to perform actions!\n')
            # Enumerate was used here for I did not want to capture the result in a var, but I wanted to know the integer value of the value used for entropy.
            for i in range(1, self.entropy):
                if random.choice([self.option1, self.option2]) == self.option1:
                    self.choices[self.option1] += 1
                else:
                    self.choices[self.option2] += 1  
        return self.flip_coin(_higher_val(self.choices))


if __name__ == '__main__':
    CoinFlip().compute_entropy()
