import requests
import logging
from typing import Optional, Dict, Any
from requests.exceptions import RequestException
from urllib3.exceptions import InsecureRequestWarning
import json

class HTTPClient:
    """A secure HTTP client with comprehensive error handling and logging."""
    
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        verify_ssl: bool = True
    ) -> Dict[str, Any]:
        """
        Make an HTTP request with proper error handling.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint
            data: Request payload
            headers: Request headers
            verify_ssl: Whether to verify SSL certificates
            
        Returns:
            Response data as dictionary
            
        Raises:
            RequestException: If the request fails
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        if not verify_ssl:
            self.logger.warning("SSL verification is disabled!")
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            
        try:
            headers = headers or {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
            
            self.logger.info(f"Making {method} request to {url}")
            response = self.session.request(
                method=method,
                url=url,
                json=data if data else None,
                headers=headers,
                timeout=self.timeout,
                verify=verify_ssl
            )
            
            # Raise an exception for bad status codes
            response.raise_for_status()
            
            try:
                return response.json()
            except json.JSONDecodeError:
                self.logger.warning("Response was not valid JSON")
                return {'raw_content': response.text}
                
        except requests.exceptions.SSLError as e:
            self.logger.error(f"SSL Error: {str(e)}")
            raise
        except requests.exceptions.ConnectionError as e:
            self.logger.error(f"Connection Error: {str(e)}")
            raise
        except requests.exceptions.Timeout as e:
            self.logger.error(f"Timeout Error: {str(e)}")
            raise
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request failed: {str(e)}")
            raise
        finally:
            self.session.close()