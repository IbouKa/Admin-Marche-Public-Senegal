import re

def replace_comma_to_espace_in_text(text):
    # this function takes text as an argument and returns a text by replacing the commas with spaces
    return str(text).replace(',', ' ')

def replace_comma_to_espace_in_df(df1):
    # this function takes a dataframe as an argument and returns the dataframe by replacing all the commas with spaces
    for col in df1.columns:
        df1[col] = df1[col].apply(replace_comma_to_espace_in_text)

def normalize_Type(text):
    # Cette fonction en argument du text et retourn le type de marché avec le bon orthographe
    text = text.lower()
    if 'travau' in text:
        return 'Travaux'
    elif 'service' in text:
        return 'Services Courants'
    elif 'fournitur' in text:
        return 'Fournitures'
    elif 'prestation' in text:
        return 'Prestationns intellectuelles'
    else:
        return 'Inconnu'


def normalize_mode_passation(text):
    # Cette fonction en argument du text et retourn le mode passation avec le bon orthographe
    text = re.sub("|;|,|'|/| ", '', text.lower().replace('.', ''))

    if ('ppel' in text and 'off' in text and 'uver' in text) or 'aoo' == text or 'aoopu' == text:
        return "Appel d'offres ouvert"
    elif ('ppel' in text and 'off' in text and 'estr' in text) or 'aor' == text or 'aorpu' == text:
        return "Appel d'offres restreint"
    elif ('ppel' in text and 'off' in text and 'nterna' in text) or 'aoi' == text:
        return "Appel d'offres international"
    elif ('ppel' in text and 'off' in text and 'quali' in text) or 'aop' == text:
        return "Appel d'offres avec préqualification"
    elif 'off' in text and 'ponta' in text:
        return "Appel d'offres spontanées négociées"
    elif ('ppel' in text and 'off' in text) or 'ao' == text:
        return "Appel d'offres"
    elif ('ppel' in text and 'anifes' in text) or ('vis' in text and 'anifes' in text):
        return "Appel à manifestation d’intérêts"
    elif 'venan' in text:
        return "Avenant"
    elif ('onsulta' in text and 'estrein' in text):
        return "Consultation restreinte"
    elif 'onventi' in text:
        return "Convention"
    elif ('emand' in text and 'ropos' in text) or 'dp' == text:
        return "Demande de proposition"
    elif ('drp' in text) or ('emand' in text and 'ensei') or ('ensei' in text and 'prix' in text):
        return "Demande de renseignements de prix"
    elif ('ntent' in text) and ('irec' in text):
        return "Entente directe"
    elif 'arch' in text and 'lien' in text:
        return "Marché de clientèle"
    elif 'arch' in text and 'omman' in text:
        return "Marché à commande"
    elif 'restation' in text and 'ntellec' in text:
        return "Prestations intellectuelles"
    elif text == 'dplr':
        return 'dplr'
    else:
        return 'Inconnu'


tauxDolCfa = {
    '2007': 478.634,
    '2008': 446.000,
    '2009': 470.293,
    '2010': 494.794,
    '2011': 471.249,
    '2012': 510.556,
    '2013': 493.900,
    '2014': 493.757,
    '2015': 591.212,
    '2016': 592.606,
    '2017': 580.657,
    '2018': 555.446,
    '2019': 585.911,
    '2020': 575.586,
    '2021': 554.531
}


def normalize_montant_in_fca_W_date(date, text):
    text = re.sub("|;|,|'|/| ", '', text.lower().replace('.', ''))

    if 'euro' in text:
        return ((float)(''.join(re.findall('\d+', text)))) * 655.9570
    elif 'dollar' in text:
        return ((float)(''.join(re.findall('\d+', text)))) * tauxDolCfa[date[-4:]]
    else:
        return (float)(''.join(re.findall('\d+', text)))


def normalize_montant_in_fca(text):
    text = re.sub("|;|,|'|/| ", '', text.lower().replace('.', ''))

    if 'euro' in text:
        return ((float)(''.join(re.findall('\d+', text)))) * 655.9570
    elif 'dollar' in text:
        return ((float)(''.join(re.findall('\d+', text)))) * 627.5900
    else:
        return (float)(''.join(re.findall('\d+', text)))


def normalize_date(text):
    # Cette fonction prend une chaine en argument et return une chaine au format "JJ/MM/AAAA"
    if re.match('([0-9]{2}/[0-9]{2}/[0-9]{4})', text):
        # Format : JJ/MM/AAAA
        return text[:2] + '/' + text[3:5] + '/' + text[-4:]
    elif re.match('([0-9]{2}/[0-9]{2}/[0-9]{2})', text):
        # Format : JJ/MM/AA
        return text[:2] + '/' + text[3:5] + '/20' + text[-2:]
    elif re.match('([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2})', text):
        # Format : AAAA/MM/JJ 00:00:00
        return text[8:10] + '/' + text[5:7] + '/' + text[:4]
    elif re.match('([0-9]{2}-avr.-[0-9]{2})', text):
        # Format : JJ-avr.-AA
        return text[:2] + '/04/20' + text[-2:]
    elif re.match('([0-9]{1}-avr.-[0-9]{2})', text):
        # Format : J-avr.-AA
        return '0' + text[0] + '/04/20' + text[-2:]
    elif re.match('([0-9]{2} juin[0-9]{4})', text):
        # Format : JJ juinAAAA
        return text[:2] + '/06/' + text[-4:]
    elif re.match('([0-9]{2}.[0-9]{2}.[0-9]{4})', text):
        # Format : JJ.MM.AAAA
        return text[:2] + '/' + text[3:5] + '/' + text[-4:]
    elif re.match('([0-9]{2}.[0-9]{2} .[0-9]{4})', text):
        # Format : JJ.MM .AAAA
        return text[:2] + '/' + text[3:5] + '/' + text[-4:]
    elif re.match('([0-9]{1}/[0-9]{2}/[0-9]{2})', text):
        # Format : J.MM .AA
        return '0' + text[0] + '/' + text[2:4] + '/' + '20' + text[-2:]
    elif text == '13 aout':
        return '13/08/2018'
    elif text == '1er août 2019':
        return '01/08/2019'
    elif text == '04septembre 2019':
        return '04/09/2019'
    elif text == '1er juillet':
        return '01/07/2020'
    elif text == '1er juin':
        return '01/06/2021'
    elif text == '28/10014':
        return '28/10/2014'
    elif text == '13/805/2015':
        return '13/05/2015'
    elif text == '1er /09/2016':
        return '01/09/2016'
    elif text == '06/0619':
        return '06/06/2019'
    elif text == '23/2019':
        return '23/06/2019'
    elif text == '09 04/ 20':
        return '09/04/2020'
    elif text == '07/6/214':
        return '07/06/2021'
    elif text == '17/6/251':
        return '17/06/2021'
    elif text == '18/821':
        return '18/08/2021'
    elif text == '007/7/21':
        return '07/07/2021'
    elif text == '18/7/251':
        return '18/07/2021'
    elif text == '18//7/21':
        return '18/07/2021'
    else:
        return 'Inconnu Format'


def get_year(text):
    return text[-4:]


def get_month(text):
    return text[3:5]


def get_day(text):
    return text[:2]


def get_trimestre(text):
    if text[3:5] in ['01', '02', '03']:
        return 'Trim1'
    elif text[3:5] in ['04', '05', '06']:
        return 'Trim2'
    elif text[3:5] in ['07', '08', '09']:
        return 'Trim3'
    else:
        return 'Trim4'


