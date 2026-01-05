import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


# BEGIN (write your solution here)
def create_db_engine(
    db_url=None,
    echo=False,
    pool_size=5,
    max_overflow=10
):
    """
    Создает и возвращает объект движка базы данных для подключения к PostgreSQL.
    
    Parameters:
    -----------
    db_url : str, optional
        Строка подключения к базе данных PostgreSQL.
        Если не указана, используется переменная окружения DATABASE_URL.
    echo : bool, optional
        Включает или отключает вывод SQL-запросов в консоль (по умолчанию False).
    pool_size : int, optional
        Размер пула соединений (по умолчанию 5).
    max_overflow : int, optional
        Максимальное количество соединений сверх размера пула (по умолчанию 10).
    
    Returns:
    --------
    engine : sqlalchemy.engine.Engine
        Объект движка базы данных SQLAlchemy.
    """
    # Если db_url не указан, берем из переменных окружения
    if db_url is None:
        db_url = os.getenv('DATABASE_URL')
    
    # Создаем движок с указанными параметрами
    engine = create_engine(
        db_url,
        echo=echo,
        pool_size=pool_size,
        max_overflow=max_overflow
    )
    
    return engine
# END
