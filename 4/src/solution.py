from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Movie
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def format_movie(movie):
    """Форматирует объект Movie в строку заданного формата."""
    return f"{movie.title} by {movie.director}, released on {movie.release_date}, duration: {movie.duration} min, genre: {movie.genre}, rating: {movie.rating}"


def get_all_movies(session):
    """Возвращает список всех фильмов в заданном формате."""
    query = select(Movie)
    result = session.execute(query)
    movies = result.scalars().all()
    
    return [format_movie(movie) for movie in movies]


def get_movies_by_director(session, director_name):
    """Возвращает список фильмов указанного режиссера, отсортированных по дате выпуска."""
    query = select(Movie).where(Movie.director == director_name).order_by(Movie.release_date)
    result = session.execute(query)
    movies = result.scalars().all()
    
    return [format_movie(movie) for movie in movies]


def get_top_rated_movies(session, n):
    """Возвращает список из n фильмов с наивысшим рейтингом, отсортированных по убыванию рейтинга."""
    query = select(Movie).order_by(Movie.rating.desc()).limit(n)
    result = session.execute(query)
    movies = result.scalars().all()
    
    return [format_movie(movie) for movie in movies]

# END
