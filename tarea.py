import numpy

escritura = open("tabla.txt", "w")


def carga():
    for i in numpy.arange(-100, 101, 0.1):
        y = str(i)
        escritura.write(y)
        x = (15-(5*i)+((3*i)**2))
        x = str(x)
        escritura.write("\t")
        escritura.write(x)
        escritura.write("\n")


carga()


escritura.close()
