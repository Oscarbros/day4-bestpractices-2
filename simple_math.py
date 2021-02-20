"""
A collection of simple math operations
"""

def simple_add(a,b):
    '''Sums two numbers.
    
    Sums the variables a and b and then returns the sum.
    
    Parameters
    ----------
    a : int, float
        First term in the addition statement.
    b 
        Second term in the addition statement.
        
    Returns
    -------
    int, float
        Sum of parameters a and b.
        
    Examples
    --------
    >>> simple_add(1,1)
    2
    '''
    return a+b

def simple_sub(a,b):
    '''Subtracts two numbers.
    
    Subtracts b from a and then returns the difference.
    
    Parameters
    ----------
    a : int, float
        First term in the subtraction statement.
    b 
        Second term in the subtraction statement.
        
    Returns
    -------
    int, float
        Returns difference between a and b.
        
    Examples
    --------
    >>> simple_sub(1,1)
    0
    '''
    return a-b
    
def simple_mult(a,b):
    '''Multiplies two numbers.
    
    Multiples the variables a and b and then returns the product.
    
    Parameters
    ----------
    a : int, float
        First factor in the multiplication statement.
    b 
        Second factor in the multiplication statement.
        
    Returns
    -------
    int, float
        Product of factors a and b.
        
    Examples
    --------
    >>> simple_mult(4,3)
    12
    '''
    return a*b
def simple_div(a,b):
    '''Divides two numbers.
    
    Divides the numerator a with the denominator b and then returns their 
    fraction.
    
    Parameters
    ----------
    a : int, float
        Numerator in the division statement.
    b 
        Denominator in the division statement.
        
    Returns
    -------
    int, float
        Fraction of numerator a and denominator b.
        
    Examples
    --------
    >>> simple_div(100,10)
    10
    '''
    return a/b

def poly_first(x, a0, a1):
    '''Evaluates first degree polynomial.
    
    Evaluates a first degree polynomial to provide information where f(x) is 
    in relation to x along the line.
    
    Parameters
    ----------
    x : int, float
        Variable in the first degree polynomial.
    a0 
        Constant that intersects the y-axis when x = 0.
    a1
        Constant that represents the slope of the polynomial.
        
    Returns
    -------
    int, float
        f(x), which is the evaluated form of the polynomial.
        
    Examples
    --------
    >>> poly_first(1,10,-3)
    7
    '''
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    '''Evaluates second degree polynomial.
    
    Evaluates a second degree polynomial to provide information where f(x) is 
    in relation to x. To evaluate the first degree part of the polynomial the 
    function calls poly_first(x, a0, a1). More information about that function
    is found within that function's documentation.
    
    Parameters
    ----------
    x : int, float
        Variable in the second degree polynomial.
    a0 
        Constant controlling the height of the polynomial.
    a1
        Constant that is involved in controlling the location where the axes 
        are symmertical.
    a2
        Constant controlling the curvature and location where the axes are 
        symmetrical.
    
    Returns
    -------
    int, float
        f(x), which is the evaluated form of the polynomial.
        
    Examples
    --------
    >>> poly_second(10,2,-3,1)
    18
    '''
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
