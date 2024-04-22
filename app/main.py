import asyncio

from app.enums.monitored_stocks import MonitoredStocks
from app.enums.monitored_indexes import MonitoredIndexes
from app.service.email import build_message_email
from app.service.gnews_api import get_news_info
from app.service.br_api import get_stock_info
from app.models.stock import Stock
from app.models.index import Index
from app.models.news import News


async def main():
    stock_object_list, index_object_list = await build_report_stocks()
    news_object_list = await build_report_news()

    build_message_email(stock_object_list, index_object_list, news_object_list)


async def build_report_stocks():
    stock_object_list = []
    index_object_list = []

    for index in MonitoredIndexes:
        data = get_stock_info(index.value)
        index_object = Index.parse_obj(data.get('results')[0])

        index_object_list.append(index_object)

    for stock in MonitoredStocks:
        data = get_stock_info(stock.value)
        stock_object = Stock.parse_obj(data.get('results')[0])

        stock_object_list.append(stock_object)

    return stock_object_list, index_object_list


async def build_report_news():
    news_object_list = []

    news_data = get_news_info()

    for news in news_data.get('articles'):
        news_object = News.parse_obj(news)

        news_object_list.append(news_object)

    return news_object_list


if __name__ == "__main__":
    asyncio.run(main())
