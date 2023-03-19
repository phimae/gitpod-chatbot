import re

def create_question_answer_pairs(documentation_text):
    qa_pairs = []

    # Split the text into sections (assuming each section starts with a markdown heading)
    sections = re.split(r'\n(#+\s.+)', documentation_text)

    for i in range(1, len(sections), 2):
        # Extract the title and content of the section
        title_match = re.match(r'(#+)\s(.+)', sections[i])
        if title_match:
            title = title_match.group(2)
            content = sections[i+1].strip()

            # Create a question based on the title
            question = "How do I " + title.lower() + "?"

            # Add the question-answer pair to the list
            qa_pairs.append((question, content))

    return qa_pairs


def main():
    # Load the combined documentation text
    with open("gitpod_combined_docs.md", "r") as f:
        documentation_text = f.read()

    # Create question-answer pairs
    qa_pairs = create_question_answer_pairs(documentation_text)

    # Save the question-answer pairs to a file
    with open("gitpod_qa_pairs.txt", "w") as f:
        for question, answer in qa_pairs:
            f.write(f"Q: {question}\nA: {answer}\n\n")

    print("Question-answer pairs saved to gitpod_qa_pairs.txt")

if __name__ == "__main__":
    main()
