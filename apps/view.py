

from apps import app
from flask import  jsonify,render_template, request,json
import time,xlrd
import numpy as np
import pymongo
from pymongo import MongoClient
from pymongo.errors import BulkWriteError
from bson.json_util import dumps
from bson.json_util import loads
from bson.objectid import ObjectId
import os
from werkzeug.utils import secure_filename
import re
from statistics import mean
from math import log
from sklearn.linear_model import LinearRegression
import math
import random

file_location=""
app.config["IMAGE_UPLOADS"] = "/app/apps/static"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF","XLSX"]
client = MongoClient("")
db = client["creditscore"]
collection = db["creditscore"]

@app.route("/")
def index():
	return render_template("layouts/index.html")
	# return render_template("layouts/index.html")

@app.route('/signUpUser', methods=['GET','POST'])
def signUpUser():
	authenticationUsers={
		  'username1':'nikhil@gmail.com',
		  'password':'Nikhil'
	 }
	 
	user =  request.form['username']
	password = request.form['password']
	if user in authenticationUsers.values():
		return json.dumps({'status':True,'user':user,'pass':password});
	else:
		return json.dumps({'status':False,'user':user,'pass':password});    
			
@app.route('/fileData',methods=['GET','POST'])
def fileData():
	if request.method=='POST':
		if request.files:
			image = request.files["image"]
			filename = secure_filename(image.filename)
			image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
			global file_location
			file_location=os.path.join(app.config["IMAGE_UPLOADS"], filename)
			workbook = xlrd.open_workbook(file_location)
			sheet = workbook.sheet_by_index(0)
			# psitrnids = int(sheet.cell_value(4,6))
			# psitrnids = sheet.cell_value(4,6)
			# psitrnid=int(psitrnids)
			# binsid = int(sheet.cell_value(5,2))
			# psiootid  = int(sheet.cell_value(4,7))
			goodtrnid = ObjectId()
			badtrnid = ObjectId()
			goodootid = ObjectId()
			badootid = ObjectId()
			binsid = ObjectId()
			na1_trn = sheet.cell_value(2,1)
			na_trn = int(na1_trn)
			trn=[]
			bins_trn=[]
			bins_trn1=[]

			resu_trn=[]

			a1 = []

			good_trn = []
			bins_good_trn = []
			resu_good_trn = []
			resu_good_trn = []
			na1_good_trn = sheet.cell_value(2,1)
			na_good_trn= int(na1_good_trn)
			for row in range(7, na_good_trn+7):
				good_trn1 = sheet.cell_value(row,2) 
				good_trn += [good_trn1]
			for j in range(0,len(good_trn)):
				a = "abc" + str(j)
				a1 +=[a]


			for i in range(0,len(good_trn)):
				resu_good_trn += [a1[i], good_trn[i]] 
						
							
			good_trn_id = { "_id": goodtrnid }
			good_trn_values = { resu_good_trn[i] : resu_good_trn[i+1] for i in range(0, len(resu_good_trn), 2)}
			good_trn_insert = {**good_trn_id , **good_trn_values}
			collection.insert_one(good_trn_insert)
			bad_trn = []
			bins_bad_trn = []
			resu_bad_trn = []
			a1 =  []
			na1_bad_trn = sheet.cell_value(2,1)
			na_bad_trn= int(na1_bad_trn)
			for row in range(7, na_bad_trn+7):
				bad_trn1 = sheet.cell_value(row,3) 
				bad_trn += [bad_trn1]
			for j in range(0,len(bad_trn)):
				a = "abc" + str(j)
				a1 +=[a]


			for i in range(0,len(bad_trn)):
				resu_bad_trn += [a1[i], bad_trn[i]] 
						
							
						
					
			bad_trn_id = { "_id": badtrnid }
			bad_trn_values = { resu_bad_trn[i] : resu_bad_trn[i+1] for i in range(0, len(resu_bad_trn), 2)}
			bad_trn_insert = {**bad_trn_id , **bad_trn_values}
			collection.insert_one(bad_trn_insert)

			resu_psi_trn = []
			psitrn = [good_trn[i] + bad_trn[i] for i in range(len(good_trn))]
			for i in range(0,len(good_trn)):
				resu_psi_trn += [a1[i], psitrn[i]]


			# b = 'psitrn'
			# a  = (random.randint(1, 20) * 511155008)
			# psiid =  ( str(a) + b )
			psiid=ObjectId()
			psi_id = { "_id": psiid }
			psi_trn_values = { resu_psi_trn[i] : resu_psi_trn[i+1] for i in range(0, len(resu_psi_trn), 2)}
			psi_trn_insert = {**psi_id , **psi_trn_values}
			collection.insert_one(psi_trn_insert)

			bins_oot=[]
			bins_oot1=[]

			resu_oot=[]

			a1 = []

			good_oot = []
			bins_good_oot = []
			resu_good_oot = []
			resu_good_oot = []
			na1_good_oot = sheet.cell_value(2,1)
			na_good_oot= int(na1_good_oot)
			for row in range(7, na_good_oot+7):
				good_oot1 = sheet.cell_value(row,4) 
				good_oot += [good_oot1]
			for j in range(0,len(good_oot)):
				a = "abc" + str(j)
				a1 +=[a]


			for i in range(0,len(good_oot)):
				resu_good_oot += [a1[i], good_oot[i]] 
						
							
			good_oot_id = { "_id": goodootid }
			good_oot_values = { resu_good_oot[i] : resu_good_oot[i+1] for i in range(0, len(resu_good_oot), 2)}
			good_oot_insert = {**good_oot_id , **good_oot_values}
			collection.insert_one(good_oot_insert)
			bad_oot = []
			bins_bad_oot = []
			resu_bad_oot = []
			a1 =  []
			na1_bad_oot = sheet.cell_value(2,1)
			na_bad_oot= int(na1_bad_oot)
			for row in range(7, na_bad_oot+7):
				bad_oot1 = sheet.cell_value(row,5) 
				bad_oot += [bad_oot1]
			for j in range(0,len(bad_oot)):
				a = "abc" + str(j)
				a1 +=[a]


			for i in range(0,len(bad_oot)):
				resu_bad_oot += [a1[i], bad_oot[i]] 
						
							
						
					
			bad_oot_id = { "_id": badootid }
			bad_oot_values = { resu_bad_oot[i] : resu_bad_oot[i+1] for i in range(0, len(resu_bad_oot), 2)}
			bad_oot_insert = {**bad_oot_id , **bad_oot_values}
			collection.insert_one(bad_oot_insert)

			resu_psi_oot = []
			psioot = [good_oot[i] + bad_oot[i] for i in range(len(good_oot))]
			for i in range(0,len(good_oot)):
				resu_psi_oot += [a1[i], psioot[i]]


			# b = 'psioot'
			# a  = (random.randint(1, 20) * 511155008)
			# psiido =  ( str(a) + b )
			psiido=ObjectId()
			psi_id = { "_id": psiido }
			psi_oot_values = { resu_psi_oot[i] : resu_psi_oot[i+1] for i in range(0, len(resu_psi_oot), 2)}
			psi_oot_insert = {**psi_id , **psi_oot_values}
			collection.insert_one(psi_oot_insert)
			trn=[]
					   
			good_trn = []
			a1 = []
			bins_good_trn = []
			resu_good_trn = []
			resu_bins = []
			na1_good_trn = sheet.cell_value(2,1)
			na_good_trn= int(na1_good_trn)
			for row in range(7, na_good_trn+7):
				bins_good_trn1 = sheet.cell_value(row,1)
				bins_good_trn += [bins_good_trn1]
			
			
			for j in range(0,len(bins_good_trn)):
				a = "abc" + str(j)
				a1 +=[a]



			for i in range(0,len(bins_good_trn)):
				resu_bins += [ a1[i], bins_good_trn[i]]


			bins_id = { "_id": binsid }
			bins_values = { resu_bins[i] : resu_bins[i+1] for i in range(0, len(resu_bins), 2)}
			bins_insert = {**bins_id , **bins_values}
			collection.insert_one(bins_insert)

			modelIds={
			"binsid":str(binsid),
			"psitrnid":str(psiid),
			"psiootid":str(psiido),
			"goodtrnid":str(goodtrnid),
			"badtrnid":str(badtrnid),
			"goodootid":str(goodootid),
			"badootid":str(badootid)
			}
			return json.dumps({'status':modelIds,'bins':bins_values,'goodtrn':good_trn_values,'badtrn':bad_trn_values,'goodoot':good_oot_values,'badoot':bad_oot_values})
		else:
			return json.dumps({'status':"no file"})
	else:
		 return render_template("layouts/test.html")

