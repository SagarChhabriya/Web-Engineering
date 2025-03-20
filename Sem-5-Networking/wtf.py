import os
from datetime import datetime


def make_commit(target_date: str):
    # Parse the target date
    current_date = datetime.strptime(target_date, "%Y-%m-%d")

    # Ensure the date is exactly what you expect
    print(f"Parsed date: {current_date}")

    # Format the date for git
    date_str = current_date.strftime('%Y-%m-%d')

    # Ensure the formatted date is correct
    print(f"Formatted date for git commit: {date_str}")

    with open('data.txt', 'a') as file:
        file.write(f'Notes: {date_str}\n')

    # Staging
    os.system('git add data.txt')

    # Commit
    os.system(f'git commit --date="{date_str}" -m "Commit for {date_str}"')

    # Push the changes
    return os.system('git push')


# Call the function with a specific target date
make_commit("2025-03-20")
