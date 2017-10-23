'''
FUNC:M_1bzy_2_4_2_8
PDB:1bzy
EC:2.4.2.8
RESI:tyr,glu,asp,asp,arg,mg,mg
LOCI:a-104,133,134,137,169,900,901;
'''
import motifFunctions as cmd
ASP_MG = { 
	'distances':
		[[7.72], [6.31], [6.08], [5.77], [10.0], [8.82], [9.21], [7.66], [11.31], [12.29], [13.46], [12.01], [12.05], [12.37], [13.53], [11.59]],
	'comparisons':
		[[('CB', 'ASP', 'MG', 'MG', 7.72)], [('CG', 'ASP', 'MG', 'MG', 6.31)], [('OD1', 'ASP', 'MG', 'MG', 6.08)], [('OD2', 'ASP', 'MG', 'MG', 5.77)], [('CB', 'ASP', 'MG', 'MG', 10.0)], [('CG', 'ASP', 'MG', 'MG', 8.82)], [('OD1', 'ASP', 'MG', 'MG', 9.21)], [('OD2', 'ASP', 'MG', 'MG', 7.66)], [('CB', 'ASP', 'MG', 'MG', 11.31)], [('CG', 'ASP', 'MG', 'MG', 12.29)], [('OD1', 'ASP', 'MG', 'MG', 13.46)], [('OD2', 'ASP', 'MG', 'MG', 12.01)], [('CB', 'ASP', 'MG', 'MG', 12.05)], [('CG', 'ASP', 'MG', 'MG', 12.37)], [('OD1', 'ASP', 'MG', 'MG', 13.53)], [('OD2', 'ASP', 'MG', 'MG', 11.59)]]}
ASP_ASP = { 
	'distances':
		[[11.72, 12.61, 13.78, 12.27], [10.79, 11.73, 12.93, 11.39], [10.06, 11.12, 12.29, 10.94], [11.03, 11.85, 13.08, 11.39], [11.72, 10.79, 10.06, 11.03], [12.61, 11.73, 11.12, 11.85], [13.78, 12.93, 12.29, 13.08], [12.27, 11.39, 10.94, 11.39]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 11.72), ('CB', 'ASP', 'CG', 'ASP', 12.61), ('CB', 'ASP', 'OD1', 'ASP', 13.78), ('CB', 'ASP', 'OD2', 'ASP', 12.27)], [('CG', 'ASP', 'CB', 'ASP', 10.79), ('CG', 'ASP', 'CG', 'ASP', 11.73), ('CG', 'ASP', 'OD1', 'ASP', 12.93), ('CG', 'ASP', 'OD2', 'ASP', 11.39)], [('OD1', 'ASP', 'CB', 'ASP', 10.06), ('OD1', 'ASP', 'CG', 'ASP', 11.12), ('OD1', 'ASP', 'OD1', 'ASP', 12.29), ('OD1', 'ASP', 'OD2', 'ASP', 10.94)], [('OD2', 'ASP', 'CB', 'ASP', 11.03), ('OD2', 'ASP', 'CG', 'ASP', 11.85), ('OD2', 'ASP', 'OD1', 'ASP', 13.08), ('OD2', 'ASP', 'OD2', 'ASP', 11.39)], [('CB', 'ASP', 'CB', 'ASP', 11.72), ('CB', 'ASP', 'CG', 'ASP', 10.79), ('CB', 'ASP', 'OD1', 'ASP', 10.06), ('CB', 'ASP', 'OD2', 'ASP', 11.03)], [('CG', 'ASP', 'CB', 'ASP', 12.61), ('CG', 'ASP', 'CG', 'ASP', 11.73), ('CG', 'ASP', 'OD1', 'ASP', 11.12), ('CG', 'ASP', 'OD2', 'ASP', 11.85)], [('OD1', 'ASP', 'CB', 'ASP', 13.78), ('OD1', 'ASP', 'CG', 'ASP', 12.93), ('OD1', 'ASP', 'OD1', 'ASP', 12.29), ('OD1', 'ASP', 'OD2', 'ASP', 13.08)], [('OD2', 'ASP', 'CB', 'ASP', 12.27), ('OD2', 'ASP', 'CG', 'ASP', 11.39), ('OD2', 'ASP', 'OD1', 'ASP', 10.94), ('OD2', 'ASP', 'OD2', 'ASP', 11.39)]]}
