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
