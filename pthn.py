import time

a = 0
while True:
	if a == 10000:
		break
	else:
		print(a)
		a+=1
		time.sleep(0.1)
