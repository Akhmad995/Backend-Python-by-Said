from flask import Flask
from flask import render_template


app = Flask(__name__) # Создается объект приложения


@app.route("/")
def index():

  params = {}
  params['name'] = 'Zaga'
  params['surname'] = 'Baga'

  return render_template("home.html", params = params)
    


@app.route("/about")
def about():
    staff = ['Магомед', 'Патимат', 'Сидредин']
    #staff = []
    return render_template("about.html", staff = staff)


@app.route("/shop")
def products():
    products = [
        {
            "name" : "iphone 10",
            "price" : "10 000",
        },
        {
            "name" : "iphone 11",
            "price" : "11 000",
        },
        {
            "name" : "iphone 12",
            "price" : "12 000",
        },
        {
            "name" : "iphone 13",
            "price" : "13 000",
        },
        {
            "name" : "iphone 14",
            "price" : "14 000",
        },
        {
            "name" : "iphone 15",
            "price" : "15 000",
        },
    ]
    
    return render_template("products.html", products = products)



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)

