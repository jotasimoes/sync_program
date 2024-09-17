import os
import shutil

def sync_folders(source, replica):
    # List the files in the source folder
    source_files = os.listdir(source)
    replica_files = os.listdir(replica)

    for file_name in source_files:
        source_file_path = os.path.join(source, file_name)
        replica_file_path = os.path.join(replica, file_name)

        # If the file doesn't exist in the replica copy it
        if not os.path.exists(replica_file_path) :
            shutil.copy2(source_file_path, replica_file_path)  # Copy file along with its metadata       
            with open(log_file, 'a') as log:  # Append the message to the log file
                log.write(f'File copied: {file_name}\n')

        # If the file is newer is source folder, update it
        if os.path.getmtime(source_file_path) > os.path.getmtime(replica_file_path):
             shutil.copy2(source_file_path, replica_file_path)  # Copy file along with its metadata
             with open(log_file, 'a') as log:  # Append the message to the log file
                log.write(f'File updated: {file_name}\n')



    for file_name in replica_files:
        source_file_path = os.path.join(source, file_name)
        replica_file_path = os.path.join(replica, file_name)

        # If the file exists in the replica but not in the source, delete it
        if not os.path.exists(source_file_path):
            os.remove(replica_file_path)
            with open(log_file, 'a') as log:  # Append the message to the log file
                log.write(f'Removed file: {file_name}\n')
        


        
if __name__ == '__main__':
    source_folder = r'C:\Users\jotas\.vscode\workspace\sync_program\source'  
    replica_folder = r'C:\Users\jotas\.vscode\workspace\sync_program\replica'     
    log_file = r'C:\Users\jotas\.vscode\workspace\sync_program\logs.txt'  
    sync_folders(source_folder, replica_folder)