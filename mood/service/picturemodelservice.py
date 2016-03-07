__author__ = 'Andre Pires'

from mood.model.models import Picture
from mood.settings import const

class PictureModelService(object):

    const.UID = "uid"
    const.MONGODB_ID = "_id"

    def find_by_key(self, uid):
        pictures = self.get_pictures_collection()
        obj = pictures.find_one({const.UID: uid})
        if obj is None:
            return None
        ## removing '_id' from the object, otherwise jsonobject will fail to deserialize
        del obj[const.MONGODB_ID]
        pic = Picture(obj)
        return pic

    def delete(self, uid):
        pictures = self.get_pictures_collection()
        result = pictures.delete_one({const.UID: uid})
        return result.deleted_count

    def save(self, picture):
        pictures = self.get_pictures_collection()
        obj = picture.to_json()
        result = pictures.update_one({"uid": picture.uid}, {"$set": obj}, upsert=True)
        return result.modified_count

    def get_pictures_collection(self):
        return const.db.pictures



