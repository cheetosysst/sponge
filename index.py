import sys
import os
import re
import json
from tabula import read_pdf
from datetime import datetime

files=[]

if len(sys.argv)<=2:
	print("Not enough arguments. Please specify input files")

skip=False
for (idx, arg) in enumerate(sys.argv):
	if skip:
		skip=False
		continue
	if arg=="-t" or arg=="-s":
		filename = sys.argv[idx+1]
		if not os.path.exists(filename):
			print("ERROR: \"{}\" does not exist, Aborting.".format(filename))
			exit()
		files.append({
			'path': filename,
			'type': "truefalse" if arg=='-t' else "selection" if arg=='-s' else ""
		})
		skip=True
		continue

reIndex = re.compile(r'[0-9]{3}')
def parseTrueFalse(raw:str,start:int):
	data=[]
	for page in raw:
		for section in page['data']:
			if not reIndex.match(section[0]['text']): continue
			data.append({
				"id": int(section[0]['text']) if start==0 else start+int(section[0]['text'])+2,
				"question": section[2]['text'].replace("\\r", "").strip(),
				"type": "truefalse",
				"options": [],
				"asset": [],
				"answer": True if section[2]['text']=='○' else False
			})
	return data

def parseSelection(raw:str,start:int):
	data=[]
	for page in raw:
		for section in page['data']:
			if not reIndex.match(section[0]['text']): continue
			content=section[2]['text'].replace("\\r","")
			data.append({
				"id": int(section[0]['text']) if start==0 else start+int(section[0]['text'])+2,
				"question": re.sub(r'\(\d+\)[^（]*', '', content).strip(),
				"type": "selection",
				"options": re.findall(r'\(\d\)(.*?)(?=\(\d\)|\。)', content),
				"asset": [],
				"answer": int(section[1]['text'])
			})
	return data

data = []
for (idx, item) in enumerate(files):
	raw=read_pdf(
		item["path"],
		guess=False,
		pages="all",
		encoding="utf-8",
		output_format="json",
	)
	if item["type"]=="truefalse":
		# print("tf len={} {}".format(len(data),item['path']))
		data=data+parseTrueFalse(raw, len(data))
	elif item['type']=="selection":
		# print("sl len={} {}".format(len(data),item['path']))
		data=data+parseSelection(raw, len(data))
	# print(json.dumps(data, ensure_ascii=False).replace("\\r",""))

# text=json.dumps(data, ensure_ascii=False).replace("\\r","")
# print('{"name":"","update":"{}",question:{}'.format(datetime.now().isoformat(), text))

text = json.dumps({
	'name': "",
	'update': datetime.now().isoformat(),
	'questions': data
}, ensure_ascii=False).replace('//r',"")
print(text)