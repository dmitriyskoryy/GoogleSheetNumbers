import gspread

sa = gspread.service_account(filename="creds.json")

sh = sa.open("SheetNumbers")

wks = sh.worksheet("Лист1")

print("Rows: ", wks.row_count)
print("value:", wks.col_count)