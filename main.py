def total_sums():
    total_students = int(input("Enter the total number of students: "))
    biology_students = int(input("Enter the number of maths students: "))
    maths_students = int(input("Enter number of biology students: "))
    bio_maths_students = biology_students + maths_students
    all_students_without_bio_maths = total_students - bio_maths_students
    print(f"Total students except Biology and Mathematics: {all_students_without_bio_maths}")
    print(f"Total Students with subjects Biology and Mathematics: {bio_maths_students}")


total_sums()
