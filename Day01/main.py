file = open('input.txt', 'r')

input = file.read().splitlines()
l1 = []
l2 = []

for el in input:
    l1.append(el.split('   ')[0])
    l2.append(el.split('   ')[1])
    
l1.sort()
l2.sort()

def solve1():

    answer = 0

    for i in enumerate(l1):
        answer += abs(int(l1[i[0]]) - int(l2[i[0]]))

    print(answer)

def solve2():
    similarity = 0
    
    for i in enumerate(l1):
        cnt = 0
        for j in enumerate(l2):
            if i[1] == j[1]:
                cnt += 1
        
        similarity += int(i[1]) * cnt

    print(similarity)


def main():
    solve1()
    solve2()

main()