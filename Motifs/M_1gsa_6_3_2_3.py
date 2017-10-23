'''
FUNC:M_1gsa_6_3_2_3
PDB:1gsa
EC:6.3.2.3
RESI:lys,arg,arg,mg,mg
LOCI:a-160,210,225,319,320;
'''
import motifFunctions as cmd
ARG_ARG = { 
	'distances':
		[[8.56, 9.88, 10.88, 10.47, 10.32, 10.54, 10.15], [7.47, 8.67, 9.76, 9.45, 9.24, 9.31, 9.23], [6.13, 7.41, 8.39, 8.04, 7.96, 8.19, 7.98], [6.13, 7.15, 7.93, 7.34, 6.99, 7.2, 6.83], [6.14, 7.1, 7.54, 6.69, 6.34, 6.83, 5.94], [6.14, 7.27, 7.55, 6.67, 6.64, 7.42, 6.22], [6.76, 7.38, 7.61, 6.56, 5.88, 6.29, 5.22], [8.56, 7.47, 6.13, 6.13, 6.14, 6.14, 6.76], [9.88, 8.67, 7.41, 7.15, 7.1, 7.27, 7.38], [10.88, 9.76, 8.39, 7.93, 7.54, 7.55, 7.61], [10.47, 9.45, 8.04, 7.34, 6.69, 6.67, 6.56], [10.32, 9.24, 7.96, 6.99, 6.34, 6.64, 5.88], [10.54, 9.31, 8.19, 7.2, 6.83, 7.42, 6.29], [10.15, 9.23, 7.98, 6.83, 5.94, 6.22, 5.22]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ARG', 8.56), ('CB', 'ARG', 'CG', 'ARG', 9.88), ('CB', 'ARG', 'CD', 'ARG', 10.88), ('CB', 'ARG', 'NE', 'ARG', 10.47), ('CB', 'ARG', 'CZ', 'ARG', 10.32), ('CB', 'ARG', 'NH1', 'ARG', 10.54), ('CB', 'ARG', 'NH2', 'ARG', 10.15)], [('CG', 'ARG', 'CB', 'ARG', 7.47), ('CG', 'ARG', 'CG', 'ARG', 8.67), ('CG', 'ARG', 'CD', 'ARG', 9.76), ('CG', 'ARG', 'NE', 'ARG', 9.45), ('CG', 'ARG', 'CZ', 'ARG', 9.24), ('CG', 'ARG', 'NH1', 'ARG', 9.31), ('CG', 'ARG', 'NH2', 'ARG', 9.23)], [('CD', 'ARG', 'CB', 'ARG', 6.13), ('CD', 'ARG', 'CG', 'ARG', 7.41), ('CD', 'ARG', 'CD', 'ARG', 8.39), ('CD', 'ARG', 'NE', 'ARG', 8.04), ('CD', 'ARG', 'CZ', 'ARG', 7.96), ('CD', 'ARG', 'NH1', 'ARG', 8.19), ('CD', 'ARG', 'NH2', 'ARG', 7.98)], [('NE', 'ARG', 'CB', 'ARG', 6.13), ('NE', 'ARG', 'CG', 'ARG', 7.15), ('NE', 'ARG', 'CD', 'ARG', 7.93), ('NE', 'ARG', 'NE', 'ARG', 7.34), ('NE', 'ARG', 'CZ', 'ARG', 6.99), ('NE', 'ARG', 'NH1', 'ARG', 7.2), ('NE', 'ARG', 'NH2', 'ARG', 6.83)], [('CZ', 'ARG', 'CB', 'ARG', 6.14), ('CZ', 'ARG', 'CG', 'ARG', 7.1), ('CZ', 'ARG', 'CD', 'ARG', 7.54), ('CZ', 'ARG', 'NE', 'ARG', 6.69), ('CZ', 'ARG', 'CZ', 'ARG', 6.34), ('CZ', 'ARG', 'NH1', 'ARG', 6.83), ('CZ', 'ARG', 'NH2', 'ARG', 5.94)], [('NH1', 'ARG', 'CB', 'ARG', 6.14), ('NH1', 'ARG', 'CG', 'ARG', 7.27), ('NH1', 'ARG', 'CD', 'ARG', 7.55), ('NH1', 'ARG', 'NE', 'ARG', 6.67), ('NH1', 'ARG', 'CZ', 'ARG', 6.64), ('NH1', 'ARG', 'NH1', 'ARG', 7.42), ('NH1', 'ARG', 'NH2', 'ARG', 6.22)], [('NH2', 'ARG', 'CB', 'ARG', 6.76), ('NH2', 'ARG', 'CG', 'ARG', 7.38), ('NH2', 'ARG', 'CD', 'ARG', 7.61), ('NH2', 'ARG', 'NE', 'ARG', 6.56), ('NH2', 'ARG', 'CZ', 'ARG', 5.88), ('NH2', 'ARG', 'NH1', 'ARG', 6.29), ('NH2', 'ARG', 'NH2', 'ARG', 5.22)], [('CB', 'ARG', 'CB', 'ARG', 8.56), ('CB', 'ARG', 'CG', 'ARG', 7.47), ('CB', 'ARG', 'CD', 'ARG', 6.13), ('CB', 'ARG', 'NE', 'ARG', 6.13), ('CB', 'ARG', 'CZ', 'ARG', 6.14), ('CB', 'ARG', 'NH1', 'ARG', 6.14), ('CB', 'ARG', 'NH2', 'ARG', 6.76)], [('CG', 'ARG', 'CB', 'ARG', 9.88), ('CG', 'ARG', 'CG', 'ARG', 8.67), ('CG', 'ARG', 'CD', 'ARG', 7.41), ('CG', 'ARG', 'NE', 'ARG', 7.15), ('CG', 'ARG', 'CZ', 'ARG', 7.1), ('CG', 'ARG', 'NH1', 'ARG', 7.27), ('CG', 'ARG', 'NH2', 'ARG', 7.38)], [('CD', 'ARG', 'CB', 'ARG', 10.88), ('CD', 'ARG', 'CG', 'ARG', 9.76), ('CD', 'ARG', 'CD', 'ARG', 8.39), ('CD', 'ARG', 'NE', 'ARG', 7.93), ('CD', 'ARG', 'CZ', 'ARG', 7.54), ('CD', 'ARG', 'NH1', 'ARG', 7.55), ('CD', 'ARG', 'NH2', 'ARG', 7.61)], [('NE', 'ARG', 'CB', 'ARG', 10.47), ('NE', 'ARG', 'CG', 'ARG', 9.45), ('NE', 'ARG', 'CD', 'ARG', 8.04), ('NE', 'ARG', 'NE', 'ARG', 7.34), ('NE', 'ARG', 'CZ', 'ARG', 6.69), ('NE', 'ARG', 'NH1', 'ARG', 6.67), ('NE', 'ARG', 'NH2', 'ARG', 6.56)], [('CZ', 'ARG', 'CB', 'ARG', 10.32), ('CZ', 'ARG', 'CG', 'ARG', 9.24), ('CZ', 'ARG', 'CD', 'ARG', 7.96), ('CZ', 'ARG', 'NE', 'ARG', 6.99), ('CZ', 'ARG', 'CZ', 'ARG', 6.34), ('CZ', 'ARG', 'NH1', 'ARG', 6.64), ('CZ', 'ARG', 'NH2', 'ARG', 5.88)], [('NH1', 'ARG', 'CB', 'ARG', 10.54), ('NH1', 'ARG', 'CG', 'ARG', 9.31), ('NH1', 'ARG', 'CD', 'ARG', 8.19), ('NH1', 'ARG', 'NE', 'ARG', 7.2), ('NH1', 'ARG', 'CZ', 'ARG', 6.83), ('NH1', 'ARG', 'NH1', 'ARG', 7.42), ('NH1', 'ARG', 'NH2', 'ARG', 6.29)], [('NH2', 'ARG', 'CB', 'ARG', 10.15), ('NH2', 'ARG', 'CG', 'ARG', 9.23), ('NH2', 'ARG', 'CD', 'ARG', 7.98), ('NH2', 'ARG', 'NE', 'ARG', 6.83), ('NH2', 'ARG', 'CZ', 'ARG', 5.94), ('NH2', 'ARG', 'NH1', 'ARG', 6.22), ('NH2', 'ARG', 'NH2', 'ARG', 5.22)]]}
ARG_MG = { 
	'distances':
		[[10.25], [10.14], [9.18], [8.11], [6.87], [6.58], [6.23], [13.08], [12.61], [11.61], [10.31], [9.16], [9.23], [8.09], [9.84], [10.35], [9.86], [8.45], [7.99], [8.9], [6.76], [11.23], [11.13], [10.26], [8.86], [8.1], [8.73], [6.9]],
	'comparisons':
		[[('CB', 'ARG', 'MG', 'MG', 10.25)], [('CG', 'ARG', 'MG', 'MG', 10.14)], [('CD', 'ARG', 'MG', 'MG', 9.18)], [('NE', 'ARG', 'MG', 'MG', 8.11)], [('CZ', 'ARG', 'MG', 'MG', 6.87)], [('NH1', 'ARG', 'MG', 'MG', 6.58)], [('NH2', 'ARG', 'MG', 'MG', 6.23)], [('CB', 'ARG', 'MG', 'MG', 13.08)], [('CG', 'ARG', 'MG', 'MG', 12.61)], [('CD', 'ARG', 'MG', 'MG', 11.61)], [('NE', 'ARG', 'MG', 'MG', 10.31)], [('CZ', 'ARG', 'MG', 'MG', 9.16)], [('NH1', 'ARG', 'MG', 'MG', 9.23)], [('NH2', 'ARG', 'MG', 'MG', 8.09)], [('CB', 'ARG', 'MG', 'MG', 9.84)], [('CG', 'ARG', 'MG', 'MG', 10.35)], [('CD', 'ARG', 'MG', 'MG', 9.86)], [('NE', 'ARG', 'MG', 'MG', 8.45)], [('CZ', 'ARG', 'MG', 'MG', 7.99)], [('NH1', 'ARG', 'MG', 'MG', 8.9)], [('NH2', 'ARG', 'MG', 'MG', 6.76)], [('CB', 'ARG', 'MG', 'MG', 11.23)], [('CG', 'ARG', 'MG', 'MG', 11.13)], [('CD', 'ARG', 'MG', 'MG', 10.26)], [('NE', 'ARG', 'MG', 'MG', 8.86)], [('CZ', 'ARG', 'MG', 'MG', 8.1)], [('NH1', 'ARG', 'MG', 'MG', 8.73)], [('NH2', 'ARG', 'MG', 'MG', 6.9)]]}
MG_ARGI = { 
	'distances':
		[9.84, 10.35, 9.86, 8.45, 7.99, 8.9, 6.76, 11.23, 11.13, 10.26, 8.86, 8.1, 8.73, 6.9],
	'comparisons':
		[('MG', 'MG', 'CB', 'ARGI', 9.84), ('MG', 'MG', 'CG', 'ARGI', 10.35), ('MG', 'MG', 'CD', 'ARGI', 9.86), ('MG', 'MG', 'NE', 'ARGI', 8.45), ('MG', 'MG', 'CZ', 'ARGI', 7.99), ('MG', 'MG', 'NH1', 'ARGI', 8.9), ('MG', 'MG', 'NH2', 'ARGI', 6.76), ('MG', 'MG', 'CB', 'ARGI', 11.23), ('MG', 'MG', 'CG', 'ARGI', 11.13), ('MG', 'MG', 'CD', 'ARGI', 10.26), ('MG', 'MG', 'NE', 'ARGI', 8.86), ('MG', 'MG', 'CZ', 'ARGI', 8.1), ('MG', 'MG', 'NH1', 'ARGI', 8.73), ('MG', 'MG', 'NH2', 'ARGI', 6.9)]}
MG_MG = { 
	'distances':
		[5.61, 5.61],
	'comparisons':
		[('MG', 'MG', 'MG', 'MG', 5.61), ('MG', 'MG', 'MG', 'MG', 5.61)]}
ARG_LYS = { 
	'distances':
		[[17.76, 17.98, 16.65, 16.69, 15.35], [18.24, 18.46, 17.17, 17.19, 15.86], [17.7, 17.81, 16.52, 16.41, 15.06], [16.82, 16.97, 15.74, 15.69, 14.4], [15.76, 15.85, 14.62, 14.52, 13.23], [15.38, 15.35, 14.06, 13.83, 12.49], [15.2, 15.35, 14.21, 14.18, 12.97], [19.05, 18.9, 17.67, 17.27, 15.96], [19.61, 19.46, 18.3, 17.9, 16.65], [18.98, 18.75, 17.65, 17.18, 15.98], [17.56, 17.35, 16.27, 15.84, 14.67], [17.11, 17.01, 15.99, 15.68, 14.56], [17.95, 17.95, 16.96, 16.74, 15.64], [15.83, 15.77, 14.77, 14.52, 13.42]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'LYS', 17.76), ('CB', 'ARG', 'CG', 'LYS', 17.98), ('CB', 'ARG', 'CD', 'LYS', 16.65), ('CB', 'ARG', 'CE', 'LYS', 16.69), ('CB', 'ARG', 'NZ', 'LYS', 15.35)], [('CG', 'ARG', 'CB', 'LYS', 18.24), ('CG', 'ARG', 'CG', 'LYS', 18.46), ('CG', 'ARG', 'CD', 'LYS', 17.17), ('CG', 'ARG', 'CE', 'LYS', 17.19), ('CG', 'ARG', 'NZ', 'LYS', 15.86)], [('CD', 'ARG', 'CB', 'LYS', 17.7), ('CD', 'ARG', 'CG', 'LYS', 17.81), ('CD', 'ARG', 'CD', 'LYS', 16.52), ('CD', 'ARG', 'CE', 'LYS', 16.41), ('CD', 'ARG', 'NZ', 'LYS', 15.06)], [('NE', 'ARG', 'CB', 'LYS', 16.82), ('NE', 'ARG', 'CG', 'LYS', 16.97), ('NE', 'ARG', 'CD', 'LYS', 15.74), ('NE', 'ARG', 'CE', 'LYS', 15.69), ('NE', 'ARG', 'NZ', 'LYS', 14.4)], [('CZ', 'ARG', 'CB', 'LYS', 15.76), ('CZ', 'ARG', 'CG', 'LYS', 15.85), ('CZ', 'ARG', 'CD', 'LYS', 14.62), ('CZ', 'ARG', 'CE', 'LYS', 14.52), ('CZ', 'ARG', 'NZ', 'LYS', 13.23)], [('NH1', 'ARG', 'CB', 'LYS', 15.38), ('NH1', 'ARG', 'CG', 'LYS', 15.35), ('NH1', 'ARG', 'CD', 'LYS', 14.06), ('NH1', 'ARG', 'CE', 'LYS', 13.83), ('NH1', 'ARG', 'NZ', 'LYS', 12.49)], [('NH2', 'ARG', 'CB', 'LYS', 15.2), ('NH2', 'ARG', 'CG', 'LYS', 15.35), ('NH2', 'ARG', 'CD', 'LYS', 14.21), ('NH2', 'ARG', 'CE', 'LYS', 14.18), ('NH2', 'ARG', 'NZ', 'LYS', 12.97)], [('CB', 'ARG', 'CB', 'LYS', 19.05), ('CB', 'ARG', 'CG', 'LYS', 18.9), ('CB', 'ARG', 'CD', 'LYS', 17.67), ('CB', 'ARG', 'CE', 'LYS', 17.27), ('CB', 'ARG', 'NZ', 'LYS', 15.96)], [('CG', 'ARG', 'CB', 'LYS', 19.61), ('CG', 'ARG', 'CG', 'LYS', 19.46), ('CG', 'ARG', 'CD', 'LYS', 18.3), ('CG', 'ARG', 'CE', 'LYS', 17.9), ('CG', 'ARG', 'NZ', 'LYS', 16.65)], [('CD', 'ARG', 'CB', 'LYS', 18.98), ('CD', 'ARG', 'CG', 'LYS', 18.75), ('CD', 'ARG', 'CD', 'LYS', 17.65), ('CD', 'ARG', 'CE', 'LYS', 17.18), ('CD', 'ARG', 'NZ', 'LYS', 15.98)], [('NE', 'ARG', 'CB', 'LYS', 17.56), ('NE', 'ARG', 'CG', 'LYS', 17.35), ('NE', 'ARG', 'CD', 'LYS', 16.27), ('NE', 'ARG', 'CE', 'LYS', 15.84), ('NE', 'ARG', 'NZ', 'LYS', 14.67)], [('CZ', 'ARG', 'CB', 'LYS', 17.11), ('CZ', 'ARG', 'CG', 'LYS', 17.01), ('CZ', 'ARG', 'CD', 'LYS', 15.99), ('CZ', 'ARG', 'CE', 'LYS', 15.68), ('CZ', 'ARG', 'NZ', 'LYS', 14.56)], [('NH1', 'ARG', 'CB', 'LYS', 17.95), ('NH1', 'ARG', 'CG', 'LYS', 17.95), ('NH1', 'ARG', 'CD', 'LYS', 16.96), ('NH1', 'ARG', 'CE', 'LYS', 16.74), ('NH1', 'ARG', 'NZ', 'LYS', 15.64)], [('NH2', 'ARG', 'CB', 'LYS', 15.83), ('NH2', 'ARG', 'CG', 'LYS', 15.77), ('NH2', 'ARG', 'CD', 'LYS', 14.77), ('NH2', 'ARG', 'CE', 'LYS', 14.52), ('NH2', 'ARG', 'NZ', 'LYS', 13.42)]]}
