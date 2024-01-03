# entry for this contest: https://tweakers.net/partners/chipsoft-prijsvraag/
# Chris Idema ©2024

import math # needed for sqrt
import sys  # needed for argv


# lookup table for button coordinates
# follows this formula: [(i%3, i//3) for i in range(0,9)] 
# coordinates are in centimeters
button_coordinates_xy= ((0,0),(1,0),(2,0), 
                        (0,1),(1,1),(2,1),
                        (0,2),(1,2),(2,2))

# calculates the total distance in cm between a sequence of buttons in the list buttons_number_list     
def calc_total_length(buttons_number_list):
    # list needs at least two buttons:
    if len(buttons_number_list) <= 1: 
        print("Error: list needs at least two buttons")
        return 0
    
    total_distance = 0
    for i in range(1,len(buttons_number_list)):

        a = buttons_number_list[i-1] 
        b = buttons_number_list[i]

        # check if button number is an int:
        if type(a) != int or type(b) != int:
            print("Error: button number not an integer")
            return 0
        
        # check if buttons are different:
        if a == b:
            print("Error: same button twice in a row")
            return 0
        
        # check if buttons are in valid range:
        if a not in range(1,9+1) or b not in range(1,9+1):
            print("Error: button not in range of 1-9")
            return 0
               
        #print(f"distance between {a} and {b}: ", end='')
        a = button_coordinates_xy[a-1] # convert button number to 0-based index and look up the coordinates
        b = button_coordinates_xy[b-1] # convert button number to 0-based index and look up the coordinates
        distance = math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2) # calculate Euclidean distance
        #print(f"{distance} cm")
        total_distance += distance
    return total_distance


if __name__ == "__main__":
    #print(sys.argv)
    if len(sys.argv) > 1:
        # example: "python chipsoft_prijsvraag.py 5 8 7 4 2 6 9 5 1"
        input = [int(button) for button in sys.argv[1:]]
        #print(input)
        output = calc_total_length(input)
        print(f"{output} cm")        
    else:
        # no input given, so run examples
        example1_input = [5,8,7,4,2,6,9,5,1]
        example1_output = calc_total_length(example1_input)
        print(f"example 1 length: {example1_output} cm")

        example2_input = [1,2,3,6,9]
        example2_output = calc_total_length(example2_input)
        print(f"example 2 length: {example2_output} cm")
