#!/usr/bin/python

import sys
import os
import SetOps

def usage():
    print(f'Usage:')
    print(f'       python3 {os.path.basename(__file__)} <Input File1> <Input File2> <Output File>')
    print(f'       For e.g.: python3 Minus.py L1.txt L2.txt R.txt')

'''
This function returns TRUE if the email is in valid format: <ID>@<service><domain>
for e.g.: thisismyID@goodemail.com
Valid Email if (i) @ char is present (ii) . char is present and occurs later than @
'''
def isValidEmailAddress(email):
    return ( (email.find('@') != -1) and \
             (email.count('@') == 1) and \
             (email.rfind('.') != -1) and \
             (email.rfind('.') > email.find('@')) \
           ) ;

'''
    This function reads all the valid email addresses from the given file
    returns the list of valid emails on Success
    returns None in case of failure
'''
def getEmailsFromFile(filename):
    lines = []
    try:
        fd = open(filename, 'r') 
        while True:
            line = fd.readline() 
            # if the line is empty, end of file is reached 
            if not line: 
                break
            elif isValidEmailAddress(line):
                lines.append(line.rstrip())

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


def main(argv):
    if len(argv) != 3 :
        print(f'Missing Input Params....')
        usage();
        exit(1)
    emails_from_file1 = getEmailsFromFile(argv[0])
    emails_from_file2 = getEmailsFromFile(argv[1])
    emails_xor        = SetOps.SetOps.Minus(emails_from_file1, emails_from_file2)
    return writeEmailsToFile(argv[2], emails_xor)

if __name__ == "__main__":
   main(sys.argv[1:])