GLU_TYR = { 
	'distances':
		[[15.3, 14.7, 13.8, 15.23, 13.45, 14.92, 14.04, 13.93], [13.92, 13.27, 12.37, 13.76, 11.98, 13.42, 12.54, 12.43], [12.85, 12.33, 11.45, 12.94, 11.23, 12.76, 11.92, 12.0], [12.94, 12.56, 11.8, 13.2, 11.73, 13.14, 12.43, 12.63], [12.06, 11.52, 10.55, 12.21, 10.33, 12.03, 11.12, 11.22]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'TYR', 15.3), ('CB', 'GLU', 'CG', 'TYR', 14.7), ('CB', 'GLU', 'CD1', 'TYR', 13.8), ('CB', 'GLU', 'CD2', 'TYR', 15.23), ('CB', 'GLU', 'CE1', 'TYR', 13.45), ('CB', 'GLU', 'CE2', 'TYR', 14.92), ('CB', 'GLU', 'CZ', 'TYR', 14.04), ('CB', 'GLU', 'OH', 'TYR', 13.93)], [('CG', 'GLU', 'CB', 'TYR', 13.92), ('CG', 'GLU', 'CG', 'TYR', 13.27), ('CG', 'GLU', 'CD1', 'TYR', 12.37), ('CG', 'GLU', 'CD2', 'TYR', 13.76), ('CG', 'GLU', 'CE1', 'TYR', 11.98), ('CG', 'GLU', 'CE2', 'TYR', 13.42), ('CG', 'GLU', 'CZ', 'TYR', 12.54), ('CG', 'GLU', 'OH', 'TYR', 12.43)], [('CD', 'GLU', 'CB', 'TYR', 12.85), ('CD', 'GLU', 'CG', 'TYR', 12.33), ('CD', 'GLU', 'CD1', 'TYR', 11.45), ('CD', 'GLU', 'CD2', 'TYR', 12.94), ('CD', 'GLU', 'CE1', 'TYR', 11.23), ('CD', 'GLU', 'CE2', 'TYR', 12.76), ('CD', 'GLU', 'CZ', 'TYR', 11.92), ('CD', 'GLU', 'OH', 'TYR', 12.0)], [('OE1', 'GLU', 'CB', 'TYR', 12.94), ('OE1', 'GLU', 'CG', 'TYR', 12.56), ('OE1', 'GLU', 'CD1', 'TYR', 11.8), ('OE1', 'GLU', 'CD2', 'TYR', 13.2), ('OE1', 'GLU', 'CE1', 'TYR', 11.73), ('OE1', 'GLU', 'CE2', 'TYR', 13.14), ('OE1', 'GLU', 'CZ', 'TYR', 12.43), ('OE1', 'GLU', 'OH', 'TYR', 12.63)], [('OE2', 'GLU', 'CB', 'TYR', 12.06), ('OE2', 'GLU', 'CG', 'TYR', 11.52), ('OE2', 'GLU', 'CD1', 'TYR', 10.55), ('OE2', 'GLU', 'CD2', 'TYR', 12.21), ('OE2', 'GLU', 'CE1', 'TYR', 10.33), ('OE2', 'GLU', 'CE2', 'TYR', 12.03), ('OE2', 'GLU', 'CZ', 'TYR', 11.12), ('OE2', 'GLU', 'OH', 'TYR', 11.22)]]}
