import re
import itertools
import pickle

data = open("mesh.msh").read()
start_end_re = re.compile("^gerber2mesh(.*?)\nEnd Data$", re.I|re.M|re.S)
#print type(start_end_re)
matches = start_end_re.findall(data)
#print matches

with open("output.txt","w+") as fp:   # use "w" to overwrite, "a" to append
    for item in matches:
        fp.write(item)
        fp.write("\n")
        fp.write("-"*40)

fp.close()

with open("output.txt") as f:
    with open("output2.txt", "w+") as f2:
        #for line in f:
        for line in itertools.islice(f,3,None):
            f2.write(line)
f.close()
f2.close()



#with open("output.txt") as f:
    #lines_after_4 = f.readlines()[4:]
    #print lines_after_4
#    print type(lines_after_4)
#    with open("output3.txt", "w+") as f3:
        #pickle.dump(lines_after_4, f3)

        
            
            
# with open("output.txt", "w+") as f:
#     for line in itertools.islice(f, 2, None):  # start=17, stop=None
#         f.write(line)
#     for _ in xrange(4):
#         #print _
#         next(fp)
#     for line in fp:
#         fp.write(line)

        
#     lines_after_4 = fp.readlines()[3:]
#     print lines_after_4
#     for item in lines_after_4:
#         fp.write(item)
#         fp.write("\n")
#         fp.write("-"*40)
#fp.close

# with open('output.txt',"w+") as f:
#     lines_after_17 = f.readlines()
#     print lines_after_17
#     for line in lines_after_17:
#         f.write(line)
#         
# with open("output.txt", "w+") as f:
#     for _ in xrange(2):
#         next(f)
#         for line in f:
#             f.write(line)
#             f.write("\n")
#             f.write("-"*40)