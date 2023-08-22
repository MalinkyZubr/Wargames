"""
This program is for brute forcing numeric passcodes in command line binaries. For leviathan 6 in OverTheWire
"""
import subprocess
import argparse


parser = argparse.ArgumentParser(description="Brute force a numeric password of a binary. Takes absolute path")
parser.add_argument('length')
parser.add_argument('path')


def subprocess_call(num, path):
    p = subprocess.run(f"{path} {num} &", shell=True, capture_output=True, text=True)
    if 'wrong' in p.stdout.lower() or 'usage' in p.stdout.lower():
        return 0
    return num
    

if __name__ == "__main__":  
    args = vars(parser.parse_args())
    if args['length'].isdecimal():
        args['length'] = int(args['length'])
    else:
        raise Exception('The value length must be an integer')
    values = list(range(10 ** args['length'] - 1)) 
    values = map(lambda x: str(x).zfill(args['length']), values)
    for pass_value in values:
        attempt_result = subprocess_call(pass_value, args['path'])
        if attempt_result:
            print(attempt_result)
            break
    
