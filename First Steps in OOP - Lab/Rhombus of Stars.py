num = int(input())
[print(' ' * (num - n) + '* ' * n) for n in range(num+1)]
[print(' ' * (num - n) + '* ' * n) for n in range(num-1, 0, -1)]
