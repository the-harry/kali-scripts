#! python3
#PRIMEIRA VEZ INSTALAR DEPENDENCIAS
#pip install selenium beautifulsoup4 lxml requests
#pacman -S geckodriver

import os
import re
import json
import time
import requests
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from string import Template

#TODO
#lista de sites
#arrumar total s4 e s5
#blv
#report

sites = ['http://proxies.my-proxy.com/proxy-list-socks5.htmlproxies.my-proxy',         
	'http://free-proxy.cz/en/proxylist/country/BR/socks/speed/all/',
	'https://premproxy.com/proxy-by-country/Brazil-01.htm',
	'http://www.gatherproxy.com/sockslist/country/?c=Brazil',
	'http://spys.ru/proxys/BR/',
	'https://www.socks-proxy.net',
	'https://www.my-proxy.com/free-socks-5-proxy.html',
	'https://free-proxy-list.net/']

log = {"total": 0, "viva": 0, "ts": "-", "s5": 0, "s4": 0, "error": ">\n"}
browser = webdriver.Firefox()
ip = list()
port = list()
est = list()
city = list()
blv = list()
socks5 = list()
tsocks = [{'ac': 0, 'al': 0, 'ap': 0, 'am': 0, 'ba': 0, 'ce': 0, 'df': 0, 'es': 0, 'go': 0, 'ma': 0, 'mt': 0, 'ms': 0, 'mg': 0, 'pa': 0, 'pb': 
0, 'pr': 0, 'pe': 0, 'pi': 0, 'rj': 0, 'rn': 0, 'rs': 0, 'ro': 0, 'rr': 0, 'sc': 0, 'sp': 0, 'se': 0, 'to': 0}, {'ac': 0, 'al': 0, 'ap': 0, 
'am': 0, 'ba': 0, 'ce': 0, 'df': 0, 'es': 0, 'go': 0, 'ma': 0, 'mt': 0, 'ms': 0, 'mg': 0, 'pa': 0, 'pb': 0, 'pr': 0, 'pe': 0, 'pi': 0, 'rj': 
0, 'rn': 0, 'rs': 0, 'ro': 0, 'rr': 0, 'sc': 0, 'sp': 0, 'se': 0, 'to': 0}]

def Crawler(sites):
	#abrir site, encontrar ip:porta, ir para o proximo
	global log, browser
	
	# 0
	try:
		browser.get(sites[0])
		raw_proxy = browser.find_element_by_css_selector('div.list')
		#salvar validos
		proxy = raw_proxy.text
	except:
		log['error'] += '>Erro ao abrir site 0.\n'

	try:
		raw_proxy = browser.find_element_by_css_selector('div.to-lock.onp-sl-content')
		proxy += raw_proxy.text
	except:
		log['error'] += '>Erro ao procurar classe oculta site 0.\n'
	
	# 1
	pg = 1
	while pg < 6:
		try:
			browser.get(sites[1]+str(pg))
			time.sleep(3)
			#clicar bnt
			bnt = browser.find_element_by_id('clickexport')
			bnt.click()
			raw_proxy = browser.find_element_by_id('zkzk')
			proxy += raw_proxy.text
			time.sleep(2)
		except:
			log['error'] += '>Erro ao abrir página: '+str(pg)+' site 1.\n'
			break
		pg += 1

	# 2
	try:
		browser.get(sites[2])
		raw_proxy = browser.find_element_by_tag_name('tbody')
		proxy += ''.join(raw_proxy.text)
	except:
		log['error'] += '>Erro ao procurar tabela site 2.\n'

	# 3
	try:
		browser.get(sites[3])
		raw_proxy = browser.find_element_by_tag_name('tbody')
		proxy += ''.join(raw_proxy.text)
	except:
		log['error'] += '>Erro ao procurar tabela site 3.\n'

	# 4
	try:
		browser.get(sites[4])
		browser.find_element_by_xpath("//select[@name='xpp']/option[text()='300']").click()
		browser.find_element_by_xpath("//select[@name='xf5']/option[text()='SOCKS']").click()
		time.sleep(3)
		raw_proxy = browser.find_element_by_tag_name('tbody')
		proxy += ''.join(raw_proxy.text)
	except:
		log['error'] += '>Erro ao procurar tabela site 4.\n'

	# 5
	try:
		browser.get(sites[5])
		browser.find_element_by_xpath("//select[@name='proxylisttable_length']/option[text()='80']").click()
		browser.find_element_by_xpath("/html/body/section[1]/div/div[2]/div/div[2]/div/table/tfoot/tr/th[3]/select/option[6]").click()
		time.sleep(2)
		raw_proxy = browser.find_element_by_tag_name('tbody')
		proxy += ''.join(raw_proxy.text)
	except:
		log['error'] += '>Erro ao procurar tabela site 5.\n'
	
	# 6
	try:
		browser.get(sites[6])
		time.sleep(2)
		raw_proxy = browser.find_element_by_css_selector('div.list')
		#salvar validos
		proxy += raw_proxy.text
	except:
		log['error'] += '>Erro ao abrir site 6.\n'

	try:
		raw_proxy = browser.find_element_by_css_selector('div.to-lock.onp-sl-content')
		proxy += raw_proxy.text
	except:
		log['error'] += '>Erro ao procurar classe oculta site 6.\n'

	#7
	try:
		browser.get(sites[7])
		time.sleep(2)
		browser.find_element_by_xpath("//select[@name='proxylisttable_length']/option[text()='80']").click()
		browser.find_element_by_xpath("/html/body/section[1]/div/div[2]/div/div[2]/div/table/tfoot/tr/th[3]/select/option[8]").click()
		time.sleep(2)
		raw_proxy = browser.find_element_by_tag_name('tbody')
		proxy += ''.join(raw_proxy.text)
	except:
                log['error'] += '>Erro ao procurar tabela site 7.\n'

	return proxy

