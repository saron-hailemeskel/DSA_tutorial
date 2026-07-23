#unique_scores=[set(student[1])for student in students]
# more of{} cuz student[] is single value not a list
# understanding nested loops 
# students-> student-> names and scores 
#                 student[0]     student[1]

if __name__ == '__main__':
  # here i forget to add it on the begining  if it was lastly stored it will only be storing the last one
    students=[] 
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    # unique_scores=[set(student[1])for student in students]
    unique={student[1]for student in students}
  # here i fogot that ubique is still a set
    unique.remove(min(unique))
    second_lowest=min(unique)
    names=[]
    for student in students:
        if student[1]==second_lowest:
            names.append(student[0])
    names.sort()  
    for name in names:
        print(name)
        
