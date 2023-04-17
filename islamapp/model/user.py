import sqlalchemy as sa
from database import db


class User(db.Model):
    __tablename__ = "user"
    user_id = sa.Column(sa.String(32), primary_key=True)
    account = sa.Column(sa.String(320), unique=True, nullable=False)
    password = sa.Column(sa.CHAR(60), nullable=False)

    def to_json(self):
        return {
            "user_id": self.user_id,
            "account": self.account,
        }