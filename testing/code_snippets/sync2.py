import os
import shutil
import time

def list_files(source, replica):
    # Get the list of files and directories in the source and replica folders
    source_files = os.listdir(source)
    replica_files = os.listdir(replica)

    print(f"Files source: ")
    print(source_files)

    print(f"Files replica: ")
    print(replica_files)

if __name__ == '__main__':
    source_folder = r'C:\Users\jotas\.vscode\workspace\sync_program\source'  # Replace with your source folder path
    replica_folder = r'C:\Users\jotas\.vscode\workspace\sync_program\replica'  # Replace with your replica folder path
    
    list_files(source_folder, replica_folder)