try:
    val = float(input("Please enter the Value to be converted : "))
except ValueError:
    # Correct pattern check
    print("Incorrect value please enter the value in the format of xxxxxxxx.yy where x and y > 0 and < 9")
    exit()
except:
    print("Something went wrong")
    print(e)
    exit()
stringVal = str(val)
decimalString = ""

# Dictionary holding number to word convertion  
words = { 0:"", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninty" }

# Max limit verification
if (len(str(int(val))) > 8):
    print(val)
    print("Value is Not supported please choose a number between 0.00 and 9,99,99,999.99")
    exit()

# Positive value check
if (val <= 0):
    print("Value should be non-zero positive")
    exit()



# Check is decimal point exists, if yes then conver the digits as expected by the output.
#   decimalString hold the final converted value

if ("." in stringVal) :
    decimalVal = stringVal.split(".")[1]
    stringVal = stringVal.split(".")[0]
    if(int(decimalVal) >=100 or int(decimalVal) < 0 or len(decimalVal) >2):
        print("Invalid Paise value",decimalVal ,"please give a value between 0, 99")
        exit()
    if(int(decimalVal) != 0 ):
        decimalString = decimalVal+"/100"

# NOTE : After this the decimal point is eleminated from stringVal and expected result for paise is stored under "decimalString" variable

# Function ValueToSting
#   Input -       value which is an integer in the range of 0 - 99.
#   Description - converts the digits to words using the words dictionary defined above
#   Output -      string of coverted number

def ValueToSting(value):
    if (value == 0):
        return ""
    if (value >= 1 and value <= 20):
        return words[value]
    if (value > 20 and value <= 99):
        result = words[value%10]
        value = value - value%10
        result = words[value%100] + " " + result
        return (result)

# Function getTotalValue
#   Input -       takes a string which consists of an value between 0 and 99999999
#   Description - converts the digits to words by spliting them on the basis of the length 
#                 and using the words dictionary defined above.
#   Output -      string of coverted number

def getTotalValue(stringVal) :
    lengthOfNumber = len(stringVal)
    intValue = int(stringVal)
    resultString = ""
    crore = " Crore "
    lakh = " Lakh "
    thousand = " Thousand "
    hundreds = " Hundred And "
    
    while (lengthOfNumber > 0):
        if lengthOfNumber <= 2:
            resultString = resultString + ValueToSting(intValue)
            lengthOfNumber = 0
        if lengthOfNumber == 3:
            tmpValue = intValue - intValue % 100
            tmpValue = int(tmpValue / 100)
            intValue = intValue % 100
            resultString = resultString + ValueToSting(tmpValue) + hundreds
            lengthOfNumber = 2
        if lengthOfNumber >=4 and lengthOfNumber <=5:
            tmpValue = intValue - intValue % 1000
            tmpValue = int(tmpValue / 1000)
            intValue = intValue % 1000
            resultString = resultString + ValueToSting(tmpValue) + thousand
            lengthOfNumber = 3
        if lengthOfNumber >=6 and lengthOfNumber <=7:
            tmpValue = intValue - intValue % 100000
            tmpValue = int(tmpValue / 100000)
            intValue = intValue % 100000
            resultString = resultString + ValueToSting(tmpValue) + lakh
            lengthOfNumber = 5
        if lengthOfNumber == 8:
            tmpValue = intValue - intValue % 10000000
            tmpValue = int(tmpValue / 10000000)
            intValue = intValue % 10000000
            resultString = resultString + ValueToSting(tmpValue) + crore
            lengthOfNumber = 7
    return resultString

# Function numberToIndianCurrencyConvert
#   Input -       value which is an integer
#   Description - converts the given interger into indian currency format
#   Output -      string of value in the format of x,xx,xx,xxx.yy

def numberToIndianCurrencyConvert(number):
    s, *d = str(number).partition(".")
    r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
    return "".join([r] + d)

print("Value recived = " , numberToIndianCurrencyConvert(val))
print("Rs. " + getTotalValue(stringVal) + " " + decimalString + " ONLY")
    