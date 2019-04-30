import random
start = input('請輸入開始值:')
end = input('請輸入結束值:')

start = int(start)
end = int(end)

if end <= start:
    end = input('請重新輸入結束值:')
    end = int(end)

r = random.randint(start, end)
count = 0
while True:
    count += 1 #count = count + 1
    num = input('請猜猜數字:')
    num = int(num)
    if num == r:
        print('你猜對了')
        print('您已經猜第', count, '次')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
    print('您已經猜第', count, '次')