from flask import Flask,render_template,request
import requests

api_key = "82b89db7b606a9d2b46f5edfda00f555"
url = "http://data.fixer.io/api/latest?access_key=" + api_key

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def fixer():
    if request.method == "POST":
        firstcurrency = request.form.get("firstCurrency") # USD
        secondcurrency = request.form.get("secondCurrency") # TRY
        amount = request.form.get("amount") # 15

        response = requests.get(url)
        app.logger.info(response)

        infos = response.json()
        app.logger.info(infos)

        firstvalue = infos["rates"][firstcurrency] # 1.18582
        secondvalue = infos["rates"][secondcurrency] # 9.290177
        result = (secondvalue/firstvalue)*float(amount)

        currencyinfo = {
            "firstcurrency":firstcurrency,
            "secondcurrency":secondcurrency,
            "amount":amount,
            "result":result
        }
         
        return render_template("index.html",info = currencyinfo)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

