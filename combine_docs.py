import os
import requests
from github import Github

# Replace with your GitHub access token
ACCESS_TOKEN = os.environ["GITHUB_ACCESS_TOKEN"]

# Repository and directory containing the documentation
REPO_NAME = "gitpod-io/website"
DOCS_DIR = "gitpod/docs"

def fetch_docs(repo, path, combined_docs):
    docs = repo.get_contents(path)

    for doc in docs:
        if doc.type == "dir":
            combined_docs = fetch_docs(repo, doc.path, combined_docs)
        elif doc.type == "file" and doc.name.endswith(".md"):
            content = requests.get(doc.download_url).text
            combined_docs += f"\n\n---\n\n{content}"
            print(f"Downloaded {doc.name}")

    return combined_docs

def main():
    # Authenticate with GitHub
    g = Github(ACCESS_TOKEN)
    repo = g.get_repo(REPO_NAME)

    # Download and combine the documentation files
    combined_docs = fetch_docs(repo, DOCS_DIR, "")

    # Save the combined documentation to a single file
    with open("gitpod_combined_docs.md", "w") as f:
        f.write(combined_docs)

    print("Combined documentation saved to gitpod_combined_docs.md")

if __name__ == "__main__":
    main()
