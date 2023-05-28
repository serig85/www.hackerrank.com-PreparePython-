if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scores_sum=0
    scores_qw=student_marks[query_name]
    for i in range(3):
        scores_sum+=scores_qw[i]
    form=format(scores_sum/3,'0.2f')    
    print(form)
