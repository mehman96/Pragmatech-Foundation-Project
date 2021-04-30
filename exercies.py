# render-template folder icinde olan file
from flask import flask,render_template

app=flask(__name__)

# hazir decorator app adinda
# index metodun return alir ekrana yazir.yeni yazilan datani goturb @app.routa gonderir 
@app.route('/')   
def index():
  return render_template('inedx.html')
#  only string 1

# __name__ -special varilibles
# application baslangic noqtesi 
# eger uzerinde isdeyim aktiv modulsa run ele sert budu
  if __name__=='__main__': 
      app.run(debug=True)
