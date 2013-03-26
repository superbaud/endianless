#!/usr/bin/python

# 16-bit endianless emulator
# by susan werner <heinousbutch@gmail.com> 

import array

# input: assembled endianless-16 code
# output: memory image at given breakpoints (supplied on the command line)
# and when the reset instruction is executed




class CPU:
    """CPU object -- holds state of a CPU, memory, and breakpoints"""

    RESET_VECTOR = 0x3fff 

    def __init__(self, initial_memory, breakpoints=[]):
        """Creates a CPU object given a memory image, along with an optional 
        list of breakpoints. 

        """
        # actual cpu state
        self.acc    = 0x0000 # 16 bit wide accumulator
        self.pc     = self.RESET_VECTOR  # 14 bit program counter
        self.carry  = False  # carry flag
        
        self.memory = initial_memory

        # other stuff
        self.breakpoints = breakpoints

        self.cycles = 0      # cycles elapsed since start


    def run(self, runcycles=0):
        """runs the CPU for the given number of cycles or until the CPU 
        executes a reset instruction, whichever comes first. runcycles=0 means no 
        limit on the cycle count"""
        
        assert runcycles >= 0

        startcycles = self.cycles
         
        while True:                 
                                    
            if (runcycles != 0) and (self.cycles - startcycles >= runcycles):
                break
            if (self.pc == self.RESET_VECTOR) and (self.cycles != 0):
                break
            if (self.pc in self.breakpoints):
                break

            print(self.pc)

            inst = self.memory[self.pc] 
            
            opcode = inst & 0xC000
            addr   = inst & 0x3fff

            if   opcode == 0x0000: # nand
                print("nand")
            elif opcode == 0x4000: # add
                print("add")
            elif opcode == 0x8000: # store
                print("store")
            elif opcode == 0xC000: # jnc
                print("jnc")
            else:                  # something seriously wrong
                assert 1 == 0 


            self.pc = (self.pc + 1) % (2**14)

            self.cycles += 1





if __name__ == "__main__":
    mem = array.array('i',[0x0000] * (2**14))
    cpu = CPU(mem, [0xf])
    cpu.run(100)
