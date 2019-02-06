from project import db


class DbOperations:
    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        print(type(obj))
        db.session.add(obj)
        db.session.commit()
        return obj

    @classmethod
    def findByParameter(cls, **kwargs):
        obj = cls(**kwargs)
        pass

    @classmethod
    def findAll(cls, **kwargs):
        pass

    @classmethod
    def update(cls,**kwargs):
        pass

    @classmethod
    def delete(cls,**kwargs):
        pass