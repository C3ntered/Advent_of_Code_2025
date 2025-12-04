def inValidID(filename):
    """
    This is a function that checks invalid codes then returns the total value of these codes.

    Duplicated numbers look like 11, 99, 222222, 1010, 88, so its even and has two segmants that are the same
    within the range of the the codes first half and second half.

    parameter codes: 
    precondition codes: Codes is a valid txt file that is not empty.
    """

    accumulated = 0
    
    with open(filename) as f: #Opens file and helps sepeate each one into a list.
        line = f.readline().strip()
        ranges = line.split(',')

        for code_range in ranges: #Goes through and reates a range that the codes can be in.
            dash_index = code_range.find('-')
            start = int(code_range[:dash_index])
            end = int(code_range[dash_index+1:])
            
            for num in range(start, end + 1): #Checks every number in the range.
                s_num = str(num)
                length = len(s_num)
                
                if length % 2 != 0: #Is the number odd? passes through because you can't tell where half is.
                    continue
                half_index = length // 2
                first_half = s_num[:half_index]
                second_half = s_num[half_index:]

                if first_half == second_half: #Checks if both halfs our equal and accumulates if they are equal.
                    accumulated += num
                    
    return accumulated


x = inValidID('Codes.txt')

def duplicates(filename):
    """
    This is a function that checks invalid codes then returns the total value of these codes.

    Duplicated numbers look like 11, 998, 222222, 1010, 88, so its even and has two segmants that are the same
    within the range of the the codes first half and second half.

    parameter codes: 
    precondition codes: Codes is a valid txt file that is not empty.
    """

    accumulated = 0
    
    with open(filename) as f: #Opens file and helps sepeate each one into a list.
        line = f.readline().strip()
        ranges = line.split(',')

        for code_range in ranges: #Goes through and reates a range that the codes can be in.
            dash_index = code_range.find('-')
            start = int(code_range[:dash_index])
            end = int(code_range[dash_index+1:])
            
            for num in range(start, end + 1): #Checks every number in the range.
                s_num = str(num)
                length = len(s_num)
                found_pattern = False  #Checks if there is a patter in the string
                for pattern_len in range(1, (length // 2) + 1): #Checks for the pattern in range
                    if length % pattern_len == 0:
                        pattern = s_num[:pattern_len]
                        repeats = length // pattern_len
                        
                        if pattern * repeats == s_num: #Exits for loop for checking and goes to accumulator
                            found_pattern = True
                            break # Found a match, stop checking sizes
                
                if found_pattern: #accumulates if found true
                    accumulated += num
        return accumulated

y = duplicates('Codes.txt')

print (x,y)