import pytest
import pytest_asyncio
from fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

try:
    from app.main import app
    from app.database import Base, get_db
except (ModuleNotFoundError, ImportError):
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from app.main import app
    from app.database import Base, get_db


### Set up a local testing database session ###
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    },
    poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    """
    Overrides the 'get_db' dependency (which injects a session into functions
    with database interactions) with TestingSessionLocal.
    """
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Override the 'get_db' dependency injection with the testing one.
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session", autouse=True)
def setup():
    Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="function")
def client():
    return TestClient(app)


@pytest_asyncio.fixture(scope="function")
async def async_client():
    async with AsyncClient(transport=ASGITransport(app=app)) as ac:
        yield ac
