def maxValue(arrayOfNumbers):
    max = arrayOfNumbers[0]
    for i in arrayOfNumbers:
        if i > max:
            max = i
    return max

import numpy as np
file = np.loadtxt('rows.txt')
diff_sum = 0
for line in file:
    diff = int(maxValue(line)) - int(min(line))
    print("Max:",int(max(line)),"Min:",int(min(line)),"Difference:",diff)
    diff_sum = diff_sum + diff
print("\nThe sum of all differences:",diff_sum)