ASP_ARG = { 
	'distances':
		[[18.91, 19.53, 18.94, 17.58, 17.34, 18.39, 16.13], [17.96, 18.6, 17.96, 16.63, 16.48, 17.6, 15.31], [17.2, 17.92, 17.34, 16.05, 15.98, 17.12, 14.85], [18.11, 18.67, 17.92, 16.59, 16.46, 17.59, 15.29], [9.19, 9.9, 9.49, 8.25, 8.29, 9.46, 7.38], [8.48, 8.94, 8.42, 7.07, 6.93, 8.1, 5.93], [7.32, 7.79, 7.41, 6.11, 5.98, 7.11, 5.13], [9.27, 9.51, 8.8, 7.38, 7.09, 8.22, 5.93]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 18.91), ('CB', 'ASP', 'CG', 'ARG', 19.53), ('CB', 'ASP', 'CD', 'ARG', 18.94), ('CB', 'ASP', 'NE', 'ARG', 17.58), ('CB', 'ASP', 'CZ', 'ARG', 17.34), ('CB', 'ASP', 'NH1', 'ARG', 18.39), ('CB', 'ASP', 'NH2', 'ARG', 16.13)], [('CG', 'ASP', 'CB', 'ARG', 17.96), ('CG', 'ASP', 'CG', 'ARG', 18.6), ('CG', 'ASP', 'CD', 'ARG', 17.96), ('CG', 'ASP', 'NE', 'ARG', 16.63), ('CG', 'ASP', 'CZ', 'ARG', 16.48), ('CG', 'ASP', 'NH1', 'ARG', 17.6), ('CG', 'ASP', 'NH2', 'ARG', 15.31)], [('OD1', 'ASP', 'CB', 'ARG', 17.2), ('OD1', 'ASP', 'CG', 'ARG', 17.92), ('OD1', 'ASP', 'CD', 'ARG', 17.34), ('OD1', 'ASP', 'NE', 'ARG', 16.05), ('OD1', 'ASP', 'CZ', 'ARG', 15.98), ('OD1', 'ASP', 'NH1', 'ARG', 17.12), ('OD1', 'ASP', 'NH2', 'ARG', 14.85)], [('OD2', 'ASP', 'CB', 'ARG', 18.11), ('OD2', 'ASP', 'CG', 'ARG', 18.67), ('OD2', 'ASP', 'CD', 'ARG', 17.92), ('OD2', 'ASP', 'NE', 'ARG', 16.59), ('OD2', 'ASP', 'CZ', 'ARG', 16.46), ('OD2', 'ASP', 'NH1', 'ARG', 17.59), ('OD2', 'ASP', 'NH2', 'ARG', 15.29)], [('CB', 'ASP', 'CB', 'ARG', 9.19), ('CB', 'ASP', 'CG', 'ARG', 9.9), ('CB', 'ASP', 'CD', 'ARG', 9.49), ('CB', 'ASP', 'NE', 'ARG', 8.25), ('CB', 'ASP', 'CZ', 'ARG', 8.29), ('CB', 'ASP', 'NH1', 'ARG', 9.46), ('CB', 'ASP', 'NH2', 'ARG', 7.38)], [('CG', 'ASP', 'CB', 'ARG', 8.48), ('CG', 'ASP', 'CG', 'ARG', 8.94), ('CG', 'ASP', 'CD', 'ARG', 8.42), ('CG', 'ASP', 'NE', 'ARG', 7.07), ('CG', 'ASP', 'CZ', 'ARG', 6.93), ('CG', 'ASP', 'NH1', 'ARG', 8.1), ('CG', 'ASP', 'NH2', 'ARG', 5.93)], [('OD1', 'ASP', 'CB', 'ARG', 7.32), ('OD1', 'ASP', 'CG', 'ARG', 7.79), ('OD1', 'ASP', 'CD', 'ARG', 7.41), ('OD1', 'ASP', 'NE', 'ARG', 6.11), ('OD1', 'ASP', 'CZ', 'ARG', 5.98), ('OD1', 'ASP', 'NH1', 'ARG', 7.11), ('OD1', 'ASP', 'NH2', 'ARG', 5.13)], [('OD2', 'ASP', 'CB', 'ARG', 9.27), ('OD2', 'ASP', 'CG', 'ARG', 9.51), ('OD2', 'ASP', 'CD', 'ARG', 8.8), ('OD2', 'ASP', 'NE', 'ARG', 7.38), ('OD2', 'ASP', 'CZ', 'ARG', 7.09), ('OD2', 'ASP', 'NH1', 'ARG', 8.22), ('OD2', 'ASP', 'NH2', 'ARG', 5.93)]]}
TYR_MG = { 
	'distances':
		[[9.24], [9.25], [8.71], [10.15], [9.16], [10.53], [10.06], [10.76], [6.74], [7.4], [7.9], [7.99], [8.86], [8.95], [9.33], [10.46]],
	'comparisons':
		[[('CB', 'TYR', 'MG', 'MG', 9.24)], [('CG', 'TYR', 'MG', 'MG', 9.25)], [('CD1', 'TYR', 'MG', 'MG', 8.71)], [('CD2', 'TYR', 'MG', 'MG', 10.15)], [('CE1', 'TYR', 'MG', 'MG', 9.16)], [('CE2', 'TYR', 'MG', 'MG', 10.53)], [('CZ', 'TYR', 'MG', 'MG', 10.06)], [('OH', 'TYR', 'MG', 'MG', 10.76)], [('CB', 'TYR', 'MG', 'MG', 6.74)], [('CG', 'TYR', 'MG', 'MG', 7.4)], [('CD1', 'TYR', 'MG', 'MG', 7.9)], [('CD2', 'TYR', 'MG', 'MG', 7.99)], [('CE1', 'TYR', 'MG', 'MG', 8.86)], [('CE2', 'TYR', 'MG', 'MG', 8.95)], [('CZ', 'TYR', 'MG', 'MG', 9.33)], [('OH', 'TYR', 'MG', 'MG', 10.46)]]}
