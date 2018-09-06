from sage.all import *

size = 80

gen = graphs.fullerenes(size)
l = list(gen)
adr = "/Users/s3000/fullerene/" + str(size) + ".txt"
file = open(adr, "w")
data = str(l[0].adjacency_matrix())
data = data.replace("[","")
data = data.replace("]","")
file.write(data)
file.close()
del gen
del l
del data

#g = graphs.BuckyBall()
#l[0].plot(vertex_labels=False, vertex_size=10).show()