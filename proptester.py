import random
import numpy as np

results = []
for i in range(0,10000):
    results.insert(0, max(random.randint(1,101),random.randint(1,101),random.randint(1,101)))

print(np.mean(results))