ARG_TYR = { 
	'distances':
		[[14.55, 13.14, 12.7, 12.39, 11.47, 11.1, 10.6, 9.42], [14.72, 13.36, 13.1, 12.47, 11.95, 11.23, 10.95, 9.86], [13.46, 12.14, 12.01, 11.2, 10.94, 10.02, 9.88, 8.93], [12.59, 11.23, 11.11, 10.22, 10.01, 8.98, 8.87, 7.86], [12.99, 11.63, 11.62, 10.53, 10.53, 9.27, 9.29, 8.28], [14.17, 12.85, 12.89, 11.7, 11.84, 10.48, 10.58, 9.6], [12.36, 10.99, 11.0, 9.86, 9.92, 8.58, 8.63, 7.62]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'TYR', 14.55), ('CB', 'ARG', 'CG', 'TYR', 13.14), ('CB', 'ARG', 'CD1', 'TYR', 12.7), ('CB', 'ARG', 'CD2', 'TYR', 12.39), ('CB', 'ARG', 'CE1', 'TYR', 11.47), ('CB', 'ARG', 'CE2', 'TYR', 11.1), ('CB', 'ARG', 'CZ', 'TYR', 10.6), ('CB', 'ARG', 'OH', 'TYR', 9.42)], [('CG', 'ARG', 'CB', 'TYR', 14.72), ('CG', 'ARG', 'CG', 'TYR', 13.36), ('CG', 'ARG', 'CD1', 'TYR', 13.1), ('CG', 'ARG', 'CD2', 'TYR', 12.47), ('CG', 'ARG', 'CE1', 'TYR', 11.95), ('CG', 'ARG', 'CE2', 'TYR', 11.23), ('CG', 'ARG', 'CZ', 'TYR', 10.95), ('CG', 'ARG', 'OH', 'TYR', 9.86)], [('CD', 'ARG', 'CB', 'TYR', 13.46), ('CD', 'ARG', 'CG', 'TYR', 12.14), ('CD', 'ARG', 'CD1', 'TYR', 12.01), ('CD', 'ARG', 'CD2', 'TYR', 11.2), ('CD', 'ARG', 'CE1', 'TYR', 10.94), ('CD', 'ARG', 'CE2', 'TYR', 10.02), ('CD', 'ARG', 'CZ', 'TYR', 9.88), ('CD', 'ARG', 'OH', 'TYR', 8.93)], [('NE', 'ARG', 'CB', 'TYR', 12.59), ('NE', 'ARG', 'CG', 'TYR', 11.23), ('NE', 'ARG', 'CD1', 'TYR', 11.11), ('NE', 'ARG', 'CD2', 'TYR', 10.22), ('NE', 'ARG', 'CE1', 'TYR', 10.01), ('NE', 'ARG', 'CE2', 'TYR', 8.98), ('NE', 'ARG', 'CZ', 'TYR', 8.87), ('NE', 'ARG', 'OH', 'TYR', 7.86)], [('CZ', 'ARG', 'CB', 'TYR', 12.99), ('CZ', 'ARG', 'CG', 'TYR', 11.63), ('CZ', 'ARG', 'CD1', 'TYR', 11.62), ('CZ', 'ARG', 'CD2', 'TYR', 10.53), ('CZ', 'ARG', 'CE1', 'TYR', 10.53), ('CZ', 'ARG', 'CE2', 'TYR', 9.27), ('CZ', 'ARG', 'CZ', 'TYR', 9.29), ('CZ', 'ARG', 'OH', 'TYR', 8.28)], [('NH1', 'ARG', 'CB', 'TYR', 14.17), ('NH1', 'ARG', 'CG', 'TYR', 12.85), ('NH1', 'ARG', 'CD1', 'TYR', 12.89), ('NH1', 'ARG', 'CD2', 'TYR', 11.7), ('NH1', 'ARG', 'CE1', 'TYR', 11.84), ('NH1', 'ARG', 'CE2', 'TYR', 10.48), ('NH1', 'ARG', 'CZ', 'TYR', 10.58), ('NH1', 'ARG', 'OH', 'TYR', 9.6)], [('NH2', 'ARG', 'CB', 'TYR', 12.36), ('NH2', 'ARG', 'CG', 'TYR', 10.99), ('NH2', 'ARG', 'CD1', 'TYR', 11.0), ('NH2', 'ARG', 'CD2', 'TYR', 9.86), ('NH2', 'ARG', 'CE1', 'TYR', 9.92), ('NH2', 'ARG', 'CE2', 'TYR', 8.58), ('NH2', 'ARG', 'CZ', 'TYR', 8.63), ('NH2', 'ARG', 'OH', 'TYR', 7.62)]]}
