# Enum4All

Enum4All is a Python-based command-line tool that acts as a wrapper for `enum4linux`. It allows users to scan multiple hosts for SMB enumeration by reading from a file containing a list of hosts. For each host, `enum4linux` is executed, and the results are output to a specified file.

## Features
- Read hosts from a file line by line.
- Run `enum4linux` on each host.
- Output the results of each scan to a specified file.
- Enhanced error handling and logging.

## Requirements
- Python 3
- `enum4linux`
- 
## Installation
Before using Enum4All, ensure that you have `enum4linux` installed on your system.
### Installing `enum4linux`
#### For macOS Users:
Install `enum4linux` using Homebrew:
```bash
brew install enum4linux
```
#### For Kali Linux Users:
Install enum4linux using apt-get:
```bash
sudo apt-get install enum4linux
```
#### Python Dependencies
Install required Python packages:

```bash
pip install -r requirements.txt
```

## Usage
To use Enum4All, run the script with the input file as an argument. Optionally, specify the output file using the -o or --output flag. 
```bash
python enum4all.py [INPUT FILE] -o [OUTPUT FILE]
```
NOTE: If the -o option is not provided, the default output file enum4all.out will be used.
```bash
python enum4all.py hosts.txt -o results.out
```

## Logs
The script generates a log file enum4all.log, containing details of the execution process and any errors encountered.

## Contributing
Contributions to Enum4All are welcome. Please feel free to fork the repository, make changes, and submit pull requests.