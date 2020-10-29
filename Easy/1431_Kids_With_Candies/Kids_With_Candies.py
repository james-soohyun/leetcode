# Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has. For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
def kidsWithCandies(candies, extraCandies):
    
    kidsArray=[]
    max = candies[0]
    for i in range(len(candies)):
        if max < candies[i]:
            max=candies[i]
    for i in range(len(candies)):
        if candies[i]+extraCandies < max:
            print('false', i, candies[i])
            kidsArray.append('false')
        else:
            print('true', i, candies[i])
            kidsArray.append('true')
    return candies