ASP_TYR = { 
	'distances':
		[[13.17, 12.79, 12.45, 13.04, 12.38, 12.97, 12.64, 12.83], [11.76, 11.38, 11.0, 11.72, 10.97, 11.7, 11.33, 11.6], [11.61, 11.11, 10.55, 11.49, 10.4, 11.36, 10.82, 10.99], [10.94, 10.71, 10.46, 11.08, 10.6, 11.22, 10.98, 11.41], [10.56, 9.11, 8.46, 8.62, 7.19, 7.37, 6.53, 5.38], [10.61, 9.14, 8.74, 8.38, 7.5, 7.04, 6.51, 5.32], [11.47, 9.99, 9.59, 9.17, 8.3, 7.79, 7.27, 5.98], [9.99, 8.59, 8.41, 7.69, 7.33, 6.41, 6.2, 5.27]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TYR', 13.17), ('CB', 'ASP', 'CG', 'TYR', 12.79), ('CB', 'ASP', 'CD1', 'TYR', 12.45), ('CB', 'ASP', 'CD2', 'TYR', 13.04), ('CB', 'ASP', 'CE1', 'TYR', 12.38), ('CB', 'ASP', 'CE2', 'TYR', 12.97), ('CB', 'ASP', 'CZ', 'TYR', 12.64), ('CB', 'ASP', 'OH', 'TYR', 12.83)], [('CG', 'ASP', 'CB', 'TYR', 11.76), ('CG', 'ASP', 'CG', 'TYR', 11.38), ('CG', 'ASP', 'CD1', 'TYR', 11.0), ('CG', 'ASP', 'CD2', 'TYR', 11.72), ('CG', 'ASP', 'CE1', 'TYR', 10.97), ('CG', 'ASP', 'CE2', 'TYR', 11.7), ('CG', 'ASP', 'CZ', 'TYR', 11.33), ('CG', 'ASP', 'OH', 'TYR', 11.6)], [('OD1', 'ASP', 'CB', 'TYR', 11.61), ('OD1', 'ASP', 'CG', 'TYR', 11.11), ('OD1', 'ASP', 'CD1', 'TYR', 10.55), ('OD1', 'ASP', 'CD2', 'TYR', 11.49), ('OD1', 'ASP', 'CE1', 'TYR', 10.4), ('OD1', 'ASP', 'CE2', 'TYR', 11.36), ('OD1', 'ASP', 'CZ', 'TYR', 10.82), ('OD1', 'ASP', 'OH', 'TYR', 10.99)], [('OD2', 'ASP', 'CB', 'TYR', 10.94), ('OD2', 'ASP', 'CG', 'TYR', 10.71), ('OD2', 'ASP', 'CD1', 'TYR', 10.46), ('OD2', 'ASP', 'CD2', 'TYR', 11.08), ('OD2', 'ASP', 'CE1', 'TYR', 10.6), ('OD2', 'ASP', 'CE2', 'TYR', 11.22), ('OD2', 'ASP', 'CZ', 'TYR', 10.98), ('OD2', 'ASP', 'OH', 'TYR', 11.41)], [('CB', 'ASP', 'CB', 'TYR', 10.56), ('CB', 'ASP', 'CG', 'TYR', 9.11), ('CB', 'ASP', 'CD1', 'TYR', 8.46), ('CB', 'ASP', 'CD2', 'TYR', 8.62), ('CB', 'ASP', 'CE1', 'TYR', 7.19), ('CB', 'ASP', 'CE2', 'TYR', 7.37), ('CB', 'ASP', 'CZ', 'TYR', 6.53), ('CB', 'ASP', 'OH', 'TYR', 5.38)], [('CG', 'ASP', 'CB', 'TYR', 10.61), ('CG', 'ASP', 'CG', 'TYR', 9.14), ('CG', 'ASP', 'CD1', 'TYR', 8.74), ('CG', 'ASP', 'CD2', 'TYR', 8.38), ('CG', 'ASP', 'CE1', 'TYR', 7.5), ('CG', 'ASP', 'CE2', 'TYR', 7.04), ('CG', 'ASP', 'CZ', 'TYR', 6.51), ('CG', 'ASP', 'OH', 'TYR', 5.32)], [('OD1', 'ASP', 'CB', 'TYR', 11.47), ('OD1', 'ASP', 'CG', 'TYR', 9.99), ('OD1', 'ASP', 'CD1', 'TYR', 9.59), ('OD1', 'ASP', 'CD2', 'TYR', 9.17), ('OD1', 'ASP', 'CE1', 'TYR', 8.3), ('OD1', 'ASP', 'CE2', 'TYR', 7.79), ('OD1', 'ASP', 'CZ', 'TYR', 7.27), ('OD1', 'ASP', 'OH', 'TYR', 5.98)], [('OD2', 'ASP', 'CB', 'TYR', 9.99), ('OD2', 'ASP', 'CG', 'TYR', 8.59), ('OD2', 'ASP', 'CD1', 'TYR', 8.41), ('OD2', 'ASP', 'CD2', 'TYR', 7.69), ('OD2', 'ASP', 'CE1', 'TYR', 7.33), ('OD2', 'ASP', 'CE2', 'TYR', 6.41), ('OD2', 'ASP', 'CZ', 'TYR', 6.2), ('OD2', 'ASP', 'OH', 'TYR', 5.27)]]}
MG_ASPI = { 
	'distances':
		[11.31, 12.29, 13.46, 12.01, 12.05, 12.37, 13.53, 11.59],
	'comparisons':
		[('MG', 'MG', 'CB', 'ASPI', 11.31), ('MG', 'MG', 'CG', 'ASPI', 12.29), ('MG', 'MG', 'OD1', 'ASPI', 13.46), ('MG', 'MG', 'OD2', 'ASPI', 12.01), ('MG', 'MG', 'CB', 'ASPI', 12.05), ('MG', 'MG', 'CG', 'ASPI', 12.37), ('MG', 'MG', 'OD1', 'ASPI', 13.53), ('MG', 'MG', 'OD2', 'ASPI', 11.59)]}
GLU_ARG = { 
	'distances':
		[[18.96, 19.99, 19.73, 18.58, 18.64, 19.76, 17.65], [17.63, 18.62, 18.31, 17.16, 17.22, 18.36, 16.22], [17.74, 18.68, 18.25, 17.1, 17.23, 18.42, 16.24], [18.67, 19.55, 19.05, 17.86, 17.94, 19.14, 16.91], [17.0, 17.97, 17.52, 16.43, 16.65, 17.88, 15.72]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 18.96), ('CB', 'GLU', 'CG', 'ARG', 19.99), ('CB', 'GLU', 'CD', 'ARG', 19.73), ('CB', 'GLU', 'NE', 'ARG', 18.58), ('CB', 'GLU', 'CZ', 'ARG', 18.64), ('CB', 'GLU', 'NH1', 'ARG', 19.76), ('CB', 'GLU', 'NH2', 'ARG', 17.65)], [('CG', 'GLU', 'CB', 'ARG', 17.63), ('CG', 'GLU', 'CG', 'ARG', 18.62), ('CG', 'GLU', 'CD', 'ARG', 18.31), ('CG', 'GLU', 'NE', 'ARG', 17.16), ('CG', 'GLU', 'CZ', 'ARG', 17.22), ('CG', 'GLU', 'NH1', 'ARG', 18.36), ('CG', 'GLU', 'NH2', 'ARG', 16.22)], [('CD', 'GLU', 'CB', 'ARG', 17.74), ('CD', 'GLU', 'CG', 'ARG', 18.68), ('CD', 'GLU', 'CD', 'ARG', 18.25), ('CD', 'GLU', 'NE', 'ARG', 17.1), ('CD', 'GLU', 'CZ', 'ARG', 17.23), ('CD', 'GLU', 'NH1', 'ARG', 18.42), ('CD', 'GLU', 'NH2', 'ARG', 16.24)], [('OE1', 'GLU', 'CB', 'ARG', 18.67), ('OE1', 'GLU', 'CG', 'ARG', 19.55), ('OE1', 'GLU', 'CD', 'ARG', 19.05), ('OE1', 'GLU', 'NE', 'ARG', 17.86), ('OE1', 'GLU', 'CZ', 'ARG', 17.94), ('OE1', 'GLU', 'NH1', 'ARG', 19.14), ('OE1', 'GLU', 'NH2', 'ARG', 16.91)], [('OE2', 'GLU', 'CB', 'ARG', 17.0), ('OE2', 'GLU', 'CG', 'ARG', 17.97), ('OE2', 'GLU', 'CD', 'ARG', 17.52), ('OE2', 'GLU', 'NE', 'ARG', 16.43), ('OE2', 'GLU', 'CZ', 'ARG', 16.65), ('OE2', 'GLU', 'NH1', 'ARG', 17.88), ('OE2', 'GLU', 'NH2', 'ARG', 15.72)]]}
