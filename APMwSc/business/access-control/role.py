from sqlalchemy.sql.schema import PrimaryKeyConstraint
class clsRole(db.Model):
    __tablename__ = 'role'
    namerole = db.column(db.string(50),         unique=False )
    idrole   = db.column(db.Integer   ,primary_key= True)