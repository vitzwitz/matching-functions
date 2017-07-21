'''
FUNC:A_1a4s_1_2_1_8
PDB:1a4s
EC:1.2.1.8
RESI:asn,glu,cys
LOCI:a-166,263,297;
'''
import motifConnection as cmd
import time as t
global d

strt = t.time()

A_1a4s_1_2_1_8 = {}
cmd.select(A_1a4s_1_2_1_8, 'cys1', 'n. CB&r. cys w. %s of n. CB&r. glu'%(d*8.79))
cmd.select(A_1a4s_1_2_1_8, 'cys2', 'n. CB&r. cys w. %s of n. CG&r. glu'%(d*9.87))
cmd.select(A_1a4s_1_2_1_8, 'cys3', 'n. CB&r. cys w. %s of n. CD&r. glu'%(d*9.67))
cmd.select(A_1a4s_1_2_1_8, 'cys4', 'n. CB&r. cys w. %s of n. OE1&r. glu'%(d*8.65))
cmd.select(A_1a4s_1_2_1_8, 'cys5', 'n. CB&r. cys w. %s of n. OE2&r. glu'%(d*10.70))
cmd.select(A_1a4s_1_2_1_8, 'cys6', 'n. CB&r. cys w. %s of n. O&r. glu'%(d*8.10))
cmd.select(A_1a4s_1_2_1_8, 'cys7', 'n. CB&r. cys w. %s of n. C&r. glu'%(d*8.26))
cmd.select(A_1a4s_1_2_1_8, 'cys8', 'n. CB&r. cys w. %s of n. CA&r. glu'%(d*9.12))
cmd.select(A_1a4s_1_2_1_8, 'cys9', 'n. CB&r. cys w. %s of n. N&r. glu'%(d*10.47))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'cys10', 'n. SG&r. cys w. %s of n. CB&r. glu'%(d*8.47))
cmd.select(A_1a4s_1_2_1_8,'cys11', 'n. SG&r. cys w. %s of n. CG&r. glu'%(d*9.28))
cmd.select(A_1a4s_1_2_1_8,'cys12', 'n. SG&r. cys w. %s of n. CD&r. glu'%(d*8.88))
cmd.select(A_1a4s_1_2_1_8,'cys13', 'n. SG&r. cys w. %s of n. OE1&r. glu'%(d*7.89))
cmd.select(A_1a4s_1_2_1_8,'cys14', 'n. SG&r. cys w. %s of n. OE2&r. glu'%(d*9.76))
cmd.select(A_1a4s_1_2_1_8,'cys15', 'n. SG&r. cys w. %s of n. O&r. glu'%(d*8.52))
cmd.select(A_1a4s_1_2_1_8,'cys16', 'n. SG&r. cys w. %s of n. C&r. glu'%(d*8.61))
cmd.select(A_1a4s_1_2_1_8,'cys17', 'n. SG&r. cys w. %s of n. CA&r. glu'%(d*9.13))
cmd.select(A_1a4s_1_2_1_8,'cys18', 'n. SG&r. cys w. %s of n. N&r. glu'%(d*10.51))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'cys19', 'n. O&r. cys w. %s of n. CB&r. glu'%(d*11.14))
cmd.select(A_1a4s_1_2_1_8,'cys20', 'n. O&r. cys w. %s of n. CG&r. glu'%(d*12.15))
cmd.select(A_1a4s_1_2_1_8,'cys21', 'n. O&r. cys w. %s of n. CD&r. glu'%(d*11.72))
cmd.select(A_1a4s_1_2_1_8,'cys22', 'n. O&r. cys w. %s of n. OE1&r. glu'%(d*10.52))
cmd.select(A_1a4s_1_2_1_8,'cys23', 'n. O&r. cys w. %s of n. OE2&r. glu'%(d*12.68))
cmd.select(A_1a4s_1_2_1_8,'cys24', 'n. O&r. cys w. %s of n. O&r. glu'%(d*10.37))
cmd.select(A_1a4s_1_2_1_8,'cys25', 'n. O&r. cys w. %s of n. C&r. glu'%(d*10.24))
cmd.select(A_1a4s_1_2_1_8,'cys26', 'n. O&r. cys w. %s of n. CA&r. glu'%(d*11.13))
cmd.select(A_1a4s_1_2_1_8,'cys27', 'n. O&r. cys w. %s of n. N&r. glu'%(d*12.51))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'cys28', 'n. C&r. cys w. %s of n. CB&r. glu'%(d*10.74))
cmd.select(A_1a4s_1_2_1_8,'cys29', 'n. C&r. cys w. %s of n. CG&r. glu'%(d*11.71))
cmd.select(A_1a4s_1_2_1_8,'cys30', 'n. C&r. cys w. %s of n. CD&r. glu'%(d*11.25))
cmd.select(A_1a4s_1_2_1_8,'cys31', 'n. C&r. cys w. %s of n. OE1&r. glu'%(d*10.08))
cmd.select(A_1a4s_1_2_1_8,'cys32', 'n. C&r. cys w. %s of n. OE2&r. glu'%(d*12.18))
cmd.select(A_1a4s_1_2_1_8,'cys33', 'n. C&r. cys w. %s of n. O&r. glu'%(d*10.17))
cmd.select(A_1a4s_1_2_1_8,'cys34', 'n. C&r. cys w. %s of n. C&r. glu'%(d*10.12))
cmd.select(A_1a4s_1_2_1_8,'cys35', 'n. C&r. cys w. %s of n. CA&r. glu'%(d*10.93))
cmd.select(A_1a4s_1_2_1_8,'cys36', 'n. C&r. cys w. %s of n. N&r. glu'%(d*12.33))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'cys37', 'n. CA&r. cys w. %s of n. CB&r. glu'%(d*10.30))
cmd.select(A_1a4s_1_2_1_8,'cys38', 'n. CA&r. cys w. %s of n. CG&r. glu'%(d*11.37))
cmd.select(A_1a4s_1_2_1_8,'cys39', 'n. CA&r. cys w. %s of n. CD&r. glu'%(d*11.11))
cmd.select(A_1a4s_1_2_1_8,'cys40', 'n. CA&r. cys w. %s of n. OE1&r. glu'%(d*10.03))
cmd.select(A_1a4s_1_2_1_8,'cys41', 'n. CA&r. cys w. %s of n. OE2&r. glu'%(d*12.10))
cmd.select(A_1a4s_1_2_1_8,'cys42', 'n. CA&r. cys w. %s of n. O&r. glu'%(d*9.49))
cmd.select(A_1a4s_1_2_1_8,'cys43', 'n. CA&r. cys w. %s of n. C&r. glu'%(d*9.64))
cmd.select(A_1a4s_1_2_1_8,'cys44', 'n. CA&r. cys w. %s of n. CA&r. glu'%(d*10.56))
cmd.select(A_1a4s_1_2_1_8,'cys45', 'n. CA&r. cys w. %s of n. N&r. glu'%(d*11.90))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'cys46', 'n. N&r. cys w. %s of n. CB&r. glu'%(d*11.10))
cmd.select(A_1a4s_1_2_1_8,'cys47', 'n. N&r. cys w. %s of n. CG&r. glu'%(d*12.11))
cmd.select(A_1a4s_1_2_1_8,'cys48', 'n. N&r. cys w. %s of n. CD&r. glu'%(d*11.85))
cmd.select(A_1a4s_1_2_1_8,'cys49', 'n. N&r. cys w. %s of n. OE1&r. glu'%(d*10.84))
cmd.select(A_1a4s_1_2_1_8,'cys50', 'n. N&r. cys w. %s of n. OE2&r. glu'%(d*12.79))
cmd.select(A_1a4s_1_2_1_8,'cys51', 'n. N&r. cys w. %s of n. O&r. glu'%(d*10.39))
cmd.select(A_1a4s_1_2_1_8,'cys52', 'n. N&r. cys w. %s of n. C&r. glu'%(d*10.67))
cmd.select(A_1a4s_1_2_1_8,'cys53', 'n. N&r. cys w. %s of n. CA&r. glu'%(d*11.53))
cmd.select(A_1a4s_1_2_1_8,'cys54', 'n. N&r. cys w. %s of n. N&r. glu'%(d*12.86))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

