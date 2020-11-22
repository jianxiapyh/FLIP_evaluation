# FLIP_evaluation for ILLIXR
use the same ground truth and estimated image you used in SSIM 
run the following command
./run groundtruth_dir estimated_dir ppd_value FLIP_value_outputfile

- MAKE Sure there is a '/' after the directory path
- the two dir order groundtruth folder first or estimated_dir does not matter
- ppd value for ILLIXR can be set to 6
- no need to make FLIP (included in the bash script)
- output will be the statistics of the images you provided 

(avg flip error& standard deviation,
avg weighted error & standard deviation
avg color difference & standard deviation
avg feature difference & standard deviation)

script final output should be something like
Average flip metric mean: 
flip metric std:
max:
color diff mean:
color diff std:
feature diff mean:
feature diff std:


To plot time series graph 
execute
python plot-time-series-final.py flip outputfile your_appname

for example you can use the provided file to see a sample output
python plot-time-series-final.py flip demo_test.txt demo
