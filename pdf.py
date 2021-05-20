import io
import os
import pdfkit
from shutil import copyfile
from bs4 import BeautifulSoup

filename = 'contract_edit.html'

def generate_contract_copy():
    copyfile('contract_base.html', 'contract_edit.html')

def generate_contract_pdf():
    pdfkit.from_file('contract_edit.html', 'contract.pdf')

def edit_contract_values(soup):
    client_name = soup.find(class_='client_name')
    client_name.string = '(Name Lastname) cetățean român,'
    address = soup.find(class_='address')
    address.string = 'cu domiciliul în (Targu Jiu..........),'
    with open(filename, 'wb') as file:
        file.write(soup.prettify('utf-8'))
    generate_contract_pdf()

def generate_pdf_contract(id_values, dates):
    generate_contract_copy()
    base = os.path.dirname(os.path.abspath(__file__))
    html = open(os.path.join(base, filename))
    soup = BeautifulSoup(html, 'html.parser')
    edit_contract_values(soup)

generate_pdf_contract('', '')