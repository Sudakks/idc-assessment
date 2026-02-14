from pdb import run
import requests
from typing import List, Tuple, Dict, Any

class OpenFDAClient:
    """
    Reusable data integration module that fetches and processes data from 
external healthcare sources
    Generalize all OpenFDA-related logic in one class

	Extensibility:
	To support EMR data, the input should be extended to consume standardized formats.
	Then it could be added by replacing the file-based input with an API-driven data source, while reusing the same validation and processing logic once the data is normalized.
    """

    base_url = "https://api.fda.gov/drug/event.json" 

    
    def __init__(self, timeout: int = 10):
        """
        timeout: timeout for HTTP requestes
		_cache: basic caching to avoid redundant API calls 
        """
        self.timeout = timeout
        self._cache: Dict[str, List[Tuple[str, int]]] = {}
    
    def query_adverse_events(self, drug_name: str, limit: int = 5)->List[Tuple[str, int]]:
        """
        Fetch top 5(limit) adverse reactions for a given drug

        drug_name: name of the drug to search for
        limit: number of top adverse reactions to return

        Returns a list of tuples (adverse_reaction, count)
        """

        cache_key = f"{drug_name.lower()}:{limit}"
        if cache_key in self._cache:
            return self._cache[cache_key]
        
        params = { 
            "search": f'patient.drug.medicinalproduct:"{drug_name}"', 
            "count": "patient.reaction.reactionmeddrapt.exact", 
            "limit": limit } 
        try:
			# Data Requests
            response = requests.get(self.base_url, params=params, timeout=self.timeout)

			# Error handling
            if response.status_code == 429:
                raise RuntimeError("OpenFDA API rate limit exceeded")
            if response.status_code != 200:
                raise RuntimeError(f"OpenFDA API error: {response.status_code} - {response.text}")

            
            data = response.json()

			# Check whether the result type and content are valid
            if "results" not in data or not data["results"]:
                raise ValueError(f"No adverse event data found for drug: {drug_name}")
            
			# Process the data to get standard format
            results = data.get("results", [])
            return_value = [
                (item["term"], item["count"])
                for item in results
            ]

            self._cache[cache_key] = return_value
            return return_value

        except requests.exceptions.Timeout:
            raise RuntimeError("Request to OpenFDA API timed out")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error while calling OpenFDA API: {e}")
