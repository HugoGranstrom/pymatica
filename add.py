def work(a, b):
    a = int(a)
    b = int(b)
    return [a + b, True]

def run():
    output = 0
    nums = input("Write the numbers you want to add separated by spaces:\n")
    nums = nums.split(" ")
    for i in range(0, len(nums)):
        current = int(nums[i])
        output += current
    print(output)
