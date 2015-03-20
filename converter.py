#tested using python 2.7.6
def converterFromRomanToArabic(romanValue):
    romanNumbers = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    res = 0
    tempRes = 0
    temp = 0
    for value in romanValue:
        decimal = romanNumbers[value]
        if temp < decimal:
            temp = temp * -1
        tempRes = tempRes + temp
        temp = decimal    
    return tempRes + temp

if __name__ == '__main__':
    print converterFromRomanToArabic('XLIV')
    print converterFromRomanToArabic('VIII')
    print converterFromRomanToArabic('XX')
    print converterFromRomanToArabic('MCMLXLIX')
    print converterFromRomanToArabic('XIX')    