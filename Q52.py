
quiz = open("text1.txt")

def double_print(count, line):
    for line in quiz:
        while count > 0:
            print(line)
            count -= 1

double_print(2, "quiz")
