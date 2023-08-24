from time import time
import cProfile
from pstats import Stats, SortKey
from numpy import random, sqrt, round
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS


def isperfect(n: int):
    """
        This function is the first helper. It takes an integer n and checks if n has a perfect square root or not.
        If n has a perfect square root, then it returns True and its perfect square root. If not, it returns False and n.

        INPUT: n as an integer.
        OUTPUT: a tuple (bool, int).

        Examples:
        isperfect(0) = (True, 0)
        isperfect(1) = (True, 1)
        isperfect(3) = (False, 3)
        isperfect(16) = (True, 4)
    """
    if n == 0 or n == 1:
        return (True, n)

    ### BEGIN CODE #####
    # Hint: you can use the range, or any sequence type. if you don't remember how it works, have a look at the documentation.
    for i in range(int(n/2)):
        if i**2 == n:  # replace None by the appropriate code.
            return (True, i)
    return (False, n)
    i = 0
    while (i**2 < n):  # and (i < int(n/2)): Why do you keep the two loops? are there not doing the same thing?
        i += 1

    if i**2 == n:
        return (True, i)
    else:
        return (False, n)
    ### END CODE #####


def getLowUpper(n: int): # This function would have been optimized too...
    """
        This function is the second helper. It takes an integer n and returns the lower and upper perfect square root to n.
        We will use two "while" loops here, but we could have used "for" loops or whatever.
        The first that will catch the first perfect square root is less than the square root of n.
        The second one will catch the first square root greater than the square root of n.

        INPUT: n as an integer.
        OUTPUT: a tuple (minsqrt:int, maxsqrt:int)

        Examples:
        getLowUpper(3) = (1,2)
        getLowUpper(15) = (3,4)
    """
    i = 1
    ### BEGIN CODE ####
    low = isperfect(n-i)
    upper = isperfect(n+i)

    while not low[0]:  # Hint: look at the second while loop.
        i += 1
        low = isperfect(n-i)

    i = 1
    while not upper[0]:
        i += 1
        upper = isperfect(n+i)

    # Hint: remember what is the output of helper 1.
    minsqrt, maxsqrt = low[1], upper[1]
    ### END CODE ####

    return minsqrt, maxsqrt


def mysqrt(n: int, error_threshold=0.000000001) -> float:
    """
        This function is the main function. It takes an interger n and returns the square root of n.
        We will use here the two helper functions we wrote previously.


        INPUT: n as an integer.
        OUTPUT: a float rst

        Examples:
        mysqrt(3) = 1.7320508076809347
        mysqrt(15) = 3.8729833462275565
    """

    ### BEGIN CODE ###
    if n == 0 or n == 1:  # Hint: remember to always start by basic case solution. for the square root problem, we have 0 and 1
        return n
    ### END CODE ###

    ### BEGIN CODE ###
    ### END CODE ###

    iteration = 0  # The variable is used to count the number of times we repeat the instructions in the while loop

    ### BEGING CODE ###
    rst = 1
    while abs(rst-(0.5*(rst+n/rst))):
        rst = 0.5*(rst+n/rst)
    ### END CODE ####

    return rst


def main():
    doc_ = """
                Welcome to the first Python assignment!!!\n
                You will write your first Python script that computes the square root of a given integer n.
                The template_hw1 provides you with the basic structure of a Python script. Please do not add anything
                out of ### BEGIND CODE ### and ### END CODE ###.

                Feel free to use print for debugging but remember to clean them up before your submission.

                NB: Your performance will not only be evaluated on your capacity to output good results.
                Please make sure you understand each line you code.
            """
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter,
                            argument_default=SUPPRESS, description=doc_)
    parser.add_argument(
        '--n', type=int, help="An integer input for which we compute the sqrt root.")
    args = parser.parse_args()
    input_n = args.n

    t0 = time()
    myvalue = mysqrt(input_n)
    t1 = time()-t0
    npvalue = sqrt(input_n)

    assert round(myvalue, 2) == round(
        myvalue, 2), "Input test failled. Please, check your script again. your sqrt = {} and numpy sqrt = {}".format(myvalue, npvalue)

    print("The input is n = {}".format(input_n))
    print("Your square root of {} is {}".format(input_n, myvalue))
    print("The numpy square root of {} is {}".format(input_n, npvalue))
    print("The error precision is ", abs(myvalue - npvalue))
    print("Runtime: %s sec." % (round(t1, 1)))

    first_test = random.randint(1, 100, 20)
    first_test_stat = 0
    for n in first_test:
        myvalue = mysqrt(n)
        npvalue = sqrt(n)
        if round(myvalue, 2) == round(sqrt(n), 2):
            first_test_stat = first_test_stat + 1

    if first_test_stat == len(first_test):
        print("All tests past.")
        print("Congratulation on achieving your first assignment.")
    else:
        success_rate = first_test_stat*100./len(first_test)
        print("Only {}% of the tests past".format(str(success_rate)))
        print("Please, check your code and try it again.")


if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = Stats(profiler).sort_stats(SortKey.CUMULATIVE)
    stats.print_stats(15)
