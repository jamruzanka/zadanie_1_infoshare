import numpy as np
file = np.loadtxt('rows.txt')
diff_sum = 0
for line in file:
    diff = int(max(line)) - int(min(line))
    print("Max:",int(max(line)),"Min:",int(min(line)),"Difference:",diff)
    diff_sum = diff_sum + diff
print("\nThe sum of all differences:",diff_sum)