# cmd.select(A_1a4s_1_2_1_8,'cys50',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18&br. cys19&br. cys20&br. cys21&br. cys22&br. cys23&br. cys24&br. cys25&br. cys26&br. cys27&br. cys28&br. cys29&br. cys30&br. cys31&br. cys32&br. cys33&br. cys34&br. cys35&br. cys36&br. cys37&br. cys38&br. cys39&br. cys40&br. cys41&br. cys42&br. cys43&br. cys44&br. cys45&br. cys46&br. cys47&br. cys48&br. cys49&br. cys50')

cmd.select(A_1a4s_1_2_1_8,'cys55', 'n. CB&r. cys w. %s of n. CB&r. asn'%(d*9.29))
cmd.select(A_1a4s_1_2_1_8,'cys56', 'n. CB&r. cys w. %s of n. CG&r. asn'%(d*8.02))
cmd.select(A_1a4s_1_2_1_8,'cys57', 'n. CB&r. cys w. %s of n. OD1&r. asn'%(d*8.20))
cmd.select(A_1a4s_1_2_1_8,'cys58', 'n. CB&r. cys w. %s of n. ND2&r. asn'%(d*6.93))
cmd.select(A_1a4s_1_2_1_8,'cys59', 'n. CB&r. cys w. %s of n. O&r. asn'%(d*11.33))
cmd.select(A_1a4s_1_2_1_8,'cys60', 'n. CB&r. cys w. %s of n. C&r. asn'%(d*10.89))
cmd.select(A_1a4s_1_2_1_8,'cys61', 'n. CB&r. cys w. %s of n. CA&r. asn'%(d*10.55))
cmd.select(A_1a4s_1_2_1_8,'cys62', 'n. CB&r. cys w. %s of n. N&r. asn'%(d*10.82))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'cys63', 'n. SG&r. cys w. %s of n. CB&r. asn'%(d*9.35))
cmd.select(A_1a4s_1_2_1_8,'cys64', 'n. SG&r. cys w. %s of n. CG&r. asn'%(d*7.99))
cmd.select(A_1a4s_1_2_1_8,'cys65', 'n. SG&r. cys w. %s of n. OD1&r. asn'%(d*8.06))
cmd.select(A_1a4s_1_2_1_8,'cys66', 'n. SG&r. cys w. %s of n. ND2&r. asn'%(d*6.98))
cmd.select(A_1a4s_1_2_1_8,'cys67', 'n. SG&r. cys w. %s of n. O&r. asn'%(d*10.87))
cmd.select(A_1a4s_1_2_1_8,'cys68', 'n. SG&r. cys w. %s of n. C&r. asn'%(d*10.49))
cmd.select(A_1a4s_1_2_1_8,'cys69', 'n. SG&r. cys w. %s of n. CA&r. asn'%(d*10.44))
cmd.select(A_1a4s_1_2_1_8,'cys70', 'n. SG&r. cys w. %s of n. N&r. asn'%(d*10.80))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'cys71', 'n. O&r. cys w. %s of n. CB&r. asn'%(d*11.57))
cmd.select(A_1a4s_1_2_1_8,'cys72', 'n. O&r. cys w. %s of n. CG&r. asn'%(d*10.57))
cmd.select(A_1a4s_1_2_1_8,'cys73', 'n. O&r. cys w. %s of n. OD1&r. asn'%(d*11.04))
cmd.select(A_1a4s_1_2_1_8,'cys74', 'n. O&r. cys w. %s of n. ND2&r. asn'%(d*9.32))
cmd.select(A_1a4s_1_2_1_8,'cys75', 'n. O&r. cys w. %s of n. O&r. asn'%(d*13.61))
cmd.select(A_1a4s_1_2_1_8,'cys76', 'n. O&r. cys w. %s of n. C&r. asn'%(d*13.40))
cmd.select(A_1a4s_1_2_1_8,'cys77', 'n. O&r. cys w. %s of n. CA&r. asn'%(d*12.99))
cmd.select(A_1a4s_1_2_1_8,'cys78', 'n. O&r. cys w. %s of n. N&r. asn'%(d*13.46))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'cys79', 'n. C&r. cys w. %s of n. CB&r. asn'%(d*10.64))
cmd.select(A_1a4s_1_2_1_8,'cys80', 'n. C&r. cys w. %s of n. CG&r. asn'%(d*9.60))
cmd.select(A_1a4s_1_2_1_8,'cys81', 'n. C&r. cys w. %s of n. OD1&r. asn'%(d*10.06))
cmd.select(A_1a4s_1_2_1_8,'cys82', 'n. C&r. cys w. %s of n. ND2&r. asn'%(d*8.33))
cmd.select(A_1a4s_1_2_1_8,'cys83', 'n. C&r. cys w. %s of n. O&r. asn'%(d*12.53))
cmd.select(A_1a4s_1_2_1_8,'cys84', 'n. C&r. cys w. %s of n. C&r. asn'%(d*12.33))
cmd.select(A_1a4s_1_2_1_8,'cys85', 'n. C&r. cys w. %s of n. CA&r. asn'%(d*12.02))
cmd.select(A_1a4s_1_2_1_8,'cys86', 'n. C&r. cys w. %s of n. N&r. asn'%(d*12.54))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'cys87', 'n. CA&r. cys w. %s of n. CB&r. asn'%(d*9.28))
cmd.select(A_1a4s_1_2_1_8,'cys88', 'n. CA&r. cys w. %s of n. CG&r. asn'%(d*8.22))
cmd.select(A_1a4s_1_2_1_8,'cys89', 'n. CA&r. cys w. %s of n. OD1&r. asn'%(d*8.67))
cmd.select(A_1a4s_1_2_1_8,'cys90', 'n. CA&r. cys w. %s of n. ND2&r. asn'%(d*6.98))
cmd.select(A_1a4s_1_2_1_8,'cys91', 'n. CA&r. cys w. %s of n. O&r. asn'%(d*11.35))
cmd.select(A_1a4s_1_2_1_8,'cys92', 'n. CA&r. cys w. %s of n. C&r. asn'%(d*11.07))
cmd.select(A_1a4s_1_2_1_8,'cys93', 'n. CA&r. cys w. %s of n. CA&r. asn'%(d*10.67))
cmd.select(A_1a4s_1_2_1_8,'cys94', 'n. CA&r. cys w. %s of n. N&r. asn'%(d*11.12))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'cys95', 'n. N&r. cys w. %s of n. CB&r. asn'%(d*8.19))
cmd.select(A_1a4s_1_2_1_8,'cys96', 'n. N&r. cys w. %s of n. CG&r. asn'%(d*7.24))
cmd.select(A_1a4s_1_2_1_8,'cys97', 'n. N&r. cys w. %s of n. OD1&r. asn'%(d*7.87))
cmd.select(A_1a4s_1_2_1_8,'cys98', 'n. N&r. cys w. %s of n. ND2&r. asn'%(d*5.94))
cmd.select(A_1a4s_1_2_1_8,'cys99', 'n. N&r. cys w. %s of n. O&r. asn'%(d*10.09))
cmd.select(A_1a4s_1_2_1_8,'cys100', 'n. N&r. cys w. %s of n. C&r. asn'%(d*9.93))
cmd.select(A_1a4s_1_2_1_8,'cys101', 'n. N&r. cys w. %s of n. CA&r. asn'%(d*9.59))
cmd.select(A_1a4s_1_2_1_8,'cys102', 'n. N&r. cys w. %s of n. N&r. asn'%(d*10.22))