@app.route('/fileDatas',methods=['GET','POST'])
def fileDatas():
	a = int(request.args.get('a', 0))
	b = str(request.args.get('b', 0))
	dri_no = 1 + 7*a
	global file_location
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(1)
	"""psitrnid = int(sheet.cell_value(4,dri_no+5))
	psiootid  = int(sheet.cell_value(4,dri_no+6))"""
	goodtrnid = ObjectId()
	badtrnid = ObjectId()
	goodootid = ObjectId()
	badootid = ObjectId()
	binsid = ObjectId()
	na1_trn = sheet.cell_value(2,dri_no)
	na_trn = int(na1_trn)
	trn=[]
	bins_trn=[]
	bins_trn1=[]

	resu_trn=[]

	a1 = []

	good_trn = []
	bins_good_trn = []
	resu_good_trn = []
	resu_good_trn = []
	na1_good_trn = sheet.cell_value(2,dri_no)
	na_good_trn= int(na1_good_trn)
	for row in range(7, na_good_trn+7):
		good_trn1 = sheet.cell_value(row,dri_no+1) 
		good_trn += [good_trn1]
	for j in range(0,len(good_trn)):
		a = "abc" + str(j)
		a1 +=[a]


	for i in range(0,len(good_trn)):
		resu_good_trn += [a1[i], good_trn[i]] 
				
					
	good_trn_id = { "_id": goodtrnid }
	good_trn_values = { resu_good_trn[i] : resu_good_trn[i+1] for i in range(0, len(resu_good_trn), 2)}
	good_trn_insert = {**good_trn_id , **good_trn_values}
	collection.insert_one(good_trn_insert)
	bad_trn = []
	bins_bad_trn = []
	resu_bad_trn = []
	a1 =  []
	na1_bad_trn = sheet.cell_value(2,dri_no)
	na_bad_trn= int(na1_bad_trn)
	for row in range(7, na_bad_trn+7):
		bad_trn1 = sheet.cell_value(row,dri_no+2) 
		bad_trn += [bad_trn1]
	for j in range(0,len(bad_trn)):
		a = "abc" + str(j)
		a1 +=[a]


	for i in range(0,len(bad_trn)):
		resu_bad_trn += [a1[i], bad_trn[i]] 
				
					
				
			
	bad_trn_id = { "_id": badtrnid }
	bad_trn_values = { resu_bad_trn[i] : resu_bad_trn[i+1] for i in range(0, len(resu_bad_trn), 2)}
	bad_trn_insert = {**bad_trn_id , **bad_trn_values}
	collection.insert_one(bad_trn_insert)

	resu_psi_trn = []
	psitrn = [good_trn[i] + bad_trn[i] for i in range(len(good_trn))]
	for i in range(0,len(good_trn)):
		resu_psi_trn += [a1[i], psitrn[i]]


	# b = 'psitrn'
	# a  = (random.randint(1, 20) * 511155008+dri)
	# psiid =  ( str(a) + b )
	psiid=ObjectId()
	psit_id = { "_id": psiid }
	psi_trn_values = { resu_psi_trn[i] : resu_psi_trn[i+1] for i in range(0, len(resu_psi_trn), 2)}
	psi_trn_insert = {**psit_id , **psi_trn_values}
	collection.insert_one(psi_trn_insert)

	bins_oot=[]
	bins_oot1=[]

	resu_oot=[]

	a1 = []

	good_oot = []
	bins_good_oot = []
	resu_good_oot = []
	resu_good_oot = []
	na1_good_oot = sheet.cell_value(2,dri_no)
	na_good_oot= int(na1_good_oot)
	for row in range(7, na_good_oot+7):
		good_oot1 = sheet.cell_value(row,dri_no+3) 
		good_oot += [good_oot1]
	for j in range(0,len(good_oot)):
		a = "abc" + str(j)
		a1 +=[a]


	for i in range(0,len(good_oot)):
		resu_good_oot += [a1[i], good_oot[i]] 
				
					
	good_oot_id = { "_id": goodootid }
	good_oot_values = { resu_good_oot[i] : resu_good_oot[i+1] for i in range(0, len(resu_good_oot), 2)}
	good_oot_insert = {**good_oot_id , **good_oot_values}
	collection.insert_one(good_oot_insert)
	bad_oot = []
	bins_bad_oot = []
	resu_bad_oot = []
	a1 =  []
	na1_bad_oot = sheet.cell_value(2,dri_no)
	na_bad_oot= int(na1_bad_oot)
	for row in range(7, na_bad_oot+7):
		bad_oot1 = sheet.cell_value(row,dri_no+4) 
		bad_oot += [bad_oot1]
	for j in range(0,len(bad_oot)):
		a = "abc" + str(j)
		a1 +=[a]


	for i in range(0,len(bad_oot)):
		resu_bad_oot += [a1[i], bad_oot[i]] 
				
					
				
			
	bad_oot_id = { "_id": badootid }
	bad_oot_values = { resu_bad_oot[i] : resu_bad_oot[i+1] for i in range(0, len(resu_bad_oot), 2)}
	bad_oot_insert = {**bad_oot_id , **bad_oot_values}
	collection.insert_one(bad_oot_insert)

	resu_psi_oot = []
	psioot = [good_oot[i] + bad_oot[i] for i in range(len(good_oot))]
	for i in range(0,len(good_oot)):
		resu_psi_oot += [a1[i], psioot[i]]


	# b = 'psioot'
	# a  = (random.randint(1, 20) * 511155008)
	# psiido =  ( str(a) + b )
	psiido=ObjectId()
	psio_id = { "_id": psiido }
	psi_oot_values = { resu_psi_oot[i] : resu_psi_oot[i+1] for i in range(0, len(resu_psi_oot), 2)}
	psi_oot_insert = {**psio_id , **psi_oot_values}
	collection.insert_one(psi_oot_insert)

	good_trn = []
	a1 = []
	bins_good_trn = []
	resu_good_trn = []
	resu_bins = []
	na1_good_trn = sheet.cell_value(2,dri_no)
	na_good_trn= int(na1_good_trn)
	for row in range(7, na_good_trn+7):
		bins_good_trn1 = sheet.cell_value(row,dri_no)
		bins_good_trn += [bins_good_trn1]
				
	for j in range(0,len(good_oot)):
		a = "abc" + str(j)
		a1 +=[a]



	for i in range(0,len(bins_good_trn)):
		resu_bins += [ a1[i], bins_good_trn[i]]


	bins_id = { "_id": binsid }
	bins_values = { resu_bins[i] : resu_bins[i+1] for i in range(0, len(resu_bins), 2)}
	bins_insert = {**bins_id , **bins_values}
	collection.insert_one(bins_insert)

	

	driverIds={
		
		"driverNames":b,
		"binsid":str(binsid),
		"psitrnid":str(psiid),
		"psiootid":str(psiido),
		"goodtrnid":str(goodtrnid),
		"badtrnid":str(badtrnid),
		"goodootid":str(goodootid),
		"badootid":str(badootid)
	}
	return json.dumps({'status':driverIds,'bins':bins_values,'goodtrn':good_trn_values,'badtrn':bad_trn_values,'goodoot':good_oot_values,'badoot':bad_oot_values})

@app.route("/index1")
def index1():
	return render_template("layouts/test.html") 

@app.route("/index2")
def index2():
	return render_template("layouts/test1.html") 

@app.route("/index3")
def index3():
	return render_template("layouts/index3.html")

@app.route("/index4")
def index4():
	return render_template("layouts/index4.html") 

@app.route("/index5")
def index5():
	return render_template("layouts/index5.html")   

