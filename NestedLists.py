#Nested Lists
# Link : hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    arr=[]
    m = []
    p=0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([])
        m.append([])
        arr[p] = [name,score]
        m[p] = score
        p+=1
    m.sort()
    arr.sort()
    m= list(dict.fromkeys(m))
    sec = m[1]
    for i in arr:
        if(sec==i[1]):
            print(i[0])
    
