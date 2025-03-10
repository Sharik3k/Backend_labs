def possible_games_sum(filename):
    limits = {'red': 12, 'green': 13, 'blue': 14}
    total = 0  
    
    with open("lab05/input (3).txt") as file:
        for line in file:
            game_id, rounds = line.split(": ")
            game_id = int(game_id.split()[1])  
            
            rounds_list = []
            for round in rounds.split("; "):
                for pair in round.split(", "):  
                    num, color = pair.split()  
                    rounds_list.append((int(num), color)) 
            
        
            if all(num <= limits[color] for num, color in rounds_list):
                total += game_id  
    
    return total

print(possible_games_sum("lab05/input (3).txt"))