@app.route("/index6")
def index6():
	return render_template("layouts/index6.html") 
		
@app.route("/api/gini")
def api_info():
	a = request.args.get('a', 0)
	b = request.args.get('b', 0)
	c = request.args.get('c', 0)
	d = request.args.get('d', 0)
	e = request.args.get('e', 0)
	bbins = []
	bins = collection.find_one({"_id": ObjectId(e) })
	for value in bins.values():
				bbins += [value]
				
		
	good_oot_cursors = list(collection.find({"_id":ObjectId(c) }))
	for record in good_oot_cursors:
		ootData = loads(dumps(record))
	good_oot=[]   
	good_oot_cursors1 = collection.find({"_id":ObjectId(c) })
	for x in good_oot_cursors1:
		I = list(x.keys())
		for i  in range(1,len(I)):
			(ootData[I[i]])
			good_oot += [ootData[I[i]]]
	bad_oot_cursors = list(collection.find({"_id":ObjectId(d) }))
	for record in bad_oot_cursors:
		ootData1 = loads(dumps(record))
	bad_oot=[]
	bad_oot_cursors1 = collection.find({"_id":ObjectId(d) })
	for y in bad_oot_cursors1:
		L = list(y.keys())
		for i  in range(1,len(L)):
			(ootData1[L[i]])
			bad_oot += [ootData1[L[i]]]
	total_good_oot = sum(good_oot)
	total_bad_oot = sum(bad_oot)
	cuml_good_oot = ( ( np.cumsum(good_oot, dtype = float) ) / total_good_oot ) * 100
	cuml_bad_oot = ( ( np.cumsum(bad_oot, dtype = float ))/ total_bad_oot)  * 100 
	gi_val1_oot = []
	gi_val2_oot = []
	gi_val_oot =[]
	gi_val_oot =  [ cuml_good_oot [0] ]
	gi_val2_oot = [cuml_good_oot[i] + cuml_good_oot[i+1] for i in range(0,(len(cuml_good_oot))-1 ) ]
	gi_val_oot = gi_val_oot + gi_val2_oot
	bi_val_oot = []
	bi_val2_oot= []
	bi_val_oot =  [ cuml_bad_oot [0] ] 
	bi_val2_oot= [ cuml_bad_oot[i+1] - cuml_bad_oot[i] for i in range(0,(len(cuml_bad_oot))-1 ) ]
	bi_val_oot = bi_val_oot + bi_val2_oot
	gini_nump_oot = [] 
	gini_nump_oot = (( np.multiply(bi_val_oot, gi_val_oot, dtype = float)   / 100) ) 
	gini_nump_oot=np.round(gini_nump_oot,2)
	total=100-np.sum(gini_nump_oot)
	total=np.round(total,2)
	total_oot = { "Total": total }
	b_oot=[]
	for i in range(0,(len(I))-1):
		b_oot += [ bbins[i+1],gini_nump_oot[i]]
	OOTDataValues = { b_oot[i]: b_oot[i+1] for i in range(0,(len(b_oot)), 2)}
	giniOOTData={**total_oot , **OOTDataValues}
	good_trn_cursors = list(collection.find({"_id":ObjectId(a) }))
	for record in good_trn_cursors:
		trnData = loads(dumps(record))
	good_trn=[]   
	good_trn_cursors1 = collection.find({"_id":ObjectId(a) })
	for x in good_trn_cursors1:
		I = list(x.keys())
		for i  in range(1,len(I)):
			(trnData[I[i]])
			good_trn += [trnData[I[i]]]
	bad_trn_cursors = list(collection.find({"_id":ObjectId(b) }))
	for record in bad_trn_cursors:
		trnData1 = loads(dumps(record))
	bad_trn=[]
	bad_trn_cursors1 = collection.find({"_id":ObjectId(b) })
	for y in bad_trn_cursors1:
		L = list(y.keys())
		for i  in range(1,len(L)):
			(trnData1[L[i]])
			bad_trn += [trnData1[L[i]]]
	total_good_trn = sum(good_trn)
	total_bad_trn = sum(bad_trn)
	cuml_good_trn = ( ( np.cumsum(good_trn, dtype = float) ) / total_good_trn ) * 100
	cuml_bad_trn = ( ( np.cumsum(bad_trn, dtype = float ))/ total_bad_trn)  * 100 
	gi_val1_trn = []
	gi_val2_trn = []
	gi_val_trn =[]
	gi_val_trn =  [ cuml_good_trn [0] ]
	gi_val2_trn = [cuml_good_trn[i] + cuml_good_trn[i+1] for i in range(0,(len(cuml_good_trn))-1 ) ]
	gi_val_trn = gi_val_trn + gi_val2_trn
	bi_val_trn = []
	bi_val2_trn= []
	bi_val_trn =  [ cuml_bad_trn [0] ] 
	bi_val2_trn= [ cuml_bad_trn[i+1] - cuml_bad_trn[i] for i in range(0,(len(cuml_bad_trn))-1 ) ]
	bi_val_trn = bi_val_trn + bi_val2_trn
	gini_nump_trn = [] 
	gini_nump_trn = (( np.multiply(bi_val_trn, gi_val_trn, dtype = float)   / 100) ) 
	gini_nump_trn=np.round(gini_nump_trn,2)
	totals=100-np.sum(gini_nump_trn)
	totals=np.round(totals,2)
	total_trn = { "Total": totals }
	b_trn=[]
	for i in range(0,(len(I))-1):
		b_trn += [ bbins[i+1],gini_nump_trn[i]]
	TRNDataValues = { b_trn[i]: b_trn[i+1] for i in range(0,(len(b_trn)), 2)}
	giniTRNData={**total_trn , **TRNDataValues}
	return json.dumps({'TRNValues':giniTRNData,'OOTValues':giniOOTData})

@app.route("/api/ks",methods=['GET','POST'])
def api_ks():
	a = request.args.get('a', 0)
	b = request.args.get('b', 0)
	c = request.args.get('c', 0)
	d = request.args.get('d', 0)
	e = request.args.get('e', 0)

	bbins = []
	bins = collection.find_one({"_id": ObjectId(e) })
	for value in bins.values():
				
				bbins += [value]
	
	good_oot_cursors = list(collection.find({"_id":ObjectId(c) }))
	for record in good_oot_cursors:
		ootData = loads(dumps(record))
	good_oot=[]   
	good_oot_cursors1 = collection.find({"_id":ObjectId(c) })
	for x in good_oot_cursors1:
		I = list(x.keys())
		for i  in range(1,len(I)):
			(ootData[I[i]])
			good_oot += [ootData[I[i]]]
	bad_oot_cursors = list(collection.find({"_id":ObjectId(d) }))
	for record in bad_oot_cursors:
		ootData1 = loads(dumps(record))
	bad_oot=[]
	bad_oot_cursors1 = collection.find({"_id":ObjectId(d) })
	for y in bad_oot_cursors1:
		L = list(y.keys())
		for i  in range(1,len(L)):
			(ootData1[L[i]])
			bad_oot += [ootData1[L[i]]]
	total_good_oot = sum(good_oot)
	total_bad_oot = sum(bad_oot)
	cuml_good_oot = ( ( np.cumsum(good_oot, dtype = float) ) / total_good_oot ) * 100
	cuml_bad_oot = ( ( np.cumsum(bad_oot, dtype = float ))/ total_bad_oot)  * 100 
	Ks_values = []
	for i in cuml_good_oot:
		for i in cuml_bad_oot :
			ks_values_oot = cuml_good_oot - cuml_bad_oot
	ks_value_oot = ks_values_oot[0]
	ks_values_oot=abs(ks_values_oot)
	ks_values_oot=np.round(ks_values_oot,2)
	total=np.max(ks_values_oot)
	total_oot = { "Total": total }
	b_oot=[]
	for i in range(0,(len(I))-1):
		b_oot += [ bbins[i+1],ks_values_oot[i]]
	OOTDataValues = { b_oot[i]: b_oot[i+1] for i in range(0,(len(b_oot)), 2)}
	ksOOTData={**total_oot , **OOTDataValues}
	good_trn_cursors = list(collection.find({"_id":ObjectId(a) }))
	for record in good_trn_cursors:
		trnData = loads(dumps(record))
	good_trn=[]   
	good_trn_cursors1 = collection.find({"_id":ObjectId(a) })
	for x in good_trn_cursors1:
		I = list(x.keys())
		for i  in range(1,len(I)):
			(trnData[I[i]])
			good_trn += [trnData[I[i]]]
	bad_trn_cursors = list(collection.find({"_id":ObjectId(b) }))
	for record in bad_trn_cursors:
		trnData1 = loads(dumps(record))
	bad_trn=[]
	bad_trn_cursors1 = collection.find({"_id":ObjectId(b) })
	for y in bad_trn_cursors1:
		L = list(y.keys())
		for i  in range(1,len(L)):
			(trnData1[L[i]])
			bad_trn += [trnData1[L[i]]]
	total_good_trn = sum(good_trn)
	total_bad_trn = sum(bad_trn)
	cuml_good_trn = ( ( np.cumsum(good_trn, dtype = float) ) / total_good_trn ) * 100
	cuml_bad_trn = ( ( np.cumsum(bad_trn, dtype = float ))/ total_bad_trn)  * 100 
	for i in cuml_good_trn:
		for i in cuml_bad_trn :
			ks_values_trn = cuml_good_trn - cuml_bad_trn
	ks_value_trn = ks_values_trn[0]
	ks_values_trn=abs(ks_values_trn)
	ks_values_trn=np.round(ks_values_trn,2)
	totals=np.max(ks_values_trn)
	total_trn = { "Total": totals }
	b_trn=[]
	for i in range(0,(len(I))-1):
		b_trn += [ bbins[i+1],ks_values_trn[i]]
	TRNDataValues = { b_trn[i]: b_trn[i+1] for i in range(0,(len(b_trn)), 2)}
	ksTRNData={**total_trn , **TRNDataValues}
	return json.dumps({'TRNValues':ksTRNData,'OOTValues':ksOOTData})
	 
