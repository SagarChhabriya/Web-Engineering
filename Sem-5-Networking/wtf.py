import os
from datetime import datetime


def make_commit(target_date: str):
    # Parse the target date
    current_date = datetime.strptime(target_date, "%Y-%m-%d")

    # Format the date for git
    date_str = current_date.strftime('%Y-%m-%d')

    with open('README.md', 'a') as file:
        file.write(f'Notes: {date_str}\n')

    # Staging
    os.system('git add data.txt')

    # Commit
    os.system(f'git commit --date="{date_str}" -m "Commit for {date_str}"')

    # Push the changes
    return os.system('git push')


def make_commit_with_file(target_date: str, file_path: str):
    # Parse the target date
    current_date = datetime.strptime(target_date, "%Y-%m-%d")

    # Format the date for git
    date_str = current_date.strftime('%Y-%m-%d')

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file at {file_path} does not exist.")
        return

    # Check if the file is a text or binary file (optional, can be adjusted)
    if file_path.lower().endswith(('.gif', '.jpg', '.png', '.exe', '.pdf')):  # Checking for common binary extensions
        print("Warning: The file appears to be binary. Appending text data to it may not be appropriate.")

    # Append the date to the file (for text files)
    # Check if file is text-based
    if os.path.splitext(file_path)[1].lower() in ['.txt', '.log', '.md']:
        with open(file_path, 'a') as file:
            file.write(f'{date_str}\n')
    else:
        print(f"Skipping writing to non-text file {file_path}")

    # Stage the file for commit
    os.system(f'git add {file_path}')

    # Commit the changes
    commit_command = f'git commit --date="{date_str}" -m "Commit for {date_str}"'
    commit_result = os.system(commit_command)

    # If commit fails, display a message
    if commit_result != 0:
        print("Git commit failed.")
        return

    # Push the changes
    push_result = os.system('git push')

    # Check if push was successful
    if push_result != 0:
        print("Git push failed.")
        return

    print(f"Successfully committed and pushed changes for {file_path}.")


# Call the function with a specific target date
# make_commit("2025-01-05")
# Custom file commit
make_commit_with_file(
    "2025-01-03", r"D:\Ao\Code\WebCode\Web-Engineering\Sem-5-Networking\Git Cheat Sheet.gif")
