import numpy as np
file = np.loadtxt('rows.txt')
diff_sum = 0
for line in file:
    print("Max:",int(max(line)),"Min:",int(min(line)))
    diff = int(max(line)) - int(min(line))
    print("Difference:",diff)
    diff_sum = diff_sum + diff
print("Sum of all differences:",diff_sum)
