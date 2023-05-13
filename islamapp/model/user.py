import sqlalchemy as sa
from database import db
import json

class User(db.Model):
    __tablename__ = "user"
    user_id = sa.Column(sa.String(32), primary_key=True)
    account = sa.Column(sa.String(320), unique=True, nullable=False)
    password = sa.Column(sa.CHAR(60), nullable=False)
    cookie = sa.Column(sa.JSON, nullable=True)
    def to_json(self):
        return {
            "user_id": self.user_id,
            "account": self.account,
        }
    def set_cookie(self, cookie_dict):
        self.cookie = json.dumps(cookie_dict)  # 將字典轉為 JSON 字串

    def get_cookie(self):
        return json.loads(self.cookie) if self.cookie else None  # 若欄位為空則回傳 None