def Checker(proxy):
	global log, browser

	#filtrar ip:port
	browser.get('http://www.checker.freeproxy.ru/ru/filter_lite/')

	txtA = browser.find_element_by_name('data')
	txtA.clear()
	txtA.send_keys(proxy)
	txtA.submit()
	 
	time.sleep(5)
	rawproxy = browser.find_element_by_css_selector('div#filter-description')
	proxy = rawproxy.text

	#loop separar 100 em 100
	count = 0
	c = 0
	lim = 100
	cem = [''] * 20
	for line in proxy.splitlines():
		count += 1
		if count < lim:
			cem[c] += line + '\n'
		else:
			c += 1
			lim += 100
			cem[c] += line + '\n'

	log['total'] = count
	#abrir testador
	browser.get('http://www.checker.freeproxy.ru/ru/checker/')

	proxy = ''

	#testar proxys loop 100 em 100
	c = 0
	while cem[c] != '':
		txtA = browser.find_element_by_tag_name('textarea')
		txtA.send_keys(cem[c])
		txtA.submit()
		time.sleep(90)
		rawproxy = browser.find_element_by_tag_name('tbody')
		proxy += browser.page_source
		browser.refresh()
		c += 1
	#timestamp
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y--%H:%M:%S')
	log['ts'] = st
	
	return proxy

def Clear(proxy):
	global log, ip,	port, socks5
	#limpar apenas socks 4 ou 5

	socks = [''] * 2
	br = ''
	soup = BeautifulSoup(proxy, features="lxml")
	count = socks_c = 0
	for tr in soup.find_all('tr'):	
		if tr.find(text=re.compile("Brazil")):
			br = tr
			if br.find(text=re.compile("SOCKS4")):
				for td in br.find_all('td'):
					socks[0] += td.text+':'
				socks[0] += '\n'
				count += 1
			elif br.find(text=re.compile("SOCKS5")):
				for td in br.find_all('td'):
					socks[1] += td.text+':'
				socks[1] += '\n'
				count += 1
				socks_c += 1
		log['viva'] = count
		log['s5'] = socks_c
		log['s4'] = count - socks_c

	#[0]=socks4 [1]=socks5



	regex = re.compile(r'(\d{2,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\:(\d{2,5})')

	#loop socks validas
	for i in range(2):
		count = 0
		matches = regex.finditer(socks[i])
		#pega ip : port
		for match in matches:
			ipp = re.split('[:]', match.group(0))
			ip.append(ipp[0])
			port.append(ipp[1])
			if(i==0):
				socks5.append('0')
			elif(i==1):
				socks5.append('1')
			count += 1
	
	return ip, port, socks5

def GeoL(ip):
	global log, est, city
	#organizar por regiao
	#max 150 p min
	#120/min = sleep 2
	api = 'http://ip-api.com/json/'
	i = 0
	while i < len(ip):
		url = api + ip[i]
		#fazer request
		r = requests.get(url)
		try:
			r.raise_for_status()
		except Exception as exc:
			log['error'] += '\n\n>Erro GeoL.: %s' % (exc)
		data = json.loads(r.text)
		#salvar est e city
		est.append(data['region'])
		city.append(data['city'])
		time.sleep(2)
		
		i += 1
	return est, city

