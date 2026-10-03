# Git_Explor_project

This is a small project to understand how Git works with each file and how to keep a Git project healthy. The experiment focuses on the `.env` file and its safety before pushing the project to Git.

# Setup

Clone the repository using:

```bash
git clone https://github.com/username/repository.git
```

Create a virtual environment for this project and install the required libraries from `requirements.txt` using:

```bash
pip install -r requirements.txt
```

# Configuration

Use the keys from the `.env.example` file, copy them, and create a `.env` file. Paste the keys into the `.env` file and modify the values with your app name and an API key of your choice.

# Run the Project

Run the main file using the following command in VS Code:

```bash
python main.py
```

You can see your app name and a Boolean value indicating whether the API key was successfully read or exists.
