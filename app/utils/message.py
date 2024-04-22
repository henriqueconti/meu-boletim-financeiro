from datetime import datetime


def build_message_email(list_acao_object, list_indice_object, news_object_list):
    subject = 'Relatório Ações {}'.format(datetime.now().strftime('%d-%m-%Y'))
    message = ''

    for indice_object in list_indice_object:
        message += '\n{}\nAbertura: {} pontos\nEncerramento: {} pontos\nVariação Diária: {}%\n'.format(
            indice_object.longName,
            indice_object.regularMarketOpen,
            indice_object.regularMarketPrice,
            indice_object.regularMarketChangePercent
        )

    for acao_object in list_acao_object:
        message += '\nAção: {}\nPreço Abertura: {}\nPreço Encerramento: {}\nVariação Diária: {}%\n'.format(
            acao_object.symbol,
            acao_object.regularMarketOpen,
            acao_object.regularMarketPrice,
            acao_object.regularMarketChangePercent
        )

    message += '\nPrincipais Notícias\n'

    for news_object in news_object_list:
        message += '\n{}\nAcesse: {}\n'.format(news_object.title, news_object.url)

    return message, subject
