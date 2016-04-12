
with open('v12-businessRecord.json', 'w') as outputfile:
    with open('analyticsWeb_SSW2010.2016-04-01-20_V12.log', 'r') as inputfile:
        for line in inputfile:
            if line[:18] == '{"businessRecord":':
                outputfile.write(line)

