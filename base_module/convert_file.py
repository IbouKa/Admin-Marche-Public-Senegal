from re import search
import pandas as pd
from bs4 import BeautifulSoup


def convert_string_to_csv(string_data) :
    soup = BeautifulSoup(string_data, "html.parser")
    data = []
    rows = soup.find_all('tr')
    i = 0

    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 10 and cols[0].text.isdigit():
            line_values = []
            k = 0
            for col in cols:
                if k == 1:
                    if search(".*[a-zA-Z].*", cols[1].text):
                        line_values.append(cols[2].text)
                        line_values.append(cols[1].text)
                    else:
                        line_values.append(cols[1].text)
                        line_values.append(cols[2].text)
                elif k == 2:
                    pass
                else:
                    line_values.append(col.text)

                k += 1
            data.append(line_values)

    df = pd.DataFrame(data, columns=['id', 'Date', 'Numéro', 'Gestion', 'Titre', 'Type', 'Mode_passation',
                                     'Autorite_Contractante', 'Montant', 'Titulaire'])

    return df