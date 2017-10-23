'''
FUNC:A_2tps_2_5_1_3
PDB:2tps
EC:2.5.1.3
RESI:arg,ser,lys
LOCI:a-59,130,159;
'''
import motifFunctions as cmd
LYS_SER = { 
	'distances':
		[[12.0, 11.28], [11.25, 10.64], [9.74, 9.14], [9.13, 8.76], [9.64, 9.26]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'SER', 12.0), ('CB', 'LYS', 'OG', 'SER', 11.28)], [('CG', 'LYS', 'CB', 'SER', 11.25), ('CG', 'LYS', 'OG', 'SER', 10.64)], [('CD', 'LYS', 'CB', 'SER', 9.74), ('CD', 'LYS', 'OG', 'SER', 9.14)], [('CE', 'LYS', 'CB', 'SER', 9.13), ('CE', 'LYS', 'OG', 'SER', 8.76)], [('NZ', 'LYS', 'CB', 'SER', 9.64), ('NZ', 'LYS', 'OG', 'SER', 9.26)]]}
ARG_SER = { 
	'distances':
		[[13.65, 12.27], [12.84, 11.52], [11.85, 10.53], [11.42, 10.2], [12.2, 11.05], [13.38, 12.2], [11.89, 10.88]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'SER', 13.65), ('CB', 'ARG', 'OG', 'SER', 12.27)], [('CG', 'ARG', 'CB', 'SER', 12.84), ('CG', 'ARG', 'OG', 'SER', 11.52)], [('CD', 'ARG', 'CB', 'SER', 11.85), ('CD', 'ARG', 'OG', 'SER', 10.53)], [('NE', 'ARG', 'CB', 'SER', 11.42), ('NE', 'ARG', 'OG', 'SER', 10.2)], [('CZ', 'ARG', 'CB', 'SER', 12.2), ('CZ', 'ARG', 'OG', 'SER', 11.05)], [('NH1', 'ARG', 'CB', 'SER', 13.38), ('NH1', 'ARG', 'OG', 'SER', 12.2)], [('NH2', 'ARG', 'CB', 'SER', 11.89), ('NH2', 'ARG', 'OG', 'SER', 10.88)]]}
ARG_LYS = { 
	'distances':
		[[11.12, 11.34, 11.16, 11.99, 11.77], [9.89, 9.98, 9.83, 10.61, 10.31], [8.69, 8.86, 8.61, 9.5, 9.41], [7.51, 7.53, 7.36, 8.21, 8.05], [6.7, 6.83, 7.02, 8.0, 7.82], [7.12, 7.56, 7.96, 9.08, 8.96], [5.83, 5.7, 6.02, 6.93, 6.66]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'LYS', 11.12), ('CB', 'ARG', 'CG', 'LYS', 11.34), ('CB', 'ARG', 'CD', 'LYS', 11.16), ('CB', 'ARG', 'CE', 'LYS', 11.99), ('CB', 'ARG', 'NZ', 'LYS', 11.77)], [('CG', 'ARG', 'CB', 'LYS', 9.89), ('CG', 'ARG', 'CG', 'LYS', 9.98), ('CG', 'ARG', 'CD', 'LYS', 9.83), ('CG', 'ARG', 'CE', 'LYS', 10.61), ('CG', 'ARG', 'NZ', 'LYS', 10.31)], [('CD', 'ARG', 'CB', 'LYS', 8.69), ('CD', 'ARG', 'CG', 'LYS', 8.86), ('CD', 'ARG', 'CD', 'LYS', 8.61), ('CD', 'ARG', 'CE', 'LYS', 9.5), ('CD', 'ARG', 'NZ', 'LYS', 9.41)], [('NE', 'ARG', 'CB', 'LYS', 7.51), ('NE', 'ARG', 'CG', 'LYS', 7.53), ('NE', 'ARG', 'CD', 'LYS', 7.36), ('NE', 'ARG', 'CE', 'LYS', 8.21), ('NE', 'ARG', 'NZ', 'LYS', 8.05)], [('CZ', 'ARG', 'CB', 'LYS', 6.7), ('CZ', 'ARG', 'CG', 'LYS', 6.83), ('CZ', 'ARG', 'CD', 'LYS', 7.02), ('CZ', 'ARG', 'CE', 'LYS', 8.0), ('CZ', 'ARG', 'NZ', 'LYS', 7.82)], [('NH1', 'ARG', 'CB', 'LYS', 7.12), ('NH1', 'ARG', 'CG', 'LYS', 7.56), ('NH1', 'ARG', 'CD', 'LYS', 7.96), ('NH1', 'ARG', 'CE', 'LYS', 9.08), ('NH1', 'ARG', 'NZ', 'LYS', 8.96)], [('NH2', 'ARG', 'CB', 'LYS', 5.83), ('NH2', 'ARG', 'CG', 'LYS', 5.7), ('NH2', 'ARG', 'CD', 'LYS', 6.02), ('NH2', 'ARG', 'CE', 'LYS', 6.93), ('NH2', 'ARG', 'NZ', 'LYS', 6.66)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_SER, d, 'A_2tps_2_5_1_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_SER, d, 'A_2tps_2_5_1_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_LYS, d, 'A_2tps_2_5_1_3')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_SER' :  match1,
		'ARG_SER' :  match2,
		'ARG_LYS' :  match3}