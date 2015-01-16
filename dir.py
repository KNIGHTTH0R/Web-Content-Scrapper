folder=['a','b','c','d']
File=range(1,10)
os.mkdir("project/try")
for f in folder:
	os.mkdir("project/try/"+f)
	for fl in File:
		myfile=open("project/try/"+f+"/file"+str(fl)+".txt",'w')
		myfile.write(f+str(fl))
		myfile.close()

