def test_length(filename):
    fileH = open(filename,'r')
    lines = fileH.readlines()
    fileH.close()
    length = len(lines)
    # print(length)
    if (len(lines) == 122):
        result = True
    else:
        result = False
    return result

def test_fields(filename):
    fileH = open(filename,'r')
    lines = fileH.readlines()
    fileH.close()
    result = True
    for line in lines:
        fields = line.split(' ')
        if (len(fields) != 10):
            result = False
            print(line)
    return result
    
file = 'BSIMM12-vert.txt'
print(f'length_ok: {test_length(file)}')
print(f'fields_ok: {test_fields(file)}')
