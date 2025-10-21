from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app
from io import BytesIO
import json

client = TestClient(app)


def test_analyze_success_and_logging(monkeypatch):
    """Test /api/v1/analyze proxies to AI service and logs result."""
    
    # Mock httpx.AsyncClient.post
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "risk": "THẤP 🟢",
        "reason": "Test reason",
        "cv_scores": {"melanoma": 0.05}
    }
    mock_response.raise_for_status = MagicMock()
    
    async def mock_post(url, files, data):
        return mock_response
    
    # Mock DB session
    mock_db = MagicMock()
    
    def override_get_db():
        yield mock_db
    
    from app.database import get_db
    from app.main import app as test_app
    test_app.dependency_overrides[get_db] = override_get_db
    
    with patch("httpx.AsyncClient.post", new=mock_post):
        fake_image = BytesIO(b"fake")
        files = {"image": ("test.jpg", fake_image, "image/jpeg")}
        data = {"symptoms_selected": "ngứa"}
        
        resp = client.post("/api/v1/analyze", files=files, data=data)
        
        assert resp.status_code == 200
        body = resp.json()
        assert body["risk"] == "THẤP 🟢"
        
        # Verify DB add was called
        assert mock_db.add.called
        assert mock_db.commit.called
    
    test_app.dependency_overrides.clear()
