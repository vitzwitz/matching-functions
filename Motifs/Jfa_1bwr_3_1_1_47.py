'''
FUNC:Jfa_1bwr_3_1_1_47
PDB:1bwr
EC:3.1.1.47
RESI:ser,gly,asn,asp,his
LOCI:a-47,74,104,192,195;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. ser'
jesstemp2 ='r. thr'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.545300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.545300+(d*0.300000)))
jesstemp6 ='n.  og '
jesstemp7 ='jessatom0 x. %s'%(2.403800+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.434200+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.403800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.434200+(d*0.300000)))
jesstemp10 ='n.  n  '
jesstemp11 ='jessatom0 x. %s'%(5.161100+(d*0.300000))
jesstemp12 ='jessatom1 x. %s'%(4.736900+(d*0.300000))
jesstemp13 ='jessatom2 x. %s'%(5.534800+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.161100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.736900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(5.534800+(d*0.300000)))
jesstemp14 ='jessatom0 x. %s'%(6.565000+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(6.120600+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(6.767000+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(1.484700+(d*0.300000))
jesstemp18 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(6.565000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.120600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.767000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.484700+(d*0.300000)))
jesstemp19 ='n.  c  '
jesstemp20 ='jessatom0 x. %s'%(7.171000+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(7.029600+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(7.706300+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(2.525000+(d*0.300000))
jesstemp24 ='br. jessatom3'
jesstemp25 ='jessatom4 x. %s'%(1.555400+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.171000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.029600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(7.706300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.525000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.555400+(d*0.300000)))
jesstemp26 ='n.  cg '
jesstemp27 ='r. asn'
jesstemp28 ='r. gln'
jesstemp29 ='jessatom0 x. %s'%(7.292200+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(7.049800+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(6.918500+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(4.726800+(d*0.300000))
jesstemp33 ='jessatom4 x. %s'%(4.272300+(d*0.300000))
jesstemp34 ='jessatom5 x. %s'%(4.211700+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp26+')&('+jesstemp27+'))|(('+jesstemp26+')&('+jesstemp28+')))&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(7.292200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(7.049800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(6.918500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(4.726800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(4.272300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(4.211700+(d*0.300000)))
jesstemp35 ='n.  od1'
jesstemp36 ='jessatom0 x. %s'%(7.494200+(d*0.300000))
jesstemp37 ='jessatom1 x. %s'%(7.090200+(d*0.300000))
jesstemp38 ='jessatom2 x. %s'%(6.726600+(d*0.300000))
jesstemp39 ='jessatom3 x. %s'%(5.353000+(d*0.300000))
jesstemp40 ='jessatom4 x. %s'%(4.999500+(d*0.300000))
jesstemp41 ='jessatom5 x. %s'%(5.221700+(d*0.300000))
jesstemp42 ='jessatom6 x. %s'%(1.242300+(d*0.300000))
jesstemp43 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp35+')&('+jesstemp27+'))|(('+jesstemp35+')&('+jesstemp28+')))&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(7.494200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(7.090200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(6.726600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(5.353000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(4.999500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(5.221700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.242300+(d*0.300000)))
jesstemp44 ='n.  nd2'
jesstemp45 ='jessatom0 x. %s'%(6.171100+(d*0.300000))
jesstemp46 ='jessatom1 x. %s'%(5.999400+(d*0.300000))
jesstemp47 ='jessatom2 x. %s'%(6.060000+(d*0.300000))
jesstemp48 ='jessatom3 x. %s'%(3.585500+(d*0.300000))
jesstemp49 ='jessatom4 x. %s'%(3.393600+(d*0.300000))
jesstemp50 ='jessatom5 x. %s'%(3.383500+(d*0.300000))
jesstemp51 ='jessatom6 x. %s'%(1.323100+(d*0.300000))
jesstemp52 ='br. jessatom6'
jesstemp53 ='jessatom7 x. %s'%(2.232100+(d*0.300000))
cmd.select('jessatom8', '(((('+jesstemp44+')&('+jesstemp27+'))|(('+jesstemp44+')&('+jesstemp28+')))&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(6.171100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(5.999400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.060000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(3.585500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(3.393600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(3.383500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.323100+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.232100+(d*0.300000)))
jesstemp54 ='r. asp'
jesstemp55 ='r. glu'
jesstemp56 ='jessatom0 x. %s'%(10.756500+(d*0.300000))
jesstemp57 ='jessatom1 x. %s'%(9.584900+(d*0.300000))
jesstemp58 ='jessatom2 x. %s'%(8.383000+(d*0.300000))
jesstemp59 ='jessatom3 x. %s'%(12.120000+(d*0.300000))
jesstemp60 ='jessatom4 x. %s'%(12.695700+(d*0.300000))
jesstemp61 ='jessatom5 x. %s'%(13.938000+(d*0.300000))
jesstemp62 ='jessatom6 x. %s'%(11.635200+(d*0.300000))
jesstemp63 ='jessatom7 x. %s'%(10.594900+(d*0.300000))
jesstemp64 ='jessatom8 x. %s'%(11.675600+(d*0.300000))
cmd.select('jessatom9', '(((('+jesstemp26+')&('+jesstemp54+'))|(('+jesstemp26+')&('+jesstemp55+')))&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(10.756500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(9.584900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(8.383000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(12.120000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(12.695700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(13.938000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(11.635200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(10.594900+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(11.675600+(d*0.300000)))
jesstemp65 ='n.  od2'
jesstemp66 ='n.  oe1'
jesstemp67 ='n.  oe2'
jesstemp68 ='jessatom0 x. %s'%(10.463600+(d*0.300000))
jesstemp69 ='jessatom1 x. %s'%(9.423300+(d*0.300000))
jesstemp70 ='jessatom2 x. %s'%(8.130500+(d*0.300000))
jesstemp71 ='jessatom3 x. %s'%(12.210900+(d*0.300000))
jesstemp72 ='jessatom4 x. %s'%(12.837100+(d*0.300000))
jesstemp73 ='jessatom5 x. %s'%(14.008700+(d*0.300000))
jesstemp74 ='jessatom6 x. %s'%(11.493800+(d*0.300000))
jesstemp75 ='jessatom7 x. %s'%(10.453500+(d*0.300000))
jesstemp76 ='jessatom8 x. %s'%(11.544300+(d*0.300000))
jesstemp77 ='jessatom9 x. %s'%(1.252400+(d*0.300000))
jesstemp78 ='br. jessatom9'
cmd.select('jessatom10', '((((('+jesstemp35+')|('+jesstemp65+'))&('+jesstemp54+'))|((('+jesstemp66+')|('+jesstemp67+'))&('+jesstemp55+')))&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(10.463600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(9.423300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(8.130500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(12.210900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(12.837100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(14.008700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(11.493800+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(10.453500+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(11.544300+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.252400+(d*0.300000)))
jesstemp79 ='n.  od2'
jesstemp80 ='n.  od1'
jesstemp81 ='n.  oe2'
jesstemp82 ='n.  oe1'
jesstemp83 ='jessatom0 x. %s'%(9.948500+(d*0.300000))
jesstemp84 ='jessatom1 x. %s'%(8.686000+(d*0.300000))
jesstemp85 ='jessatom2 x. %s'%(7.564900+(d*0.300000))
jesstemp86 ='jessatom3 x. %s'%(11.069600+(d*0.300000))
jesstemp87 ='jessatom4 x. %s'%(11.645300+(d*0.300000))
jesstemp88 ='jessatom5 x. %s'%(12.948200+(d*0.300000))
jesstemp89 ='jessatom6 x. %s'%(10.908000+(d*0.300000))
jesstemp90 ='jessatom7 x. %s'%(9.918200+(d*0.300000))
jesstemp91 ='jessatom8 x. %s'%(10.877700+(d*0.300000))
jesstemp92 ='jessatom9 x. %s'%(1.282700+(d*0.300000))
jesstemp93 ='br. jessatom9'
jesstemp94 ='jessatom10 x. %s'%(2.211900+(d*0.300000))
cmd.select('jessatom11', '((((('+jesstemp79+')|('+jesstemp80+'))&('+jesstemp54+'))|((('+jesstemp81+')|('+jesstemp82+'))&('+jesstemp55+')))&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+')&('+jesstemp91+')&('+jesstemp92+')&('+jesstemp93+')&('+jesstemp94+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(9.948500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(8.686000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(7.564900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(11.069600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(11.645300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(12.948200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(10.908000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(9.918200+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(10.877700+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.282700+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.211900+(d*0.300000)))
jesstemp95 ='r. his'
jesstemp96 ='jessatom0 x. %s'%(6.575100+(d*0.300000))
jesstemp97 ='jessatom1 x. %s'%(5.534800+(d*0.300000))
jesstemp98 ='jessatom2 x. %s'%(4.252100+(d*0.300000))
jesstemp99 ='jessatom3 x. %s'%(8.898100+(d*0.300000))
jesstemp100 ='jessatom4 x. %s'%(9.786900+(d*0.300000))
jesstemp101 ='jessatom5 x. %s'%(10.928200+(d*0.300000))
jesstemp102 ='jessatom6 x. %s'%(9.049600+(d*0.300000))
jesstemp103 ='jessatom7 x. %s'%(8.282000+(d*0.300000))
jesstemp104 ='jessatom8 x. %s'%(8.726400+(d*0.300000))
jesstemp105 ='jessatom9 x. %s'%(4.262200+(d*0.300000))
jesstemp106 ='jessatom10 x. %s'%(3.928900+(d*0.300000))
jesstemp107 ='jessatom11 x. %s'%(3.696600+(d*0.300000))
cmd.select('jessatom12', '(('+jesstemp26+')&('+jesstemp95+')&('+jesstemp96+')&('+jesstemp97+')&('+jesstemp98+')&('+jesstemp99+')&('+jesstemp100+')&('+jesstemp101+')&('+jesstemp102+')&('+jesstemp103+')&('+jesstemp104+')&('+jesstemp105+')&('+jesstemp106+')&('+jesstemp107+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom12 x. %s)'%(6.575100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom12 x. %s)'%(5.534800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom12 x. %s)'%(4.252100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom12 x. %s)'%(8.898100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom12 x. %s)'%(9.786900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom12 x. %s)'%(10.928200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom12 x. %s)'%(9.049600+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom12 x. %s)'%(8.282000+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom12 x. %s)'%(8.726400+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom12 x. %s)'%(4.262200+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom12 x. %s)'%(3.928900+(d*0.300000)))
cmd.select('jessatom11', 'jessatom11 & (jessatom12 x. %s)'%(3.696600+(d*0.300000)))
jesstemp108 ='n.  nd1'
jesstemp109 ='jessatom0 x. %s'%(7.413400+(d*0.300000))
jesstemp110 ='jessatom1 x. %s'%(6.201400+(d*0.300000))
jesstemp111 ='jessatom2 x. %s'%(5.019700+(d*0.300000))
jesstemp112 ='jessatom3 x. %s'%(8.918300+(d*0.300000))
jesstemp113 ='jessatom4 x. %s'%(9.645500+(d*0.300000))
jesstemp114 ='jessatom5 x. %s'%(10.877700+(d*0.300000))
jesstemp115 ='jessatom6 x. %s'%(8.938500+(d*0.300000))
jesstemp116 ='jessatom7 x. %s'%(8.080000+(d*0.300000))
jesstemp117 ='jessatom8 x. %s'%(8.746600+(d*0.300000))
jesstemp118 ='jessatom9 x. %s'%(3.403700+(d*0.300000))
jesstemp119 ='jessatom10 x. %s'%(3.413800+(d*0.300000))
jesstemp120 ='jessatom11 x. %s'%(2.585600+(d*0.300000))
jesstemp121 ='jessatom12 x. %s'%(1.434200+(d*0.300000))
jesstemp122 ='br. jessatom12'
cmd.select('jessatom13', '(('+jesstemp108+')&('+jesstemp95+')&('+jesstemp109+')&('+jesstemp110+')&('+jesstemp111+')&('+jesstemp112+')&('+jesstemp113+')&('+jesstemp114+')&('+jesstemp115+')&('+jesstemp116+')&('+jesstemp117+')&('+jesstemp118+')&('+jesstemp119+')&('+jesstemp120+')&('+jesstemp121+')&('+jesstemp122+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom13 x. %s)'%(7.413400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom13 x. %s)'%(6.201400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom13 x. %s)'%(5.019700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom13 x. %s)'%(8.918300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom13 x. %s)'%(9.645500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom13 x. %s)'%(10.877700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom13 x. %s)'%(8.938500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom13 x. %s)'%(8.080000+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom13 x. %s)'%(8.746600+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom13 x. %s)'%(3.403700+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom13 x. %s)'%(3.413800+(d*0.300000)))
cmd.select('jessatom11', 'jessatom11 & (jessatom13 x. %s)'%(2.585600+(d*0.300000)))
cmd.select('jessatom12', 'jessatom12 & (jessatom13 x. %s)'%(1.434200+(d*0.300000)))
jesstemp123 ='n.  ne2'
jesstemp124 ='jessatom0 x. %s'%(5.514600+(d*0.300000))
jesstemp125 ='jessatom1 x. %s'%(4.262200+(d*0.300000))
jesstemp126 ='jessatom2 x. %s'%(3.141100+(d*0.300000))
jesstemp127 ='jessatom3 x. %s'%(6.817500+(d*0.300000))
jesstemp128 ='jessatom4 x. %s'%(7.625500+(d*0.300000))
jesstemp129 ='jessatom5 x. %s'%(8.817300+(d*0.300000))
jesstemp130 ='jessatom6 x. %s'%(7.171000+(d*0.300000))
jesstemp131 ='jessatom7 x. %s'%(6.484200+(d*0.300000))
jesstemp132 ='jessatom8 x. %s'%(6.787200+(d*0.300000))
jesstemp133 ='jessatom9 x. %s'%(5.534800+(d*0.300000))
jesstemp134 ='jessatom10 x. %s'%(5.484300+(d*0.300000))
jesstemp135 ='jessatom11 x. %s'%(4.646000+(d*0.300000))
jesstemp136 ='jessatom12 x. %s'%(2.201800+(d*0.300000))
jesstemp137 ='br. jessatom12'
jesstemp138 ='jessatom13 x. %s'%(2.171500+(d*0.300000))
cmd.select('jessatom14', '(('+jesstemp123+')&('+jesstemp95+')&('+jesstemp124+')&('+jesstemp125+')&('+jesstemp126+')&('+jesstemp127+')&('+jesstemp128+')&('+jesstemp129+')&('+jesstemp130+')&('+jesstemp131+')&('+jesstemp132+')&('+jesstemp133+')&('+jesstemp134+')&('+jesstemp135+')&('+jesstemp136+')&('+jesstemp137+')&('+jesstemp138+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom14 x. %s)'%(5.514600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom14 x. %s)'%(4.262200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom14 x. %s)'%(3.141100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom14 x. %s)'%(6.817500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom14 x. %s)'%(7.625500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom14 x. %s)'%(8.817300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom14 x. %s)'%(7.171000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom14 x. %s)'%(6.484200+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom14 x. %s)'%(6.787200+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom14 x. %s)'%(5.534800+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom14 x. %s)'%(5.484300+(d*0.300000)))
cmd.select('jessatom11', 'jessatom11 & (jessatom14 x. %s)'%(4.646000+(d*0.300000)))
cmd.select('jessatom12', 'jessatom12 & (jessatom14 x. %s)'%(2.201800+(d*0.300000)))
cmd.select('jessatom13', 'jessatom13 & (jessatom14 x. %s)'%(2.171500+(d*0.300000)))
cmd.select('Jfa_1bwr_3_1_1_47', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11|br. jessatom12|br. jessatom13|br. jessatom14')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
cmd.delete('jessatom9')
cmd.delete('jessatom10')
cmd.delete('jessatom11')
cmd.delete('jessatom12')
cmd.delete('jessatom13')
cmd.delete('jessatom14')