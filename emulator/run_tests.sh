#!/bin/sh

pre="output/rv64ui-p-"
post=".out"
files="sp_addi sp_div sp_dmem sp_mul spe"

for i in $files; do
    f=$pre$i$post
    rm $f
    make -j2 $f
done
