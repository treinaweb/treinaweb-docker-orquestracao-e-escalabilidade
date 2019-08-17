from app import app

# Generate a randon key for csrf
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True)