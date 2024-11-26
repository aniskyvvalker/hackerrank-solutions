# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split(" "))

hyphen = "-"
bar = ".|."

bar_num = 1

welcome = hyphen * int((M-7)/2) + "WELCOME" + hyphen * int((M-7)/2)

emp = []

for line in range(N):
    # Number of .|. for each line
    hyphen_num_bar = int((M-3*bar_num)/2)
    # Line design
    line = hyphen*hyphen_num_bar + bar*bar_num + hyphen*hyphen_num_bar
    # Incrementing the number of .|.
    bar_num += 2

    if hyphen_num_bar == 3:
        emp.append(line)
        print(line)
        print(welcome)
        emp.reverse()
        for elm in emp:
            print(elm)
        break
    else:
        emp.append(line)
        print(line)


