#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
import json, urllib
reload(sys)
sys.setdefaultencoding('utf-8')
#http headers
print 'Content-Type: text/html'
print # fin header http
#body
print '<!DOCTYPE html>'
print '<html>'
print '<head>'
print '  <meta charset="utf-8" />'
print '  <title>Test</title>'
print '  <link rel="stylesheet" type="text/css" href="./css/style.css" />'
print '</head>'
print '<body>'

##############################################

####### Connecion au site
xkcdconnect = urllib.urlopen('http://xkcd.com/info.0.json')

####### Conversion en fichier
xkcddata = xkcdconnect.read()

####### Test du chargement du JSON
try:

	# Recuperation du JSON
	message = json.loads(xkcddata)

	# Afficher l'image
	if (message.has_key('img')!= True):
		print 'Pas d\'image pour cette fois'
	else:
		print '<h1>{0}</h1>'.format(str(message['safe_title']))
		print '<img src="'+ str(message['img']) +'" alt="'+ str(message['num']) +'" />'

	# Lien vers l'ancienne image :
	print 'Previously: <a href="http://xkcd.com/' + str(message['num']) + '/info.0.json"> Here </a>'

# Si ca ne marche pas on retourne une erreur
except ValueError , e:
	print e.message

##############################################

print '</body>'
print '</html>'