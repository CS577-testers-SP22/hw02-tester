from subprocess import Popen, PIPE
import json
from tqdm import tqdm
import difflib

TEST_FILE = 'tests.json'

with open(TEST_FILE, 'r') as f:
    tests = json.load(f)

def shell(cmd, stdin=None):
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    out, err = p.communicate(input=stdin.encode() if stdin else None)
    return out.decode('utf8'), err.decode('utf8')
print('Building:')
buildOutput, buildError = shell('make build')
print(buildOutput)
print(buildError)

for testName, testCase in tqdm(tests.items()):
    userOutput, userError = shell('make run', stdin=testCase['input'])
    userOutput = '\n'.join(userOutput.split('\n')[1:]) # first line is Makefile's run command
    if userOutput != testCase['output']:
        print(f"Failed test: {testName}")
        print(f"Input:\n{testCase['input']}\n")
        print(f"Expected output:\n{testCase['output']}\n")
        print(f"Program output:\n{userOutput}\n")
        print(f"Program error:\n{userError}")
        print('Difference between user and expected outputs:')
        for i,s in enumerate(difflib.ndiff(userOutput, testCase['output'])):
            if s[0]==' ': continue
            elif s[0]=='-':
                print(u'Delete "{}" from position {}'.format(s[-1],i))
            elif s[0]=='+':
                print(u'Add "{}" to position {}'.format(s[-1],i))    
        print()   
        exit()

print('All tests passed.')