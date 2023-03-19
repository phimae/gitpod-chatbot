import json

input_file = "gitpod_qa_pairs.txt"
output_file = "gitpod_qa_pairs.jsonl"

with open(input_file, "r") as fin, open(output_file, "w") as fout:
    lines = fin.readlines()
    
    for i in range(0, len(lines), 2):
        question = lines[i].strip()
        answer = lines[i + 1].strip()

        qa_pair = {"question": question, "answer": answer}
        fout.write(json.dumps(qa_pair) + "\n")

print(f"Converted {input_file} to {output_file}")


# then run python convert_to_jsonl.py in terminal