@app.route("/api/risk",methods=['GET','POST'])
def api_risk():
	a = request.args.get('a', 0)
	b = request.args.get('b', 0)
	c = request.args.get('c', 0)
	d = request.args.get('d', 0)
	e = request.args.get('e', 0)


	bbins = []
	bins = collection.find_one({"_id": ObjectId(e) })
	for value in bins.values():
				bbins += [value]
	good_oot_cursors = list(collection.find({"_id":ObjectId(c) }))
	for record in good_oot_cursors:
		ootData = loads(dumps(record))
	good_oot=[]   
	good_oot_cursors1 = collection.find({"_id":ObjectId(c) })
	for x in good_oot_cursors1:
		I = list(x.keys())
		for i  in range(1,len(I)):
			(ootData[I[i]])
			good_oot += [ootData[I[i]]]
	bad_oot_cursors = list(collection.find({"_id":ObjectId(d) }))
	for record in bad_oot_cursors:
		ootData1 = loads(dumps(record))
	bad_oot=[]
	bad_oot_cursors1 = collection.find({"_id":ObjectId(d) })
	for y in bad_oot_cursors1:
		L = list(y.keys())
		for i  in range(1,len(L)):
			(ootData1[L[i]])
			bad_oot += [ootData1[L[i]]]
	total_good_oot = sum(good_oot)
	total_bad_oot = sum(bad_oot)
	risk_rank_oot = [] 
	risk_rank_oot = [float(x)/y for x,y in zip(good_oot,bad_oot)]
	risk_rank_oot=np.round(risk_rank_oot,2)
	riskrankoottoal= 0
	for i in range(1,(len(risk_rank_oot)-1)):
		if(risk_rank_oot[i] > risk_rank_oot[i+1]):
			riskrankoottoal = riskrankoottoal+1
	total_oot = { "Total": riskrankoottoal }
	b_oot=[]
	for i in range(0,(len(I))-1):
		b_oot += [ bbins[i+1],risk_rank_oot[i]]
	OOTDataValues = { b_oot[i]: b_oot[i+1] for i in range(0,(len(b_oot)), 2)}
	riskOOTData={**total_oot , **OOTDataValues}
	good_trn_cursors = list(collection.find({"_id":ObjectId(a) }))
	for record in good_trn_cursors:
		trnData = loads(dumps(record))
	good_trn=[]   
	good_trn_cursors1 = collection.find({"_id":ObjectId(a) })
	for x in good_trn_cursors1:
		I = list(x.keys())
		for i  in range(1,len(I)):
			(trnData[I[i]])
			good_trn += [trnData[I[i]]]
	bad_trn_cursors = list(collection.find({"_id":ObjectId(b) }))
	for record in bad_trn_cursors:
		trnData1 = loads(dumps(record))
	bad_trn=[]
	bad_trn_cursors1 = collection.find({"_id":ObjectId(b) })
	for y in bad_trn_cursors1:
		L = list(y.keys())
		for i  in range(1,len(L)):
			(trnData1[L[i]])
			bad_trn += [trnData1[L[i]]]
	total_good_trn = sum(good_trn)
	total_bad_trn = sum(bad_trn)
	risk_rank_trn = [] 
	risk_rank_trn = [float(x)/y for x,y in zip(good_trn,bad_trn)]
	risk_rank_trn=np.round(risk_rank_trn,2)
	riskranktrntotal = 0
	for i in range(1,(len(risk_rank_trn)-1)):
		if(risk_rank_trn[i] > risk_rank_trn[i+1]):
			riskranktrntotal = riskranktrntotal+1
	b_trn=[]
	total_trn = { "Total": riskranktrntotal}
	for i in range(0,(len(I))-1):
		b_trn += [ bbins[i+1],risk_rank_trn[i]]
	TRNDataValues = { b_trn[i]: b_trn[i+1] for i in range(0,(len(b_trn)), 2)}
	riskTRNData={**total_trn , **TRNDataValues}
	return json.dumps({'TRNValues':riskTRNData,'OOTValues':riskOOTData})

