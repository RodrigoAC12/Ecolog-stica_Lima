"""Safety checks: never run Base.metadata.drop_all against a non-test database."""
import pytest

from conftest import validate_test_database_url


@pytest.mark.parametrize(
    "url",
    [
        "postgresql+psycopg://operator:password@localhost/ecologistica",
        "postgresql+psycopg://operator:password@localhost/production",
        "sqlite:////tmp/ecologistica.db",
        "postgresql+psycopg://operator:password@localhost/",
    ],
)
def test_reject_non_test_database_urls(url):
    with pytest.raises(ValueError, match="test database|test_"):
        validate_test_database_url(url)


@pytest.mark.parametrize(
    "url",
    [
        "postgresql+psycopg://operator:password@localhost/ecologistica_test",
        "postgresql+psycopg://operator:password@localhost/test_ecologistica",
        "sqlite:////tmp/ecologistica_test.db",
        "sqlite:///:memory:",
    ],
)
def test_allow_explicit_test_database_urls(url):
    validate_test_database_url(url)
