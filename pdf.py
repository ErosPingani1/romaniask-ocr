import os
import pdfkit
from shutil import copyfile
from bs4 import BeautifulSoup

filename = 'contract_edit.html'

def generate_contract_copy():
    copyfile('contract_base.html', 'contract_edit.html')

def create_pdf():
    pdfkit.from_file('contract_edit.html', 'contract.pdf')

def edit_contract_values(soup, id_values, contractInfo):
    client_name = soup.find(class_='client_name')
    client_name.string = id_values['lastname'] + ' ' + id_values['name'] + ' cetățean român,'

    address = soup.find(class_='address')
    address.string = 'cu domiciliul în ' + id_values['address'] + ','

    id_info = soup.find(class_="id_info")
    id_info.string = 'posesor al C.I. seria ' + id_values['id']['serial'] + ' nr ' + id_values['id']['number'] + ', eliberată de ' + id_values['issued_by'] + ','

    cnp = soup.find(class_='cnp')
    cnp.string = 'C.N.P ' + id_values['cnp']

    amounts = soup.find(class_='amounts')
    amounts.string = 'de ' + contractInfo['amount'] + ' lei pentru perioada de ' + contractInfo['length'] + ' zile'

    contract_length = soup.find(class_='contract_length')
    contract_length.string = 'durată de ' + contractInfo['length'] + ' zile'

    dates = soup.find(class_='dates')
    dates.string = 'data ' + contractInfo['startingDate'] + ' până la data de ' + contractInfo['endingDate'] + ','

    with open(filename, 'wb') as file:
        file.write(soup.prettify('utf-8'))
    create_pdf()

def generate_pdf_contract(id_values, contract_info):
    generate_contract_copy()
    base = os.path.dirname(os.path.abspath(__file__))
    html = open(os.path.join(base, filename))
    soup = BeautifulSoup(html, 'html.parser')
    edit_contract_values(soup, id_values, contract_info)