@app.route("/api/psi",methods=['GET','POST'])
def api_psi():
	# a = request.args.get('a', 0)
	# b = request.args.get('b', 0)
	# e = int(request.args.get('e', 0))

	# bbins = []
	# bins = collection.find_one({"_id": e})
	# for value in bins.values():
	# 	bbins += [value]
	# oot_cursors = list(collection.find({"_id":b }))
	# for record in oot_cursors:
	# 	ootData = loads(dumps(record))
	# oot=[]   
	# oot_cursors1 = collection.find({"_id":b })
	# for x in oot_cursors1:
	# 	I = list(x.keys())
	# 	for i  in range(1,len(I)):
	# 		(ootData[I[i]])
	# 		oot += [ootData[I[i]]]
	# total_psi_oot=sum(oot)
	# trn_cursors = list(collection.find({"_id":a }))
	# for record in trn_cursors:
	# 	trnData1 = loads(dumps(record))
	# trn=[]
	# trn_cursors1 = collection.find({"_id":a })
	# for y in trn_cursors1:
	# 	L = list(y.keys())
	# 	for i  in range(1,len(L)):
	# 		(trnData1[L[i]])
	# 		trn += [trnData1[L[i]]]
	# total_psi_trn=sum(trn)
	# psi_oot = [(x / total_psi_oot)* 100 for x in oot]
	# psi_trn = [(x / total_psi_trn)* 100 for x in trn]
	# psi_oot=np.round(psi_oot,2)
	# psi_trn=np.round(psi_trn,2)
	# nnew = np.divide(psi_trn,psi_oot)  
	# psi_val1 = np.log(nnew)
	# used = np.subtract(psi_trn, psi_oot)
	# psi = np.multiply(used , psi_val1)
	# total_psi = sum(psi)
	# total_psi=round(total_psi,2)
	# b_oot=[]
	# total_oot = { "Total": total_psi }
	# for i in range(0,(len(I))-1):
	# 	b_oot += [ bbins[i+1],psi_oot[i]]
	# OOTDataValues = { b_oot[i]: b_oot[i+1] for i in range(0,(len(b_oot)), 2)}
	# psiOOTData={**total_oot , **OOTDataValues}
	# b_trn=[]
	# total_trn = { "Total": total_psi }
	# for i in range(0,(len(I))-1):
	# 	b_trn += [ bbins[i+1],psi_trn[i]]
	# TRNDataValues = { b_trn[i]: b_trn[i+1] for i in range(0,(len(b_trn)), 2)}
	# psiTRNData={**total_trn , **TRNDataValues}
	# return json.dumps({'TRNValues':psiTRNData,'OOTValues':psiOOTData})
	a = request.args.get('a', 0)
	b = request.args.get('b', 0)
	e = request.args.get('e', 0)

	bbins = []
	bins = collection.find_one({"_id": ObjectId(e) })
	for value in bins.values():
		bbins += [value]


	
	oot_cursors = list(collection.find({"_id":ObjectId(b) }))
	for record in oot_cursors:
		ootData = loads(dumps(record))
	oot=[]   
	oot_cursors1 = collection.find({"_id":ObjectId(b) })
	for x in oot_cursors1:
		I = list(x.keys())
		for i in range(1,len(I)):
			(ootData[I[i]])
			oot += [ootData[I[i]]]
	total_psi_oot=sum(oot)
	trn_cursors = list(collection.find({"_id":ObjectId(a) }))
	for record in trn_cursors:
		trnData1 = loads(dumps(record))
	trn=[]
	trn_cursors1 = collection.find({"_id":ObjectId(a) })
	for y in trn_cursors1:
		L = list(y.keys())
		for i  in range(1,len(L)):
			(trnData1[L[i]])
			trn += [trnData1[L[i]]]
	total_psi_trn=sum(trn)
	psi_oot = [(x / total_psi_oot)* 100 for x in oot]
	psi_trn = [(x / total_psi_trn)* 100 for x in trn]
	psi_oot=np.round(psi_oot,2)
	psi_trn=np.round(psi_trn,2)
	nnew = np.divide(psi_trn,psi_oot)  
	psi_val1 = np.log(nnew)
	used = np.subtract(psi_trn, psi_oot)
	psi = np.multiply(used , psi_val1)
	total_psi = sum(psi)
	total_psi=np.round(total_psi,2)
	b_oot=[]
	total_oot = { "Total": total_psi }
	for i in range(0,(len(trn))-1):
		b_oot += [ bbins[i+1],psi_oot[i]]
	OOTDataValues = { b_oot[i]: b_oot[i+1] for i in range(0,(len(b_oot)), 2)}
	psiOOTData={**total_oot , **OOTDataValues}
	b_trn=[]
	total_trn = { "Total": total_psi }
	for i in range(0,(len(trn))-1):
		b_trn += [ bbins[i+1],psi_trn[i]]
	TRNDataValues = { b_trn[i]: b_trn[i+1] for i in range(0,(len(b_trn)), 2)}
	psiTRNData={**total_trn , **TRNDataValues}
	return json.dumps({'TRNValues':psiTRNData,'OOTValues':psiOOTData})


@app.route("/api/bad",methods=['GET','POST'])
def api_bad():
	a = request.args.get('a', 0)
	b = request.args.get('b', 0)
	c = request.args.get('c', 0)
	d = request.args.get('d', 0)
	e = request.args.get('e', 0)
	bbins = []
	bins = collection.find_one({"_id": ObjectId(e) })
	for value in bins.values():
				bbins += [value]
	
	
	good_oot_cursors = list(collection.find({"_id":ObjectId(c) }))
	for record in good_oot_cursors:
		ootData = loads(dumps(record))
	good_oot=[]   
	good_oot_cursors1 = collection.find({"_id":ObjectId(c) })
	for x in good_oot_cursors1:
		I = list(x.keys())
		for i  in range(1,len(I)):
			(ootData[I[i]])
			good_oot += [ootData[I[i]]]
	bad_oot_cursors = list(collection.find({"_id":ObjectId(d) }))
	for record in bad_oot_cursors:
		ootData1 = loads(dumps(record))
	bad_oot=[]
	bad_oot_cursors1 = collection.find({"_id":ObjectId(d) })
	for y in bad_oot_cursors1:
		L = list(y.keys())
		for i  in range(1,len(L)):
			(ootData1[L[i]])
			bad_oot += [ootData1[L[i]]]
	total_good_oot = sum(good_oot)
	total_bad_oot = sum(bad_oot)
	bad_rate_oot = [ float (y) / ( x + y) * 100  for x,y in zip(good_oot,bad_oot)]
	bad_rate_oot=np.round(bad_rate_oot,2)
	total=float(total_bad_oot)/(total_good_oot+total_bad_oot) * 100
	total=np.round(total,2)
	total_oot = { "Total": total }
	b_oot=[]
	for i in range(0,(len(I))-1):
		b_oot += [ bbins[i+1],bad_rate_oot[i]]
	OOTDataValues = { b_oot[i]: b_oot[i+1] for i in range(0,(len(b_oot)), 2)}
	badRateOOTData={**total_oot , **OOTDataValues}
	good_trn_cursors = list(collection.find({"_id":ObjectId(a) }))
	for record in good_trn_cursors:
		trnData = loads(dumps(record))
	good_trn=[]   
	good_trn_cursors1 = collection.find({"_id":ObjectId(a) })
	for x in good_trn_cursors1:
		I = list(x.keys())
		for i  in range(1,len(I)):
			(trnData[I[i]])
			good_trn += [trnData[I[i]]]
	bad_trn_cursors = list(collection.find({"_id":ObjectId(b) }))
	for record in bad_trn_cursors:
		trnData1 = loads(dumps(record))
	bad_trn=[]
	bad_trn_cursors1 = collection.find({"_id":ObjectId(b) })
	for y in bad_trn_cursors1:
		L = list(y.keys())
		for i  in range(1,len(L)):
			(trnData1[L[i]])
			bad_trn += [trnData1[L[i]]]
	total_good_trn = sum(good_trn)
	total_bad_trn = sum(bad_trn)
	bad_rate_trn = [ float (y) / ( x + y) * 100  for x,y in zip(good_trn,bad_trn)]
	bad_rate_trn=np.round(bad_rate_trn,2)
	totals=float(total_bad_trn)/(total_good_trn+total_bad_trn) * 100
	totals=np.round(totals,2)
	total_trn = { "Total": totals }
	b_trn=[]
	for i in range(0,(len(I))-1):
		b_trn += [ bbins[i+1],bad_rate_trn[i]]
	TRNDataValues = { b_trn[i]: b_trn[i+1] for i in range(0,(len(b_trn)), 2)}
	badRateTRNData={**total_trn , **TRNDataValues}
	return json.dumps({'TRNValues':badRateTRNData,'OOTValues':badRateOOTData})

