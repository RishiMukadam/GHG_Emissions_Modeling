import pandas as pd

file_path = r'C:\Users\Rushikesh\Desktop\Internship\GHG_Emissions_Modeling\data\SupplyChainEmissionFactorsforUSIndustriesCommodities.xlsx'
years = range(2010, 2017)
all_data = []

for year in years:
    for source in ['Commodity', 'Industry']:
        sheet = f"{year}_Detail_{source}"
        df = pd.read_excel(file_path, sheet_name=sheet)
        df.columns = df.columns.str.strip()
        df['Source'] = source
        df['Year'] = year
        df.rename(columns={
            f'{source} Code': 'Code',
            f'{source} Name': 'Name'
        }, inplace=True)
        all_data.append(df)

combined_df = pd.concat(all_data, ignore_index=True)
combined_df.to_csv(r'C:\Users\Rushikesh\Desktop\Internship\GHG_Emissions_Modeling\data\combined_emissions_data.csv', index=False)

