"""Unit tests for the API module."""
import pytest
from unittest.mock import Mock, patch
from twspace_dl.api import GraphQLAPI, HTTPClient


class TestGraphQLAPI:
    """Test cases for the GraphQLAPI class."""

    @pytest.fixture
    def mock_graphql_api(self):
        """Create a mock GraphQLAPI instance for testing."""
        mock_client = Mock(spec=HTTPClient)
        mock_cookies = {"ct0": "test_token", "auth_token": "test_auth"}
        
        with patch('twspace_dl.api.validate_cookies'):
            api = GraphQLAPI(mock_client, "graphql", mock_cookies)
        
        # Mock the user_id method to return a test user ID
        api.user_id = Mock(return_value="123456789")
        
        return api

    def test_user_id_from_url_x_com_with_https(self, mock_graphql_api):
        """Test user_id_from_url with x.com domain and https protocol."""
        result = mock_graphql_api.user_id_from_url("https://x.com/protosphinx")
        assert result == "123456789"
        mock_graphql_api.user_id.assert_called_once_with("protosphinx")

    def test_user_id_from_url_x_com_with_http(self, mock_graphql_api):
        """Test user_id_from_url with x.com domain and http protocol."""
        result = mock_graphql_api.user_id_from_url("http://x.com/protosphinx")
        assert result == "123456789"
        mock_graphql_api.user_id.assert_called_once_with("protosphinx")

    def test_user_id_from_url_x_com_without_protocol(self, mock_graphql_api):
        """Test user_id_from_url with x.com domain without protocol."""
        result = mock_graphql_api.user_id_from_url("x.com/protosphinx")
        assert result == "123456789"
        mock_graphql_api.user_id.assert_called_once_with("protosphinx")

    def test_user_id_from_url_x_com_with_trailing_slash(self, mock_graphql_api):
        """Test user_id_from_url with x.com domain and trailing slash."""
        result = mock_graphql_api.user_id_from_url("https://x.com/protosphinx/")
        assert result == "123456789"
        mock_graphql_api.user_id.assert_called_once_with("protosphinx")

    def test_user_id_from_url_x_com_with_multiple_trailing_slashes(self, mock_graphql_api):
        """Test user_id_from_url with x.com domain and multiple trailing slashes."""
        result = mock_graphql_api.user_id_from_url("https://x.com/protosphinx///")
        assert result == "123456789"
        mock_graphql_api.user_id.assert_called_once_with("protosphinx")

    def test_user_id_from_url_twitter_com_with_https(self, mock_graphql_api):
        """Test user_id_from_url with twitter.com domain and https protocol."""
        result = mock_graphql_api.user_id_from_url("https://twitter.com/protosphinx")
        assert result == "123456789"
        mock_graphql_api.user_id.assert_called_once_with("protosphinx")

    def test_user_id_from_url_twitter_com_with_http(self, mock_graphql_api):
        """Test user_id_from_url with twitter.com domain and http protocol."""
        result = mock_graphql_api.user_id_from_url("http://twitter.com/protosphinx")
        assert result == "123456789"
        mock_graphql_api.user_id.assert_called_once_with("protosphinx")

    def test_user_id_from_url_twitter_com_without_protocol(self, mock_graphql_api):
        """Test user_id_from_url with twitter.com domain without protocol."""
        result = mock_graphql_api.user_id_from_url("twitter.com/protosphinx")
        assert result == "123456789"
        mock_graphql_api.user_id.assert_called_once_with("protosphinx")

    def test_user_id_from_url_twitter_com_with_trailing_slash(self, mock_graphql_api):
        """Test user_id_from_url with twitter.com domain and trailing slash."""
        result = mock_graphql_api.user_id_from_url("https://twitter.com/protosphinx/")
        assert result == "123456789"
        mock_graphql_api.user_id.assert_called_once_with("protosphinx")

    def test_user_id_from_url_twitter_com_with_multiple_trailing_slashes(self, mock_graphql_api):
        """Test user_id_from_url with twitter.com domain and multiple trailing slashes."""
        result = mock_graphql_api.user_id_from_url("https://twitter.com/protosphinx///")
        assert result == "123456789"
        mock_graphql_api.user_id.assert_called_once_with("protosphinx")

    def test_user_id_from_url_with_underscore_in_username(self, mock_graphql_api):
        """Test user_id_from_url with underscore in username."""
        result = mock_graphql_api.user_id_from_url("https://twitter.com/proto_sphinx")
        assert result == "123456789"
        mock_graphql_api.user_id.assert_called_once_with("proto_sphinx")

    def test_user_id_from_url_with_numbers_in_username(self, mock_graphql_api):
        """Test user_id_from_url with numbers in username."""
        result = mock_graphql_api.user_id_from_url("https://x.com/user123")
        assert result == "123456789"
        mock_graphql_api.user_id.assert_called_once_with("user123")

    def test_user_id_from_url_invalid_url_no_username(self, mock_graphql_api):
        """Test user_id_from_url with invalid URL (no username)."""
        with pytest.raises(RuntimeError, match="Invalid Twitter user URL"):
            mock_graphql_api.user_id_from_url("https://x.com/")

    def test_user_id_from_url_invalid_url_with_path(self, mock_graphql_api):
        """Test user_id_from_url with invalid URL (extra path)."""
        with pytest.raises(RuntimeError, match="Invalid Twitter user URL"):
            mock_graphql_api.user_id_from_url("https://x.com/protosphinx/status/123")

    def test_user_id_from_url_invalid_url_wrong_domain(self, mock_graphql_api):
        """Test user_id_from_url with invalid URL (wrong domain)."""
        with pytest.raises(RuntimeError, match="Invalid Twitter user URL"):
            mock_graphql_api.user_id_from_url("https://facebook.com/protosphinx")

    def test_user_id_from_url_invalid_url_with_special_chars(self, mock_graphql_api):
        """Test user_id_from_url with invalid URL (special characters in username)."""
        with pytest.raises(RuntimeError, match="Invalid Twitter user URL"):
            mock_graphql_api.user_id_from_url("https://x.com/proto@sphinx")

    def test_user_id_from_url_empty_string(self, mock_graphql_api):
        """Test user_id_from_url with empty string."""
        with pytest.raises(RuntimeError, match="Invalid Twitter user URL"):
            mock_graphql_api.user_id_from_url("")

    def test_user_id_from_url_none_type(self, mock_graphql_api):
        """Test user_id_from_url with None type."""
        with pytest.raises(AttributeError):
            mock_graphql_api.user_id_from_url(None)
