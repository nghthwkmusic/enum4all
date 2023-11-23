import argparse
import logging
import subprocess
import shutil

def is_enum4linux_installed():
    """Check if enum4linux is installed."""
    return shutil.which("enum4linux") is not None

def run_enum4linux(host):
    """Run enum4linux on a given host and return the output."""
    try:
        result = subprocess.check_output(["enum4linux", host], text=True)
        return result
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running enum4linux on {host}: {e}")
        return f"Error running enum4linux on {host}: {e}"

def main(input_file, output_file):
    """Main function to read hosts and run enum4linux on each."""
    logging.basicConfig(filename='enum4all.log', level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')

    if not is_enum4linux_installed():
        logging.error("enum4linux is not installed.")
        print("Error: 'enum4linux' is not installed on your system.")
        print("Installation instructions:")
        print("  - For macOS: Install using Homebrew with 'brew install enum4linux'")
        print("  - For Kali Linux: Install with 'sudo apt-get install enum4linux'")
        return

    with open(input_file, 'r') as file:
        hosts = file.readlines()

    with open(output_file, 'w') as outfile:
        for host in hosts:
            host = host.strip()
            logging.info(f"Running enum4linux on {host}")
            output = run_enum4linux(host)
            outfile.write(f"Results for {host}:\n{output}\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run enum4linux on a list of hosts.')
    parser.add_argument('input_file', help='File containing list of hosts, one per line.')
    parser.add_argument('-o', '--output', default='enum4all.out', 
                        help='Output file to write results to. Default is enum4all.out.')

    args = parser.parse_args()

    main(args.input_file, args.output)