# cmd.select(A_1a4s_1_2_1_8,'cys100',' br. cys51&br. cys52&br. cys53&br. cys54&br. cys55&br. cys56&br. cys57&br. cys58&br. cys59&br. cys60&br. cys61&br. cys62&br. cys63&br. cys64&br. cys65&br. cys66&br. cys67&br. cys68&br. cys69&br. cys70&br. cys71&br. cys72&br. cys73&br. cys74&br. cys75&br. cys76&br. cys77&br. cys78&br. cys79&br. cys80&br. cys81&br. cys82&br. cys83&br. cys84&br. cys85&br. cys86&br. cys87&br. cys88&br. cys89&br. cys90&br. cys91&br. cys92&br. cys93&br. cys94&br. cys95&br. cys96&br. cys97&br. cys98&br. cys99&br. cys100')

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

# cmd.select(A_1a4s_1_2_1_8,'cys',' cys50&cys100&br. cys101&br. cys102')
cmd.select(A_1a4s_1_2_1_8,'glu1', 'n. CB&r. glu w. %s of n. CB&cys'%(d*8.79))
cmd.select(A_1a4s_1_2_1_8,'glu2', 'n. CB&r. glu w. %s of n. SG&cys'%(d*8.47))
cmd.select(A_1a4s_1_2_1_8,'glu3', 'n. CB&r. glu w. %s of n. O&cys'%(d*11.14))
cmd.select(A_1a4s_1_2_1_8,'glu4', 'n. CB&r. glu w. %s of n. C&cys'%(d*10.74))
cmd.select(A_1a4s_1_2_1_8,'glu5', 'n. CB&r. glu w. %s of n. CA&cys'%(d*10.30))
cmd.select(A_1a4s_1_2_1_8,'glu6', 'n. CB&r. glu w. %s of n. N&cys'%(d*11.10))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'glu7', 'n. CG&r. glu w. %s of n. CB&cys'%(d*9.87))
cmd.select(A_1a4s_1_2_1_8,'glu8', 'n. CG&r. glu w. %s of n. SG&cys'%(d*9.28))
cmd.select(A_1a4s_1_2_1_8,'glu9', 'n. CG&r. glu w. %s of n. O&cys'%(d*12.15))
cmd.select(A_1a4s_1_2_1_8,'glu10', 'n. CG&r. glu w. %s of n. C&cys'%(d*11.71))
cmd.select(A_1a4s_1_2_1_8,'glu11', 'n. CG&r. glu w. %s of n. CA&cys'%(d*11.37))
cmd.select(A_1a4s_1_2_1_8,'glu12', 'n. CG&r. glu w. %s of n. N&cys'%(d*12.11))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'glu13', 'n. CD&r. glu w. %s of n. CB&cys'%(d*9.67))
cmd.select(A_1a4s_1_2_1_8,'glu14', 'n. CD&r. glu w. %s of n. SG&cys'%(d*8.88))
cmd.select(A_1a4s_1_2_1_8,'glu15', 'n. CD&r. glu w. %s of n. O&cys'%(d*11.72))
cmd.select(A_1a4s_1_2_1_8,'glu16', 'n. CD&r. glu w. %s of n. C&cys'%(d*11.25))
cmd.select(A_1a4s_1_2_1_8,'glu17', 'n. CD&r. glu w. %s of n. CA&cys'%(d*11.11))
cmd.select(A_1a4s_1_2_1_8,'glu18', 'n. CD&r. glu w. %s of n. N&cys'%(d*11.85))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'glu19', 'n. OE1&r. glu w. %s of n. CB&cys'%(d*8.65))
cmd.select(A_1a4s_1_2_1_8,'glu20', 'n. OE1&r. glu w. %s of n. SG&cys'%(d*7.89))
cmd.select(A_1a4s_1_2_1_8,'glu21', 'n. OE1&r. glu w. %s of n. O&cys'%(d*10.52))
cmd.select(A_1a4s_1_2_1_8,'glu22', 'n. OE1&r. glu w. %s of n. C&cys'%(d*10.08))
cmd.select(A_1a4s_1_2_1_8,'glu23', 'n. OE1&r. glu w. %s of n. CA&cys'%(d*10.03))
cmd.select(A_1a4s_1_2_1_8,'glu24', 'n. OE1&r. glu w. %s of n. N&cys'%(d*10.84))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'glu25', 'n. OE2&r. glu w. %s of n. CB&cys'%(d*10.70))
cmd.select(A_1a4s_1_2_1_8,'glu26', 'n. OE2&r. glu w. %s of n. SG&cys'%(d*9.76))
cmd.select(A_1a4s_1_2_1_8,'glu27', 'n. OE2&r. glu w. %s of n. O&cys'%(d*12.68))
cmd.select(A_1a4s_1_2_1_8,'glu28', 'n. OE2&r. glu w. %s of n. C&cys'%(d*12.18))
cmd.select(A_1a4s_1_2_1_8,'glu29', 'n. OE2&r. glu w. %s of n. CA&cys'%(d*12.10))
cmd.select(A_1a4s_1_2_1_8,'glu30', 'n. OE2&r. glu w. %s of n. N&cys'%(d*12.79))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'glu31', 'n. O&r. glu w. %s of n. CB&cys'%(d*8.10))
cmd.select(A_1a4s_1_2_1_8,'glu32', 'n. O&r. glu w. %s of n. SG&cys'%(d*8.52))
cmd.select(A_1a4s_1_2_1_8,'glu33', 'n. O&r. glu w. %s of n. O&cys'%(d*10.37))
cmd.select(A_1a4s_1_2_1_8,'glu34', 'n. O&r. glu w. %s of n. C&cys'%(d*10.17))
cmd.select(A_1a4s_1_2_1_8,'glu35', 'n. O&r. glu w. %s of n. CA&cys'%(d*9.49))
cmd.select(A_1a4s_1_2_1_8,'glu36', 'n. O&r. glu w. %s of n. N&cys'%(d*10.39))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'glu37', 'n. C&r. glu w. %s of n. CB&cys'%(d*8.26))
cmd.select(A_1a4s_1_2_1_8,'glu38', 'n. C&r. glu w. %s of n. SG&cys'%(d*8.61))
cmd.select(A_1a4s_1_2_1_8,'glu39', 'n. C&r. glu w. %s of n. O&cys'%(d*10.24))
cmd.select(A_1a4s_1_2_1_8,'glu40', 'n. C&r. glu w. %s of n. C&cys'%(d*10.12))
cmd.select(A_1a4s_1_2_1_8,'glu41', 'n. C&r. glu w. %s of n. CA&cys'%(d*9.64))
cmd.select(A_1a4s_1_2_1_8,'glu42', 'n. C&r. glu w. %s of n. N&cys'%(d*10.67))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'glu43', 'n. CA&r. glu w. %s of n. CB&cys'%(d*9.12))
cmd.select(A_1a4s_1_2_1_8,'glu44', 'n. CA&r. glu w. %s of n. SG&cys'%(d*9.13))
cmd.select(A_1a4s_1_2_1_8,'glu45', 'n. CA&r. glu w. %s of n. O&cys'%(d*11.13))
cmd.select(A_1a4s_1_2_1_8,'glu46', 'n. CA&r. glu w. %s of n. C&cys'%(d*10.93))
cmd.select(A_1a4s_1_2_1_8,'glu47', 'n. CA&r. glu w. %s of n. CA&cys'%(d*10.56))
cmd.select(A_1a4s_1_2_1_8,'glu48', 'n. CA&r. glu w. %s of n. N&cys'%(d*11.53))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'glu49', 'n. N&r. glu w. %s of n. CB&cys'%(d*10.47))
cmd.select(A_1a4s_1_2_1_8,'glu50', 'n. N&r. glu w. %s of n. SG&cys'%(d*10.51))
cmd.select(A_1a4s_1_2_1_8,'glu51', 'n. N&r. glu w. %s of n. O&cys'%(d*12.51))
cmd.select(A_1a4s_1_2_1_8,'glu52', 'n. N&r. glu w. %s of n. C&cys'%(d*12.33))
cmd.select(A_1a4s_1_2_1_8,'glu53', 'n. N&r. glu w. %s of n. CA&cys'%(d*11.90))
cmd.select(A_1a4s_1_2_1_8,'glu54', 'n. N&r. glu w. %s of n. N&cys'%(d*12.86))
# cmd.select(A_1a4s_1_2_1_8,'glu50',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27&br. glu28&br. glu29&br. glu30&br. glu31&br. glu32&br. glu33&br. glu34&br. glu35&br. glu36&br. glu37&br. glu38&br. glu39&br. glu40&br. glu41&br. glu42&br. glu43&br. glu44&br. glu45&br. glu46&br. glu47&br. glu48&br. glu49&br. glu50')

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'glu55', 'n. CB&r. glu w. %s of n. CB&r. asn'%(d*13.49))
cmd.select(A_1a4s_1_2_1_8,'glu56', 'n. CB&r. glu w. %s of n. CG&r. asn'%(d*12.01))
cmd.select(A_1a4s_1_2_1_8,'glu57', 'n. CB&r. glu w. %s of n. OD1&r. asn'%(d*11.27))
cmd.select(A_1a4s_1_2_1_8,'glu58', 'n. CB&r. glu w. %s of n. ND2&r. asn'%(d*11.70))
cmd.select(A_1a4s_1_2_1_8,'glu59', 'n. CB&r. glu w. %s of n. O&r. asn'%(d*15.05))
cmd.select(A_1a4s_1_2_1_8,'glu60', 'n. CB&r. glu w. %s of n. C&r. asn'%(d*14.17))
cmd.select(A_1a4s_1_2_1_8,'glu61', 'n. CB&r. glu w. %s of n. CA&r. asn'%(d*14.06))
cmd.select(A_1a4s_1_2_1_8,'glu62', 'n. CB&r. glu w. %s of n. N&r. asn'%(d*13.61))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'glu63', 'n. CG&r. glu w. %s of n. CB&r. asn'%(d*14.47))
cmd.select(A_1a4s_1_2_1_8,'glu64', 'n. CG&r. glu w. %s of n. CG&r. asn'%(d*12.97))
cmd.select(A_1a4s_1_2_1_8,'glu65', 'n. CG&r. glu w. %s of n. OD1&r. asn'%(d*12.19))
cmd.select(A_1a4s_1_2_1_8,'glu66', 'n. CG&r. glu w. %s of n. ND2&r. asn'%(d*12.69))
cmd.select(A_1a4s_1_2_1_8,'glu67', 'n. CG&r. glu w. %s of n. O&r. asn'%(d*15.76))
cmd.select(A_1a4s_1_2_1_8,'glu68', 'n. CG&r. glu w. %s of n. C&r. asn'%(d*14.91))
cmd.select(A_1a4s_1_2_1_8,'glu69', 'n. CG&r. glu w. %s of n. CA&r. asn'%(d*14.95))
cmd.select(A_1a4s_1_2_1_8,'glu70', 'n. CG&r. glu w. %s of n. N&r. asn'%(d*14.53))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'glu71', 'n. CD&r. glu w. %s of n. CB&r. asn'%(d*14.74))
cmd.select(A_1a4s_1_2_1_8,'glu72', 'n. CD&r. glu w. %s of n. CG&r. asn'%(d*13.23))
cmd.select(A_1a4s_1_2_1_8,'glu73', 'n. CD&r. glu w. %s of n. OD1&r. asn'%(d*12.55))
cmd.select(A_1a4s_1_2_1_8,'glu74', 'n. CD&r. glu w. %s of n. ND2&r. asn'%(d*12.82))
cmd.select(A_1a4s_1_2_1_8,'glu75', 'n. CD&r. glu w. %s of n. O&r. asn'%(d*15.89))
cmd.select(A_1a4s_1_2_1_8,'glu76', 'n. CD&r. glu w. %s of n. C&r. asn'%(d*15.16))
cmd.select(A_1a4s_1_2_1_8,'glu77', 'n. CD&r. glu w. %s of n. CA&r. asn'%(d*15.29))
cmd.select(A_1a4s_1_2_1_8,'glu78', 'n. CD&r. glu w. %s of n. N&r. asn'%(d*15.03))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'glu79', 'n. OE1&r. glu w. %s of n. CB&r. asn'%(d*14.23))
cmd.select(A_1a4s_1_2_1_8,'glu80', 'n. OE1&r. glu w. %s of n. CG&r. asn'%(d*12.72))
cmd.select(A_1a4s_1_2_1_8,'glu81', 'n. OE1&r. glu w. %s of n. OD1&r. asn'%(d*12.15))
cmd.select(A_1a4s_1_2_1_8,'glu82', 'n. OE1&r. glu w. %s of n. ND2&r. asn'%(d*12.18))
cmd.select(A_1a4s_1_2_1_8,'glu83', 'n. OE1&r. glu w. %s of n. O&r. asn'%(d*15.49))
cmd.select(A_1a4s_1_2_1_8,'glu84', 'n. OE1&r. glu w. %s of n. C&r. asn'%(d*14.81))
cmd.select(A_1a4s_1_2_1_8,'glu85', 'n. OE1&r. glu w. %s of n. CA&r. asn'%(d*14.90))
cmd.select(A_1a4s_1_2_1_8,'glu86', 'n. OE1&r. glu w. %s of n. N&r. asn'%(d*14.74))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'glu87', 'n. OE2&r. glu w. %s of n. CB&r. asn'%(d*15.59))
cmd.select(A_1a4s_1_2_1_8,'glu88', 'n. OE2&r. glu w. %s of n. CG&r. asn'%(d*14.09))
cmd.select(A_1a4s_1_2_1_8,'glu89', 'n. OE2&r. glu w. %s of n. OD1&r. asn'%(d*13.39))
cmd.select(A_1a4s_1_2_1_8,'glu90', 'n. OE2&r. glu w. %s of n. ND2&r. asn'%(d*13.71))
cmd.select(A_1a4s_1_2_1_8,'glu91', 'n. OE2&r. glu w. %s of n. O&r. asn'%(d*16.53))
cmd.select(A_1a4s_1_2_1_8,'glu92', 'n. OE2&r. glu w. %s of n. C&r. asn'%(d*15.83))
cmd.select(A_1a4s_1_2_1_8,'glu93', 'n. OE2&r. glu w. %s of n. CA&r. asn'%(d*16.07))
cmd.select(A_1a4s_1_2_1_8,'glu94', 'n. OE2&r. glu w. %s of n. N&r. asn'%(d*15.84))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'glu95', 'n. O&r. glu w. %s of n. CB&r. asn'%(d*12.55))
cmd.select(A_1a4s_1_2_1_8,'glu96', 'n. O&r. glu w. %s of n. CG&r. asn'%(d*11.17))
cmd.select(A_1a4s_1_2_1_8,'glu97', 'n. O&r. glu w. %s of n. OD1&r. asn'%(d*10.52))
cmd.select(A_1a4s_1_2_1_8,'glu98', 'n. O&r. glu w. %s of n. ND2&r. asn'%(d*10.88))
cmd.select(A_1a4s_1_2_1_8,'glu99', 'n. O&r. glu w. %s of n. O&r. asn'%(d*14.67))
cmd.select(A_1a4s_1_2_1_8,'glu100', 'n. O&r. glu w. %s of n. C&r. asn'%(d*13.71))
cmd.select(A_1a4s_1_2_1_8,'glu101', 'n. O&r. glu w. %s of n. CA&r. asn'%(d*13.25))
cmd.select(A_1a4s_1_2_1_8,'glu102', 'n. O&r. glu w. %s of n. N&r. asn'%(d*12.67))
# cmd.select(A_1a4s_1_2_1_8,'glu100',' br. glu51&br. glu52&br. glu53&br. glu54&br. glu55&br. glu56&br. glu57&br. glu58&br. glu59&br. glu60&br. glu61&br. glu62&br. glu63&br. glu64&br. glu65&br. glu66&br. glu67&br. glu68&br. glu69&br. glu70&br. glu71&br. glu72&br. glu73&br. glu74&br. glu75&br. glu76&br. glu77&br. glu78&br. glu79&br. glu80&br. glu81&br. glu82&br. glu83&br. glu84&br. glu85&br. glu86&br. glu87&br. glu88&br. glu89&br. glu90&br. glu91&br. glu92&br. glu93&br. glu94&br. glu95&br. glu96&br. glu97&br. glu98&br. glu99&br. glu100')

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'glu103', 'n. C&r. glu w. %s of n. CB&r. asn'%(d*13.44))
cmd.select(A_1a4s_1_2_1_8,'glu104', 'n. C&r. glu w. %s of n. CG&r. asn'%(d*12.02))
cmd.select(A_1a4s_1_2_1_8,'glu105', 'n. C&r. glu w. %s of n. OD1&r. asn'%(d*11.42))
cmd.select(A_1a4s_1_2_1_8,'glu106', 'n. C&r. glu w. %s of n. ND2&r. asn'%(d*11.61))
cmd.select(A_1a4s_1_2_1_8,'glu107', 'n. C&r. glu w. %s of n. O&r. asn'%(d*15.49))
cmd.select(A_1a4s_1_2_1_8,'glu108', 'n. C&r. glu w. %s of n. C&r. asn'%(d*14.58))
cmd.select(A_1a4s_1_2_1_8,'glu109', 'n. C&r. glu w. %s of n. CA&r. asn'%(d*14.19))
cmd.select(A_1a4s_1_2_1_8,'glu110', 'n. C&r. glu w. %s of n. N&r. asn'%(d*13.70))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'glu111', 'n. CA&r. glu w. %s of n. CB&r. asn'%(d*14.25))
cmd.select(A_1a4s_1_2_1_8,'glu112', 'n. CA&r. glu w. %s of n. CG&r. asn'%(d*12.79))
cmd.select(A_1a4s_1_2_1_8,'glu113', 'n. CA&r. glu w. %s of n. OD1&r. asn'%(d*12.11))
cmd.select(A_1a4s_1_2_1_8,'glu114', 'n. CA&r. glu w. %s of n. ND2&r. asn'%(d*12.43))
cmd.select(A_1a4s_1_2_1_8,'glu115', 'n. CA&r. glu w. %s of n. O&r. asn'%(d*16.06))
cmd.select(A_1a4s_1_2_1_8,'glu116', 'n. CA&r. glu w. %s of n. C&r. asn'%(d*15.16))
cmd.select(A_1a4s_1_2_1_8,'glu117', 'n. CA&r. glu w. %s of n. CA&r. asn'%(d*14.91))
cmd.select(A_1a4s_1_2_1_8,'glu118', 'n. CA&r. glu w. %s of n. N&r. asn'%(d*14.43))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'glu119', 'n. N&r. glu w. %s of n. CB&r. asn'%(d*15.15))
cmd.select(A_1a4s_1_2_1_8,'glu120', 'n. N&r. glu w. %s of n. CG&r. asn'%(d*13.72))
cmd.select(A_1a4s_1_2_1_8,'glu121', 'n. N&r. glu w. %s of n. OD1&r. asn'%(d*12.96))
cmd.select(A_1a4s_1_2_1_8,'glu122', 'n. N&r. glu w. %s of n. ND2&r. asn'%(d*13.47))
cmd.select(A_1a4s_1_2_1_8,'glu123', 'n. N&r. glu w. %s of n. O&r. asn'%(d*16.96))
cmd.select(A_1a4s_1_2_1_8,'glu124', 'n. N&r. glu w. %s of n. C&r. asn'%(d*15.99))
cmd.select(A_1a4s_1_2_1_8,'glu125', 'n. N&r. glu w. %s of n. CA&r. asn'%(d*15.71))
cmd.select(A_1a4s_1_2_1_8,'glu126', 'n. N&r. glu w. %s of n. N&r. asn'%(d*15.10))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

