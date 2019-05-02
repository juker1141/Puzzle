print('拆炸彈')
import random
start = int(input('請設定隨機整數最小值: '))
end = int(input('請設定隨機整數最大值: '))
message = '請猜出' + str(start) + '-' + str(end) + '中的隨機整數: '

puzzle = random.randint(start, end)
count = 0
while True:
	pwd = input(message)
	pwd = int(pwd)
	count = count + 1
	if pwd == puzzle:
		print('恭喜猜對了!')
		print('總共試了', count, '次')
		break
	elif pwd > puzzle:
		print('比' ,pwd ,'還要小')
	elif pwd < puzzle:
		print('比' ,pwd ,'還要大')
	print('總共試了', count, '次')