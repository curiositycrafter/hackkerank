if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a=student_marks.get(query_name)
    print(f"{sum(a)/len(a):.2f}")
#or even round(a,no of dec places can be used)