# cmd.select(A_1a4s_1_2_1_8,'glu',' glu50&glu100&br. glu101&br. glu102&br. glu103&br. glu104&br. glu105&br. glu106&br. glu107&br. glu108&br. glu109&br. glu110&br. glu111&br. glu112&br. glu113&br. glu114&br. glu115&br. glu116&br. glu117&br. glu118&br. glu119&br. glu120&br. glu121&br. glu122&br. glu123&br. glu124&br. glu125&br. glu126')

cmd.select(A_1a4s_1_2_1_8,'asn1', 'n. CB&r. asn w. %s of n. CB&cys'%(d*9.29))
cmd.select(A_1a4s_1_2_1_8,'asn2', 'n. CB&r. asn w. %s of n. SG&cys'%(d*9.35))
cmd.select(A_1a4s_1_2_1_8,'asn3', 'n. CB&r. asn w. %s of n. O&cys'%(d*11.57))
cmd.select(A_1a4s_1_2_1_8,'asn4', 'n. CB&r. asn w. %s of n. C&cys'%(d*10.64))
cmd.select(A_1a4s_1_2_1_8,'asn5', 'n. CB&r. asn w. %s of n. CA&cys'%(d*9.28))
cmd.select(A_1a4s_1_2_1_8,'asn6', 'n. CB&r. asn w. %s of n. N&cys'%(d*8.19))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'asn7', 'n. CG&r. asn w. %s of n. CB&cys'%(d*8.02))
cmd.select(A_1a4s_1_2_1_8,'asn8', 'n. CG&r. asn w. %s of n. SG&cys'%(d*7.99))
cmd.select(A_1a4s_1_2_1_8,'asn9', 'n. CG&r. asn w. %s of n. O&cys'%(d*10.57))
cmd.select(A_1a4s_1_2_1_8,'asn10', 'n. CG&r. asn w. %s of n. C&cys'%(d*9.60))
cmd.select(A_1a4s_1_2_1_8,'asn11', 'n. CG&r. asn w. %s of n. CA&cys'%(d*8.22))
cmd.select(A_1a4s_1_2_1_8,'asn12', 'n. CG&r. asn w. %s of n. N&cys'%(d*7.24))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'asn13', 'n. OD1&r. asn w. %s of n. CB&cys'%(d*8.20))
cmd.select(A_1a4s_1_2_1_8,'asn14', 'n. OD1&r. asn w. %s of n. SG&cys'%(d*8.06))
cmd.select(A_1a4s_1_2_1_8,'asn15', 'n. OD1&r. asn w. %s of n. O&cys'%(d*11.04))
cmd.select(A_1a4s_1_2_1_8,'asn16', 'n. OD1&r. asn w. %s of n. C&cys'%(d*10.06))
cmd.select(A_1a4s_1_2_1_8,'asn17', 'n. OD1&r. asn w. %s of n. CA&cys'%(d*8.67))
cmd.select(A_1a4s_1_2_1_8,'asn18', 'n. OD1&r. asn w. %s of n. N&cys'%(d*7.87))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'asn19', 'n. ND2&r. asn w. %s of n. CB&cys'%(d*6.93))
cmd.select(A_1a4s_1_2_1_8,'asn20', 'n. ND2&r. asn w. %s of n. SG&cys'%(d*6.98))
cmd.select(A_1a4s_1_2_1_8,'asn21', 'n. ND2&r. asn w. %s of n. O&cys'%(d*9.32))
cmd.select(A_1a4s_1_2_1_8,'asn22', 'n. ND2&r. asn w. %s of n. C&cys'%(d*8.33))
cmd.select(A_1a4s_1_2_1_8,'asn23', 'n. ND2&r. asn w. %s of n. CA&cys'%(d*6.98))
cmd.select(A_1a4s_1_2_1_8,'asn24', 'n. ND2&r. asn w. %s of n. N&cys'%(d*5.94))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'asn25', 'n. O&r. asn w. %s of n. CB&cys'%(d*11.33))
cmd.select(A_1a4s_1_2_1_8,'asn26', 'n. O&r. asn w. %s of n. SG&cys'%(d*10.87))
cmd.select(A_1a4s_1_2_1_8,'asn27', 'n. O&r. asn w. %s of n. O&cys'%(d*13.61))
cmd.select(A_1a4s_1_2_1_8,'asn28', 'n. O&r. asn w. %s of n. C&cys'%(d*12.53))
cmd.select(A_1a4s_1_2_1_8,'asn29', 'n. O&r. asn w. %s of n. CA&cys'%(d*11.35))
cmd.select(A_1a4s_1_2_1_8,'asn30', 'n. O&r. asn w. %s of n. N&cys'%(d*10.09))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'asn31', 'n. C&r. asn w. %s of n. CB&cys'%(d*10.89))
cmd.select(A_1a4s_1_2_1_8,'asn32', 'n. C&r. asn w. %s of n. SG&cys'%(d*10.49))
cmd.select(A_1a4s_1_2_1_8,'asn33', 'n. C&r. asn w. %s of n. O&cys'%(d*13.40))
cmd.select(A_1a4s_1_2_1_8,'asn34', 'n. C&r. asn w. %s of n. C&cys'%(d*12.33))
cmd.select(A_1a4s_1_2_1_8,'asn35', 'n. C&r. asn w. %s of n. CA&cys'%(d*11.07))
cmd.select(A_1a4s_1_2_1_8,'asn36', 'n. C&r. asn w. %s of n. N&cys'%(d*9.93))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'asn37', 'n. CA&r. asn w. %s of n. CB&cys'%(d*10.55))
cmd.select(A_1a4s_1_2_1_8,'asn38', 'n. CA&r. asn w. %s of n. SG&cys'%(d*10.44))
cmd.select(A_1a4s_1_2_1_8,'asn39', 'n. CA&r. asn w. %s of n. O&cys'%(d*12.99))
cmd.select(A_1a4s_1_2_1_8,'asn40', 'n. CA&r. asn w. %s of n. C&cys'%(d*12.02))
cmd.select(A_1a4s_1_2_1_8,'asn41', 'n. CA&r. asn w. %s of n. CA&cys'%(d*10.67))
cmd.select(A_1a4s_1_2_1_8,'asn42', 'n. CA&r. asn w. %s of n. N&cys'%(d*9.59))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'asn43', 'n. N&r. asn w. %s of n. CB&cys'%(d*10.82))
cmd.select(A_1a4s_1_2_1_8,'asn44', 'n. N&r. asn w. %s of n. SG&cys'%(d*10.80))
cmd.select(A_1a4s_1_2_1_8,'asn45', 'n. N&r. asn w. %s of n. O&cys'%(d*13.46))
cmd.select(A_1a4s_1_2_1_8,'asn46', 'n. N&r. asn w. %s of n. C&cys'%(d*12.54))
cmd.select(A_1a4s_1_2_1_8,'asn47', 'n. N&r. asn w. %s of n. CA&cys'%(d*11.12))
cmd.select(A_1a4s_1_2_1_8,'asn48', 'n. N&r. asn w. %s of n. N&cys'%(d*10.22))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'asn49', 'n. CB&r. asn w. %s of n. CB&glu'%(d*13.49))
cmd.select(A_1a4s_1_2_1_8,'asn50', 'n. CB&r. asn w. %s of n. CG&glu'%(d*14.47))
cmd.select(A_1a4s_1_2_1_8,'asn51', 'n. CB&r. asn w. %s of n. CD&glu'%(d*14.74))
cmd.select(A_1a4s_1_2_1_8,'asn52', 'n. CB&r. asn w. %s of n. OE1&glu'%(d*14.23))
cmd.select(A_1a4s_1_2_1_8,'asn53', 'n. CB&r. asn w. %s of n. OE2&glu'%(d*15.59))
cmd.select(A_1a4s_1_2_1_8,'asn54', 'n. CB&r. asn w. %s of n. O&glu'%(d*12.55))
cmd.select(A_1a4s_1_2_1_8,'asn55', 'n. CB&r. asn w. %s of n. C&glu'%(d*13.44))
cmd.select(A_1a4s_1_2_1_8,'asn56', 'n. CB&r. asn w. %s of n. CA&glu'%(d*14.25))
cmd.select(A_1a4s_1_2_1_8,'asn57', 'n. CB&r. asn w. %s of n. N&glu'%(d*15.15))

