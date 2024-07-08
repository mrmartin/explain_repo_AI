import os
import sys
import pickle
from openai import OpenAI

client = OpenAI(api_key = "actual-key-here")

def summarize_file_contents(file_name, file_contents):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",#gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are an AI that explains the content of code files, and entire project folders."},
            {"role": "user", "content": """file path: MarketCast/LLM_to_Survey.ipynb
contents:
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "32ac3be2-947f-45fc-9f03-3ea9b938ab7c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ChatCompletionMessage(content='text:\\nAbsolutely, I have added a dropdown for selecting a country to your form:\\n\\njson:\\n{\\n    \"title\": \"Sample Form\",\\n    \"fields\": [\\n        {\\n            \"type\": \"text\",\\n            \"label\": \"First Name\",\\n            \"name\": \"first_name\",\\n            \"placeholder\": \"Enter your first name\"\\n        },\\n        {\\n            \"type\": \"text\",\\n            \"label\": \"Last Name\",\\n            \"name\": \"last_name\",\\n            \"placeholder\": \"Enter your last name\"\\n        },\\n        {\\n            \"type\": \"email\",\\n            \"label\": \"Email\",\\n            \"name\": \"email\",\\n            \"placeholder\": \"Enter your email\"\\n        },\\n        {\\n            \"type\": \"select\",\\n            \"label\": \"Country\",\\n            \"name\": \"country\",\\n            \"options\": [\\n                {\"value\": \"\", \"text\": \"Please select a country\"},\\n                {\"value\": \"usa\", \"text\": \"United States\"},\\n                {\"value\": \"can\", \"text\": \"Canada\"},\\n                {\"value\": \"uk\", \"text\": \"United Kingdom\"}\\n            ]\\n        },\\n        {\\n            \"type\": \"submit\",\\n            \"value\": \"Submit\"\\n        }\\n    ]\\n}', role='assistant', function_call=None, tool_calls=None)\n"
     ]
    }
   ],
   "source": [
    "#first, test gpt-4 access here:\n",
    "from openai import OpenAI\n",
    "client = OpenAI(api_key = \"actual-key-here\")\n",
    "\n",
    "completion = client.chat.completions.create(\n",
    "  model=\"gpt-4-turbo\",\n",
    "  messages=[\n",
    "    {\"role\": \"system\", \"content\": \"\"\"\n",
    "You are a helpful JSON survey designer. Your answer always consists of two parts: the 'text' answer, and the 'json' of the form.\n",
    "The form you are creating is being displayed and viewed by the user, address their requirements and any comments on it.\n",
    "\n",
    "JSON Form Format Specification\n",
    "------------------------------\n",
    "This JSON format is designed for defining web forms with various input types. Each form is represented as a JSON object containing a title and a list of field objects. Each field object specifies the type, label, name, and additional attributes relevant to the field type, such as placeholder text for input fields or options for select fields.\n",
    "\n",
    "Attributes:\n",
    "- title (string): The title of the form, displayed as a header.\n",
    "- fields (array): An array of objects, each representing a single form field.\n",
    "\n",
    "Field Object Attributes:\n",
    "- type (string): The type of the input field (e.g., \"text\", \"email\", \"select\", \"submit\").\n",
    "- label (string): The label text associated with the input field.\n",
    "- name (string): The name attribute for the input field, used to identify form data.\n",
    "- placeholder (string, optional): A placeholder text for \"text\" and \"email\" input types.\n",
    "- options (array of objects, optional): Used only for \"select\" type; each object has `value` and `text` properties representing one dropdown option.\n",
    "- value (string, optional): Default value for input types like \"submit\".\n",
    "\n",
    "Example:\n",
    "A simple JSON defining a form with one text input and a submit button might look like:\n",
    "\n",
    "{\n",
    "    \"title\": \"Contact Form\",\n",
    "    \"fields\": [\n",
    "        {\n",
    "            \"type\": \"text\",\n",
    "            \"label\": \"Your Name\",\n",
    "            \"name\": \"name\",\n",
    "            \"placeholder\": \"Enter your name\"\n",
    "        },\n",
    "        {\n",
    "            \"type\": \"submit\",\n",
    "            \"value\": \"Submit\"\n",
    "        }\n",
    "    ]\n",
    "}\n",
    "\"\"\"},\n",
    "    {\"role\": \"user\", \"content\": \"I want  a simple form that contains First Name, Last Name, and email.\"},\n",
    "    {\"role\": \"assistant\", \"content\": \"\"\"\n",
    "text:\n",
    "That's easy, here is your form in the required format:\n",
    "\n",
    "json:\n",
    "{\n",
    "    \"title\": \"Sample Form\",\n",
    "    \"fields\": [\n",
    "        {\n",
    "            \"type\": \"text\",\n",
    "            \"label\": \"First Name\",\n",
    "            \"name\": \"first_name\",\n",
    "            \"placeholder\": \"Enter your first name\"\n",
    "        },\n",
    "        {\n",
    "            \"type\": \"text\",\n",
    "            \"label\": \"Last Name\",\n",
    "            \"name\": \"last_name\",\n",
    "            \"placeholder\": \"Enter your last name\"\n",
    "        },\n",
    "        {\n",
    "            \"type\": \"email\",\n",
    "            \"label\": \"Email\",\n",
    "            \"name\": \"email\",\n",
    "            \"placeholder\": \"Enter your email\"\n",
    "        },\n",
    "        {\n",
    "            \"type\": \"submit\",\n",
    "            \"value\": \"Submit\"\n",
    "        }\n",
    "    ]\n",
    "}\n",
    "\"\"\"},\n",
    "    {\"role\": \"user\", \"content\": \"Ok, now add a country dropdown\"},\n",
    "  ]\n",
    ")\n",
    "\n",
    "print(completion.choices[0].message)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "6e935014-84d0-4183-bdd7-b74cf58febc3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Absolutely, I have added a dropdown for selecting a country to your form:\n",
      "form.json                                     100% 1011    18.7KB/s   00:00    \n"
     ]
    }
   ],
   "source": [
    "reply = completion.choices[0].message.content\n",
    "text_reply = reply.split(\"\"\"text:\n",
    "\"\"\")[1].split(\"\"\"\n",
    "json:\n",
    "\"\"\")[0].strip()\n",
    "\n",
    "json_reply = reply.split(\"\"\"\n",
    "json:\n",
    "\"\"\")[1].strip()\n",
    "\n",
    "print(text_reply)\n",
    "\n",
    "with open('form.json', 'w') as file:\n",
    "    file.write(json_reply)\n",
    "\n",
    "!scp form.json subtitlecat.com:/var/www/html/martintech/json_form_maker/"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

Describe what this file does and how, in a single sentence."""},
            {"role": "assistant", "content": "LLM_to_Survey.ipynb contains a jupyter prototype of a JSON survey designer, using openai's API to gpt-4-turbo to convert a natural language description of a survey into a json file that contains the specified form."},
            {"role": "user", "content": f"""path: {file_name}
contents:
{file_contents}

Describe what this file does and how, in a single sentence."""}
        ]
    )
    return response.choices[0].message.content

