from app.enums.monitored_stocks import MonitoredStocks
from app.enums.monitored_indexes import MonitoredIndexes
from app.service.email import build_message_email
from app.service.br_api import get_infos_stock
from app.models.stock import Stock
from app.models.index import Index


def build_report_stocks():
    list_stock_object = []
    list_index_object = []

    for index in MonitoredIndexes:
        data = get_infos_stock(index.value)
        index_object = Index.parse_obj(data.get('results')[0])

        list_index_object.append(index_object)

    for stock in MonitoredStocks:
        data = get_infos_stock(stock.value)
        stock_object = Stock.parse_obj(data.get('results')[0])

        list_stock_object.append(stock_object)

    build_message_email(list_stock_object, list_index_object)


build_report_stocks()
