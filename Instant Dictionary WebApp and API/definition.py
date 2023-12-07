

# this file contains the definition class

# importing libraries
import pandas

class Definition:
    """
    This class contains the term that needs to be searched on the dictionary.
    """

    # constructor
    def __init__(self, term):
        self.term = term

    # get()
    def get(self):
        """
        This function looks the definition of self.term and returns it.
        :return:
        """
        # creating a dataframe object
        df = pandas.read_csv("data.csv")
        # now that we have our dataframe object,
        # we can look into the dictionary for the term and
        # return it

        # looking in the dictionary
        answer = tuple(df.loc[df.word == f"{self.term}"]['definition'])
        return answer


if __name__ == "__main__":
    d = Definition("sun")
    print(d.get())