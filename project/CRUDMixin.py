from project import db


class CRUDMixin:
    @classmethod
    def save(cls, **kwargs):
        obj = cls(**kwargs)
        db.session.add(obj)
        db.session.commit()
        return obj

    @classmethod
    def update(cls, **kwargs):
        obj = cls(**kwargs)
        db.session.commit()
        return obj
