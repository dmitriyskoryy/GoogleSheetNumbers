import gspread

class GoogleSheets:
    sa = gspread.service_account(filename="creds.json")


    def open_sheet(self):
        sheet = self.sa.open("SheetNumbers")
        return sheet


    def get_worksheet(self):
        sheet = self.open_sheet()
        worksheet = sheet.worksheet("Лист1")
        return worksheet



wks = GoogleSheets()
dd = wks.get_worksheet()
print("Rows: ", dd.row_count)
print("value:", dd.col_count)