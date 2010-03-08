#!/usr/bin/env python
# -*- coding: utf-8 -*-


# use python-crypto pkg's AES object
# by sylecn@yahoo.com.cn

from Crypto.Cipher import AES

# you can generate your own key when first time run
# or use this static one
key='mengshejiushiniu';

aesObj = AES.new(key, AES.MODE_ECB)

def encode(orgstr):
	plain =  orgstr + '\x00' * (16 - len(orgstr) % 16)
	encstr = aesObj.encrypt(plain)
	return encstr

def decode(encstr):
	decstr = aesObj.decrypt(str(encstr))
	while decstr[-1] == '\x00' :
		decstr = decstr[:-1]
	return decstr
