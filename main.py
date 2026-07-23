from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/bilgiler")
def bilgi():
    bilgiler = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.","2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.","2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor."]
    return '<p>' + random.choice(bilgiler) + '</p>'
app.run(debug=True)

@app.route("/secret")
def secret_page():
  return "Burası gizli sayfa!"
if __name__ == "__main__":
app.run(debug=True)
