all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    student_dict = {}
    for key in all_array:   # 0(N)
        student_dict[key] = True    # 공간복잡도도 0(N)

    for key in all_array:   # 0(N)
        del student_dict[key]


print(get_absent_student(all_students, present_students))