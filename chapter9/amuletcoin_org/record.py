from collections import UserList
import datetime


class Record:
    def __init__(self, date, category, expense):
        self.date = datetime.date.fromisoformat(date)
        self.category = category
        self.expense = int(expense)

    def __repr__(self):
        return f"Record(date={self.date}, category={self.category}, expense={self.expense})"


class RecordList(UserList):
    def __init__(self, data):
        self.data = data

    def category_total(self, start=None, end=None):
        self.sort(key=lambda x: x.date)
        if start is None:
            start = self[0].date
        if end is None:
            end = self[-1].date

        category_total = {
            "total": 0
        }
        for record in self:
            if start <= record.date <= end:
                category_total[record.category] = record.expense + category_total.get(record.category, 0)
                category_total["total"] += record.expense
        return category_total
