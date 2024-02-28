#-*- coding=utf-8 -*-
import argparse
import pandas as pd
import codecs
import sys
from conlleval import *
from os import listdir,path

import csv

for j in listdir('Intput/'):
	predict_path=path.join('Intput/',j)
	print(predict_path)
	name=j.replace('.txt','')
	print(name)
	# try:
	if "WA" in name:
		truth='MultiNER-Health_truth_WA.txt'
	elif "FT" in name:
		truth='MultiNER-Health_truth_FT.txt'
	elif "SM" in name:
		truth='MultiNER-Health_truth_SM.txt'
	df_truth =  pd.read_csv('answer/{}'.format(truth),encoding='utf-8',delimiter=' ',header=None,skip_blank_lines =False, quoting=csv.QUOTE_NONE)
	df_prediction =  pd.read_csv(predict_path,encoding='utf-8',delimiter=' ',header=None,skip_blank_lines =False, quoting=csv.QUOTE_NONE)
	df = pd.concat([df_truth,df_prediction[1]],axis=1)
	output_name=str(name)+"_Eval.txt"
	if not os.path.exists('Eval/'):
		os.makedirs('Eval/')
	df.to_csv(path.join('Eval/',output_name),encoding='utf-8',header=None,index=None,sep=" ")

