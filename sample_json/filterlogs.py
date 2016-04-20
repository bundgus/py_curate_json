
with open('analyticsWeb_SSW2010.2016-04-17-14_WCI_sswhlp1201_inst8-businessRecord.log', 'a') as outputfile:
    with open('analyticsWeb_SSW2010.2016-04-17-14_WCI_sswhlp1203_inst8.log', 'r') as inputfile:
        for line in inputfile:
            if line[:18] == '{"businessRecord":':
                outputfile.write(line)

