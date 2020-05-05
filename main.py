from flask import Flask,render_template,redirect,request
import tempsens

app = Flask(__name__)

@app.route("/",methods = ["GET"])
def index():
	return render_template('index.html')

@app.route("/submit",methods=['POST'])
def submit(): 
	data = request.form
	print(data['low'],data['up'],end='\n')
	tempsens.highbound=float(data['up'])
	tempsens.lowbound=float(data['low'])
	tempsens.flag=0
	#print(f"up===>{request.form.get('up')}",end='\n')
	return render_template("show.html",data=data)

@app.route("/submit2",methods=['POST'])
def submit2():
	data2=request.form
	print(data2['quantity'])
	tempsens.flag=1
	return render_template("show2.html",data=data2)



if(__name__=='__main__'):
	app.run(port='7000')
	print(tempsens.flag)
	#tempsens.flag=int(input("Press 0 for static OR 1 for Dynamic : "))
	#tempsens.activate()

    