@app.route("/api/modelsummary",methods=['GET','POST'])
def api_summary():
	a = request.args.get('a', 0)
	b = request.args.get('b', 0)
	c = request.args.get('c', 0)
	d = request.args.get('d', 0)
	e = request.args.get('e', 0)
	f = request.args.get('f', 0)
	good_oot_cursors = list(collection.find({"_id":ObjectId(c) }))
	for record in good_oot_cursors:
		ootData = loads(dumps(record))
	good_oot=[]   
	good_oot_cursors1 = collection.find({"_id":ObjectId(c) })
	for x in good_oot_cursors1:
		I = list(x.keys())
		for i  in range(1,len(I)):
			(ootData[I[i]])
			good_oot += [ootData[I[i]]]
	bad_oot_cursors = list(collection.find({"_id":ObjectId(d) }))
	for record in bad_oot_cursors:
		ootData1 = loads(dumps(record))
	bad_oot=[]
	bad_oot_cursors1 = collection.find({"_id":ObjectId(d) })
	for y in bad_oot_cursors1:
		L = list(y.keys())
		for i  in range(1,len(L)):
			(ootData1[L[i]])
			bad_oot += [ootData1[L[i]]]
	total_good_oot = sum(good_oot)
	total_bad_oot = sum(bad_oot)
	cuml_good_oot = ( ( np.cumsum(good_oot, dtype = float) ) / total_good_oot ) * 100
	cuml_bad_oot = ( ( np.cumsum(bad_oot, dtype = float ))/ total_bad_oot)  * 100 
	gi_val1_oot = []
	gi_val2_oot = []
	gi_val_oot =[]
	gi_val_oot =  [ cuml_good_oot [0] ]
	gi_val2_oot = [cuml_good_oot[i] + cuml_good_oot[i+1] for i in range(0,(len(cuml_good_oot))-1 ) ]
	gi_val_oot = gi_val_oot + gi_val2_oot
	bi_val_oot = []
	bi_val2_oot= []
	bi_val_oot =  [ cuml_bad_oot [0] ] 
	bi_val2_oot= [ cuml_bad_oot[i+1] - cuml_bad_oot[i] for i in range(0,(len(cuml_bad_oot))-1 ) ]
	bi_val_oot = bi_val_oot + bi_val2_oot
	gini_nump_oot = [] 
	gini_nump_oot = (( np.multiply(bi_val_oot, gi_val_oot, dtype = float)   / 100) ) 
	gini_nump_oot=np.round(gini_nump_oot,2)
	giniOOTTotal=100-np.sum(gini_nump_oot)
	giniOOTTotal=np.round(giniOOTTotal,2)
	good_trn_cursors = list(collection.find({"_id":ObjectId(a) }))
	for record in good_trn_cursors:
		trnData = loads(dumps(record))
	good_trn=[]   
	good_trn_cursors1 = collection.find({"_id":ObjectId(a) })
	for x in good_trn_cursors1:
		I = list(x.keys())
		for i  in range(1,len(I)):
			(trnData[I[i]])
			good_trn += [trnData[I[i]]]
	bad_trn_cursors = list(collection.find({"_id":ObjectId(b) }))
	for record in bad_trn_cursors:
		trnData1 = loads(dumps(record))
	bad_trn=[]
	bad_trn_cursors1 = collection.find({"_id":ObjectId(b) })
	for y in bad_trn_cursors1:
		L = list(y.keys())
		for i  in range(1,len(L)):
			(trnData1[L[i]])
			bad_trn += [trnData1[L[i]]]
	total_good_trn = sum(good_trn)
	total_bad_trn = sum(bad_trn)
	cuml_good_trn = ( ( np.cumsum(good_trn, dtype = float) ) / total_good_trn ) * 100
	cuml_bad_trn = ( ( np.cumsum(bad_trn, dtype = float ))/ total_bad_trn)  * 100 
	gi_val1_trn = []
	gi_val2_trn = []
	gi_val_trn =[]
	gi_val_trn =  [ cuml_good_trn [0] ]
	gi_val2_trn = [cuml_good_trn[i] + cuml_good_trn[i+1] for i in range(0,(len(cuml_good_trn))-1 ) ]
	gi_val_trn = gi_val_trn + gi_val2_trn
	bi_val_trn = []
	bi_val2_trn= []
	bi_val_trn =  [ cuml_bad_trn [0] ] 
	bi_val2_trn= [ cuml_bad_trn[i+1] - cuml_bad_trn[i] for i in range(0,(len(cuml_bad_trn))-1 ) ]
	bi_val_trn = bi_val_trn + bi_val2_trn
	gini_nump_trn = [] 
	gini_nump_trn = (( np.multiply(bi_val_trn, gi_val_trn, dtype = float)   / 100) ) 
	gini_nump_trn=np.round(gini_nump_trn,2)
	giniTRNTotal=100-np.sum(gini_nump_trn)
	giniTRNTotal=np.round(giniTRNTotal,2)
	for i in cuml_good_oot:
		for i in cuml_bad_oot :
			ks_values_oot = cuml_good_oot - cuml_bad_oot
	ks_value_oot = ks_values_oot[0]
	ks_values_oot=abs(ks_values_oot)
	ks_values_oot=np.round(ks_values_oot,2)
	ksOOTTotal=np.max(ks_values_oot)
	for i in cuml_good_trn:
		for i in cuml_bad_trn :
			ks_values_trn = cuml_good_trn - cuml_bad_trn
	ks_value_trn = ks_values_trn[0]
	ks_values_trn=abs(ks_values_trn)
	ks_values_trn=np.round(ks_values_trn,2)
	ksTRNTotal=np.max(ks_values_trn)
	risk_rank_oot = [] 
	risk_rank_oot = [float(x)/y for x,y in zip(good_oot,bad_oot)]
	risk_rank_oot=np.round(risk_rank_oot,2)
	riskrankoottotal= 0
	for i in range(1,(len(risk_rank_oot)-1)):
		if(risk_rank_oot[i] > risk_rank_oot[i+1]):
			riskrankoottotal = riskrankoottotal+1
	risk_rank_trn = [] 
	risk_rank_trn = [float(x)/y for x,y in zip(good_trn,bad_trn)]
	risk_rank_trn=np.round(risk_rank_trn,2)
	riskranktrntotal = 0
	for i in range(1,(len(risk_rank_trn)-1)):
		if(risk_rank_trn[i] > risk_rank_trn[i+1]):
			riskranktrntotal = riskranktrntotal+1
	oot_cursors = list(collection.find({"_id":ObjectId(f) }))
	for record in oot_cursors:
		psiootData = loads(dumps(record))
	oot=[]   
	oot_cursors1 = collection.find({"_id":ObjectId(f) })
	for x in oot_cursors1:
		I = list(x.keys())
		for i  in range(1,len(I)):
			(psiootData[I[i]])
			oot += [psiootData[I[i]]]
	total_psi_oot=sum(oot)
	trn_cursors = list(collection.find({"_id":ObjectId(e) }))
	for record in trn_cursors:
		trnpsiData = loads(dumps(record))
	trn=[]
	trn_cursors1 = collection.find({"_id":ObjectId(e) })
	for y in trn_cursors1:
		L = list(y.keys())
		for i  in range(1,len(L)):
			(trnpsiData[L[i]])
			trn += [trnpsiData[L[i]]]
	total_psi_trn=sum(trn)
	psi_oot = [(x / total_psi_oot)* 100 for x in oot]
	psi_trn = [(x / total_psi_trn)* 100 for x in trn]
	psi_oot=np.round(psi_oot,2)
	psi_trn=np.round(psi_trn,2)
	nnew = np.divide(psi_trn,psi_oot)  
	psi_val1 = np.log(nnew)
	used = np.subtract(psi_trn, psi_oot)
	psi = np.multiply(used , psi_val1)
	total_psi = sum(psi)
	total_psi=np.round(total_psi,2)
	bad_rate_oot = [ float (y) / ( x + y) * 100  for x,y in zip(good_oot,bad_oot)]
	bad_rate_oot=np.round(bad_rate_oot,2)
	badRateTRNTotal=float(total_bad_oot)/(total_good_oot+total_bad_oot) * 100
	badRateTRNTotal=np.round(badRateTRNTotal,2)
	bad_rate_trn = [ float (y) / ( x + y) * 100  for x,y in zip(good_trn,bad_trn)]
	bad_rate_trn=np.round(bad_rate_trn,2)
	badRateOOTTotal=float(total_bad_trn)/(total_good_trn+total_bad_trn) * 100
	badRateOOTTotal=np.round(badRateOOTTotal,2)
	trnTotal={
		'GINI':giniTRNTotal,
		'KS':ksTRNTotal,
		'RISKRANKING':riskranktrntotal,
		'PSI':total_psi,
		'BADRATE':badRateTRNTotal
	}
	ootTotal={
		'GINI':giniOOTTotal,
		'KS':ksOOTTotal,
		'RISKRANKING':riskrankoottotal,
		'PSI':total_psi,
		'BADRATE':badRateOOTTotal
	}
	return json.dumps({"TRNValues": trnTotal,"OOTValues"  : ootTotal})

