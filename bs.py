
grid =[]
for i in range(9):
    grid.append(str(i))

def print_layers():
    layer1 = grid[:3]
    layer2 = grid[3:6]
    layer3 = grid[6:9]
    print('|'.join(layer1).upper())
    print('|'.join(layer2).upper())
    print('|'.join(layer3).upper())
print_layers()
print(grid[0:5:4])