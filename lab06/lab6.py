with open("lab06/input (4).txt", "r") as file:
    lines = file.readlines()


points_X = 1  
points_Y = 2  
points_Z = 3  

total_score = 0  

for line in lines:
    opponent_choice, my_choice = line.split()  
    
    
    if (opponent_choice == 'A' and my_choice == 'X') or \
       (opponent_choice == 'B' and my_choice == 'Y') or \
       (opponent_choice == 'C' and my_choice == 'Z'):
        round_score = 3 
    elif (opponent_choice == 'A' and my_choice == 'Y') or \
         (opponent_choice == 'B' and my_choice == 'Z') or \
         (opponent_choice == 'C' and my_choice == 'X'):
        round_score = 6  
    else:
        round_score = 0  
    

    if my_choice == "X":
        shape_score = points_X
    elif my_choice == "Y":
        shape_score = points_Y
    else:
        shape_score = points_Z
    

    total_score += round_score + shape_score


print("Підсумковий рахунок за всі раунди:", total_score)