import os
from datetime import datetime, timedelta

def make_commit(target_date: str, current_date: datetime = None):
    if current_date is None:
        current_date = datetime.strptime(target_date, "%Y-%m-%d")
    
    # If we reach today's date, just push
    if current_date > datetime.now():
        return os.system('git push')
    
    # Format the date for git
    date_str = current_date.strftime('%Y-%m-%d')
    
    with open('data.txt', 'a') as file:
        file.write(f'{date_str}\n')

    # Staging 
    os.system('git add data.txt')

    # Commit 
    os.system(f'git commit --date="{date_str}" -m "Commit for {date_str}"')

    # Recur for the previous day
    return make_commit(target_date, current_date + timedelta(days=1))

# Call the function with a specific target date
make_commit("2024-10-15")
