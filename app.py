# Student Quarterly Average Calculator

def calculate_average(grades, coefficients):
    total_weighted_score = 0
    total_coefficients = 0
    
    for subject, coefficient in coefficients.items():
        total_coefficients += coefficient
        total_weighted_score += grades[subject] * coefficient
    
    return total_weighted_score / total_coefficients

def get_student_grades(coefficients):
    grades = {}
    for subject in coefficients.keys():
        test = float(input(f"Enter the test score for {subject} (0-20): "))
        assignments = float(input(f"Enter the assignments score for {subject} (0-20): "))
        exam = float(input(f"Enter the exam score for {subject} (0-40): "))
        
        average_note = ((test + assignments) / 2 + exam) / 3
        grades[subject] = average_note
    return grades

def main():
    coefficients = {
        "Math": 4,
        "Arabic": 5,
        "French": 3,
        "English": 2,
        "Islamic": 2,
        "Civics": 1,
        "History/Geography": 3,
        "Science": 2,
        "Physics": 2
    }
    
    print("Welcome to the Student Quarterly Average Calculator!")
    student_grades = get_student_grades(coefficients)
    quarterly_average = calculate_average(student_grades, coefficients)
    
    print(f"The student's quarterly average is: {quarterly_average:.2f}")

if __name__ == "__main__":
    main()