from datetime import datetime


def build_message_email(stock_object_list, index_object_list, news_object_list):
    subject = 'Relatório Ações {}'.format(datetime.now().strftime('%d-%m-%Y'))
    message = ''

    for index_object in index_object_list:
        message += '\n{}\nAbertura: {} pontos\nEncerramento: {} pontos\nVariação Diária: {}%\n'.format(
            index_object.longName,
            index_object.regularMarketOpen,
            index_object.regularMarketPrice,
            index_object.regularMarketChangePercent
        )

    for stock_object in stock_object_list:
        message += '\nAção: {}\nPreço Abertura: {}\nPreço Encerramento: {}\nVariação Diária: {}%\n'.format(
            stock_object.symbol,
            stock_object.regularMarketOpen,
            stock_object.regularMarketPrice,
            stock_object.regularMarketChangePercent
        )

    message += '\nPrincipais Notícias\n'

    for news_object in clear_news_list(news_object_list):
        message += '\n{}\nAcesse: {}\n'.format(news_object.title, news_object.url)

    return message, subject


def clear_news_list(news_object_list):
    cleaned_news_object_list = []

    for news_object in news_object_list:
        if 'Bolsa Família' not in news_object.content:
            cleaned_news_object_list.append(news_object)
    return cleaned_news_object_list
