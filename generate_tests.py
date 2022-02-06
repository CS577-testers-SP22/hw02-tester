from subprocess import Popen, PIPE
from random import random, seed
from tqdm import tqdm
from pprint import pprint
import json

MAX_TESTS = 100
MAX_INSTANCES = 10
MAX_NODES = 20
MAX_STRING_SIZE = 10
EDGE_CHANCE = .5 # chance for edge between 2 nodes
SEED = 1234

seed(SEED)

def generateInput():
    '''returns a string that is valid input'''
    strings = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    instances = int(random() * MAX_INSTANCES) + 1
    test = f'{instances}'

    for _ in range(instances):
        nodeNames = []
        nodeSize = int(random() * MAX_NODES) + 1
        test += f'\n{nodeSize}'
        for _ in range(nodeSize):
            name = ''.join(strings[int(random() * len(strings))] for _ in range(1 + int(random() * MAX_STRING_SIZE)))
            while name in nodeNames:
                name = ''.join(strings[int(random() * len(strings))] for _ in range(1 + int(random() * MAX_STRING_SIZE)))
            nodeNames.append(name)
        nodeNames = sorted(nodeNames) # make sure in 0-9A-Za-z order
        # print(nodeSize, nodeNames)
        nodes = {n:[] for n in nodeNames}
        for n1 in nodeNames:
            for n2 in nodeNames:
                if n1 in nodes[n2]:
                    nodes[n1].append(n2)
                    continue
                if nodeNames.index(n1) >= nodeNames.index(n2): # same node or already checked
                    continue
                if random() < EDGE_CHANCE:
                    nodes[n1].append(n2)
        for n, edges in nodes.items():
            test += f'\n{n} {" ".join(edges)}'.strip(' ')

    return test

def shell(cmd, stdin=None):
    out, err = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE).communicate(input=stdin.encode())
    return out.decode('utf8').strip(), err.decode('utf8').strip()

getPython = lambda testCase: shell('python3 DFS.py', stdin=testCase)
getJava = lambda testCase: shell('java DFS', stdin=testCase)

tests = dict()

for i in tqdm(range(MAX_TESTS)):
    test = generateInput()
    # print(test)
    java, jerr = getJava(test)
    python, perr = getPython(test)
    if java != python:
        print(f'Java\n{java}')
        print()
        print(f'Java error\n{jerr}')
        print()
        print(f'Python\n{python}')
        print()
        print(f'Python error\n{jerr}')
        print()
        print(f'Input\n{test}')
        exit()
    tests[f'test{i}'] = {'input':test, 'output':python}
        # print(test)

pprint(tests)
with open('tests.json', 'w+') as f:
    json.dump(tests, f, indent=4)