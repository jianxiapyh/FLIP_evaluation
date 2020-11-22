import sys
import numpy
filename=sys.argv[1]
image_num=0
average=0
color_average=0
feature_average=0
weighted_average=0
weighted_data =[]
data=[]
color_data=[]
feature_data=[]
with open('%s' % filename, 'r') as input:
    content = input.readlines()
    content = [x.strip('\n') for x in content]
    for line in content:
        line_input = line.split(" ");
        weighted_average  += float(line_input[1])
        average += float(line_input[2])
        weighted_data.append(float(line_input[1]))
        data.append(float(line_input[2]))
        
        color_average += float(line_input[3])
        feature_average += float(line_input[4])
        color_data.append(float(line_input[3]))
        feature_data.append(float(line_input[4]))
        image_num += 1

print('Average weighted flip metric mean: {}'.format(weighted_average/image_num))
print('flip metric weighted std: {}'.format(numpy.std(weighted_data)))
print('max: {}'.format(numpy.amax(weighted_data)))
print('Average flip metric mean: {}'.format(average/image_num))
print('flip metric std: {}'.format(numpy.std(data)))
print('max: {}'.format(numpy.amax(data)))

print('color diff mean: {}'.format(color_average/image_num))
print('color diff std: {}'.format(numpy.std(color_data)))
print('feature diff mean: {}'.format(feature_average/image_num))
print('feature diff std: {}'.format(numpy.std(feature_data)))
