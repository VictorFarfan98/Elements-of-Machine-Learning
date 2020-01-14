def checkTriangle(file):
    """
    Read a file and return 'el camino de adyacentes que suma el total más largo'

    Keyword arguments:
    file -- A string with file
    """
    with open(file) as f:
        lastindex, total = (0, 0)
        for line in f:
            line = line.split()
            try:
                total += int(max(line[lastindex], line[lastindex + 1]))
                if max(line[lastindex], line[lastindex + 1]) == line[lastindex + 1]:
                    lastindex += 1
            except:
                total += int(line[lastindex])

    return total


f = "Tarea 1/triangle.txt"
print(checkTriangle(f))
