import math
#6
def ReverseString(UserInput):
    return UserInput[::-1]

#print(ReverseString(input()))
#7
def has_33(nums):
    if len(nums) == 1:
        return False
    elif len(nums) == 2:
        return nums[0] == 3 and nums[1] == 3
    else:
        first=nums[0]
        for i in range(1,len(nums)-1):
            if first == 3 and nums[i] == 3:
                return True
            first = nums[i]

#print(has_33([1,3,3,1]))

#8
def spy_game(List:list)->(bool):
    if len(List) < 3:
        return False
    else:
        for i in range (len(List)-2):
            if List[i] == 0:
                if List[i+1] == 0 and List[i+2] == 7:
                    return True
    return False 
            
#print(spy_game([1,0,0,0,0,7,3,2]))
#9

def VolumeOfSphere(radius):
    return (4/3)*(radius**3)*math.pi

#print(VolumeOfSphere(5))



#11

def palindrom(string):
    if string == string[::-1]:
        print("YES")
    else:
        print("NO")


string = input()
palindrom(string)


#12


def histogtram(*x):
    for i in x:
        print(i * '*')
        
x, y, z = int(input()), int(input()), int(input())
histogtram(x, y, z)


