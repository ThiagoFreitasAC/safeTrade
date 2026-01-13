
import time
from typing import Optional, Dict, Tuple
from datetime import datetime

class Signer:
    """
    responsável por assinar requisições
    """
    

    def sign(self, instruction: str, params: Optional[Dict] = None) -> Tuple[Dict, int]:
        
        if not instruction:
            raise ValueError("instruction deve ser fornecida")

        """ 
            Hora de agora da região UTC e em milissegundos
            timestamp para assinatura
        """

        timestamp = int(datetime.now(timezone.utc).timestamp() * 1000)
        window = 5000

        """ lista de partes para assinatura """
        signature_parts = [f"instruction={instruction}"]
        
        """ ordena parâmetros alfabeticamente (exigencia da API)"""
        if params:
            sorted_params = sorted(params.items())
            for key, value in sorted_params:
                signature_parts.append(f"{key}={value}")
                
        signature_parts.append(f"timestamp={timestamp}")
        signature_parts.append(f"window={window}")
        
        """ string final para assinar """
        sign_string = "&".join(signature_parts)
        
        """ gera assinatura"""
        signature = self.authenticator.sign_message(sign_string)
        
        """ headers"""
        headers = {
            "X-API-Key": self.authenticator.get_api_key(),
            "X-Timestamp": str(timestamp),
            "X-Window": str(window),
            "X-Signature": signature,
            "Content-Type": "application/json; charset=utf-8"
        }
    
        return headers, timestamp