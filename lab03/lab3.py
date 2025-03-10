
def task1(lines):
        total = 0  #зберігання загальної суми
        for line in lines:
            number = []  # цифр з рядка
            for char in line:
                if char.isdigit():  # Перевіряємо, чи є символ цифрою
                    number.append(char)  # Додаємо цифру до списку
            if number:  
                first_digit = number[0]  
                last_digit = number[-1]
                number = int(first_digit + last_digit)  
                total = total + number 
        return total  
with open('lab03/input (1).txt', 'r') as txt:
        lines = txt.readlines() 
    
result = task1(lines)
print(result) 