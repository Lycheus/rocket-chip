#!/bin/sh

cat trace.raw | spike-dasm > trace.out
./align trace.out > trace.bnd
cat trace.out | ./cfilter > trace.rtl

