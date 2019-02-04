 def karatsuba(x,y):

        """Karatsuba multiplication algorithm.
        Return the product of two numbers in an efficient manner
        @author Shashank
        date: 23-09-2018
        Hello
        Parameters
        ----------
        x : int
            First Number 
        y : int
            Second Number   

        Returns
        -------
        prod : int
               The product of two numbers 

        Examples
        --------
        >>> import Karatsuba.karatsuba
        >>> a = 1234567899876543211234567899876543211234567899876543211234567890
        >>> b = 9876543211234567899876543211234567899876543211234567899876543210
        >>> Karatsuba.karatsuba(a,b)
        12193263210333790590595945731931108068998628253528425547401310676055479323014784354458161844612101832860844366209419311263526900
        """
        if len(str(x)) == 1 or len(str(y)) == 1:
            return x*y
        else:
            n = max(len(str(x)), len(str(y)))
            m = n/2

            a = x/10**m
            b = x%10**m
            c = y/10**m
            d = y%10**m

            ac = karatsuba(a,c)                             #step 1
            bd = karatsuba(b,d)                             #step 2
            ad_plus_bc = karatsuba(a+b, c+d) - ac - bd      #step 3
            prod = ac*10**(2*m) + bd + ad_plus_bc*10**m     #step 4
            return prod