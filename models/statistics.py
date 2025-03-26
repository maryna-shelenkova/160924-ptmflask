from sqlalchemy.orm import Mapped, mapped_column, relationship
from models import db

class Statistic(db.Model):
    __tablename__ = 'statistics'
    __table_args__ = {'extend_existing': True}

    question_id: Mapped[int] = mapped_column(
        db.Integer,
        db.ForeignKey('questions.id', ondelete="CASCADE"),
        primary_key=True
    )
    agree_count: Mapped[int] = mapped_column(
        db.Integer,
        server_default="0",
        nullable=False
    )
    disagree_count: Mapped[int] = mapped_column(
        db.Integer,
        server_default="0",
        nullable=False
    )

    question: Mapped['Question'] = relationship('Question', back_populates='statistics')

    def __repr__(self):
        return f'<Statistic for Question {self.question_id}: {self.agree_count} agree, {self.disagree_count} disagree>'

