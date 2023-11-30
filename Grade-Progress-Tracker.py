def number_to_words(num):
    if 1 <= num <= 12:
        number_words = [
            "first", "second", "third", "fourth", "fifth", "sixth",
            "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
        ]
        return number_words[num - 1]
    else:
        return str(num) + "th"

average_grade = 0
student_name = input("Enter the student's name: ")
years_counter = 1
fail_counter = 0

while True:
    annual_grade = float(input(f"Enter {number_to_words(years_counter)} year's annual grade for {student_name}: "))

    if annual_grade < 2 or annual_grade > 6:
        print("Invalid grade option, please select a grade based on the six-point grading system.")
        continue
    if annual_grade >= 4:
        years_counter += 1
        average_grade += annual_grade
    else:
        fail_counter += 1

    if fail_counter > 1:
        print(f"{student_name} has been excluded at {number_to_words(years_counter)} grade")
        break
    if years_counter >= 13:
        print(f"{student_name} graduated. Average grade: {(average_grade / 12):.2f}")
        break
