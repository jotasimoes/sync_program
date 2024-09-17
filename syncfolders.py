import os
import shutil
import argparse
import time

def sync_folders(source, replica,log_file, interval):

    # listing the files in source and replica folder
    source_files = os.listdir(source)
    replica_files = os.listdir(replica)

    # for every file in source folder
    # combine source and replica folder path with file name to create full path of the item
    # if the file doesn't exist in the replica copy it to source
    # if the file modification time is newer in the source folder, update it in replica

    for file_name in source_files:        
        source_file_path = os.path.join(source, file_name)
        replica_file_path = os.path.join(replica, file_name)
       
        if not os.path.exists(replica_file_path) :
            shutil.copy2(source_file_path, replica_file_path)  # copy file and metadata       
            with open(log_file, 'a') as log:  
                log.write(f'File copied: {file_name}\n')
        
        if os.path.getmtime(source_file_path) > os.path.getmtime(replica_file_path):
             shutil.copy2(source_file_path, replica_file_path)  
             with open(log_file, 'a') as log:  
                log.write(f'File updated: {file_name}\n')


    # for every file in replica folder
    # combine source and replica folder path with file name to create full path of the item
    # if the file exists in the replica but not in the source, delete it    

    for file_name in replica_files:
        source_file_path = os.path.join(source, file_name)
        replica_file_path = os.path.join(replica, file_name)
        
        if not os.path.exists(source_file_path):
            os.remove(replica_file_path)
            with open(log_file, 'a') as log: 
                log.write(f'Removed file: {file_name}\n')

    time.sleep(interval)  # delay for the specified synchronization interval
        
def main():
     parser = argparse.ArgumentParser(description='Synchronize two folders')

    # define the expected arguments
     parser.add_argument('source', type=str, help='Source path')
     parser.add_argument('replica', type=str, help='Replica path')
     parser.add_argument('log_file', type=str, help='Log file path')
     parser.add_argument('interval', type=int, help='Synchronization interval')
     args = parser.parse_args()

     while True:
         sync_folders(args.source, args.replica, args.log_file, args.interval)
        
if __name__ == '__main__':
    main()