def is_text_file(file_path):
    text_extensions = ['.py', '.java', '.c', '.cpp', '.txt', '.md', '.js', '.html', '.css', '.sh', '.rb', '.php', '.json', '.xml', '.markdown', '.yml', '.yaml', '.pl', '.pm', '.bat', '.ps1', '.ini', '.cfg', '.conf', '.properties', '.toml', '.rs', '.r', '.jl', '.ipynb', '.rmd', '.lua', '.go', '.ts', '.tsx', '.jsx', '.vbs', '.asm', '.s', '.vb', '.cs', '.sql', '.erl', '.hrl', '.ex', '.exs', '.hs', '.lhs', 'Gemfile', 'Makefile', 'makefile', 'CMakeLists.txt', 'Dockerfile', '.dockerignore', 'Vagrantfile', '.gitignore', '.gitattributes', 'Pipfile', 'requirements.txt', 'setup.py', 'build.gradle', 'pom.xml', 'composer.json', 'webpack.config.js', '.babelrc', '.eslintrc', '.prettierrc', '.editorconfig', 'Jenkinsfile', '.travis.yml', 'circle.yml', '.npmrc', 'package.json', '.env']
    return any(file_path.endswith(ext) for ext in text_extensions)

def save_hierarchy_to_pickle(hierarchy, file_path="hierarchy.pkl"):
    with open(file_path, 'wb') as file:
        pickle.dump(hierarchy, file)

def process_file(file_path, hierarchy):
    if is_text_file(file_path):
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            file_contents = file.read()
        print("summarizing " + file_path)
        summary = summarize_file_contents(file_path, file_contents)
        hierarchy[file_path] = summary
        save_hierarchy_to_pickle(hierarchy)  # Save after each file processing
        return f"Summary of {os.path.basename(file_path)}:\n{summary}\n\n"
    else:
        print("skipping " + file_path)
        hierarchy[file_path] = "non-text file"
        save_hierarchy_to_pickle(hierarchy)  # Save after each file processing
        return f"File: {os.path.basename(file_path)} (non-text file)\n"

def recursive_file_gathering_and_summarizing(directory, hierarchy):
    result = ""
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.name.startswith('.'):
                    continue  # Skip hidden files and folders
                if entry.is_file():
                    result += process_file(entry.path, hierarchy)
                elif entry.is_dir():
                    subdir_hierarchy = {}
                    subdir_contents = recursive_file_gathering_and_summarizing(entry.path, subdir_hierarchy)
                    subdir_summary = summarize_file_contents(entry.path, subdir_contents)
                    hierarchy[entry.path] = {
                        "summary": subdir_summary,
                        "contents": subdir_hierarchy
                    }
                    save_hierarchy_to_pickle(hierarchy)  # Save after each directory processing
                    result += f"Summary of directory {entry.name}:\n{subdir_summary}\n"
    except PermissionError:
        pass  # Ignore directories that can't be accessed
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)
    
    root_directory = sys.argv[1]
    if not os.path.isdir(root_directory):
        print(f"Error: {root_directory} is not a valid directory")
        sys.exit(1)
    
    hierarchy = {}
    result_string = recursive_file_gathering_and_summarizing(root_directory, hierarchy)
    root_summary = summarize_file_contents(root_directory, result_string)
    root_hierarchy = {}
    root_hierarchy[root_directory] = {
            "summary": root_summary,
            "contents": hierarchy
        }
    save_hierarchy_to_pickle(root_hierarchy)  # Final save after completion
    print(root_directory)
    print(root_summary)

