#!/bin/bash
ref_dir=$1
test_dir=$2
#ppd=$3
output_file=$3
offset=$4

clang++ -O3 FLIP.cpp -o Flip

ref_dirlist=$(find $1 -type f -name "*.png" | sort -V)

for reffile in $ref_dirlist ; do
        basename="${reffile##*/}"
#        echo $basename
        filename="${basename%%.*}"
        extension="${reffile##*.}"
 #       echo "comparing image name $filename with extension $extension"
        mod_filename=$((filename+offset))
#        echo $mod_filename
        dot="."
        testfile="$test_dir$mod_filename$dot$extension"
#        echo $testfile
#        echo $testfile
        task="./Flip $reffile $testfile -ppd 11 -outputfile $output_file -v 0 -imagename $mod_filename"
        sleep 1
        $task & 
#        $task 
done

python cal_average_weighted_mean.py $output_file