GLU_MG = { 
	'distances':
		[[9.01], [8.01], [6.58], [6.2], [6.18], [13.39], [12.24], [11.04], [10.61], [10.72]],
	'comparisons':
		[[('CB', 'GLU', 'MG', 'MG', 9.01)], [('CG', 'GLU', 'MG', 'MG', 8.01)], [('CD', 'GLU', 'MG', 'MG', 6.58)], [('OE1', 'GLU', 'MG', 'MG', 6.2)], [('OE2', 'GLU', 'MG', 'MG', 6.18)], [('CB', 'GLU', 'MG', 'MG', 13.39)], [('CG', 'GLU', 'MG', 'MG', 12.24)], [('CD', 'GLU', 'MG', 'MG', 11.04)], [('OE1', 'GLU', 'MG', 'MG', 10.61)], [('OE2', 'GLU', 'MG', 'MG', 10.72)]]}
ARG_MG = { 
	'distances':
		[[17.8], [18.48], [17.67], [16.53], [16.74], [18.0], [15.78], [17.83], [18.07], [16.92], [15.77], [15.84], [16.98], [14.86]],
	'comparisons':
		[[('CB', 'ARG', 'MG', 'MG', 17.8)], [('CG', 'ARG', 'MG', 'MG', 18.48)], [('CD', 'ARG', 'MG', 'MG', 17.67)], [('NE', 'ARG', 'MG', 'MG', 16.53)], [('CZ', 'ARG', 'MG', 'MG', 16.74)], [('NH1', 'ARG', 'MG', 'MG', 18.0)], [('NH2', 'ARG', 'MG', 'MG', 15.78)], [('CB', 'ARG', 'MG', 'MG', 17.83)], [('CG', 'ARG', 'MG', 'MG', 18.07)], [('CD', 'ARG', 'MG', 'MG', 16.92)], [('NE', 'ARG', 'MG', 'MG', 15.77)], [('CZ', 'ARG', 'MG', 'MG', 15.84)], [('NH1', 'ARG', 'MG', 'MG', 16.98)], [('NH2', 'ARG', 'MG', 'MG', 14.86)]]}
