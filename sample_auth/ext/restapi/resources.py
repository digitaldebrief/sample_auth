from flask import abort, jsonify
from flask_restful import Resource
from flask_simplelogin import login_required

from sample_auth.models import Product


class ProductResource(Resource):
    def get(self):
        products = Product.query.all() or abort(204)
        return jsonify(
            {"products": [product.to_dict() for product in products]}
        )

    @login_required(basic=True, username="admin")
    def post(self):
        """
        Creates a new product.

        Only admin user authenticated using basic auth can post
        Basic takes base64 encoded username:password.

        # curl -XPOST localhost:5000/api/v1/product/ \
        #  -H "Authorization: Basic YWRtaW46MTIzNAo" \
        #  -H "Content-Type: application/json"
        #  -d "{'name':'my_awesome_product', 'price':5, 'description':'Mindblowing awesomeness'}"
        """
        return NotImplementedError(
            "Someone please complete this example and send a PR :)"
        )


class ProductItemResource(Resource):
    def get(self, product_id):
        product = Product.query.filter_by(id=product_id).first() or abort(404)
        return jsonify(product.to_dict())
