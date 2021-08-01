def get_primes(nums):
    for num in nums:
        flag = False
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    flag = True
                    break

        if not flag:
            if num not in [1, 0]:
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
