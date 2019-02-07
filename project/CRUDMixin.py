from project import db


class CRUDMixin:
    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        print('create')
        print(type(obj))
        print(kwargs)
        db.session.add(obj)
        db.session.commit()
        return obj

    @classmethod
    def find_all(cls, **kwargs):
        obj = cls(**kwargs)
        return obj.query.all()

    @classmethod
    def find_by_parameter(cls, **kwargs):
        obj = cls(**kwargs)
        print('findByParameter')
        print(type(obj))
        print(obj)
        print(kwargs)
        print(kwargs.get('email'))
        print(kwargs.get('passwd'))
        print(obj.query.filter_by(**kwargs))
        return obj.query.filter_by(**kwargs)

    @classmethod
    def update(cls, **kwargs):
        pass

    @classmethod
    def delete(cls, **kwargs):
        pass
