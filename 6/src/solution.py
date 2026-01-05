from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload
from models import Base, Movie
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def get_movies_with_directors(session):
    """
    Возвращает список всех фильмов с их режиссерами.
    Использует один оптимизированный запрос с joinedload.
    """
    query = (
        session.query(Movie)
        .options(joinedload(Movie.director))  # Загружаем связанных режиссеров
        .order_by(Movie.title)  # Сортируем по названию фильма
    )
    
    return query.all()
# END
