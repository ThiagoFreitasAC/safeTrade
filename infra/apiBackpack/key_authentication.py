import base64
from cryptography.hazmat.primitives.asymmetric import ed25519
class BackpackAPI:
    """
    Cliente para API da Backpack Exchange
    """
    
    def __init__(self, api_key_base64: str, private_key_base64: str):
        if not api_key_base64 or not private_key_base64:
            raise ValueError("api_key_base64 e private_key_base64 devem ser fornecidos")
        
        self.api_key = api_key_base64

        try:    
            # Converte chave privada de base64 para objeto ED25519
            private_key_bytes = base64.b64decode(private_key_base64)
            self.private_key = ed25519.Ed25519PrivateKey.from_private_bytes(private_key_bytes)
        
        except Exception as e:
            # ERRO SÊNIOR: Tratar exceção com f-string para não quebrar se 'e' não for str
            raise ValueError(f"Erro ao decodificar a chave privada (Verifique se é Base64 válida): {e}")
        
        # URL base da API Backpack
        self.base_url = "https://api.backpack.exchange"

    def get_api_key(self) -> str:
        """Retorna a chave pública (API Key)."""
        return self.api_key
    
    def get_private_key(self):
        """Retorna o objeto da chave privada """
        return self.private_key

    def sign_message(self, message: str) -> str:
        """
        Assina uma mensagem usando criptografia assimétrica (ED25519).
        
        Args:
            message: A string exata que a API espera (instruction + params + timestamp...)
            
        Returns:
            String em Base64 contendo a assinatura digital.
        """
        signature_bytes = self.private_key.sign(message.encode('utf-8'))
        return base64.b64encode(signature_bytes).decode('utf-8')