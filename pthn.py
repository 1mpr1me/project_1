import time

a = 0
while true:
	if a == 10000:
		break
	else:
		print(a)
		a+=1
		time.sleep(0.1)