GLU_ASP = { 
	'distances':
		[[7.5, 7.44, 6.62, 8.51], [6.89, 6.52, 5.49, 7.56], [6.69, 5.95, 4.93, 6.76], [6.02, 5.38, 4.68, 6.11], [7.58, 6.58, 5.47, 7.19], [12.36, 13.74, 14.68, 13.99], [10.94, 12.31, 13.27, 12.53], [11.0, 12.33, 13.37, 12.46], [11.79, 13.05, 14.14, 13.05], [10.46, 11.83, 12.84, 12.01]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 7.5), ('CB', 'GLU', 'CG', 'ASP', 7.44), ('CB', 'GLU', 'OD1', 'ASP', 6.62), ('CB', 'GLU', 'OD2', 'ASP', 8.51)], [('CG', 'GLU', 'CB', 'ASP', 6.89), ('CG', 'GLU', 'CG', 'ASP', 6.52), ('CG', 'GLU', 'OD1', 'ASP', 5.49), ('CG', 'GLU', 'OD2', 'ASP', 7.56)], [('CD', 'GLU', 'CB', 'ASP', 6.69), ('CD', 'GLU', 'CG', 'ASP', 5.95), ('CD', 'GLU', 'OD1', 'ASP', 4.93), ('CD', 'GLU', 'OD2', 'ASP', 6.76)], [('OE1', 'GLU', 'CB', 'ASP', 6.02), ('OE1', 'GLU', 'CG', 'ASP', 5.38), ('OE1', 'GLU', 'OD1', 'ASP', 4.68), ('OE1', 'GLU', 'OD2', 'ASP', 6.11)], [('OE2', 'GLU', 'CB', 'ASP', 7.58), ('OE2', 'GLU', 'CG', 'ASP', 6.58), ('OE2', 'GLU', 'OD1', 'ASP', 5.47), ('OE2', 'GLU', 'OD2', 'ASP', 7.19)], [('CB', 'GLU', 'CB', 'ASP', 12.36), ('CB', 'GLU', 'CG', 'ASP', 13.74), ('CB', 'GLU', 'OD1', 'ASP', 14.68), ('CB', 'GLU', 'OD2', 'ASP', 13.99)], [('CG', 'GLU', 'CB', 'ASP', 10.94), ('CG', 'GLU', 'CG', 'ASP', 12.31), ('CG', 'GLU', 'OD1', 'ASP', 13.27), ('CG', 'GLU', 'OD2', 'ASP', 12.53)], [('CD', 'GLU', 'CB', 'ASP', 11.0), ('CD', 'GLU', 'CG', 'ASP', 12.33), ('CD', 'GLU', 'OD1', 'ASP', 13.37), ('CD', 'GLU', 'OD2', 'ASP', 12.46)], [('OE1', 'GLU', 'CB', 'ASP', 11.79), ('OE1', 'GLU', 'CG', 'ASP', 13.05), ('OE1', 'GLU', 'OD1', 'ASP', 14.14), ('OE1', 'GLU', 'OD2', 'ASP', 13.05)], [('OE2', 'GLU', 'CB', 'ASP', 10.46), ('OE2', 'GLU', 'CG', 'ASP', 11.83), ('OE2', 'GLU', 'OD1', 'ASP', 12.84), ('OE2', 'GLU', 'OD2', 'ASP', 12.01)]]}