# cmd.select(A_1a4s_1_2_1_8,'asn50',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18&br. asn19&br. asn20&br. asn21&br. asn22&br. asn23&br. asn24&br. asn25&br. asn26&br. asn27&br. asn28&br. asn29&br. asn30&br. asn31&br. asn32&br. asn33&br. asn34&br. asn35&br. asn36&br. asn37&br. asn38&br. asn39&br. asn40&br. asn41&br. asn42&br. asn43&br. asn44&br. asn45&br. asn46&br. asn47&br. asn48&br. asn49&br. asn50')

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'asn58', 'n. CG&r. asn w. %s of n. CB&glu'%(d*12.01))
cmd.select(A_1a4s_1_2_1_8,'asn59', 'n. CG&r. asn w. %s of n. CG&glu'%(d*12.97))
cmd.select(A_1a4s_1_2_1_8,'asn60', 'n. CG&r. asn w. %s of n. CD&glu'%(d*13.23))
cmd.select(A_1a4s_1_2_1_8,'asn61', 'n. CG&r. asn w. %s of n. OE1&glu'%(d*12.72))
cmd.select(A_1a4s_1_2_1_8,'asn62', 'n. CG&r. asn w. %s of n. OE2&glu'%(d*14.09))
cmd.select(A_1a4s_1_2_1_8,'asn63', 'n. CG&r. asn w. %s of n. O&glu'%(d*11.17))
cmd.select(A_1a4s_1_2_1_8,'asn64', 'n. CG&r. asn w. %s of n. C&glu'%(d*12.02))
cmd.select(A_1a4s_1_2_1_8,'asn65', 'n. CG&r. asn w. %s of n. CA&glu'%(d*12.79))
cmd.select(A_1a4s_1_2_1_8,'asn66', 'n. CG&r. asn w. %s of n. N&glu'%(d*13.72))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'asn67', 'n. OD1&r. asn w. %s of n. CB&glu'%(d*11.27))
cmd.select(A_1a4s_1_2_1_8,'asn68', 'n. OD1&r. asn w. %s of n. CG&glu'%(d*12.19))
cmd.select(A_1a4s_1_2_1_8,'asn69', 'n. OD1&r. asn w. %s of n. CD&glu'%(d*12.55))
cmd.select(A_1a4s_1_2_1_8,'asn70', 'n. OD1&r. asn w. %s of n. OE1&glu'%(d*12.15))
cmd.select(A_1a4s_1_2_1_8,'asn71', 'n. OD1&r. asn w. %s of n. OE2&glu'%(d*13.39))
cmd.select(A_1a4s_1_2_1_8,'asn72', 'n. OD1&r. asn w. %s of n. O&glu'%(d*10.52))
cmd.select(A_1a4s_1_2_1_8,'asn73', 'n. OD1&r. asn w. %s of n. C&glu'%(d*11.42))
cmd.select(A_1a4s_1_2_1_8,'asn74', 'n. OD1&r. asn w. %s of n. CA&glu'%(d*12.11))
cmd.select(A_1a4s_1_2_1_8,'asn75', 'n. OD1&r. asn w. %s of n. N&glu'%(d*12.96))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'asn76', 'n. ND2&r. asn w. %s of n. CB&glu'%(d*11.70))
cmd.select(A_1a4s_1_2_1_8,'asn77', 'n. ND2&r. asn w. %s of n. CG&glu'%(d*12.69))
cmd.select(A_1a4s_1_2_1_8,'asn78', 'n. ND2&r. asn w. %s of n. CD&glu'%(d*12.82))
cmd.select(A_1a4s_1_2_1_8,'asn79', 'n. ND2&r. asn w. %s of n. OE1&glu'%(d*12.18))
cmd.select(A_1a4s_1_2_1_8,'asn80', 'n. ND2&r. asn w. %s of n. OE2&glu'%(d*13.71))
cmd.select(A_1a4s_1_2_1_8,'asn81', 'n. ND2&r. asn w. %s of n. O&glu'%(d*10.88))
cmd.select(A_1a4s_1_2_1_8,'asn82', 'n. ND2&r. asn w. %s of n. C&glu'%(d*11.61))
cmd.select(A_1a4s_1_2_1_8,'asn83', 'n. ND2&r. asn w. %s of n. CA&glu'%(d*12.43))
cmd.select(A_1a4s_1_2_1_8,'asn84', 'n. ND2&r. asn w. %s of n. N&glu'%(d*13.47))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'asn85', 'n. O&r. asn w. %s of n. CB&glu'%(d*15.05))
cmd.select(A_1a4s_1_2_1_8,'asn86', 'n. O&r. asn w. %s of n. CG&glu'%(d*15.76))
cmd.select(A_1a4s_1_2_1_8,'asn87', 'n. O&r. asn w. %s of n. CD&glu'%(d*15.89))
cmd.select(A_1a4s_1_2_1_8,'asn88', 'n. O&r. asn w. %s of n. OE1&glu'%(d*15.49))
cmd.select(A_1a4s_1_2_1_8,'asn89', 'n. O&r. asn w. %s of n. OE2&glu'%(d*16.53))
cmd.select(A_1a4s_1_2_1_8,'asn90', 'n. O&r. asn w. %s of n. O&glu'%(d*14.67))
cmd.select(A_1a4s_1_2_1_8,'asn91', 'n. O&r. asn w. %s of n. C&glu'%(d*15.49))
cmd.select(A_1a4s_1_2_1_8,'asn92', 'n. O&r. asn w. %s of n. CA&glu'%(d*16.06))
cmd.select(A_1a4s_1_2_1_8,'asn93', 'n. O&r. asn w. %s of n. N&glu'%(d*16.96))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'asn94', 'n. C&r. asn w. %s of n. CB&glu'%(d*14.17))
cmd.select(A_1a4s_1_2_1_8,'asn95', 'n. C&r. asn w. %s of n. CG&glu'%(d*14.91))
cmd.select(A_1a4s_1_2_1_8,'asn96', 'n. C&r. asn w. %s of n. CD&glu'%(d*15.16))
cmd.select(A_1a4s_1_2_1_8,'asn97', 'n. C&r. asn w. %s of n. OE1&glu'%(d*14.81))
cmd.select(A_1a4s_1_2_1_8,'asn98', 'n. C&r. asn w. %s of n. OE2&glu'%(d*15.83))
cmd.select(A_1a4s_1_2_1_8,'asn99', 'n. C&r. asn w. %s of n. O&glu'%(d*13.71))
cmd.select(A_1a4s_1_2_1_8,'asn100', 'n. C&r. asn w. %s of n. C&glu'%(d*14.58))
cmd.select(A_1a4s_1_2_1_8,'asn101', 'n. C&r. asn w. %s of n. CA&glu'%(d*15.16))
cmd.select(A_1a4s_1_2_1_8,'asn102', 'n. C&r. asn w. %s of n. N&glu'%(d*15.99))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

