import random
import numpy as np

allnum = 113287
sample9 = random.sample(range(0,113287),int(allnum * 0.09))
sample8 = random.sample(sample9,int(allnum * 0.08))
sample7 = random.sample(sample8,int(allnum * 0.07))
sample6 = random.sample(sample7,int(allnum * 0.06))
sample5 = random.sample(sample6,int(allnum * 0.05))
sample4 = random.sample(sample5,int(allnum * 0.04))
sample3 = random.sample(sample4,int(allnum * 0.03))
sample2 = random.sample(sample3,int(allnum * 0.02))

sample_9 = []
sample_8 = []
sample_7 = []
sample_6 = []
sample_5 = []
sample_4 = []
sample_3 = []
sample_2 = []


for i in sample9:
	sample_9.append(i*5)
	sample_9.append(i*5+1)
	sample_9.append(i*5+2)
	sample_9.append(i*5+3)
	sample_9.append(i*5+4)

for i in sample8:
	sample_8.append(i*5)
	sample_8.append(i*5+1)
	sample_8.append(i*5+2)
	sample_8.append(i*5+3)
	sample_8.append(i*5+4)

for i in sample7:
	sample_7.append(i*5)
	sample_7.append(i*5+1)
	sample_7.append(i*5+2)
	sample_7.append(i*5+3)
	sample_7.append(i*5+4)

for i in sample6:
	sample_6.append(i*5)
	sample_6.append(i*5+1)
	sample_6.append(i*5+2)
	sample_6.append(i*5+3)
	sample_6.append(i*5+4)

for i in sample5:
	sample_5.append(i*5)
	sample_5.append(i*5+1)
	sample_5.append(i*5+2)
	sample_5.append(i*5+3)
	sample_5.append(i*5+4)

for i in sample4:
	sample_4.append(i*5)
	sample_4.append(i*5+1)
	sample_4.append(i*5+2)
	sample_4.append(i*5+3)
	sample_4.append(i*5+4)

for i in sample3:
	sample_3.append(i*5)
	sample_3.append(i*5+1)
	sample_3.append(i*5+2)
	sample_3.append(i*5+3)
	sample_3.append(i*5+4)

for i in sample2:
	sample_2.append(i*5)
	sample_2.append(i*5+1)
	sample_2.append(i*5+2)
	sample_2.append(i*5+3)
	sample_2.append(i*5+4) 

random.shuffle(sample_9)
random.shuffle(sample_8)
random.shuffle(sample_7)
random.shuffle(sample_6)
random.shuffle(sample_5)
random.shuffle(sample_4)
random.shuffle(sample_3)
random.shuffle(sample_2)

sample_9 = np.array(sample_9)
sample_8 = np.array(sample_8)
sample_7 = np.array(sample_7)
sample_6 = np.array(sample_6)
sample_5 = np.array(sample_5)
sample_4 = np.array(sample_4)
sample_3 = np.array(sample_3)
sample_2 = np.array(sample_2)


np.save("./selection/9.npy", sample_9)
np.save("./selection/8.npy", sample_8)
np.save("./selection/7.npy", sample_7)
np.save("./selection/6.npy", sample_6)
np.save("./selection/5.npy", sample_5)
np.save("./selection/4.npy", sample_4)
np.save("./selection/3.npy", sample_3)
np.save("./selection/2.npy", sample_2)