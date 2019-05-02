print('拆炸彈')
import random
start = int(input('請設定隨機整數最小值: '))
end = int(input('請設定隨機整數最大值: '))

puzzle = random.randint(start, end)
count = 0
while True:
	pwd = input('請猜出範圍中的隨機整數: ')
	pwd = int(pwd)
	count = count + 1
	if pwd == puzzle:
		print('恭喜猜對了!')
		print('已經試了', count, '次')
		break
	elif pwd > puzzle:
		print('比' ,pwd ,'還要小')
	elif pwd < puzzle:
		print('比' ,pwd ,'還要大')
	print('已經試了', count, '次')