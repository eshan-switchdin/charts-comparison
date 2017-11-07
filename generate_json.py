#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A script to convert the csv data from the website to echarts compatible json
'''

import sys
import time
import dateutil.parser

def main():
    data={}
    if len(sys.argv) < 2:
        print("please provide the csv file name as the argument")
        exit(1)

    with open( sys.argv[1] ) as csvfile:

        file_contents=csvfile.read().split('\n')
        for attr in file_contents[0].split(','):
            data[attr]=[]

        ignore_first_line=False

        for line in file_contents:
            if ignore_first_line:
                line=line.split(',')
                for value in range (len(line)):
                    if line[value] == '':
                        line[value]=0
                    try:
                        data[file_contents[0].split(',')[value]].append(float(line[value]))
                    except Exception as e:
                        data[file_contents[0].split(',')[value]].append((line[value]))

            else:
                ignore_first_line=True

        csvfile.close()

    data_out=[]
    timestamp=[]
    for data_type, data_array in data.items():
        if data_type != 'Timestamp':
            data_out.append({'name':data_type, 'type':'bar', 'data':data_array})
        else:
            timestamp=list(map(lambda x:str((dateutil.parser.parse(x)).date())+' '+str((dateutil.parser.parse(x)).time()), data_array[:-1]))



    print('var all_data=')
    print(data_out)
    print('var timestamp = ')
    print(timestamp)




if __name__ == '__main__':
    main()
