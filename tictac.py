nums = [1,2,3,4,5,6,7,8,9]
i = 0
check = False
def grid():
    for items in  nums:
        if i % 3 !=0:
            print(f"{items}|")
            i= i+ 1
        else:
            print("-+-+-")
            i= i+ 1

def xchoice(i):
    i = i-1
    nums[i] = "x"

def ochoice(i):
    i= i-1
    nums[i] = "o"

def check():
    if nums[0] == nums[1] and nums[2] == nums[1]:
        return True
    elif nums[0] == nums[3] and nums[3] == nums[6]:
        return True
    elif nums[0] == nums[4] and nums[4] == nums[8]:
        return True
    elif nums[1] == nums[4] and nums[4] ==nums[7]:
        return True
    elif nums[2] == nums[5] and nums[8]== nums[5]:
        return True
    elif nums[2]==nums[4]and nums[4] == nums[6]:
        return True
    elif nums[3] == nums[4] and nums[4]==nums[5]:
        return True
    elif nums[6] == nums[7] and nums[7]== nums[8]:
        return True
    else:
        return False
    

def main():
    while check!= True:
        grid()
        user = int(input("x's turn to choose a square(1-9): "))
        xchoice(user)
        check = check()
        grid()
        user = int(input("o's turn to choose a square(1-9): "))
        ochoice(user)
        check = check()
    print("Good Game. Thanks for playing!")