@app.route("/api/voi",methods=['GET','POST'])
def api_driverpsi():
	a = request.args.get('a', 0)
	b = request.args.get('b', 0)
	c = request.args.get('c', 0)
	d = request.args.get('d', 0)
	e=request.args.get('e',0)
	good_oot_cursors = list(collection.find({"_id":ObjectId(c) }))
	for record in good_oot_cursors:
		ootData = loads(dumps(record))
	good_oot=[]   
	good_oot_cursors1 = collection.find({"_id":ObjectId(c) })
	for x in good_oot_cursors1:
		I = list(x.keys())
		for i  in range(1,len(I)):
			(ootData[I[i]])
			good_oot += [ootData[I[i]]]
	bad_oot_cursors = list(collection.find({"_id":ObjectId(d) }))
	for record in bad_oot_cursors:
		ootData1 = loads(dumps(record))
	bad_oot=[]
	bad_oot_cursors1 = collection.find({"_id":ObjectId(d) })
	for y in bad_oot_cursors1:
		L = list(y.keys())
		for i  in range(1,len(L)):
			(ootData1[L[i]])
			bad_oot += [ootData1[L[i]]]
	total_good_oot = sum(good_oot)
	total_bad_oot = sum(bad_oot)
	voi_good_oot_values = [(x / total_good_oot)* 100 for x in good_oot]
	voi_bad_oot_values1 = [(x / total_bad_oot)* 100 for x in bad_oot]
	voi_oot_values = np.divide(voi_good_oot_values,voi_bad_oot_values1)
	voi_oot_log = np.log(voi_oot_values)
	used = np.subtract(voi_good_oot_values, voi_bad_oot_values1)
	voi_oot = np.multiply(used , voi_oot_log)
	voi_oot=np.round(voi_oot,2)
	total=sum(voi_oot) * 0.01
	total=np.round(total,2)
	total_voi_oot = {"Total":total}
	b_oot=[]
	for i in range(0,(len(I))-1):
		b_oot += [ I[i+1],voi_oot[i]]
	OOTDataValues = { b_oot[i]: b_oot[i+1] for i in range(0,(len(b_oot)), 2)}
	voiOOTData={**total_voi_oot , **OOTDataValues}
	good_trn_cursors = list(collection.find({"_id":ObjectId(a) }))
	for record in good_trn_cursors:
		trnData = loads(dumps(record))
	good_trn=[]   
	good_trn_cursors1 = collection.find({"_id":ObjectId(a) })
	for x in good_trn_cursors1:
		I = list(x.keys())
		for i  in range(1,len(I)):
			(trnData[I[i]])
			good_trn += [trnData[I[i]]]
	bad_trn_cursors = list(collection.find({"_id":ObjectId(b) }))
	for record in bad_trn_cursors:
		trnData1 = loads(dumps(record))
	bad_trn=[]
	bad_trn_cursors1 = collection.find({"_id":ObjectId(b) })
	for y in bad_trn_cursors1:
		L = list(y.keys())
		for i  in range(1,len(L)):
			(trnData1[L[i]])
			bad_trn += [trnData1[L[i]]]
	total_good_trn = sum(good_trn)
	total_bad_trn = sum(bad_trn)
	voi_good_trn_values = [(x / total_good_trn)* 100 for x in good_trn]
	voi_bad_trn_values1 = [(x / total_bad_trn)* 100 for x in bad_trn]
	voi_trn_values = np.divide(voi_good_trn_values,voi_bad_trn_values1)
	voi_trn_log = np.log(voi_trn_values)
	useds = np.subtract(voi_good_trn_values, voi_bad_trn_values1)
	voi_trn = np.multiply(useds, voi_trn_log)
	voi_trn=np.round(voi_trn,2)
	totals=sum(voi_trn) * 0.01
	totals=np.round(totals)
	total_voi_trn = {"Total":totals}
	b_trn=[]
	bbins = []
	bins = collection.find_one({"_id": ObjectId(e) })
	for value in bins.values():
		bbins += [value]
	for i in range(0,(len(I))-1):
		b_trn += [ bbins[i+1],voi_trn[i]]
	TRNDataValues = { b_trn[i]: b_trn[i+1] for i in range(0,(len(b_trn)), 2)}
	voiTRNData={**total_voi_trn , **TRNDataValues}
	return json.dumps({'TRNValues':voiTRNData,'OOTValues':voiOOTData})

