#given code 
#def remove_even(numbers):
#    for n in numbers:
    #     if n%2==0:
    #         numbers.remove(n)
    # return numbers
#this code is iterating over the same array which we are going to change so it doesnt work
#In the below code i iterated over a copy

def remove_even(numbers):
    for n in numbers[:]:
        if n%2==0:
            numbers.remove(n)
    return numbers
nums1=[2,4,6,8]
nums2=[1,2,3,4,5,6,7,8,9,10]
print(remove_even(nums1))
print(remove_even(nums2))
