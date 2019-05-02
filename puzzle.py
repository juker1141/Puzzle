print('拆炸彈')
import random
puzzle = random.randint(1,10)

while True:
	pwd = input('請猜出1-100中的隨機整數: ')
	pwd = int(pwd)
	if pwd == puzzle:
		print('恭喜猜對了!')
		break
	elif pwd > puzzle:
		print('比' ,pwd ,'還要小')
	elif pwd < puzzle:
		print('比' ,pwd ,'還要大')