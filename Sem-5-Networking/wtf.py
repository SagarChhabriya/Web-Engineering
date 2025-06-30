# import os
# from datetime import datetime


# def make_commit(target_date: str):
#     # Parse the target date
#     current_date = datetime.strptime(target_date, "%Y-%m-%d")

#     # Ensure the date is exactly what you expect
#     print(f"Parsed date: {current_date}")

#     # Format the date for git
#     date_str = current_date.strftime('%Y-%m-%d')

#     # Ensure the formatted date is correct
#     print(f"Formatted date for git commit: {date_str}")

#     with open('data.txt', 'a') as file:
#         file.write(f'Notes: {date_str}\n')

#     # Staging
#     os.system('git add data.txt')

#     # Commit
#     os.system(f'git commit --date="{date_str}" -m "Commit for {date_str}"')

#     # Push the changes
#     return os.system('git push')


# # Call the function with a specific target date
# make_commit("2025-06-02")

import os
import shutil
import random
from datetime import datetime
import subprocess

def make_commit_with_file(target_date: str, file_path: str, repo_path: str):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Input file does not exist: {file_path}")

    if not os.path.isdir(repo_path) or not os.path.isdir(os.path.join(repo_path, '.git')):
        raise NotADirectoryError(f"Target is not a valid Git repository: {repo_path}")

    commit_datetime = datetime.strptime(target_date, "%Y-%m-%d")

    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)

    random_datetime = commit_datetime.replace(
        hour=random_hour,
        minute=random_minute,
        second=random_second
    )

    git_timestamp = random_datetime.strftime('%Y-%m-%dT%H:%M:%S+0000')

    filename = os.path.basename(file_path)
    dest_path = os.path.join(repo_path, filename)

    if os.path.exists(dest_path):
        os.remove(dest_path)

    shutil.copy2(file_path, dest_path)
    print(f"Copied {file_path} → {dest_path}")

    original_cwd = os.getcwd()
    os.chdir(repo_path)

    try:
        subprocess.run(['git', 'pull'], check=True)
        subprocess.run(['git', 'add', filename], check=True)

        result = subprocess.run(
            ['git', 'diff', '--cached', '--name-only'],
            capture_output=True, text=True, check=True
        )
        staged_files = result.stdout.strip()
        print(f"Staged files:\n{staged_files}")

        if not staged_files:
            print("No changes staged. Nothing to commit.")
            return

        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = git_timestamp
        env['GIT_COMMITTER_DATE'] = git_timestamp

        commit_message = f"Add {filename}"

        subprocess.run(['git', 'commit', '-m', commit_message], env=env, check=True)
        subprocess.run(['git', 'push'], check=True)

        print(f"✅ Commit pushed with date: {git_timestamp}")

    finally:
        os.chdir(original_cwd)


if __name__ == "__main__":
    make_commit_with_file(
        "2025-06-29",  # Target date
        r"D:\Ao\Code\AI\natural-language-processing\README.md",  # File path
        r"D:\Ao\Code\AI\natural-language-processing"  # Repo path
    )

