def work(a, b):
    a = float(a)
    b = float(b)
    return [a + b, True]

def run():
    output = 0
    nums = input("Write the numbers you want to add separated by spaces:\n")
    nums = nums.split(" ")
    for i in range(0, len(nums)):
        current = float(nums[i])
        output += current
    print(output)
