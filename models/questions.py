from models import db
from sqlalchemy.orm import Mapped, mapped_column

class Question(db.Model):
    __tablename__ = 'questions'
    __table_args__ = {'extend_existing': True}  # Добавлено

    id: Mapped[int] = mapped_column(
        db.Integer,
        db.Identity(always=True),
        primary_key=True,
        autoincrement=True
    )
    text: Mapped[str] = mapped_column(
        db.String(255),
    )
    category_id: Mapped[int] = mapped_column(
        db.Integer,
        db.ForeignKey('categories.id'),
    )

    category: Mapped['Category'] = db.relationship('Category', back_populates='questions')
    answers: Mapped[list['Answer']] = db.relationship










