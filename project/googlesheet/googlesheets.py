import gspread

class GoogleSheets:
    """Класс подключения к гугл таблице"""
    sa = gspread.service_account(filename="./creds.json")


    def open_sheet(self):
        """Метод возвращает таблицу гугл"""
        sheet = self.sa.open("SheetNumbers")
        return sheet


    def get_worksheet(self):
        """Метод возвращает рабочий лист с данными из таблицы гугл"""
        sheet = self.open_sheet()
        worksheet = sheet.worksheet("Лист1")
        return worksheet

