#return the number of 1s from a binary resulted from an integer number
def number_of_ones(number):
    sum_1 = 0
    while (number > 0):
        sum_1+=number&1
        number>>=1
    return sum_1

def main():
    number = input("number=?")
    print (number_of_ones(int(number)))

main()
    