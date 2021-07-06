#! /Users/mohds/anaconda3/python.exe
import cgi
import subprocess as sp
print("content-type: text/html\r\n")

f=cgi.FieldStorage()
cmd = f.getvalue("x")

if cmd == "MH12DE1433":
	print('''
	<pre>
	Car Model: Ford Figo	
	Registration Name: Nikhil Tiwari
    Registration Number: HJk452XXXXXXX
	Registration Date: 27/8/2015
	Fuel Type: Petrol
	Location: Maharashtra, India
	Vehicle Class: Sedan
	Insurance Upto: 26/8/2025
	</pre>''')
elif cmd == "HR26DK8337":
	print('''<pre>
	Car Model: Maruti Suzuki Swift	
	Registration Name: Ashish Shukla
    Registration Number: KL234H2XXXXXXX
	Registration Date: 7/9/2016
	Fuel Type: Petrol
	Location: Haryana, India
	Vehicle Class: Sedan
	Insurance Upto: 6/9/2026
	</pre>''')

elif cmd == "H982 FKL":
	print('''<pre>
	Car Model: Mercedes GLA 250
	Registration Name: Shreyansh Singh
    Registration Number: UIVBN3XXXXXXX
	Registration Date: 20/5/2019
	Fuel Type: Petrol
	Location: Noida Uttar Pradesh, India
	Vehicle Class: SUV
	Insurance Upto: 19/5/2029
	</pre>''')