# cmd.select(A_1a4s_1_2_1_8,'asn100',' br. asn51&br. asn52&br. asn53&br. asn54&br. asn55&br. asn56&br. asn57&br. asn58&br. asn59&br. asn60&br. asn61&br. asn62&br. asn63&br. asn64&br. asn65&br. asn66&br. asn67&br. asn68&br. asn69&br. asn70&br. asn71&br. asn72&br. asn73&br. asn74&br. asn75&br. asn76&br. asn77&br. asn78&br. asn79&br. asn80&br. asn81&br. asn82&br. asn83&br. asn84&br. asn85&br. asn86&br. asn87&br. asn88&br. asn89&br. asn90&br. asn91&br. asn92&br. asn93&br. asn94&br. asn95&br. asn96&br. asn97&br. asn98&br. asn99&br. asn100')


cmd.select(A_1a4s_1_2_1_8,'asn103', 'n. CA&r. asn w. %s of n. CB&glu'%(d*14.06))
cmd.select(A_1a4s_1_2_1_8,'asn104', 'n. CA&r. asn w. %s of n. CG&glu'%(d*14.95))
cmd.select(A_1a4s_1_2_1_8,'asn105', 'n. CA&r. asn w. %s of n. CD&glu'%(d*15.29))
cmd.select(A_1a4s_1_2_1_8,'asn106', 'n. CA&r. asn w. %s of n. OE1&glu'%(d*14.90))
cmd.select(A_1a4s_1_2_1_8,'asn107', 'n. CA&r. asn w. %s of n. OE2&glu'%(d*16.07))
cmd.select(A_1a4s_1_2_1_8,'asn108', 'n. CA&r. asn w. %s of n. O&glu'%(d*13.25))
cmd.select(A_1a4s_1_2_1_8,'asn109', 'n. CA&r. asn w. %s of n. C&glu'%(d*14.19))
cmd.select(A_1a4s_1_2_1_8,'asn110', 'n. CA&r. asn w. %s of n. CA&glu'%(d*14.91))
cmd.select(A_1a4s_1_2_1_8,'asn111', 'n. CA&r. asn w. %s of n. N&glu'%(d*15.71))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

