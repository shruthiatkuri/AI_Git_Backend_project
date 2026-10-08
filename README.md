# Git_Explor_project

This is a small project to understand how Git works with each file and how to keep a Git project healthy. The experiment focuses on the `.env` file and its safety before pushing the project to Git.

# Setup

Clone the repository using:

```bash
git clone https://github.com/shruthiatkuri/AI_Git_Backend_project.git
```

Create a virtual environment for this project.

For Windows, create the virtual environment using:

```bash
python -m venv .venv
```

Activate the virtual environment using:

```bash
.venv\Scripts\Activate.ps1
```

For macOS/Linux:

```bash
source .venv/bin/activate
```

Install the required libraries from `requirements.txt` using:

```bash
pip install -r requirements.txt
```

**# Configuration**

Use the keys from the `.env.example` file, copy them, and create a `.env` file. Paste the keys into the `.env` file and modify the values with your app name and an API key of your choice.

Currently, it contains two keys. The first key, `APP_NAME`, is simply the name of the app, project, or software of your choice. The second key, `API_KEY`, stores the API key of any provider you want to work with.

**# Run the Project**

Run the main file using the following command in VS Code:

```bash
python main.py
```

You can see your app name and a Boolean value indicating whether the API key was successfully read or exists. If `APP_NAME` or `API_KEY` is not found, the program displays a clear error message.
