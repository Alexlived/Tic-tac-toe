import random
chars = ['x','o']
grid = []
valid_pos = []
for i in range(9):
    valid_pos.append(int(i+1))
for i in range(9):
   grid.append(' ')
def print_layers():
    layer1 = grid[:3]
    layer2 = grid[3:6]
    layer3 = grid[6:9]
    print('|'.join(layer1).upper())
    print('|'.join(layer2).upper())
    print('|'.join(layer3).upper())
def u_char():
    while True:
        print('Would you like to be X or O')
        u_ch = input('>').lower()
        if u_ch not in chars:
            print('That is not a valid choice,try again')
        else:
            chars.remove(u_ch)
            return u_ch
def u_input():
    while True:
        print('Where would you like to go?(1 for top left and 9 for top right)')
        u_input =input('>')
        u_input = int(u_input)
        if u_input not in valid_pos:
            print('Not a valid position,Try again')
        else:
            return u_input
def win_check(char):
    grid_d = grid[:]
    for i in range(len(grid_d)):
        if grid_d[i] == char:
            grid_d[i] = True 
        else:
            grid_d[i] = False
    char = True
    win=False
    if all(grid_d[:3]) == char:
        win = True
    elif all(grid_d[3:6]) == char:
        win = True
    elif all(grid_d[6:9]) == char:
        win = True
    elif all(grid_d[0:7:3])  == char:
        win = True
    elif all(grid_d[1:8:3]) == char:
        win = True
    elif all (grid_d[2:9:3]) == char:
        win = True
    elif all(grid_d[0:9:4]) == char:
        win = True
    elif all(grid_d[2:8:2]) == char:
        win = True
    else:
        win = False
    return win
def main():
    us_ch = u_char()
    if us_ch == 'x':
        comp_char = 'o'
    else:
        comp_char = 'x'
    while True:
        print_layers()
        us_input = u_input()
        grid[int(us_input)-1] = us_ch
        valid_pos.remove(us_input)
        if win_check(us_ch) == True:
            print_layers()
            print('You won!Game over')
            quit()       
        else:
            comp_choice = random.choice(valid_pos)
            grid[int(comp_choice)] = comp_char
            if comp_choice in valid_pos:
                valid_pos.remove(comp_choice+1)
            if win_check(comp_char) == True:
                print_layers()
                print('You lost!Game over')
                quit()
                

main()   
