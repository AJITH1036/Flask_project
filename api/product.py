
from flask_restful import Resource,request
from flask_sqlalchemy import SQLAlchemy
from app import db
from models import productModel


class Products(Resource):
    response = {"status": 400, "message": "product not created", "data":"No data"}

    def post(self):
        product_data = request.get_json()
        name = product_data["name"]
        price = product_data["price"]
        description = product_data["description"]
        product = productModel.Products(name = name,price = price, description = description)
        db.session.add(product)
        db.session.commit()
        self.response["status"] = 201
        self.response["message"] = "product created successfully"
        self.response["data"] = product_data
        return self.response, 201

    def get(self):
        Products = productModel.Products.query.all()
        if Products:
            all_products =[]
            for product in Products:
                product_list = {
                    "id":product.id,
                    "name":product.name,
                    "description":product.description,
                    "price":product.price
                }
                all_products.append(product_list)
            self.response["status"] = 200
            self.response["message"] = "Products list fetched successfuly"
            self.response["data"] = all_products
            return self.response,200
        else:
            return self.response,404


     
class EditProducts(Resource): 


    response = {"status": 400, "message": "Incorrect product id", "data":"No data"}

    def get(self,pid):
        product = productModel.Products.query.filter_by(id = pid).first()
        if product:
                product_list = {
                    "id":product.id,
                    "name":product.name,
                    "description":product.description,
                    "price":product.price
                }
                self.response["status"] = 200
                self.response["message"] = "Products details fetched successfuly"
                self.response["data"] = product_list
                return self.response,200
        else:
            return self.response,404

    def put(self,pid):
        product = productModel.Products.query.filter_by(id=pid).first()
        if product:
            product_data = request.get_json()
            name = product_data["name"]
            price = product_data["price"]
            description = product_data["description"]
            product.name = name
            product.description = description
            product.price = price
            db.session.commit()
            self.response["status"] = 201
            self.response["message"] = "product Updated successfully"
            self.response["data"] = product_data
            return self.response, 201
        else:
            return self.response,404


    def delete(self,pid):
        product = productModel.Products.query.filter_by(id=pid).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            self.response["status"] = 201
            self.response["message"] = "product Deleted successfully"
            self.response["data"] = f"pid {pid} deleted "
            return self.response, 201
        else:
            return self.response,404
