#importamos las clases y los metodos
from flask import Flask,render_template,redirect,request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/',methods=['GET','POST'])
def aritmetica():
    if request.method =="POST":
        #valores que recibo del form n1,n2 son pasados
        num1=float(request.form.get('n1'))
        num2=float(request.form.get('n2'))
        #realizamos las operaciones
        suma=num1+num2
        resta=num1-num2
        multiplicacion=num1*num2
        division=num1/num2
        return render_template('index.html',total_suma=suma,
                                            total_resta=resta,
                                            total_multiplicacion=multiplicacion,
                                            total_division=division)
    return render_template('index.html')

@app.route('/divisa',methods=['GET','POST'])
def conversion():
    if request.method =="POST":
        #valores que recibo del form n son pasados
        n=float(request.form.get('n'))
        #realizamos las operaciones
        divisa=n/4212 
        divisas=round(divisa,2)
        mexico=n*0.0046
        return render_template('divisa.html',total_divisa=divisas,
                                            total_mexico=mexico)
    
    return render_template('divisa.html')
    
@app.route('/longitudes',methods=['GET','POST'])
def conver():
    if request.method =="POST":
        #valores que recibo del form n son pasados
        valor=float(request.form.get('v'))
        #realizamos las operaciones
        hectómetro=valor*10
        decámetro=valor*100
        metro=valor*1000
        decímetro=valor*10000
        centimetro=valor*100000
        milimetro=valor*1000000
        return render_template('longitudes.html',total_hectometro=hectómetro,
                                                total_decametro=decámetro,
                                                total_metro=metro,
                                                total_decimetro=decímetro,
                                                total_centimetro=centimetro,
                                                total_milimetro=milimetro)
    
    return render_template('longitudes.html')

 

if __name__ == "__main__":
   app.run(debug=True)
