
import pandas as pd
#pd.options.display.max_columns = None

file_path = 'C:/Users/mhouts/OneDrive - Centric/Documents/Portfolio/Centric/ContactlijstExcel.xlsx'

df = pd.read_excel(file_path)



groupCompany = df.groupby('Company')

print(df)