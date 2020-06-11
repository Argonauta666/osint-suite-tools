import re
from bs4 import BeautifulSoup
import modules.config as config
import modules.er as er

def parser_email(text):

	r = re.compile(r"[a-z0-9!#$%&'*+-/=?^_`{|}~]{1,64}@[a-zA-Z0-9]{1,255}\.[a-zA-Z0-9-]{1,24}")
	results = r.findall(text)
	if results:
		for x in results:
			x = er.replace_acentos(er.remove_tags(er.replace_letras_raras(str(x))))
			print("|--------[INFO][PARSER][EMAIL][>] " + x)
			if len(x) <20:
				config.emailsData_list.append(x)

def parser_n_tlfn(text):


	all_matches_telf = re.compile(r"(?:(?:\+(?:[0]{0,4})?)?34[. -]{0,3})?[6789][0-9]{2}[ ]{0,3}(?:[0-9][ ]?){5}[0-9]")
	
	'''
		Fuentes para buscar patrones:
		.............................

		https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s03.html
		https://zadarma.com/es/tariffs/numbers/latvia/riga/
		http://www.asifunciona.com/tablas/pref_telefonos/pref_telefonos_1.htm
		https://en.wikipedia.org/wiki/List_of_mobile_telephone_prefixes_by_country
	'''
	international_numbers = re.compile(r"\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}")

	results_spain = all_matches_telf.findall(text)
	results_international = international_numbers.findall(text)


	for x in results_spain:
		print("|--------[INFO][PARSER][SPAIN][NUMBER PHONE][>] " + x)
		config.phonesData_list.append(x)
	list(set(config.phonesData_list))
	
	for x in results_international:
		print("|--------[INFO][PARSER][INTERNACIONAL][NUMBER PHONE][>] " + x)
		#config.phonesData_list.append(x)

def parser_IBAN(text):

	r = re.compile(r"[a-zA-Z]{2}[0-9]{0,2}[ ]?([0-9]{4}[ ]?){5}")
	results = r.findall(text)
	if results:
		for x in results:
			print ("|--------[INFO][PARSER][IBAN][>] " + str(x))
		

def parser_EN_DATE(text):
	date = re.findall(r'([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))', text)
	if date:
		for x in date:
			print ("|--------[INFO][PARSER][DATE][>] " + str(x))
	date_barra = re.findall(r'^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$', text)
	if date_barra:
		for x in date_barra:
			print ("|--------[INFO][PARSER][DATE][>] " + str(x))
	date_guion = re.findall(r'\d{4}-\d{2}-\d{2}', text)
	if date_guion:
		for x in date_guion:
			print ("|--------[INFO][PARSER][DATE][>] " + str(x))

def parser_DNI(text):
	
	r = re.compile(r"(^[0-9]{8,8}[A-Za-z]$)")
	results = r.findall(text)
	if results:
		for x in results:
			print ("|--------[INFO][PARSER][DNI][>] " + str(x))
			config.DNIData_list.append(str(x))
def parserMAIN(text):

	parser_EN_DATE(text)
	parser_DNI(text)
	parser_email(text)
	parser_IBAN(text)
	parser_n_tlfn(text)