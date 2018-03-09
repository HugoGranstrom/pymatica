def work(a, b):
    a = int(a)
    b = int(b)
    return [a * b, True]
    
def run():
    output = 1
    nums = input("Write the numbers you want to multiply separated by spaces:\n")
    nums = nums.split(" ")
    for i in range(0, len(nums)):
        current = int(nums[i])
        output *= current
    print(output)
