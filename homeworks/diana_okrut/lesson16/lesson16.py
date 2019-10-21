def Zip(unzip):
    if unzip == '':
        return ''
    zip = ''
    counta = 0
    countb = 0
    countc = 0
    for i in unzip:
        if i == 'a':
            counta += 1
            zip = 'a' + str(counta)
        elif i == 'b':
            countb += 1
            zip = 'a' + str(counta) + 'b' + str(countb)
        elif i == 'c':
            countc += 1
            zip = 'a' + str(counta) + 'b' + str(countb) + 'c' + str(countc)
    return zip


def Unzip(zip):
    if zip == '':
        return ''
    unzip = ''
    if len(zip) == 2:
        unzip = zip[0] * int(zip[1])
    elif len(zip) == 4:
        unzip = zip[0] * int(zip[1]) + zip[2] * int(zip[3])
    elif len(zip) == 6:
        unzip = zip[0] * int(zip[1]) + zip[2] * int(zip[3]) + zip[4] * int(zip[5])
    else:
        unzip = zip[0] * int(zip[1:3]) + zip[3] * int(zip[4:6]) + zip[6] * int(zip[7])
    return unzip
