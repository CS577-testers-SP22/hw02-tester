from subprocess import Popen, PIPE
import json
from tqdm import tqdm

TEST_FILE = 'tests.json'

with open(TEST_FILE, 'r') as f:
    tests = json.load(f)

def shell(cmd, stdin=None):
    out, err = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE).communicate(input=stdin.encode())
    return out.decode('utf8').strip(), err.decode('utf8').strip()

for _, testCase in tqdm(tests.items()):
    userOutput, userError = shell('make run', stdin=testCase['input'])
    userOutput = '\n'.join(userOutput.split('\n')[1:]) # first line is Makefile's run command
    if userOutput != testCase['output']:
        print(f"Input:\n{testCase['input']}\n")
        print(f"Expected output:\n{testCase['output']}\n")
        print(f"Program output:\n{userOutput}\n")
        print(f"Program error:\n{userError}")
        exit()

# print(tests)