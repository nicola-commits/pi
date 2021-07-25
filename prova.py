def pi_place_cal():
    num_pi= '3.141592653589793238462643383279502884197169399375105820974944'
    lenght_pi = len(num_pi)
    decimal_input = int(input("What will be the number to stop Pi?____"))

    while decimal_input >= lenght_pi:
        try:
            decimal_input = int(input("Enter a lower number please: "))
        except ValueError:
            continue

    #you can remove the else as you can't go on without a valid input
    decimal_input+=1
    Find_PI_to_the_Nth_digit = num_pi[:decimal_input] #you can remove that zero
    print(Find_PI_to_the_Nth_digit)
if __name__ == '__main__':
    pi_place_cal()