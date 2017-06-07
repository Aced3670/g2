n="ATGATCAGTATGGCAATC"
for i in range(0,16):
 if  i%3==0:
  if n[i]=="T":
   if n[i+1]=="T":
    if n[i+2]=="T" or "C":
     print "Phe"
    else:
     print "Leu"
   elif n[i+1]=="C":
    print "Ser"
   elif n[i+1]=="A":
    if n[i+2]=="T" or "C":
     print "Tyr"
    else:
     print "STOP"
   else:
    if n[i+2]=="C" or "T":
     print "Cys"
    elif n[i+2]=="G":
     print "Trp"
    else:
     print "STOP"
  elif n[i]=="C":
   if n[i+1]=="T":
    print "Leu"
   elif n[i+1]=="C":
    print "Pro"
   elif n[i+1]=="A":
    if n[i+2]=="T" or "C":
     print "His" 
    else:
     print "Gln"
   elif n[i+1]=="G":
    print "Arg"
  elif n[i]=="A":
   if n[i+1]=="T":
    if n[i+2]=="M":
     print "Met"
    else:
     print "Ile"
   elif n[i+1]=="C":
    print "Thr"
   elif n[i+1]=="A":
    if n[i+2]=="A" or "G":
     print "Asn"
    else:
     print "Lys"
   else:
    if n[i+2]=="T" or "C":
     print "Ser"
    else:
     print "Arg"
  else:
   if n[i+1]=="T":
    print "Val"
   elif n[i+1]=="A":
    print "Ala"
   elif n[i+1]=="A":
    if n[i+2]=="T" or "C":
     print "Asp"
    else:
     print "Glu"
   else:
    print "Gly"
