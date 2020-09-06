import sys
import os
import SetOps

def usage():
    print(f'Usage:')
    print(f'       python3 {os.path.basename(__file__)} <Input File1> <Input File2> <Output File>')
    print(f'       For e.g.: python3 Union.py L1.txt L2.txt R.txt')

'''
Use the readFile function to read line by line from the file
'''
def readFile(filename):
    lines = []
    try:
        fd = open(filename, 'r') 
        while True:
            line = fd.readline() 
            # if the line is empty, end of file is reached 
            if not line: 
                break
            else:
                lines.append(line)

        fd.close() 
        return lines
    except IOError as e1:
        print(f'File IO error: {e1}')
        return None
    except Exception as e2:
        print(f'Generic error: {e2}')
        return None

'''
    This function writes the list of emails to the given file
    returns the size of the file on success
    returns None in case of failure
'''
def writeEmailsToFile(filename, emails=None):
    if filename is None or '':
        print(f'Error: Provide a non-empty string value to FileName!!')
        return None
    if emails is None:
        print(f'Warning: Emails List is None')
    try:
        with open(filename, 'w') as f:
            for email in emails:
                f.write(email + '\n')
            f.close()
    except IOError as e1:
        print(f'File IO error: {e1}')
        return None
    except Exception as e2:
        print(f'Generic error: {e2}')
        return None
    else:
        return os.stat(filename).st_size

'''
    This function reads all the valid email addresses from the given file
    returns the list of valid emails on Success
    returns None in case of failure
'''
def getEmailsFromFile(filename):
    emails = []
    if filename is None or '':
        print(f'Error: Provide a non-empty string value to FileName!!')
        return None
    try:
        with open(filename) as f:
            for email in f.readlines():
                if email.count('@') != 1 or email.count('.') < 1:
                    #print(f'{email} is not a valid email address')
                    continue
                emails.append(email.rstrip())
            f.close()
    #except FileNotFoundException as e:
    #   print(f'File {filename}: read error: {e}')
    except IOError as e1:
        print(f'File IO error: {e1}')
        return None
    except Exception as e2:
        print(f'Generic error: {e2}')
        return None
    else:
        return emails

def main(argv):
    if len(argv) != 3 :
        print(f'Missing Input Params....')
        usage();
        exit(1)
    emails_from_file1 = getEmailsFromFile(argv[0])
    emails_from_file2 = getEmailsFromFile(argv[1])
    emails_union      = SetOps.SetOps.Union(emails_from_file1, emails_from_file2)
    return writeEmailsToFile(argv[2], emails_union)

if __name__ == "__main__":
   main(sys.argv[1:])
