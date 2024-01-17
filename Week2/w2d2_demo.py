#W2D2 Text File Opening + 1D Lists

import csv

total_records = 0

#create empty lists for each field
fnames = []
lnames = []
favenums =[]
faveanimals = []
#week2/demo/
with open("w2d2_demoTextFile.txt") as csvfile:
        #we must indent when connected to & reading the file

        file = csv.reader(csvfile)

        for rec in file:

            print(rec)

            #append field data to the appropriate 
            fnames.append(rec[0])
            lnames.append(rec[1])
            favenums.append(int(rec[2]))

            #len() --> returns length of a structure (lists);
            #the maximum length of rec is: 4
            
            if len(rec) == 4:

                faveanimals.append(rec[3])
            else: #rec[3] does not exist 
                 faveanimals.append("---")


        #process fnames + faveanimals list to display
        for index in range(0, len(fnames)):
            print(f"{fnames[index]}'s fave animnal is: {faveanimals [index]}")

