from flask import abort, jsonify
from flask_restful import Resource, reqparse
from flask_simplelogin import login_required

from sample_auth.models import Product
from sample_auth.ext.database import db


class ProductResource(Resource):

    def get(self):
        products = Product.query.all() or abort(204)
        return jsonify(
            {"products": [product.to_dict() for product in products]}
        )

    def post(self):
        """
        Creates a new product.

        Only admin user authenticated using basic auth can post
        Basic takes base64 encoded username:password.

        curl -XPOST localhost:5000/api/v1/product/ \
         -H "Authorization: Basic YWRtaW46MTIzNAo" \
         -H "Content-Type: application/json" \
         -d '{"name":"Rye", "price":5, "description":"This bread has a grain with strong flavor"}'
        """
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('price', type=float)
        parser.add_argument('description', type=str)
        args = parser.parse_args()
        new_product = Product(name=args['name'], price=args['price'], description=args['description'])
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()) if new_product else abort(500)

class ProductItemResource(Resource):
    def get(self, product_id):
        product = Product.query.filter_by(id=product_id).first() or abort(404)
        return jsonify(product.to_dict())
