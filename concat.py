# # import pandas library
# import pandas as pd
#
# # read csv file
# df = pd.read_csv("KEY PLAN-1.csv", encoding ="ISO-8859-1", engine='python')
# print(df)
# df = df.dropna()
#
# # concatenate the string
# df['t e x t'] = df.groupby(['l e v e l'])['t e x t'].transform(lambda x : ' '.join(x))
#
# # df['Text'] = df.groupby(['Height'])['Text'].transform(lambda x : ' '.join(x))
#
# # df.drop(columns=['A', 'B', 'C', 'D', 'E','F','G','Height', 'J','K', 'I'], inplace=True)
# df.drop(columns=['l e v e l ', 'p a g e _ n u m', 'b l o c k _ n u m', 'p a r _ n u m', 'l i n e _ n u m', 'w o r d _ n u m', 'l e f t', 't o p', 'w i d t h', 'h e i g h t', 'c o n f'], inplace=True)
#
# # drop duplicate data
# df = df.drop_duplicates('t e x t')
#
# df = df.to_csv("new_made.csv",index=False)
#
# # show the dataframe
# print(df)


# import pandas library
import pandas as pd
import os
#
# input_dir = 'Input_Csv'
# file_name = 'demo1_New.csv'
#
# csv_filename = input_dir + os.sep + "csv\\" + file_name[:-4] + ".csv"
# read csv file
df = pd.read_csv("680000.csv",encoding = "ISO-8859-1", engine='python')
# print(df)
df = df.dropna()

# concatenate the string
df['Text'] = df.groupby(['Height'])['Text'].transform(lambda x : ' '.join(x))


df.drop(columns=['A', 'B', 'C', 'D', 'E','F','G','Height', 'J','K'], inplace=True)

# df.drop(columns=[', '', '', '', '','','','Height', '','', ''], inplace=True)

# drop duplicate data
df = df.drop_duplicates('Text')
# output_dir = 'converted_csv'
# conv_csv_filename = output_dir + os.sep + "csv\\" + file_name[:-4] + ".csv"
df = df.to_csv("conv_demo11.csv",index=False)

# show the dataframe
print(df)

