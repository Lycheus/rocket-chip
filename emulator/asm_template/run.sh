clang test.S -c -o test_asm.o
clang test.c -c
riscv64-unknown-linux-gnu-gcc test.o test_asm.o -o test -L ~/riscv/riscv-llvm/runtime -lsoftboundcets_rt -lm -static -march=rv64gc -mabi=lp64
llvm-objdump -D test > dump
spike pk test
../emulator-freechips.rocketchip.system-DefaultConfig -V ~/riscv/_install/bin/pk test
