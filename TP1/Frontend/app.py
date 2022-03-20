from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
if __name__ == '__main__':
	app.run(port=os.getenv("PORT"),debug = True)
#Messi
#asdkfl;a;lksfdas
