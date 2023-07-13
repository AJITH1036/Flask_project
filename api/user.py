
from flask_restful import Resource,request
from flask_sqlalchemy import SQLAlchemy
from app import db
from models import userModel


class User(Resource):
    response = {"status": 400, "message": "User not created", "data":"No data"}

    def post(self):
        user_data = request.get_json()
        name = user_data["name"]
        phone = user_data["phone"]
        email = user_data["email"]
        user = userModel.Users(name = name,phone = phone, email = email)
        db.session.add(user)
        db.session.commit()
        self.response["status"] = 201
        self.response["message"] = "User created successfully"
        self.response["data"] = user_data
        return self.response, 201

    def get(self):
        users = userModel.Users.query.all()
        if users:
            all_users =[]
            for user in users:
                user_list = {
                    "id":user.id,
                    "name":user.name,
                    "email":user.email,
                    "phone":user.phone
                }
                all_users.append(user_list)
            self.response["status"] = 200
            self.response["message"] = "Users list fetched successfuly"
            self.response["data"] = all_users
            return self.response,200
        else:
            return self.response,404


     
class UserEdit(Resource): 


    response = {"status": 400, "message": "Incorrect user id", "data":"No data"}

    def get(self,user_id):
        user = userModel.Users.query.filter_by(id = user_id).first()
        if user:
                user_list = {
                    "id":user.id,
                    "name":user.name,
                    "email":user.email,
                    "phone":user.phone
                }
                self.response["status"] = 200
                self.response["message"] = "Users details fetched successfuly"
                self.response["data"] = user_list
                return self.response,200
        else:
            return self.response,404

    def put(self,user_id):
        user = userModel.Users.query.filter_by(id=user_id).first()
        if user:
            user_data = request.get_json()
            name = user_data["name"]
            phone = user_data["phone"]
            email = user_data["email"]
            user.name = name
            user.email = email
            user.phone = phone
            db.session.commit()
            self.response["status"] = 201
            self.response["message"] = "User Updated successfully"
            self.response["data"] = user_data
            return self.response, 201
        else:
            return self.response,404


    def delete(self,user_id):
        user = userModel.Users.query.filter_by(id=user_id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            self.response["status"] = 201
            self.response["message"] = "User Deleted successfully"
            self.response["data"] = f"user_id {user_id} deleted "
            return self.response, 201
        else:
            return self.response,404
