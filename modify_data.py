import json

# Open the original file for reading
with open("gitpod_qa_pairs.jsonl", "r") as f:
    # Create a list to hold the modified data
    new_data = []

    # Loop through each line of the file
    for line in f:
        try:
            # Try to load the line as JSON
            obj = json.loads(line)

            # Extract the question and answer
            question = obj["question"]
            answer = obj["answer"]

            # Create a new object with the correct keys
            new_obj = {"prompt": question, "completion": ""}

            # Append the new object to the list
            new_data.append(new_obj)
        except json.JSONDecodeError:
            # If the line is not valid JSON, skip it
            pass

# Write the new data back to the file
with open("gitpod_qa_pairs.jsonl", "w") as f:
    for obj in new_data:
        json.dump(obj, f)
        f.write("\n")
