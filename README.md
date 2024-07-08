# Explain Repo AI

`python3 filename_traversal.py /path/to/repository/`

A very simple script for reading every relevant file in a project, summarizing it, and summarizing every folder. The result is a tree of summaries in `hierarchy.pkl`. 

There's another script that converts `hierarchy.pkl` into `hierearchy.md`, which looks like this:

`python3 visualize.py`

- **/home/martin/Documents/explain_repo_AI/**
  - /home/martin/Documents/explain_repo_AI/filename_traversal.py
    - Summary:
      filename_traversal.py is a Python script that recursively traverses a directory, summarizes the contents of text files using OpenAI's GPT-3.5-turbo model, and saves the hierarchy of files and summaries in a pickle file, ultimately providing a summary of the entire directory's contents.
  - /home/martin/Documents/explain_repo_AI/visualize.py
    - Summary:
      The visualize.py script loads a hierarchical structure from a pickle file, generates a markdown representation of the hierarchy including summaries, and then writes it to a markdown file named 'hierarchy.md' in utf-8 encoding.
  - /home/martin/Documents/explain_repo_AI/hierarchy.md
    - Summary:
      The hierarchy.md file outlines the structure and contents of the mrmartin.github.io project directory, detailing various subdirectories, files, and summaries of resources such as blog posts, images, configuration files, and reusable components for a Jekyll-based website hosted by Martin Kolar.
  - /home/martin/Documents/explain_repo_AI/hierarchy.pkl (non-text file)
  - Summary:
    The project folder at /home/martin/Documents/explain_repo_AI/ consists of scripts for traversing directories, summarizing text files with OpenAI's GPT-3.5-turbo, visualizing file hierarchies in a markdown format, and storing the structures in a pickle file - all tailored for analyzing and documenting the contents of the mrmartin.github.io project.
