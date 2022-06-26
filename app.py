from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys


app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing exception module")
    except Exception as e:
        housing = HousingException(e,sys)
        #raise HousingException(e,sys) from e 
        logging.info(housing.error_message)    
        logging.info("we are testing logging module")
    return "starting the machine learning project"

if __name__=="__main__":
    app.run(debug=True)
