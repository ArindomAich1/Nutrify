from flask import render_template, request, url_for
from main import app, db
from main.models import foodData, admin

DataList= []

@app.route("/", methods=['GET','POST'])
def homepage():
    foodTable= foodData.query.all()

    return render_template('index.html', foodTable= foodTable)


@app.route("/submit", methods=['GET', 'POST'])
def amountSelection():
    vegList= []
    foodTable= foodData.query.all()
    if request.method == 'POST':
        
        item=request.form.getlist('veggie')
        print(item)
        for i in item:
            for j in foodTable:
                if int(i)== j.id:
                    vegList.append(j.foodName)
    global DataList
    DataList= vegList
    print(DataList)
    return render_template('ammountSelection.html', list=vegList)

@app.route("/result", methods=['GET','POST'])
def result():
    ammount=[]
    index= 1
    print(str(index))
    print('vegList')
    print(DataList)
    if request.method== 'POST':
        for item in DataList:
            amnt= request.form.get(str(index))
            if not amnt:
                return 'amnt none'
            amnt= float(amnt)/100
            amnt= round(amnt, 3)
            ammount.append(amnt)
            index=index+1
        
        print(DataList)
        print(ammount)
        fats = 0
        carbs = 0
        protein = 0
        energy = 0
        index=0
        foodTable= foodData.query.all()
        for item in DataList:
            for food in foodTable:
                if food.foodName == item:
                    fats= fats+food.fats*ammount[index]
                    carbs= carbs+food.carbs*ammount[index]
                    protein= protein+food.protein*ammount[index]
                    energy= energy+ food.energy*ammount[index]
            
            index= index+1
        fats=round(fats,3)
        carbs=round(carbs,3)
        protein=round(protein,3)
        energy=round(energy,3)
        return render_template('result.html',fats=fats,carbs=carbs, protein=protein,energy=energy, DataList=DataList, ammount=ammount)
    return render_template('result.html',fats=fats,carbs=carbs, protein=protein,energy=energy)
        


@app.route("/admin", methods=['GET','POST'])
def login():
    return render_template('admin.html')

@app.route('/adminAddItem', methods=['GET', 'POST'])

def addItem():
    admin_list= admin.query.all()
    if request.method== 'POST':
        username= request.form.get('username')
        password= request.form.get('password')

        for admin_detail in admin_list:
            if username== admin_detail.username and password== admin_detail.password:
                return render_template('adminAddItem.html')
        return 'invalid username/password'
    return 'you are not logged in'


@app.route("/itemAdded", methods= ['GET','POST'])

def itemAdded():
    if request.method == 'POST':
        foodName=request.form.get('name')
        carbs=request.form.get('carbs')
        protein=request.form.get('protein')
        fats=request.form.get('fat')
        energy=request.form.get('energy')

        newFood= foodData(foodName=foodName, carbs=carbs, protein=protein, fats=fats, energy=energy )
        
        db.session.add(newFood)
        db.session.commit()

        return render_template('adminAddItem.html')
    return 'you are not logged in'




    


