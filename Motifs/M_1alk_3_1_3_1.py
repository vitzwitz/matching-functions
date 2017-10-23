'''
FUNC:M_1alk_3_1_3_1
PDB:1alk
EC:3.1.3.1
RESI:ser,arg,zn,zn,mg
LOCI:a-102,166,450,451,452;
'''
import motifFunctions as cmd
SER_ZNI = { 
	'distances':
		[[5.55], [4.13]],
	'comparisons':
		[[('CB', 'SER', 'ZN', 'ZNI', 5.55)], [('OG', 'SER', 'ZN', 'ZNI', 4.13)]]}
ARG_ZNI = { 
	'distances':
		[[12.71], [12.53], [11.17], [10.32], [8.99], [8.42], [8.45]],
	'comparisons':
		[[('CB', 'ARG', 'ZN', 'ZNI', 12.71)], [('CG', 'ARG', 'ZN', 'ZNI', 12.53)], [('CD', 'ARG', 'ZN', 'ZNI', 11.17)], [('NE', 'ARG', 'ZN', 'ZNI', 10.32)], [('CZ', 'ARG', 'ZN', 'ZNI', 8.99)], [('NH1', 'ARG', 'ZN', 'ZNI', 8.42)], [('NH2', 'ARG', 'ZN', 'ZNI', 8.45)]]}
ZN_ZN = { 
	'distances':
		[5.99, 5.99],
	'comparisons':
		[('ZN', 'ZN', 'ZN', 'ZN', 5.99), ('ZN', 'ZN', 'ZN', 'ZN', 5.99)]}
ARG_MG = { 
	'distances':
		[[12.11], [12.29], [11.36], [10.14], [9.11], [9.36], [7.96]],
	'comparisons':
		[[('CB', 'ARG', 'MG', 'MG', 12.11)], [('CG', 'ARG', 'MG', 'MG', 12.29)], [('CD', 'ARG', 'MG', 'MG', 11.36)], [('NE', 'ARG', 'MG', 'MG', 10.14)], [('CZ', 'ARG', 'MG', 'MG', 9.11)], [('NH1', 'ARG', 'MG', 'MG', 9.36)], [('NH2', 'ARG', 'MG', 'MG', 7.96)]]}
MG_ZNI = { 
	'distances':
		[6.64],
	'comparisons':
		[('MG', 'MG', 'ZN', 'ZNI', 6.64)]}
ZN_ARG = { 
	'distances':
		[13.01, 12.29, 10.88, 10.0, 8.74, 8.26, 8.34, 12.71, 12.53, 11.17, 10.32, 8.99, 8.42, 8.45],
	'comparisons':
		[('ZN', 'ZN', 'CB', 'ARG', 13.01), ('ZN', 'ZN', 'CG', 'ARG', 12.29), ('ZN', 'ZN', 'CD', 'ARG', 10.88), ('ZN', 'ZN', 'NE', 'ARG', 10.0), ('ZN', 'ZN', 'CZ', 'ARG', 8.74), ('ZN', 'ZN', 'NH1', 'ARG', 8.26), ('ZN', 'ZN', 'NH2', 'ARG', 8.34), ('ZN', 'ZN', 'CB', 'ARG', 12.71), ('ZN', 'ZN', 'CG', 'ARG', 12.53), ('ZN', 'ZN', 'CD', 'ARG', 11.17), ('ZN', 'ZN', 'NE', 'ARG', 10.32), ('ZN', 'ZN', 'CZ', 'ARG', 8.99), ('ZN', 'ZN', 'NH1', 'ARG', 8.42), ('ZN', 'ZN', 'NH2', 'ARG', 8.45)]}
ZN_MG = { 
	'distances':
		[8.88, 6.64],
	'comparisons':
		[('ZN', 'ZN', 'MG', 'MG', 8.88), ('ZN', 'ZN', 'MG', 'MG', 6.64)]}
ZN_SER = { 
	'distances':
		[7.91, 6.86, 5.55, 4.13],
	'comparisons':
		[('ZN', 'ZN', 'CB', 'SER', 7.91), ('ZN', 'ZN', 'OG', 'SER', 6.86), ('ZN', 'ZN', 'CB', 'SER', 5.55), ('ZN', 'ZN', 'OG', 'SER', 4.13)]}
SER_ARG = { 
	'distances':
		[[9.47, 9.57, 8.36, 7.63, 6.48, 6.03, 6.13], [10.72, 10.68, 9.4, 8.55, 7.28, 6.81, 6.77]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ARG', 9.47), ('CB', 'SER', 'CG', 'ARG', 9.57), ('CB', 'SER', 'CD', 'ARG', 8.36), ('CB', 'SER', 'NE', 'ARG', 7.63), ('CB', 'SER', 'CZ', 'ARG', 6.48), ('CB', 'SER', 'NH1', 'ARG', 6.03), ('CB', 'SER', 'NH2', 'ARG', 6.13)], [('OG', 'SER', 'CB', 'ARG', 10.72), ('OG', 'SER', 'CG', 'ARG', 10.68), ('OG', 'SER', 'CD', 'ARG', 9.4), ('OG', 'SER', 'NE', 'ARG', 8.55), ('OG', 'SER', 'CZ', 'ARG', 7.28), ('OG', 'SER', 'NH1', 'ARG', 6.81), ('OG', 'SER', 'NH2', 'ARG', 6.77)]]}
SER_MG = { 
	'distances':
		[[6.49], [6.01]],
	'comparisons':
		[[('CB', 'SER', 'MG', 'MG', 6.49)], [('OG', 'SER', 'MG', 'MG', 6.01)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_ZNI, d, 'M_1alk_3_1_3_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_ZNI, d, 'M_1alk_3_1_3_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ZN_ZN, d, 'M_1alk_3_1_3_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ARG_MG, d, 'M_1alk_3_1_3_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(MG_ZNI, d, 'M_1alk_3_1_3_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ZN_ARG, d, 'M_1alk_3_1_3_1')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ZN_MG, d, 'M_1alk_3_1_3_1')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ZN_SER, d, 'M_1alk_3_1_3_1')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(SER_ARG, d, 'M_1alk_3_1_3_1')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(SER_MG, d, 'M_1alk_3_1_3_1')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_ZNI' :  match1,
		'ARG_ZNI' :  match2,
		'ZN_ZN' :  match3,
		'ARG_MG' :  match4,
		'MG_ZNI' :  match5,
		'ZN_ARG' :  match6,
		'ZN_MG' :  match7,
		'ZN_SER' :  match8,
		'SER_ARG' :  match9,
		'SER_MG' :  match10}