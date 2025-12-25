if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    unique_scores = list(set(arr)) 
  #What a set function in python does is that so when you a list,tuple or a string it creates an empty set and adds only the unique elements into the set 

    if len(unique_scores) < 2:
        print("No runner up") 
  #Here we are putting up a condition if the length of the set unique_scores id less that 2 then it becomes an invalid set cause we need a second highest number so if the unique set has only 1 number eventhough if the initial array has 5 of them which practically the same i.e, let's say the array is = [5,5,5,5,5] then this scenario comes into play and it automatically get rejected as it does not satisfy the criteria
    else:
        unique_scores.sort(reverse=True)
  #The reverse = True in python arranges the list in descending order .sort is generally used for lists and for other datatypes it variates.
        print(unique_scores[1])