def Blv(ip):
	global browser, blv
	#achar api ou site para consulta
	#organizar por menos blacklistadas dentro das regioes
	#browser.get('https://www.s.org/search_ip.php')
	#fazer loop ips validos
	i = 0
	while i < len(ip):
		blv.append(0)
		i += 1

	return blv


def Report(ip, port, socks5, est, city, blv, log):
	global browser, tsocks
	#pegar informações 
	i = 0
	debug = ''
	while i < len(ip):
		debug += str(ip[i]) +' '+ str(port[i]) +' '+ str(est[i]) +' '+ str(city[i]) +' ' + str(socks5[i]) +' '+ str(blv[i]) +'\n'
		i += 1
	#print('\n\n' + str(log['error']))
	#print('\n\n' + str(log['total']))
	#print('\n\n' + str(log['viva']))
	#print('\n\n' + str(log['s4']))
	#print('\n\n' + str(log['s5']))
	#print('\n\n' + str(log['ts']))
	
	#loop conta socks 4 e 5
	for i in range(len(socks5)):
		if (socks5[i] == 1):
			#contar estado por estado	
			if (est[i] == 'AC'):
				tsocks[1]['ac'] += 1
			elif (est[i] == 'AL'):
				tsocks[1]['al'] += 1
			elif (est[i] == 'AP'):
				tsocks[1]['ap'] += 1
			elif (est[i] == 'AM'):
				tsocks[1]['am'] += 1
			elif (est[i] == 'BA'):
				tsocks[1]['ba'] += 1
			elif (est[i] == 'CE'):
				tsocks[1]['ce'] += 1
			elif (est[i] == 'DF'):
				tsocks[1]['df'] += 1
			elif (est[i] == 'ES'):
				tsocks[1]['es'] += 1
			elif (est[i] == 'GO'):
				tsocks[1]['go'] += 1
			elif (est[i] == 'MA'):
				tsocks[1]['ma'] += 1
			elif (est[i] == 'MT'):
				tsocks[1]['mt'] += 1
			elif (est[i] == 'MS'):
				tsocks[1]['ms'] += 1
			elif (est[i] == 'MG'):
				tsocks[1]['mg'] += 1
			elif (est[i] == 'PA'):
				tsocks[1]['pa'] += 1
			elif (est[i] == 'PB'):
				tsocks[1]['pb'] += 1
			elif (est[i] == 'PR'):
				tsocks[1]['pr'] += 1
			elif (est[i] == 'PE'):
				tsocks[1]['pe'] += 1
			elif (est[i] == 'PI'):
				tsocks[1]['pi'] += 1
			elif (est[i] == 'RJ'):
				tsocks[1]['rj'] += 1
			elif (est[i] == 'RN'):
				tsocks[1]['rn'] += 1
			elif (est[i] == 'RS'):
				tsocks[1]['rs'] += 1
			elif (est[i] == 'RO'):
				tsocks[1]['ro'] += 1
			elif (est[i] == 'RR'):
				tsocks[1]['rr'] += 1
			elif (est[i] == 'SC'):
				tsocks[1]['sc'] += 1
			elif (est[i] == 'SP'):
				tsocks[1]['sp'] += 1
			elif (est[i] == 'SE'):
				tsocks[1]['se'] += 1
			elif (est[i] == 'TO'):
				tsocks[1]['to'] += 1
		else:
				
			if (est[i] == 'AC'):
				tsocks[0]['ac'] += 1
			elif (est[i] == 'AL'):
				tsocks[0]['al'] += 1
			elif (est[i] == 'AP'):
				tsocks[0]['ap'] += 1
			elif (est[i] == 'AM'):
				tsocks[0]['am'] += 1
			elif (est[i] == 'BA'):
				tsocks[0]['ba'] += 1
			elif (est[i] == 'CE'):
				tsocks[0]['ce'] += 1
			elif (est[i] == 'DF'):
				tsocks[0]['df'] += 1
			elif (est[i] == 'ES'):
				tsocks[0]['es'] += 1
			elif (est[i] == 'GO'):
				tsocks[0]['go'] += 1
			elif (est[i] == 'MA'):
				tsocks[0]['ma'] += 1
			elif (est[i] == 'MT'):
				tsocks[0]['mt'] += 1
			elif (est[i] == 'MS'):
				tsocks[0]['ms'] += 1
			elif (est[i] == 'MG'):
				tsocks[0]['mg'] += 1
			elif (est[i] == 'PA'):
				tsocks[0]['pa'] += 1
			elif (est[i] == 'PB'):
				tsocks[0]['pb'] += 1
			elif (est[i] == 'PR'):
				tsocks[0]['pr'] += 1
			elif (est[i] == 'PE'):
				tsocks[0]['pe'] += 1
			elif (est[i] == 'PI'):
				tsocks[0]['pi'] += 1
			elif (est[i] == 'RJ'):
				tsocks[0]['rj'] += 1
			elif (est[i] == 'RN'):
				tsocks[0]['rn'] += 1
			elif (est[i] == 'RS'):
				tsocks[0]['rs'] += 1
			elif (est[i] == 'RO'):
				tsocks[0]['ro'] += 1
			elif (est[i] == 'RR'):
				tsocks[0]['rr'] += 1
			elif (est[i] == 'SC'):
				tsocks[0]['sc'] += 1
			elif (est[i] == 'SP'):
				tsocks[0]['sp'] += 1
			elif (est[i] == 'SE'):
				tsocks[0]['se'] += 1
			elif (est[i] == 'TO'):
				tsocks[0]['to'] += 1
	table = ''
	
	#carregar table 5
	if (tsocks[1]['ac'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['ac'] + 1) +'">Acre - AC</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'AC'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['al'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['al'] + 1) +'">Alagoas - AL</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'AL'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['ap'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['ap'] + 1) +'">Amapá - AP</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'AP'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] + '</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['am'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['am'] + 1) +'">Amazonas - AM</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'AM'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['ba'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['ba'] + 1) +'">Bahia - BA</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'BA'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['ce'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['ce'] + 1) +'">Ceará - CE</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'CE'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['df'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['df'] + 1) +'">Distrito Federal - DF</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'DF'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['es'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['es'] + 1) +'">Espírito Santo - ES</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'ES'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['go'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['go'] + 1) +'">Goiás - GO</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'GO'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['ma'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['ma'] + 1) +'">Maranhão - MA</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'MA'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['mt'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['mt'] + 1) +'">Mato Grosso - MT</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'MT'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['ms'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['ms'] + 1) +'">Mato Grosso do Sul - MS</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'MS'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['mg'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['mg'] + 1) +'">Minas Gerais - MG</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'MG'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['pa'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['pa'] + 1) +'">Pará - PA</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'PA'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['pb'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['pb'] + 1) +'">Paraíba - PB</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'PB'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['pr'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['pr'] + 1) +'">Paraná - PR</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'PR'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['pe'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['pe'] + 1) +'">Pernambuco - PE</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'PE'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n' 
	if(tsocks[1]['pi'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['pi'] + 1) +'">Piauí - PI</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'PI'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['rj'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['rj'] + 1) +'">Rio de Janeiro - RJ</td></tr>\n'
		for c in range(len(est)):
			if(socks5[c] == 1 and est[c] == 'RJ'):
					table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['rn'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['rn'] + 1) +'">Rio Grande do Norte - RN</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'RN'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['rs'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['rs'] + 1) +'">Rio Grande do Sul - RS</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'RS'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['ro'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['ro'] + 1) +'">Rondônia - RO</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'RO'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['rr'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['rr'] + 1) +'">Roraima - RR</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'RR'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['sc'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['sc'] + 1) +'">Santa Catarina - SC</td></tr>\n'
		for c in range(len(est)):
			if(socks5[c] == 1 and est[c] == 'SC'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['sp'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['sp'] + 1) +'">São Paulo - SP</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 1 and est[c] == 'SP'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['se'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['se'] + 1) +'">Sergipe - SE</td></tr>\n'
		for c in range(len(est)):
			if(socks5[c] == 1 and est[c] == 'SE'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[1]['to'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[1]['to'] + 1) +'">Tocantins - TO</td></tr>\n'
		for c in range(len(est)):
			if(socks5[c] == 1 and est[c] == 'TO'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	
	table += """
		</tbody>
		</table>
		</div>
		<div class="tab">
		<table id="s4">
		<caption class="socks4">Socks4</caption>
		  <thead>
		    <tr>
			 <th>Estado</th>
		      <th>Cidade</th>
		      <th>IP</th>
		      <th>Port</th>
			<th>BLV</th>
		    </tr>
		  </thead>
		  <tbody>
		"""

	#carregar sock4
	if(tsocks[0]['ac'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['ac'] + 1) +'">Acre - AC</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'AC'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['al'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['al'] + 1) +'">Alagoas - AL</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'AL'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['ap'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['ap'] + 1) +'">Amapá - AP</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'AP'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['am'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['am'] + 1) +'">Amazonas - AM</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'AM'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['ba'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['ba'] + 1) +'">Bahia - BA</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'BA'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['ce'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['ce'] + 1) +'">Ceará - CE</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and  est[c] == 'CE'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['df'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['df'] + 1) +'">Distrito Federal - DF</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'DF'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['es'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['es'] + 1) +'">Espírito Santo - ES</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'ES'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['go'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['go'] + 1) +'">Goiás - GO</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'GO'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['ma'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['ma'] + 1) +'">Maranhão - MA</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'MA'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['mt'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['mt'] + 1) +'">Mato Grosso - MT</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'MT'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['ms'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['ms'] + 1) +'">Mato Grosso do Sul - MS</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'MS'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['mg'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['mg'] + 1) +'">Minas Gerais - MG</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'MG'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['pa'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['pa'] + 1) +'">Pará - PA</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'PA'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['pb'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['pb'] + 1) +'">Paraíba - PB</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'PB'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['pr'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['pr'] + 1) +'">Paraná - PR</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'PR'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['pe'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['pe'] + 1) +'">Pernambuco - PE</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'PE'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['pi'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['pi'] + 1) +'">Piauí - PI</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'PI'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['rj'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['rj'] + 1) +'">Rio de Janeiro - RJ</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'RJ'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['rn'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['rn'] + 1) +'">Rio Grande do Norte - RN</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'RN'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['rs'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['rs'] + 1) +'">Rio Grande do Sul - RS</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'RS'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['ro'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['ro'] + 1) +'">Rondônia - RO</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'RO'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['rr'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['rr'] + 1) +'">Roraima - RR</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'RR'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['sc'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['sc'] + 1) +'">Santa Catarina - SC</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'SC'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['sp'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['sp'] + 1) +'">São Paulo - SP</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'SP'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['se'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['se'] + 1) +'">Sergipe - SE</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'SE'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'
	if(tsocks[0]['to'] > 0):
		table += '<tr><td rowspan="'+ str(tsocks[0]['to'] + 1) +'">Tocantins - TO</td></tr>\n'
		for c in range(len(est)):
			if (socks5[c] == 0 and est[c] == 'TO'):
				table += '<tr><td>'+ city[c] +'</td><td>'+ ip[c] +'</td><td>'+ port[c] +'</td><td>'+ blv[c] +'</td></tr>\n'

	#gerar html
	html =	Template("""
		<!doctype html>
		<html lang="pt-BR">
		<head>
		<title>Relatório $ts </title>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<style>
		.tab{display:inline-block;margin:0 6% 0;}
		h2{display:inline;border-left: 1px black solid;border-right:1px black solid;padding:2px 2% 2px;}
		table, td, th{ border: 1px black solid; border-collapse: collapse;}
		th, .info{background-color:rgba(0,0,128,0.6); color:white;}
		.socks4{background-color: rgba(128,0,0,0.4);}
		.socks5{background-color: rgba(0,128,0,0.4);}
		.hide{display:none;}
		</style>
		</head>
		<body>
		<br>
		<div class="info">
		<h2>$ts</h2>
		<h2>Proxys encontradas: $total</h2>
		<h2>Total proxys vivas: $vivas</h2>
		<h2>Socks5: $s5</h2>
		<h2>Socks4: $s4</h2>
		</div>
		<br>
		<div class="tab">
		<table id="s5">
		<caption class="socks5">Socks5</caption>
		  <thead>
		  <!-- Cabeçalio -->
		    <tr>
		      <th>Estado</th>
		      <th>Cidade</th>
		      <th>IP</th>
		      <th>Port</th>
		      <th>BLV</th>
		    </tr>
		  </thead>
		  <tbody>
		$tabela
		</tbody>
		</table>
		</div>
		<div class="info">
		<h2>Erros:</h2>
		<p>$erro<br>$debug</p>
		</div>
		<script>
		var r = document.getElementById("s5").getElementsByTagName("tr").length; if (r < 2){ 
document.getElementById("s5").style.display="none"; } r = document.getElementById("s4").getElementsByTagName("tr").length; if (r < 2){ 
document.getElementById("s4").style.display="none";
}		</script>
		</body>
		</html>
		""")

	# salvar e abrir relatorio
	#caminho
	cwd = os.getcwd()
	file = open(log['ts']+'.html',"w")
	file.write(html.safe_substitute(erro=log['error'], tabela=table, s4=log['s4'], s5=log['s5'], total=log['total'], vivas=log['viva'], ts=log['ts'], debug=debug))
	file.close()
	browser.get('file://' + cwd + '/' + log['ts'] + '.html')

if __name__ == '__main__':
	#criar log entre as funçoes
	#definir variaveis globais e acessos
	raw = Crawler(sites)
	vivas = Checker(raw)
	ip, port, socks5 = Clear(vivas)
	est, city = GeoL(ip)
	blv = Blv(ip)
	print(log['error'])
	Report(ip, port, socks5, est, city, blv, log)
