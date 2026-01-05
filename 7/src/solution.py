from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Director
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def delete_director(session, director_id):
    """
    Удаляет режиссёра и все связанные с ним фильмы.
    
    Args:
        session: Сессия SQLAlchemy
        director_id: ID режиссёра для удаления
    """
    # Находим режиссёра по ID
    director = session.query(Director).get(director_id)
    
    if director:
        # При каскадном удалении достаточно удалить режиссёра
        # SQLAlchemy автоматически удалит все связанные фильмы
        session.delete(director)
        session.commit()
        return True
    else:
        # Режиссёр не найден
        return False
# END
