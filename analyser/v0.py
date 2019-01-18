#!/usr/bin/python3

import re
import sys
from collections import deque

def insn_parse(dumpfile):
    funcs = {}

    insn_re = re.compile(r'    (.+)?:\t.+? +?\t(.+)?\t')

    out = True
    key = None
    first = None
    
    for line in dumpfile:
        res = re.match(r'    (.+)?:\t.+? +?\t(.+)?\t', line)

        if res == None:
            out = True
            continue

        pc = res.group(1)
        insn = res.group(2)

        if out:
            key = pc
            funcs[key] = []
            out = False

            if first == None:
                first = pc

        operands = line.strip().split('\t')[-1].split(' ')[0].split(',')

        funcs[key].append((pc, insn, tuple(operands)))

    return (first, funcs)

j_insns = ('jal', 'jalr', 'beq', 'bne', 'blt', 'bge', 'bltu', 'bgeu', 'j', 'jr', 'call', 'tail')

class Func(object):
    def __init__(self, insns):
        self.insns = insns
        self.calls = []
        self.sps = {0}

    def find_calls(self, funcs):
        sp = 0

        for insn in self.insns:
            if insn[2][0] == 'sp':
                if insn[1] != 'addi':
                    sp = 0
                else:
                    sp += int(insn[2][-1])
                    self.sps.add(sp)
            elif insn[1] in j_insns and insn[2][-1] in funcs:
                self.calls.append((insn[2][-1], sp))

        return (self.calls, self.sps)


class SPDiffs(object):
    def __init__(self, first, funcs):
        self.funcs = funcs
        self.first = first

        self.diff_set = set({})
        self.calc_diffs()

    def diffs(self):
        return self.diff_set

    def calc_diffs(self):
        #skip _start as it sets up the sp
        first_call = self.funcs[self.first].find_calls(self.funcs.keys())[0]

        if len(first_call) != 1:
            print("MALFORMED _start, EXITING!")
            exit()

        q = deque([(first_call[0][0], 0)])
        visited = set({})

        while len(q) > 0:
            (func_pc, sp) = q.popleft()
            self.diff_set.add(sp)

            func = self.funcs[func_pc]

            (calls, sps) = func.find_calls(self.funcs.keys())

            for call in calls:
                call = (call[0], call[1] + sp)

                if call[0] == func_pc:
                    print("RECURSION FOUND")
                    continue

                if call not in visited:
                    visited.add(call)
                    q.append(call)

            for _sp in sps:
                self.diff_set.add(sp + _sp)


def main():
    if len(sys.argv) < 2:
        print('Please provide a riscv objdump.')
        exit()

    for f in sys.argv[1:]:
        print(f)

        with open(f, 'r') as dumpfile:
            (first, funcs) = insn_parse(dumpfile)

        funcs = {k: Func(v) for (k, v) in funcs.items()}

        diff_set = SPDiffs(first, funcs).diffs()

        for diff in diff_set:
            if diff % 16 != 0:
                print("UNALIGNED SP %d" % (diff))

        print(diff_set)
        print(min(diff_set))
    

if __name__ == '__main__':
    main()
