# app-pacakage  2ci obyekt
# run etmek ucun

from app import app

if __name__=='__main__':
    app.run(debug=True)
 
from main.routes import*
from admin.routes import*