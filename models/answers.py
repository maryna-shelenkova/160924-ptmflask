
from models import db
from sqlalchemy.orm import Mapped, mapped_column

class Answer(db.Model):
    __tablename__ = 'answers'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(
        db.Integer,
        db.Identity(always=True),
        primary_key=True,
        autoincrement=True
    )
    question_id: Mapped[int] = mapped_column(
        db.Integer,
        db.ForeignKey('questions.id'),
    )
    is_agree: Mapped[bool] = mapped_column(
        db.Boolean,
    )

    question: Mapped['Question'] = db.relationship('Question', back_populates='answers')

    def __repr__(self):
        return f'Answer for Question {self.question_id}: {self.is_agree}'
