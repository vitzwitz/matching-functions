'''
FUNC:P_1uou_2_4_2_4
PDB:1uou
EC:2.4.2.4
RESI:his,arg,lys
LOCI:a-116,202,221;
'''
import motifFunctions as cmd
HIS_ARG = { 
	'distances':
		[[18.24, 18.35, 17.06, 16.27, 14.95, 14.49, 14.18], [16.94, 17.1, 15.84, 15.1, 13.78, 13.39, 12.97], [16.76, 16.89, 15.63, 15.02, 13.74, 13.5, 12.81], [15.87, 16.1, 14.89, 14.08, 12.77, 12.32, 12.03], [15.61, 15.8, 14.58, 14.01, 12.74, 12.55, 11.79], [15.01, 15.26, 14.08, 13.38, 12.09, 11.77, 11.25]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 18.24), ('CB', 'HIS', 'CG', 'ARG', 18.35), ('CB', 'HIS', 'CD', 'ARG', 17.06), ('CB', 'HIS', 'NE', 'ARG', 16.27), ('CB', 'HIS', 'CZ', 'ARG', 14.95), ('CB', 'HIS', 'NH1', 'ARG', 14.49), ('CB', 'HIS', 'NH2', 'ARG', 14.18)], [('CG', 'HIS', 'CB', 'ARG', 16.94), ('CG', 'HIS', 'CG', 'ARG', 17.1), ('CG', 'HIS', 'CD', 'ARG', 15.84), ('CG', 'HIS', 'NE', 'ARG', 15.1), ('CG', 'HIS', 'CZ', 'ARG', 13.78), ('CG', 'HIS', 'NH1', 'ARG', 13.39), ('CG', 'HIS', 'NH2', 'ARG', 12.97)], [('ND1', 'HIS', 'CB', 'ARG', 16.76), ('ND1', 'HIS', 'CG', 'ARG', 16.89), ('ND1', 'HIS', 'CD', 'ARG', 15.63), ('ND1', 'HIS', 'NE', 'ARG', 15.02), ('ND1', 'HIS', 'CZ', 'ARG', 13.74), ('ND1', 'HIS', 'NH1', 'ARG', 13.5), ('ND1', 'HIS', 'NH2', 'ARG', 12.81)], [('CD2', 'HIS', 'CB', 'ARG', 15.87), ('CD2', 'HIS', 'CG', 'ARG', 16.1), ('CD2', 'HIS', 'CD', 'ARG', 14.89), ('CD2', 'HIS', 'NE', 'ARG', 14.08), ('CD2', 'HIS', 'CZ', 'ARG', 12.77), ('CD2', 'HIS', 'NH1', 'ARG', 12.32), ('CD2', 'HIS', 'NH2', 'ARG', 12.03)], [('CE1', 'HIS', 'CB', 'ARG', 15.61), ('CE1', 'HIS', 'CG', 'ARG', 15.8), ('CE1', 'HIS', 'CD', 'ARG', 14.58), ('CE1', 'HIS', 'NE', 'ARG', 14.01), ('CE1', 'HIS', 'CZ', 'ARG', 12.74), ('CE1', 'HIS', 'NH1', 'ARG', 12.55), ('CE1', 'HIS', 'NH2', 'ARG', 11.79)], [('NE2', 'HIS', 'CB', 'ARG', 15.01), ('NE2', 'HIS', 'CG', 'ARG', 15.26), ('NE2', 'HIS', 'CD', 'ARG', 14.08), ('NE2', 'HIS', 'NE', 'ARG', 13.38), ('NE2', 'HIS', 'CZ', 'ARG', 12.09), ('NE2', 'HIS', 'NH1', 'ARG', 11.77), ('NE2', 'HIS', 'NH2', 'ARG', 11.25)]]}
