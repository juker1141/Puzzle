print('拆炸彈')
import random
puzzle = random.randint(1,10)
count = 0
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
	count = count + 1
	print('已經試了', count, '次')