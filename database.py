#!/usr/bin/python3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                                                                                                                           #
# ________    ________      ________         ___      _______       ________      _________                   ________      #
#|\   __  \  |\   __  \    |\   __  \       |\  \    |\  ___ \     |\   ____\    |\___   ___\                |\   ____\     #
#\ \  \|\  \ \ \  \|\  \   \ \  \|\  \      \ \  \   \ \   __/|    \ \  \___|    \|___ \  \_|  ____________  \ \  \___|_    #
# \ \   ____\ \ \   _  _\   \ \  \\\  \   __ \ \  \   \ \  \_|/__   \ \  \            \ \  \  |\____________\ \ \_____  \   #
#  \ \  \___|  \ \  \\  \|   \ \  \\\  \ |\  \\_\  \   \ \  \_|\ \   \ \  \____        \ \  \ \|____________|  \|____|\  \  #
#   \ \__\      \ \__\\ _\    \ \_______\\ \________\   \ \_______\   \ \_______\       \ \__\                   ____\_\  \ #
#    \|__|       \|__|\|__|    \|_______| \|________|    \|_______|    \|_______|        \|__|                  |\_________\#
#                                                                                                               \|_________|#
#                                                             v0                                                            #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#
#                                                     DATABASE MANAGEMENT

import sqlite3

#create however many database files you want
class connector():
	db = sqlite3.connect('database.db')

#init functions
class init():
	def config_init():
		cur = connector.db.cursor()
		cur.execute('CREATE TABLE config(sc_height,sc_width,app_font,app_fontSize,dflt_windowSize,c_rad,b_size,b_colour)')
		cur.execute('''
			INSERT INTO config VALUES(75,100,'Ubuntu',14,'600x500',10,75,'teal')
		''')
		connector.db.commit()

	def core_init():
		cur = connector.db.cursor()
		cur.execute('CREATE TABLE core(sc_id,f_class,code)')

#init.config_init()
#init.core_init()

def test(sc_id,f_class,code):
	cur = connector.db.cursor()
	cmd = 'INSERT INTO core VALUES("{i}","{j}","{k}")'.format(i=sc_id,j=f_class,k=code)
	cur.execute(cmd)
	connector.db.commit()

#test(1,'hello',"print('helloDB')")