ARG_LYS = { 
	'distances':
		[[16.33, 15.23, 14.78, 13.34, 12.52], [16.01, 14.96, 14.69, 13.29, 12.37], [14.64, 13.66, 13.44, 12.09, 11.08], [14.53, 13.64, 13.34, 12.02, 10.93], [13.49, 12.65, 12.28, 11.01, 9.87], [13.78, 13.06, 12.61, 11.41, 10.23], [12.27, 11.38, 11.03, 9.74, 8.62]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'LYS', 16.33), ('CB', 'ARG', 'CG', 'LYS', 15.23), ('CB', 'ARG', 'CD', 'LYS', 14.78), ('CB', 'ARG', 'CE', 'LYS', 13.34), ('CB', 'ARG', 'NZ', 'LYS', 12.52)], [('CG', 'ARG', 'CB', 'LYS', 16.01), ('CG', 'ARG', 'CG', 'LYS', 14.96), ('CG', 'ARG', 'CD', 'LYS', 14.69), ('CG', 'ARG', 'CE', 'LYS', 13.29), ('CG', 'ARG', 'NZ', 'LYS', 12.37)], [('CD', 'ARG', 'CB', 'LYS', 14.64), ('CD', 'ARG', 'CG', 'LYS', 13.66), ('CD', 'ARG', 'CD', 'LYS', 13.44), ('CD', 'ARG', 'CE', 'LYS', 12.09), ('CD', 'ARG', 'NZ', 'LYS', 11.08)], [('NE', 'ARG', 'CB', 'LYS', 14.53), ('NE', 'ARG', 'CG', 'LYS', 13.64), ('NE', 'ARG', 'CD', 'LYS', 13.34), ('NE', 'ARG', 'CE', 'LYS', 12.02), ('NE', 'ARG', 'NZ', 'LYS', 10.93)], [('CZ', 'ARG', 'CB', 'LYS', 13.49), ('CZ', 'ARG', 'CG', 'LYS', 12.65), ('CZ', 'ARG', 'CD', 'LYS', 12.28), ('CZ', 'ARG', 'CE', 'LYS', 11.01), ('CZ', 'ARG', 'NZ', 'LYS', 9.87)], [('NH1', 'ARG', 'CB', 'LYS', 13.78), ('NH1', 'ARG', 'CG', 'LYS', 13.06), ('NH1', 'ARG', 'CD', 'LYS', 12.61), ('NH1', 'ARG', 'CE', 'LYS', 11.41), ('NH1', 'ARG', 'NZ', 'LYS', 10.23)], [('NH2', 'ARG', 'CB', 'LYS', 12.27), ('NH2', 'ARG', 'CG', 'LYS', 11.38), ('NH2', 'ARG', 'CD', 'LYS', 11.03), ('NH2', 'ARG', 'CE', 'LYS', 9.74), ('NH2', 'ARG', 'NZ', 'LYS', 8.62)]]}
HIS_LYS = { 
	'distances':
		[[9.25, 9.94, 9.21, 9.89, 9.8], [8.51, 8.97, 8.07, 8.6, 8.54], [7.42, 7.81, 6.86, 7.54, 7.69], [9.03, 9.25, 8.22, 8.44, 8.26], [7.36, 7.41, 6.23, 6.62, 6.8], [8.38, 8.36, 7.18, 7.26, 7.19]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYS', 9.25), ('CB', 'HIS', 'CG', 'LYS', 9.94), ('CB', 'HIS', 'CD', 'LYS', 9.21), ('CB', 'HIS', 'CE', 'LYS', 9.89), ('CB', 'HIS', 'NZ', 'LYS', 9.8)], [('CG', 'HIS', 'CB', 'LYS', 8.51), ('CG', 'HIS', 'CG', 'LYS', 8.97), ('CG', 'HIS', 'CD', 'LYS', 8.07), ('CG', 'HIS', 'CE', 'LYS', 8.6), ('CG', 'HIS', 'NZ', 'LYS', 8.54)], [('ND1', 'HIS', 'CB', 'LYS', 7.42), ('ND1', 'HIS', 'CG', 'LYS', 7.81), ('ND1', 'HIS', 'CD', 'LYS', 6.86), ('ND1', 'HIS', 'CE', 'LYS', 7.54), ('ND1', 'HIS', 'NZ', 'LYS', 7.69)], [('CD2', 'HIS', 'CB', 'LYS', 9.03), ('CD2', 'HIS', 'CG', 'LYS', 9.25), ('CD2', 'HIS', 'CD', 'LYS', 8.22), ('CD2', 'HIS', 'CE', 'LYS', 8.44), ('CD2', 'HIS', 'NZ', 'LYS', 8.26)], [('CE1', 'HIS', 'CB', 'LYS', 7.36), ('CE1', 'HIS', 'CG', 'LYS', 7.41), ('CE1', 'HIS', 'CD', 'LYS', 6.23), ('CE1', 'HIS', 'CE', 'LYS', 6.62), ('CE1', 'HIS', 'NZ', 'LYS', 6.8)], [('NE2', 'HIS', 'CB', 'LYS', 8.38), ('NE2', 'HIS', 'CG', 'LYS', 8.36), ('NE2', 'HIS', 'CD', 'LYS', 7.18), ('NE2', 'HIS', 'CE', 'LYS', 7.26), ('NE2', 'HIS', 'NZ', 'LYS', 7.19)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ARG, d, 'P_1uou_2_4_2_4')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_LYS, d, 'P_1uou_2_4_2_4')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_LYS, d, 'P_1uou_2_4_2_4')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ARG' :  match1,
		'ARG_LYS' :  match2,
		'HIS_LYS' :  match3}