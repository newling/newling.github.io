import commands
import os
import socket

filenames = [
#"posters/2017/nips/clarans/clarans_poster.pdf", 
"slides/2017/nips/clarans/clarans_spotlight.pdf",
#"slides/2017/smld/clarans/newling_smld.pdf",
#"cv_4.pdf"
]

if socket.gethostname() == "goudurix11" or "idbean":
  fetchpaths = {}
  for fn in filenames:
    fetchpaths[fn] = os.path.join("../idiap-ftex", fn)
  fetchpaths["cv_4.pdf"] = "../cv/cv_4.pdf"


else:
  raise RuntimeWarning("Unrecognised hostname : ", socket.gethostname())
  fetchpaths = {}
  for fn in filenames:
    fetchpaths[fn] = "where/should/this/pdf/be/sourced/from/?"
    

for fn in filenames: 
  print "sourcing %s"%(fn,) 
  commands.getstatusoutput("cp %s %s "%(fetchpaths[fn], fn))