LYS_MG = { 
	'distances':
		[[11.29], [11.28], [10.18], [10.09], [8.97], [11.89], [11.9], [11.25], [11.22], [10.53]],
	'comparisons':
		[[('CB', 'LYS', 'MG', 'MG', 11.29)], [('CG', 'LYS', 'MG', 'MG', 11.28)], [('CD', 'LYS', 'MG', 'MG', 10.18)], [('CE', 'LYS', 'MG', 'MG', 10.09)], [('NZ', 'LYS', 'MG', 'MG', 8.97)], [('CB', 'LYS', 'MG', 'MG', 11.89)], [('CG', 'LYS', 'MG', 'MG', 11.9)], [('CD', 'LYS', 'MG', 'MG', 11.25)], [('CE', 'LYS', 'MG', 'MG', 11.22)], [('NZ', 'LYS', 'MG', 'MG', 10.53)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_ARG, d, 'M_1gsa_6_3_2_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_MG, d, 'M_1gsa_6_3_2_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(MG_ARGI, d, 'M_1gsa_6_3_2_3')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(MG_MG, d, 'M_1gsa_6_3_2_3')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ARG_LYS, d, 'M_1gsa_6_3_2_3')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(LYS_MG, d, 'M_1gsa_6_3_2_3')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_ARG' :  match1,
		'ARG_MG' :  match2,
		'MG_ARGI' :  match3,
		'MG_MG' :  match4,
		'ARG_LYS' :  match5,
		'LYS_MG' :  match6}