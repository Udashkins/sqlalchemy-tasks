from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Movie, Director
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def get_movies_with_directors(session):
    stmt = (
        select(Movie, Director.name)
        .join(Director, Movie.director_id == Director.id)
        .order_by(Movie.title)
    )
    
    result = session.execute(stmt)
    movies_list = []
    
    for movie, director_name in result:
        movie_str = (
            f"{movie.title} by {director_name}, "
            f"released on {movie.release_date}, "
            f"duration: {movie.duration} min, "
            f"genre: {movie.genre}, "
            f"rating: {movie.rating}"
        )
        movies_list.append(movie_str)
    
    return movies_list


# Пример использования функции
if __name__ == "__main__":
    with session() as s:
        # Добавляем тестовые данные
        director1 = Director(name="Frank Darabont")
        director2 = Director(name="Christopher Nolan")
        
        s.add(director1)
        s.add(director2)
        s.commit()
        
        movie1 = Movie(
            title="The Shawshank Redemption",
            director_id=director1.id,
            release_date=datetime.date(1994, 9, 23),
            duration=142,
            genre="Drama",
            rating=9.3
        )
        
        movie2 = Movie(
            title="Inception",
            director_id=director2.id,
            release_date=datetime.date(2010, 7, 16),
            duration=148,
            genre="Sci-Fi",
            rating=8.8
        )
        
        s.add(movie1)
        s.add(movie2)
        s.commit()
        
        # Вызываем функцию и выводим результат
        movies = get_movies_with_directors(s)
        for movie in movies:
            print(movie)
# END
