from typing import Union, Callable
from math import copysign, log

Number = Union[int, float]


def fixedPoint(function: Callable, initialEstimative: Number, tolerance: float, verbose=False):

    def stopCriteria() -> bool:
        """Checks if the difference between two consecutive estimatives is
        small enough ( < tolerance )

        Returns:
            bool: returns True if the stop criteria has been reached. Otherwise,
            returns False
        """

        if abs(u - f_u) >= tolerance:
            return False
        else:
            return True

    def printValues() -> None:
        """Prints the current iteration value of u inputed in the function() and the expression result (f_u)
        """
        if verbose:
            print(f'u = {u}     f_u = {f_u}')

    # Assign the estimative inputed by the user as first value for u
    u: Number = initialEstimative

    # Calculate its respective expression result
    f_u: Number = function(u)

    # Print u and f_u
    printValues()

    # Repeat the iteration until stop criteria is reached
    while not stopCriteria():
        u = f_u
        f_u = function(u)
        printValues()

    return u

if __name__ == '__main__':
    print(fixedPoint(lambda x: 3*(0.1*x+1.7)/(1+log(x)), 1.2, 1e-5, True))
