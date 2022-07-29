from flask_restful import Resource

from models.family_mart import FamilyMartModel


class FamilyMart(Resource):
    def get(self, name):
        item = FamilyMartModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'Store not found.'}, 404