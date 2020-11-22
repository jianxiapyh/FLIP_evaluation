#!/bin/bash
ref_dir=$1
test_dir=$2
ppd=$3
output_file=$4

clang++ -O3 FLIP.cpp -o Flip

ref_dirlist=$(find $1 -type f | sort -V)

for reffile in $ref_dirlist ; do
        filename="${reffile##*/}"
        echo "comparing image $filename"
        testfile="$test_dir$filename"
#        echo $testfile
        task="./Flip $reffile $testfile -ppd 11 -outputfile $output_file -v 0 -imagename $filename"
        sleep 1
        $task & 
#        $task 
done

python cal_average_weighted_mean.py $output_file
