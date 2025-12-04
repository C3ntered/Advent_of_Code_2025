def Part1 ():
    """ 
    Function to see when you spin to zero and you return the amount of times you did

    precondition: num is an int between 0-99
    """
    num = 50 #Start at number 50

    count = 0

    with open ('Rotation.txt') as f:
        for line in f:
            line = line.strip()

            if line[0] == 'L':
                num -= int(line[1:])
            elif line[0] == 'R':
                num += int(line[1:])

            if  num >= 100:
                num = (num) % 100
            elif num < 0:
                num = (num) % 100
            
            if num == 0:
                count += 1

    print (count)
                

def Part2():
    """
    Count the number of times you pass zero or are on zero
    """
    num = 50 #Start at number 50

    count = 0 #Counts the number of times it passes zero

    with open ('Rotation.txt') as f:
        for line in f:
            line = line.strip()

            if line[0] == 'R':
                step = 1  
            else:
                 step = -1

            for _ in range(int(line[1:])):
                num = (num + step) % 100
                if num == 0:
                    count += 1
        
    print (count)

x = Part1()
y = Part2()