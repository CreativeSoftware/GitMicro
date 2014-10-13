started = False
collected_lines = []
with open("mesh.msh", "r") as fp:
    for i, line in enumerate(fp.readlines()):
        if line.rstrip() == "gerber2mesh":
            started = True
            print "started at line", i # counts from zero !
            continue
        if started and line.rstrip()=="End Data":
            print "end at line", i
            break
        # process line
        collected_lines.append(line.rstrip())

print len(collected_lines)

for i in collected_lines:
    print collected_lines