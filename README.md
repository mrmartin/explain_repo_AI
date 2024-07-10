# Explain Repo AI

`python3 filename_traversal.py /path/to/repository/`

A very simple script for reading every relevant file in a project, summarizing it, and summarizing every folder. The result is a tree of summaries in `hierarchy.pkl`. 

There's another script that converts `hierarchy.pkl` into `hierearchy.md`, which looks like this:

`python3 visualize.py`

## Example output, when running on this project

<details>
  <summary><b>/home/martin/Documents/explain_repo_AI/</b></summary>
  The project folder at /home/martin/Documents/explain_repo_AI/ consists of scripts for traversing directories, summarizing text files with OpenAI's GPT-3.5-turbo, visualizing file hierarchies in a markdown format, and storing the structures in a pickle file - includes example outputs on the mrmartin.github.io project.
<details>
  <summary><b>/home/martin/Documents/explain_repo_AI/filename_traversal.py</b></summary>
  filename_traversal.py is a Python script that recursively traverses a directory, summarizes the contents of text files using OpenAI's GPT-3.5-turbo model, and saves the hierarchy of files and summaries in a pickle file, ultimately providing a summary of the entire directory's contents.
</details>
<details>
  <summary><b>/home/martin/Documents/explain_repo_AI/visualize.py</b></summary>
  The visualize.py script loads a hierarchical structure from a pickle file, generates a markdown representation of the hierarchy including summaries, and then writes it to a markdown file named 'hierarchy.md' in utf-8 encoding.
</details>
<details>
  <summary><b>/home/martin/Documents/explain_repo_AI/hierarchy.md</b></summary>
  The hierarchy.md file outlines the structure and contents of the mrmartin.github.io project directory, detailing various subdirectories, files, and summaries of resources such as blog posts, images, configuration files, and reusable components for a Jekyll-based website hosted by Martin Kolar.
</details>
- <b>/home/martin/Documents/explain_repo_AI/hierarchy.pkl</b> (non-text file)
</details>

## Another example 

Open <i>hierarchy.md</i> above for a bigger example
