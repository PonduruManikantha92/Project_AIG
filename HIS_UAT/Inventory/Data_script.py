import pandas as pd

# Load the Excel files
hrms_df = pd.read_excel("C:\\Users\\10013887\\Downloads\\one_aig_active_users.xlsx")
his_df = pd.read_excel("C:\\Users\\10013887\\Downloads\\HIS_Finale.xlsx")

# Print actual column names
print("HRMS columns:", hrms_df.columns.tolist())
print("HIS columns:", his_df.columns.tolist())

# Use correct column names based on print output
# For example, let's assume column is 'Employee ID'
hrms_ids = hrms_df['employee_id'].astype(str).str.strip().str.upper()
his_ids = his_df['employee_id'].astype(str).str.strip().str.upper()

# Print sample values
print("Sample HRMS IDs:", hrms_ids.head())
print("Sample HIS IDs:", his_ids.head())

# Find common employee_ids
common_ids = pd.Series(list(set(hrms_ids) & set(his_ids)), name='common_employee_id')

# Save to Excel
common_ids.to_excel("C:\\Users\\10013887\\Downloads\\common_employee_ids.xlsx", index=False)

print("✅ Common employee_ids saved to 'common_employee_ids.xlsx'")
