import pytest
from digitalai.release.release_api_client import ReleaseAPIClient


@pytest.fixture(scope="session")
def release_api_client():
    """Setup: Create a client for the integration test session"""
    client = ReleaseAPIClient("http://localhost:5516", "admin", "admin")

    # Setup code here
    print("\n🔧 Setting up integration tests...")

    yield client

    # Teardown code here
    print("\n🧹 Tearing down integration tests...")
    # Add cleanup logic if needed
