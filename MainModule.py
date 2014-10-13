import re
import itertools
import csv


gerber2meshFile = "mesh.msh"
patternFile= "temp.out"
MaterialFile = "material.txt"
n_LINES = 3
csv_file = r"Material.csv"
#csvfile = "testcsv.out"

def readGerber2MeshFile(gerber2meshFile, patternFile, MaterialFile, n_LINES):
    data = open(gerber2meshFile).read()
    start_end_re = re.compile("^gerber2mesh(.*?)\nEnd Data$", re.I|re.M|re.S)
    matches = start_end_re.findall(data)


    with open(patternFile,"w") as fp:
        for item in matches:
            fp.write(item)
            fp.write("\n")
            fp.write("-"*40)
    fp.close()
    with open(patternFile) as f:
        with open(MaterialFile, "w+") as fm:
            for line in itertools.islice(f, n_LINES, None):
                fm.write(line)
    f.close()
    fm.close()
    return
    
def converTxtIntoCSV(txtFile, outcsvFile):
    
    txtFile = csv.reader(open(txtFile, "rb"), delimiter = '\t')
    outcsvFile = csv.writer(open(outcsvFile, 'wb'))
    outcsvFile.writerows(txtFile)
    return
  
if __name__ == "__main__":
    readGerber2MeshFile(gerber2meshFile, patternFile, MaterialFile, n_LINES)
    converTxtIntoCSV( MaterialFile,csv_file)
    element = '266488'
    with open(csv_file, 'rb') as f:
        reader = csv.reader(f, delimiter ='\n')
        for row in reader:
            #print row
            if element == row[0]:
                print "true"
      
   
    
    