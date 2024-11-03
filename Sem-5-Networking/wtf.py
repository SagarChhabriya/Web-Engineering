import os
from datetime import datetime

def make_commit(target_date: str):
    # Parse the target date
    current_date = datetime.strptime(target_date, "%Y-%m-%d")
    
    # Format the date for git
    date_str = current_date.strftime('%Y-%m-%d')
    
    with open('data.txt', 'a') as file:
        file.write(f'{date_str}\n')

    # Staging 
    os.system('git add data.txt')

    # Commit 
    os.system(f'git commit --date="{date_str}" -m "Commit for {date_str}"')

    # Push the changes
    return os.system('git push')

# Call the function with a specific target date
make_commit("2024-11-01")
