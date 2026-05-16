def load_questions():
    """
    Load content from file into a list of lists
    , each inner list a question.
    """
    question_list = []
    in_file = open("questionnaire.txt", "r")

    in_file.readline()   # read and discard the header
    for line in in_file.readlines():
        question_data = line.split("|")
        question_data[-1] = int(question_data[-1])
        question_list.append(question_data)
    in_file.close()
    return question_list


def display_question(question):
    """Display a question in MCQ format."""
    question_text = question[0]
    marks = question[-1]
    options = question[1:5]
    print(f"{question_text}     [{marks} marks]")
    for index in range(len(options)):
        print(f"{index + 1}) {options[index]}")


def get_user_answer(question):
    """Get user answer and score the user."""
    choice = int(input("Choice: "))
    user_answer = question[choice]   # getting the text of your choice
    answer = question[5]             # getting the text of the answer
    if user_answer == answer:
        print("Correct!")
        score = question[-1]
    else:
        print("Wrong!")
        score = 0
    return score


def start_questionnaire(questions):
    """Display each question in the list of questions."""
    total_score = 0
    for index in range(len(questions)):
        print(f"Question {index + 1}:")
        display_question(questions[index])
        total_score = total_score + get_user_answer(questions[index])
        print()
    return total_score

def main():
    # 1. load the file into a list of lists
    #    each list is a question with options and answer and marks
    questions = load_questions()

    # 2. start questionnaire
    total_score = start_questionnaire(questions)

    # 3. display total score
    print(f"Total score is {total_score}")

if __name__ == '__main__':
    main()