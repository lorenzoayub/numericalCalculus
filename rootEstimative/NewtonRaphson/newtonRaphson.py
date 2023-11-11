from typing import Union, Callable, Any


def newtonRaphson(function: Callable[[float], float], initialEst: Union[int, float], rootTol: float, yTol: float, maxIter: int, verbose=False) -> dict[str, Any]:
    """Function that estimates functions root by Newton-Raphson method

    Args:
        function (Callable[[float], float]): function whose root should be estimated
        initialEst (Union[int, float]): root initial estimative
        rootTol (float): tolerance for successive root estimatives
        yTol (float): tolerance of function's absolute value (<<1)
        maxIter (int): maximum number of iterations
        verbose (bool, optional): if True, prints the current iteration + current root estimative +
#             current function value in when  x=root_estimative. Defaults to False.

    Returns:
        dict[str, Any]: dictionary containing final results data. It follows the format:
            {'iterations': 10, 'root': 3.1415962122769004, 'y value': 1.1599610161283636e-12, 'Stop Condition Code': 1}

            such that,
                iterations -> number of iterations ran
                root -> final estimative for function root
                y value -> function evaluated at 'root' (above)
                Stop Condition Code -> code that inform how the function stopped
                                    (1 = Number of iterations exceeded;
                                    2 = Function value at current root estimative <= yTol;
                                    3 = (x_iter - x_pastIter) < rootTol .)
    """
    def functionDerivative(x: Union[int, float], h=1e-6, zeroSlope=1e-7) -> float:
        """Numerically calculates the derivative function value at point x, using progressive approximation.

        Args:
            x (Union[int, float]): x value of the derivative function
            h (float, optional): value used for approximating function derivate, such that 
                                f'(x) = lim{h --> 0} ( f(x+h) - f(x) )/h
                                Defaults to 1e-6.
            zeroSlope (float, optional): derivative value considered for method non-convergence. When the 
                                        derivate value is << 1, the method may diverge. Defaults to 1e-7

        Returns:
            float: derivative value at x
        """
        derivativeValue: float = (1/h)*(function(x+h) - function(x))
        assert derivativeValue > zeroSlope
        return derivativeValue
    
    
    # Defining parameters before entering loop
    yValue: float = function(initialEst)
    x_pastIter: float = initialEst
    x_iter: float = initialEst

    # Defining iteration counter
    iterCounter: int = 0

    
    while iterCounter < maxIter:# Stop Condition 01: Number of iterations exceeded
        
        stopCode: int = 1


        # Stop Condition 02: Function value at current root estimative is close enough to zero
        if abs(yValue) <= yTol:
            stopCode: int = 2
            break
        
        # Updating iteration counter
        iterCounter += 1

        # Updating current and past iteration root estimatives 
        x_pastIter = x_iter
        x_iter = x_pastIter - minhaFuncao(x_pastIter)/functionDerivative(x_pastIter)

        # Updating function value at current root estimative
        yValue = function(x_iter)
        
        # If verbose is True, print iteration data
        if verbose:
            print(f'Iter: {iterCounter}\tx_k = {x_iter}\ty_k = {yValue}')

        # Stop Condition 03: Difference between current and past iteration root estimatives is too small
        if abs(x_iter - x_pastIter) < rootTol:
            stopCode: int = 3
            break
    

    # Returning results
    return {'iterations': iterCounter, 'root': x_iter, 'y value': yValue, 'Stop Condition Code': stopCode} 

if __name__ == '__main__':
    print(newtonRaphson(function=minhaFuncao, initialEst=8.31, rootTol=1e-7, yTol=1e-7, maxIter=20))

