import argparse

def parse_arguments():
    # Create an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser(description='Synchronize two folders')

    # Define the expected arguments
    parser.add_argument('source', type=str, help='Source path')
    parser.add_argument('replica', type=str, help='Replica path')
    parser.add_argument('log_file', type=str, help='Log file path')
    parser.add_argument('interval', type=int, help='Synchronization interval')

    # Parse the arguments and return them
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    print(f'Source: {args.source}')
    print(f'Replica: {args.replica}')
    print(f'Log File: {args.log_file}')
    print(f'Interval: {args.interval} seconds')