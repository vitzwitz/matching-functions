'''
FUNC:P_2tps_2_5_1_3
PDB:2tps
EC:2.5.1.3
RESI:arg,ser,lys
LOCI:a-59,130,159;
'''
import motifFunctions as cmd
SER_LYS = { 
	'distances':
		[[12.17, 11.38, 9.88, 9.19, 9.81], [11.45, 10.76, 9.28, 8.79, 9.4]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'LYS', 12.17), ('CB', 'SER', 'CG', 'LYS', 11.38), ('CB', 'SER', 'CD', 'LYS', 9.88), ('CB', 'SER', 'CE', 'LYS', 9.19), ('CB', 'SER', 'NZ', 'LYS', 9.81)], [('OG', 'SER', 'CB', 'LYS', 11.45), ('OG', 'SER', 'CG', 'LYS', 10.76), ('OG', 'SER', 'CD', 'LYS', 9.28), ('OG', 'SER', 'CE', 'LYS', 8.79), ('OG', 'SER', 'NZ', 'LYS', 9.4)]]}
ARG_SER = { 
	'distances':
		[[13.61, 12.27], [12.9, 11.61], [11.98, 10.68], [11.5, 10.31], [12.33, 11.21], [13.52, 12.37], [12.01, 11.02]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'SER', 13.61), ('CB', 'ARG', 'OG', 'SER', 12.27)], [('CG', 'ARG', 'CB', 'SER', 12.9), ('CG', 'ARG', 'OG', 'SER', 11.61)], [('CD', 'ARG', 'CB', 'SER', 11.98), ('CD', 'ARG', 'OG', 'SER', 10.68)], [('NE', 'ARG', 'CB', 'SER', 11.5), ('NE', 'ARG', 'OG', 'SER', 10.31)], [('CZ', 'ARG', 'CB', 'SER', 12.33), ('CZ', 'ARG', 'OG', 'SER', 11.21)], [('NH1', 'ARG', 'CB', 'SER', 13.52), ('NH1', 'ARG', 'OG', 'SER', 12.37)], [('NH2', 'ARG', 'CB', 'SER', 12.01), ('NH2', 'ARG', 'OG', 'SER', 11.02)]]}
ARG_LYS = { 
	'distances':
		[[11.09, 11.17, 11.06, 11.76, 11.54], [9.85, 9.81, 9.75, 10.41, 10.1], [8.72, 8.8, 8.63, 9.42, 9.36], [7.57, 7.47, 7.37, 8.12, 7.97], [6.8, 6.82, 7.08, 7.97, 7.75], [7.13, 7.47, 7.95, 8.99, 8.83], [6.03, 5.75, 6.14, 6.91, 6.55]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'LYS', 11.09), ('CB', 'ARG', 'CG', 'LYS', 11.17), ('CB', 'ARG', 'CD', 'LYS', 11.06), ('CB', 'ARG', 'CE', 'LYS', 11.76), ('CB', 'ARG', 'NZ', 'LYS', 11.54)], [('CG', 'ARG', 'CB', 'LYS', 9.85), ('CG', 'ARG', 'CG', 'LYS', 9.81), ('CG', 'ARG', 'CD', 'LYS', 9.75), ('CG', 'ARG', 'CE', 'LYS', 10.41), ('CG', 'ARG', 'NZ', 'LYS', 10.1)], [('CD', 'ARG', 'CB', 'LYS', 8.72), ('CD', 'ARG', 'CG', 'LYS', 8.8), ('CD', 'ARG', 'CD', 'LYS', 8.63), ('CD', 'ARG', 'CE', 'LYS', 9.42), ('CD', 'ARG', 'NZ', 'LYS', 9.36)], [('NE', 'ARG', 'CB', 'LYS', 7.57), ('NE', 'ARG', 'CG', 'LYS', 7.47), ('NE', 'ARG', 'CD', 'LYS', 7.37), ('NE', 'ARG', 'CE', 'LYS', 8.12), ('NE', 'ARG', 'NZ', 'LYS', 7.97)], [('CZ', 'ARG', 'CB', 'LYS', 6.8), ('CZ', 'ARG', 'CG', 'LYS', 6.82), ('CZ', 'ARG', 'CD', 'LYS', 7.08), ('CZ', 'ARG', 'CE', 'LYS', 7.97), ('CZ', 'ARG', 'NZ', 'LYS', 7.75)], [('NH1', 'ARG', 'CB', 'LYS', 7.13), ('NH1', 'ARG', 'CG', 'LYS', 7.47), ('NH1', 'ARG', 'CD', 'LYS', 7.95), ('NH1', 'ARG', 'CE', 'LYS', 8.99), ('NH1', 'ARG', 'NZ', 'LYS', 8.83)], [('NH2', 'ARG', 'CB', 'LYS', 6.03), ('NH2', 'ARG', 'CG', 'LYS', 5.75), ('NH2', 'ARG', 'CD', 'LYS', 6.14), ('NH2', 'ARG', 'CE', 'LYS', 6.91), ('NH2', 'ARG', 'NZ', 'LYS', 6.55)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_LYS, d, 'P_2tps_2_5_1_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_SER, d, 'P_2tps_2_5_1_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_LYS, d, 'P_2tps_2_5_1_3')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_LYS' :  match1,
		'ARG_SER' :  match2,
		'ARG_LYS' :  match3}