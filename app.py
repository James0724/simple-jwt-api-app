#Imports 
import os
from flask import Flask, request
import jwt

JWT_SECRECT = os.environ.get('JWT_SECRECT', 'super1234')


app = Flask(__name__)


# Controllers
@app.route('/')
def index():
  return 'Healthy'

@app.route('/auth', methods=['POST'])
def auth():
  body = request.get_json()

  email = body['email']
  return jwt.encode({'email':email}, JWT_SECRECT)

# Show Venue Details
@app.route('/content', methods=['GET'])
def content():
  headers = request.headers #header set to contain token from auth route
  auth = headers['Authorization'] #authorization should contain prefix bearer
  parts = auth.split()
  token = parts[1]
  return jwt.decode(token, JWT_SECRECT, algorithms=['HS256'])


#Error Handler

@app.errorhandler(404)
def not_found_error(error):
    return 'errors/not found'

#Launch

if __name__ == '__main__':
  app.run(host='0.0.0.0')



