from datetime import datetime

today_date = datetime.now().strftime('%d-%m-%Y')


def build_message_email(stock_object_list, index_object_list, news_object_list):
    subject = 'Relatório Mercado Financeiro {}'.format(today_date)
    message = ''

    for index_object in index_object_list:
        message += format_messsage('Índice', index_object)

    for stock_object in stock_object_list:
        message += format_messsage('Ação', stock_object)

    message += '\nPrincipais Notícias\n'

    for news_object in clear_news_list(news_object_list):
        message += '\n{}\nAcesse: {}\n'.format(news_object.title, news_object.url)

    return message, subject


def format_messsage(object_type, data_object):
    return '\n{}: {}\nAbertura: {}\nEncerramento: {}\nVariação Diária: {}%\n'.format(
        object_type,
        data_object.longName if object_type == "Índice" else data_object.symbol,
        data_object.regularMarketPreviousClose,
        data_object.regularMarketPrice,
        data_object.regularMarketChangePercent
    )


def clear_news_list(news_object_list):
    cleaned_news_object_list = []

    for news_object in news_object_list:
        if ('Bolsa Família' not in news_object.content) and \
                ('Day Trade Hoje' not in news_object.title):
            cleaned_news_object_list.append(news_object)
    return cleaned_news_object_list
