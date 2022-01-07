# importing the pandas library
import pandas as pd

# reading the csv file
df = pd.read_csv("employeedata_csv.csv")
df = pd.read_excel('employeedata_xlsx.xlsx')

# updating the column value/data
df.loc[0, 'Email Address'] = 'william.smith@handsinhands.org'
df.loc[1, 'Email Address'] = 'rezza.fred@handsinhands.org'
df.loc[2, 'Email Address'] = 'mohan.kumar@handsinhands.org'
df.loc[3, 'Email Address'] = 'cindy.mac@handsinhands.org'
df.loc[4, 'Email Address'] = 'vince.jose@handsinhands.org'
df.loc[5, 'Email Address'] = 'rajiv.lamar@handsinhands.org'
df.loc[6, 'Email Address'] = 'john.thomas@handsinhands.org'
df.loc[7, 'Email Address'] = 'chin.yeu@handsinhands.org'
df.loc[8, 'Email Address'] = 'oshane.mathew@handsinhands.org'
df.loc[9, 'Email Address'] = 'linda.greedman@handsinhands.org'
df.loc[10, 'Email Address'] = 'peter.theil@handsinhands.org'
df.loc[11, 'Email Address'] = 'marissa.mayer@handsinhands.org'
df.loc[12, 'Email Address'] = 'mark.zuckerberg@handsinhands.org'
df.loc[13, 'Email Address'] = 'elon.musk@handsinhands.org'
df.loc[14, 'Email Address'] = 'jack.dorsey@handsinhands.org'
df.loc[15, 'Email Address'] = 'tim.cook@handsinhands.org'
df.loc[16, 'Email Address'] = 'jeff.kissok@handsinhands.org'
df.loc[17, 'Email Address'] = 'eric.djou@handsinhands.org'
df.loc[18, 'Email Address'] = 'larry.page@handsinhands.org'
df.loc[19, 'Email Address'] = 'boris.anaba@handsinhands.org'
df.loc[20, 'Email Address'] = 'abigael.armstrong@handsinhands.org'
df.loc[21, 'Email Address'] = 'benjamin.burton@handsinhands.org'
df.loc[22, 'Email Address'] = 'charles.chapman@handsinhands.org'
df.loc[23, 'Email Address'] = 'danica.donaldson@handsinhands.org'
df.loc[24, 'Email Address'] = 'ellen.eisentein@handsinhands.org'
df.loc[25, 'Email Address'] = 'frederick.fergeson@handsinhands.org'
df.loc[26, 'Email Address'] = 'gabrielle.grimaldi@handsinhands.org'
df.loc[27, 'Email Address'] = 'henry.henderson@handsinhands.org'
df.loc[28, 'Email Address'] = 'marcelle.batupe@handsinhands.org'
df.loc[29, 'Email Address'] = 'naomie.yatche@handsinhands.org'

# writing into the file
df.to_csv("newcsv.csv", index=False)
df.to_excel("newxlsx.xlsx", index=False)

print(df)