cmd.select(A_1a4s_1_2_1_8,'asn112', 'n. N&r. asn w. %s of n. CB&glu'%(d*13.61))
cmd.select(A_1a4s_1_2_1_8,'asn113', 'n. N&r. asn w. %s of n. CG&glu'%(d*14.53))
cmd.select(A_1a4s_1_2_1_8,'asn114', 'n. N&r. asn w. %s of n. CD&glu'%(d*15.03))
cmd.select(A_1a4s_1_2_1_8,'asn115', 'n. N&r. asn w. %s of n. OE1&glu'%(d*14.74))
cmd.select(A_1a4s_1_2_1_8,'asn116', 'n. N&r. asn w. %s of n. OE2&glu'%(d*15.84))
cmd.select(A_1a4s_1_2_1_8,'asn117', 'n. N&r. asn w. %s of n. O&glu'%(d*12.67))
cmd.select(A_1a4s_1_2_1_8,'asn118', 'n. N&r. asn w. %s of n. C&glu'%(d*13.70))
cmd.select(A_1a4s_1_2_1_8,'asn119', 'n. N&r. asn w. %s of n. CA&glu'%(d*14.43))
cmd.select(A_1a4s_1_2_1_8,'asn120', 'n. N&r. asn w. %s of n. N&glu'%(d*15.10))

cmd.match(A_1a4s_1_2_1_8)
A_1a4s_1_2_1_8 = cmd.delete(A_1a4s_1_2_1_8)

print "We succeeded"

motif = t.time() - strt
print "Time to go thru motif:", motif, "seconds"
# cmd.select(A_1a4s_1_2_1_8,'asn',' asn50&asn100&br. asn101&br. asn102&br. asn103&br. asn104&br. asn105&br. asn106&br. asn107&br. asn108&br. asn109&br. asn110&br. asn111&br. asn112&br. asn113&br. asn114&br. asn115&br. asn116&br. asn117&br. asn118&br. asn119&br. asn120')

# cmd.delete(A_1a4s_1_2_1_8)
# cmd.select(A_1a4s_1_2_1_8,'A_1a4s_1_2_1_8', 'cys|glu|asn')
# cmd.delete(A_1a4s_1_2_1_8),'cys')
# cmd.delete(A_1a4s_1_2_1_8),'glu')
# cmd.delete(A_1a4s_1_2_1_8),'asn')