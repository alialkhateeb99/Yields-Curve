import os
from flask import Flask, render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import openpyxl
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'

db = SQLAlchemy(app)
ma = Marshmallow(app)

class TodoModel(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.String, nullable=False)
    item = db.Column(db.String(80), nullable=False)
    value = db.Column(db.Float, nullable=False)

    def __str__(self):
        return f'{self.date}, {self.item},{self.value}, {self.id}'

class TodoModelSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = ("id","date","item","value")


@app.route('/values',methods=['GET'])
def index():
    queries = TodoModel.query.all()
    user_schema = TodoModelSchema(many=True)
    output = user_schema.dump(queries)
    
    #return render_template('index.html', queries=queries)
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
    