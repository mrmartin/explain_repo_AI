import pickle

def load_hierarchy_from_pickle(file_path="hierarchy.pkl"):
    with open(file_path, 'rb') as file:
        hierarchy = pickle.load(file)
    return hierarchy

def generate_markdown(hierarchy, level=0):
    markdown = ""

    for path, content in hierarchy.items():
        if isinstance(content, dict):
            markdown += f"<details>\n"
            markdown += f"  <summary>{path}</summary>\n"
            markdown += f"  {content['summary']}\n"
            markdown += generate_markdown(content["contents"], level + 1)
            markdown += f"</details>\n"
        else:
            if content == "non-text file":
                markdown += f"- {path} (non-text file)\n"
            else:
                markdown += f"<details>\n"
                markdown += f"  <summary>{path}</summary>\n"
                markdown += f"  {content}\n"
                markdown += f"</details>\n"

    return markdown

if __name__ == "__main__":
    hierarchy = load_hierarchy_from_pickle("hierarchy.pkl")
    
    markdown_content = generate_markdown(hierarchy)

    with open("hierarchy.md", "w", encoding="utf-8") as markdown_file:
        markdown_file.write(markdown_content)

    print("Markdown file 'hierarchy.md' has been created.")
