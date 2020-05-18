print('prime factorazation begins ')


def prime_check(num):
    for number in range(2,num):
        if num%number == 0 :
            return False
        
        return True 


def factorazation_begins(number):
    control = True
    LCM = []
    num = number  
    while control:
        if num%2 == 0:
            LCM.append(2)
            num = num/2
        elif num%3 == 0:
            LCM.append(3)
            num = num/3    
        elif num%5 == 0:
            LCM.append(5)
            num = num/5
        elif num%7 == 0:
            LCM.append(7)
            num = num/7
        elif num%13 == 0:
            LCM.append(13)
            num = num%13
        elif num in [1,2,3,5,7,11] or prime_check(num):
            LCM.append(num)
            break
            
    return LCM

def main():
    number = int(input('Enter number here '))
    result = factorazation_begins(number)
    return result

print(main())