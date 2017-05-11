import random
import time

nif_letter_mask =['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)

def randomNif():
    nif_number = random.randint(10000000,99999999)
    nif_letter = nif_letter_mask[nif_number % 23]
    return str(nif_number)+nif_letter;

def alignmentProductCategory(idProduct, productCategoy):
    if idProduct in range (0,2):
        return productCategoy[0]
    else:
        if idProduct in range (2,23):
            return productCategoy[1]
        else:
            if (idProduct in range (23,27)):
                return productCategoy[2]
            else:
                if (idProduct in range (27,39)):
                    return productCategoy[3]
                else:
                    if (idProduct in range (39,42)):
                        return productCategoy[4]
                    else:
                        if (idProduct in range(42,46)):
                            return productCategoy[5]
    return None;