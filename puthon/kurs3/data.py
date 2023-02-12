import requests
from download_clients import load_clients
import datetime

class Event:

    def __init__(self, title="", date=datetime.date.today()):
        self.title = title
        self.date = date

    def __repr__(self):
        return f"({self.date}"

##events.sort(key=lambda event: event.date)

def from_(re):
    from_list = []
    for i in filtered_by_data():
        desc_operation = i.get('from')
        if i.get('from') == None:
            from_list.append('Данные отсутствуют')

        else:
            from_list.append(desc_operation)

    return from_list[re]

def to_(to):
    to_list = []
    for i in filtered_by_data():
        desc_operation = i.get('to')
        to.list.apped(desc_operation)

    return to_list[to]

def parse_description_transaction(transactions_data: Dict[str, str]) - > str:
    description = transactions_data.get('description')
    return description

