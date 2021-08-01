def fibonacci():
    nums = [0, 1, 1]
    for n in nums:
        yield n
    while True:
        num = nums[-1] + nums[-2]
        nums.append(num)
        yield num


generator = fibonacci()
for i in range(5):
    print(next(generator))