@app.route("/api/driversummary",methods=['GET','POST'])
def driver_summary():
	a = request.args.get('a', 0)
	b = request.args.get('b', 0)
	c = request.args.get('c', 0)
	d = request.args.get('d', 0)
	e = request.args.get('e', 0)
	f = request.args.get('f', 0)
	good_oot_cursors = list(collection.find({"_id":ObjectId(c) }))
	for record in good_oot_cursors:
		ootData = loads(dumps(record))
	good_oot=[]   
	good_oot_cursors1 = collection.find({"_id":ObjectId(c) })
	for x in good_oot_cursors1:
		I = list(x.keys())
		for i  in range(1,len(I)):
			(ootData[I[i]])
			good_oot += [ootData[I[i]]]
	bad_oot_cursors = list(collection.find({"_id":ObjectId(d) }))
	for record in bad_oot_cursors:
		ootData1 = loads(dumps(record))
	bad_oot=[]
	bad_oot_cursors1 = collection.find({"_id":ObjectId(d) })
	for y in bad_oot_cursors1:
		L = list(y.keys())
		for i  in range(1,len(L)):
			(ootData1[L[i]])
			bad_oot += [ootData1[L[i]]]
	total_good_oot = sum(good_oot)
	total_bad_oot = sum(bad_oot)
	cuml_good_oot = ( ( np.cumsum(good_oot, dtype = float) ) / total_good_oot ) * 100
	cuml_bad_oot = ( ( np.cumsum(bad_oot, dtype = float ))/ total_bad_oot)  * 100 
	gi_val1_oot = []
	gi_val2_oot = []
	gi_val_oot =[]
	gi_val_oot =  [ cuml_good_oot [0] ]
	gi_val2_oot = [cuml_good_oot[i] + cuml_good_oot[i+1] for i in range(0,(len(cuml_good_oot))-1 ) ]
	gi_val_oot = gi_val_oot + gi_val2_oot
	bi_val_oot = []
	bi_val2_oot= []
	bi_val_oot =  [ cuml_bad_oot [0] ] 
	bi_val2_oot= [ cuml_bad_oot[i+1] - cuml_bad_oot[i] for i in range(0,(len(cuml_bad_oot))-1 ) ]
	bi_val_oot = bi_val_oot + bi_val2_oot
	gini_nump_oot = [] 
	gini_nump_oot = (( np.multiply(bi_val_oot, gi_val_oot, dtype = float)   / 100) ) 
	gini_nump_oot=np.round(gini_nump_oot,2)
	giniOOTTotal=100-np.sum(gini_nump_oot)
	giniOOTTotal=np.round(giniOOTTotal,2)
	good_trn_cursors = list(collection.find({"_id":ObjectId(a) }))
	for record in good_trn_cursors:
		trnData = loads(dumps(record))
	good_trn=[]   
	good_trn_cursors1 = collection.find({"_id":ObjectId(a) })
	for x in good_trn_cursors1:
		I = list(x.keys())
		for i  in range(1,len(I)):
			(trnData[I[i]])
			good_trn += [trnData[I[i]]]
	bad_trn_cursors = list(collection.find({"_id":ObjectId(b) }))
	for record in bad_trn_cursors:
		trnData1 = loads(dumps(record))
	bad_trn=[]
	bad_trn_cursors1 = collection.find({"_id":ObjectId(b) })
	for y in bad_trn_cursors1:
		L = list(y.keys())
		for i  in range(1,len(L)):
			(trnData1[L[i]])
			bad_trn += [trnData1[L[i]]]
	total_good_trn = sum(good_trn)
	total_bad_trn = sum(bad_trn)
	cuml_good_trn = ( ( np.cumsum(good_trn, dtype = float) ) / total_good_trn ) * 100
	cuml_bad_trn = ( ( np.cumsum(bad_trn, dtype = float ))/ total_bad_trn)  * 100 
	gi_val1_trn = []
	gi_val2_trn = []
	gi_val_trn =[]
	gi_val_trn =  [ cuml_good_trn [0] ]
	gi_val2_trn = [cuml_good_trn[i] + cuml_good_trn[i+1] for i in range(0,(len(cuml_good_trn))-1 ) ]
	gi_val_trn = gi_val_trn + gi_val2_trn
	bi_val_trn = []
	bi_val2_trn= []
	bi_val_trn =  [ cuml_bad_trn [0] ] 
	bi_val2_trn= [ cuml_bad_trn[i+1] - cuml_bad_trn[i] for i in range(0,(len(cuml_bad_trn))-1 ) ]
	bi_val_trn = bi_val_trn + bi_val2_trn
	gini_nump_trn = [] 
	gini_nump_trn = (( np.multiply(bi_val_trn, gi_val_trn, dtype = float)   / 100) ) 
	gini_nump_trn=np.round(gini_nump_trn,2)
	giniTRNTotal=100-np.sum(gini_nump_trn)
	giniTRNTotal=np.round(giniTRNTotal,2)
	for i in cuml_good_oot:
		for i in cuml_bad_oot :
			ks_values_oot = cuml_good_oot - cuml_bad_oot
	ks_value_oot = ks_values_oot[0]
	ks_values_oot=abs(ks_values_oot)
	ks_values_oot=np.round(ks_values_oot,2)
	ksOOTTotal=np.max(ks_values_oot)
	for i in cuml_good_trn:
		for i in cuml_bad_trn :
			ks_values_trn = cuml_good_trn - cuml_bad_trn
	ks_value_trn = ks_values_trn[0]
	ks_values_trn=abs(ks_values_trn)
	ks_values_trn=np.round(ks_values_trn,2)
	ksTRNTotal=np.max(ks_values_trn)
	risk_rank_oot = [] 
	risk_rank_oot = [float(x)/y for x,y in zip(good_oot,bad_oot)]
	risk_rank_oot=np.round(risk_rank_oot,2)
	riskrankoottotal= 0
	for i in range(1,(len(risk_rank_oot)-1)):
		if(risk_rank_oot[i] > risk_rank_oot[i+1]):
			riskrankoottotal = riskrankoottotal+1
	risk_rank_trn = [] 
	risk_rank_trn = [float(x)/y for x,y in zip(good_trn,bad_trn)]
	risk_rank_trn=np.round(risk_rank_trn,2)
	riskranktrntotal = 0
	for i in range(1,(len(risk_rank_trn)-1)):
		if(risk_rank_trn[i] > risk_rank_trn[i+1]):
			riskranktrntotal = riskranktrntotal+1
	oot_cursors = list(collection.find({"_id":ObjectId(f) }))
	for record in oot_cursors:
		psiootData = loads(dumps(record))
	oot=[]   
	oot_cursors1 = collection.find({"_id":ObjectId(f) })
	for x in oot_cursors1:
		I = list(x.keys())
		for i  in range(1,len(I)):
			(psiootData[I[i]])
			oot += [psiootData[I[i]]]
	total_psi_oot=sum(oot)
	trn_cursors = list(collection.find({"_id":ObjectId(e) }))
	for record in trn_cursors:
		trnpsiData = loads(dumps(record))
	trn=[]
	trn_cursors1 = collection.find({"_id":ObjectId(e) })
	for y in trn_cursors1:
		L = list(y.keys())
		for i  in range(1,len(L)):
			(trnpsiData[L[i]])
			trn += [trnpsiData[L[i]]]
	total_psi_trn=sum(trn)
	psi_oot = [(x / total_psi_oot)* 100 for x in oot]
	psi_trn = [(x / total_psi_trn)* 100 for x in trn]
	psi_oot=np.round(psi_oot,2)
	psi_trn=np.round(psi_trn,2)
	nnew = np.divide(psi_trn,psi_oot)  
	psi_val1 = np.log(nnew)
	used = np.subtract(psi_trn, psi_oot)
	psi = np.multiply(used , psi_val1)
	total_psi = sum(psi)
	total_psi=np.round(total_psi,2)
	bad_rate_oot = [ float (y) / ( x + y) * 100  for x,y in zip(good_oot,bad_oot)]
	bad_rate_oot=np.round(bad_rate_oot,2)
	badRateTRNTotal=float(total_bad_oot)/(total_good_oot+total_bad_oot) * 100
	badRateTRNTotal=np.round(badRateTRNTotal,2)
	bad_rate_trn = [ float (y) / ( x + y) * 100  for x,y in zip(good_trn,bad_trn)]
	bad_rate_trn=np.round(bad_rate_trn,2)
	badRateOOTTotal=float(total_bad_trn)/(total_good_trn+total_bad_trn) * 100
	badRateOOTTotal=np.round(badRateOOTTotal,2)
	voi_good_oot_values = [(x / total_good_oot)* 100 for x in good_oot]
	voi_bad_oot_values1 = [(x / total_bad_oot)* 100 for x in bad_oot]
	voi_oot_values = np.divide(voi_good_oot_values,voi_bad_oot_values1)
	voi_oot_log = np.log(voi_oot_values)
	used = np.subtract(voi_good_oot_values, voi_bad_oot_values1)
	voi_oot = np.multiply(used , voi_oot_log)
	voi_oot=np.round(voi_oot,2)
	voiTRNtotal=sum(voi_oot) * 0.01
	voiTRNtotal=np.round(voiTRNtotal,2)
	voi_good_trn_values = [(x / total_good_trn)* 100 for x in good_trn]
	voi_bad_trn_values1 = [(x / total_bad_trn)* 100 for x in bad_trn]
	voi_trn_values = np.divide(voi_good_trn_values,voi_bad_trn_values1)
	voi_trn_log = np.log(voi_trn_values)
	useds = np.subtract(voi_good_trn_values, voi_bad_trn_values1)
	voi_trn = np.multiply(useds, voi_trn_log)
	voi_trn=np.round(voi_trn,2)
	voiOOTTotal=sum(voi_trn) * 0.01
	voiOOTTotal=np.round(voiOOTTotal,2)
	trnTotal={
		'GINI':giniTRNTotal,
		'KS':ksTRNTotal,
		'RISKRANKING':riskranktrntotal,
		'PSI':total_psi,
		'BADRATE':badRateTRNTotal,
		'VOI':voiTRNtotal*10
	}
	ootTotal={
		'GINI':giniOOTTotal,
		'KS':ksOOTTotal,
		'RISKRANKING':riskrankoottotal,
		'PSI':total_psi,
		'BADRATE':badRateOOTTotal,
		'VOI':voiOOTTotal*10
	}
	return json.dumps({"TRNValues": trnTotal,"OOTValues"  : ootTotal})



	



	 

 
	 









@app.route("/api/pdo",methods=['GET','POST'])
def api_pdo():
	# global file_location
	file_location = "C:/Users/chand/Downloads/ready.xlsx"
	workbook = xlrd.open_workbook(file_location)
	sheet3 = workbook.sheet_by_index(2)
	oot = []
	amean = []
	meean = []
	for row in range(1,6):
		mean1 = sheet3.cell_value(row,4)
		meean += [mean1]
			
		
	
	good = []

	for row in range(1,6):
		good1 = sheet3.cell_value(row,5)    
		good += [good1]        
	bad = []
	for row in range(1,6):
		bad1 = sheet3.cell_value(row,6)    
		bad += [bad1]    

	bad_rate = []
	log_bad = []
	loglist = []
	for i in range(0,len(good)):
		bad_rate += [good[i] / bad[i]]
	loglist  = [math.log(i) for i in bad_rate]


	arrmean = np.array(meean)
	lloglist = np.array(loglist)

	arrmean = arrmean.reshape(-1,1)

	model = LinearRegression()
	model.fit(arrmean,lloglist)
	model = LinearRegression().fit(arrmean, lloglist)

	intercept = model.intercept_
	intercept=np.round(intercept,2)
	slope =  model.coef_
	slope=np.round(slope,2)

	pdo_calib = 20

	pd_obs = math.log(2)/ (model.coef_)

	pdo_val = (pd_obs - pdo_calib) / (pdo_calib)
	pdo_val=np.round(pdo_val,2)

	return json.dumps({"Intercept":intercept,"Slope":slope[0],"PDOVal":pdo_val[0]})


	



	 

 
	 













