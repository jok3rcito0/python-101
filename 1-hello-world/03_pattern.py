# Write code below 💖

current_number = 1

for line in range(1, 5): // here a fancy way to write 4 
    spaces = max(6 - 2 * (line - 1), 0) (we calculate the spaces on each line) 
    
    row = " " * spaces
    
    for i in range(line): (inception for other for to add the numbers depend the line, if line is equal 1, so current_number is 1 stop and star again. then if line 2 so add two numbers and start un 2 because the previous += add 1 to curren_number so 2, again 3 ) 
        row += " " + str(current_number)
        current_number += 1
    
    print(row)
