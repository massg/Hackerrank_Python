#Find the Runner-Up Score!
#Link : hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr = list(dict.fromkeys(arr))  # to remove duplicates
    print(arr[-2]) # second last element in the sorted list