MG_MG = { 
	'distances':
		[6.9, 6.9],
	'comparisons':
		[('MG', 'MG', 'MG', 'MG', 6.9), ('MG', 'MG', 'MG', 'MG', 6.9)]}
TYR_ASPI = { 
	'distances':
		[[10.56, 10.61, 11.47, 9.99], [9.11, 9.14, 9.99, 8.59], [8.46, 8.74, 9.59, 8.41], [8.62, 8.38, 9.17, 7.69], [7.19, 7.5, 8.3, 7.33], [7.37, 7.04, 7.79, 6.41], [6.53, 6.51, 7.27, 6.2], [5.38, 5.32, 5.98, 5.27]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASPI', 10.56), ('CB', 'TYR', 'CG', 'ASPI', 10.61), ('CB', 'TYR', 'OD1', 'ASPI', 11.47), ('CB', 'TYR', 'OD2', 'ASPI', 9.99)], [('CG', 'TYR', 'CB', 'ASPI', 9.11), ('CG', 'TYR', 'CG', 'ASPI', 9.14), ('CG', 'TYR', 'OD1', 'ASPI', 9.99), ('CG', 'TYR', 'OD2', 'ASPI', 8.59)], [('CD1', 'TYR', 'CB', 'ASPI', 8.46), ('CD1', 'TYR', 'CG', 'ASPI', 8.74), ('CD1', 'TYR', 'OD1', 'ASPI', 9.59), ('CD1', 'TYR', 'OD2', 'ASPI', 8.41)], [('CD2', 'TYR', 'CB', 'ASPI', 8.62), ('CD2', 'TYR', 'CG', 'ASPI', 8.38), ('CD2', 'TYR', 'OD1', 'ASPI', 9.17), ('CD2', 'TYR', 'OD2', 'ASPI', 7.69)], [('CE1', 'TYR', 'CB', 'ASPI', 7.19), ('CE1', 'TYR', 'CG', 'ASPI', 7.5), ('CE1', 'TYR', 'OD1', 'ASPI', 8.3), ('CE1', 'TYR', 'OD2', 'ASPI', 7.33)], [('CE2', 'TYR', 'CB', 'ASPI', 7.37), ('CE2', 'TYR', 'CG', 'ASPI', 7.04), ('CE2', 'TYR', 'OD1', 'ASPI', 7.79), ('CE2', 'TYR', 'OD2', 'ASPI', 6.41)], [('CZ', 'TYR', 'CB', 'ASPI', 6.53), ('CZ', 'TYR', 'CG', 'ASPI', 6.51), ('CZ', 'TYR', 'OD1', 'ASPI', 7.27), ('CZ', 'TYR', 'OD2', 'ASPI', 6.2)], [('OH', 'TYR', 'CB', 'ASPI', 5.38), ('OH', 'TYR', 'CG', 'ASPI', 5.32), ('OH', 'TYR', 'OD1', 'ASPI', 5.98), ('OH', 'TYR', 'OD2', 'ASPI', 5.27)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_MG, d, 'M_1bzy_2_4_2_8')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ASP, d, 'M_1bzy_2_4_2_8')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_TYR, d, 'M_1bzy_2_4_2_8')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_ARG, d, 'M_1bzy_2_4_2_8')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TYR_MG, d, 'M_1bzy_2_4_2_8')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ARG_TYR, d, 'M_1bzy_2_4_2_8')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ASP_TYR, d, 'M_1bzy_2_4_2_8')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(MG_ASPI, d, 'M_1bzy_2_4_2_8')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(GLU_ARG, d, 'M_1bzy_2_4_2_8')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(GLU_MG, d, 'M_1bzy_2_4_2_8')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(ARG_MG, d, 'M_1bzy_2_4_2_8')
	if match11 == []:
		 flag = True
		 break
	match12 , totTime12 = cmd.detect(GLU_ASP, d, 'M_1bzy_2_4_2_8')
	if match12 == []:
		 flag = True
		 break
	match13 , totTime13 = cmd.detect(MG_MG, d, 'M_1bzy_2_4_2_8')
	if match13 == []:
		 flag = True
		 break
	match14 , totTime14 = cmd.detect(TYR_ASPI, d, 'M_1bzy_2_4_2_8')
	if match14 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_MG' :  match1,
		'ASP_ASP' :  match2,
		'GLU_TYR' :  match3,
		'ASP_ARG' :  match4,
		'TYR_MG' :  match5,
		'ARG_TYR' :  match6,
		'ASP_TYR' :  match7,
		'MG_ASPI' :  match8,
		'GLU_ARG' :  match9,
		'GLU_MG' :  match10,
		'ARG_MG' :  match11,
		'GLU_ASP' :  match12,
		'MG_MG' :  match13,
		'TYR_ASPI' :  match14}