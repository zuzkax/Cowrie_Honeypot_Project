import os
import pandas as pd
from collections import defaultdict

folder_path = r"C:\directory\" 

command_groups = defaultdict(list)

csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')] #table of .csv file names  

if not csv_files:
    print("directory is empty, no .csv files.")

for file in csv_files:
    file_path = os.path.join(folder_path, file) #string -> directory

    try:
        df = pd.read_csv(file_path) #read file

        if 'session' in df.columns and 'message' in df.columns:
            for session in df['session'].unique(): #for  session
                session_commands = df['message'].tolist() #add message column (coments)
                session_commands_str = " ".join(session_commands)# table -> string

                command_groups[session_commands_str].append(session)#add sessions coments to dictonary,
              
        else:
            print("no matching columns (message, session)")
    except Exception as e:
        print(f"file error {file}: {e}")

same_command_sessions = []
unique_command_sessions = []

for command_str, sessions in command_groups.items():
    if len(sessions) > 1:
        same_command_sessions.append(sessions)
    else:
        unique_command_sessions.append(sessions)

print(f"Not unique sessions: {same_command_sessions}")
print(f"Unique: {unique_command_sessions}")

print(f"Number of not unique sessions")
print(len(same_command_sessions))
print(f"Number of unique sessions")
print(len(unique_command_sessions))
