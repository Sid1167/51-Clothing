from flask import Flask,render_template,request
from flask import request,url_for,redirect
import database as db
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route("/contactus")
def contactus():
    return render_template('contactus.html')

@app.route("/clist")
def clist():
    clothinglist = db.getall()
    return render_template("clist.html",clothinglist=clothinglist)

@app.route("/addclothing",methods=['GET','POST'])
def addclothing():
    if request.method=='GET':
        return render_template('addclothing.html')
    elif request.method=='POST':
        cname = request.form['clothingName']
        cprice = request.form['clothingPrice']
        pdes = request.form['clothingDescription']
        db.insert(cname,cprice,pdes)
        return redirect(url_for('clist'))

@app.route("/deleteclothing/<int:id>",methods=['POST','GET'])
def deleteclothing(id):
    if request.method=='GET':
        clothing = db.searchbyId(id)
        return render_template('confirm.html',clothing=clothing)
    elif request.method=='POST':
        db.delete(id)
        return redirect(url_for('clist'))

@app.route("/updateclothing/<int:id>",methods=['GET','POST'])
def updtateclothing(id):
    if request.method=='GET':
        clothing = db.searchbyId(id)
        return render_template('updateclothing.html',clothing=clothing)
    elif request.method=='POST':
        cid = request.form['clothingId']
        cname = request.form['clothingName']
        cprice = request.form['clothingPrice']
        cdes = request.form['clothingDescription']
        db.update(cid,cname,cprice,cdes)
        return redirect(url_for('clist'))

@app.route("/sortbyname")
def sortname():
    clothinglist = db.sortbyName()
    return render_template("sortbyname.html",clothinglist=clothinglist)
    
@app.route("/sortbynamedesc")
def sortbynamedesc():
    clothinglist = list(db.getall())
    clothinglist.sort(key=lambda t:t[1],reverse=True)
    return render_template("clist.html",clothinglist=clothinglist)

@app.route("/sortbyprice")
def sortprice():
    clothinglist = db.sortbyPrice()
    return render_template("clist.html",clothinglist=clothinglist)
@app.route("/sortbypricedesc")
def sortbypricedesc():
    clothinglist = list(db.getall())
    
    clothinglist.sort(key=lambda t:t[2],reverse=True)
    return render_template("clist.html",clothinglist=clothinglist)

@app.route("/search")
def search():
    searchby = request.args['searchby']
    if searchby =='id':
        id = eval(request.args['query'])
        clothinglist = db.searchbyId(id)
    else:
        name = request.args['query']
        clothinglist = db.searchbyName(name)
    return render_template("clist.html",clothinglist=clothinglist)
        


if __name__=='__main__':
    app.run(debug=True)