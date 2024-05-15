import os
import pandas as pd

def csv_to_excel(filename_csv, filename_rect_csv, filename_xlsx):
    # Check if the Excel file already exists
    if not os.path.exists(filename_xlsx):
        # Create an empty Excel file with one sheet
        with pd.ExcelWriter(filename_xlsx, engine='openpyxl') as writer:
            # Create an empty DataFrame
            df_empty = pd.DataFrame()
            # Write the empty DataFrame to the Excel file
            df_empty.to_excel(writer, sheet_name='Sheet1', index=False)
    
    # Read data from the CSV files
    df_csv = pd.read_csv(filename_csv)
    df_rect_csv = pd.read_csv(filename_rect_csv)
    
    # Write data to different sheets of Excel file
    with pd.ExcelWriter(filename_xlsx, mode='a', engine='openpyxl') as writer:  # 'a' for append mode
        # Rename existing 'Sheet1' to 'Sheet1_old'
        writer.book.remove(writer.book['Sheet1'])
        # Write data from filename.csv to Sheet1 starting from row 2
        df_csv.to_excel(writer, sheet_name='Sheet1', startrow=1, index=False, header=False)
        
        # Write data from filename-rect.csv to Sheet2 starting from row 1
        df_rect_csv.to_excel(writer, sheet_name='Sheet2', index=False, )


# Specify the filenames

file_name_list = ['8006','8008','8011','8012','8015','8016','8017','8018','8019','8020','8021','8022','8023','8024']
for file in file_name_list:
# Call the function to convert CSV files to Excel
    filename_csv = file+'.csv'
    filename_rect_csv = file+'-rect.csv'
    filename_xlsx = file+'.xlsx'
    csv_to_excel(filename_csv, filename_rect_csv, filename_xlsx)
