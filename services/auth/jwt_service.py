from typing import Dict, Union
import jwt


class JwtService:
    
    def __new__(cls, secret: str, algoritm: str = "HS256"):
        if not hasattr(cls, '_instance'):
            cls.secret = secret
            cls.algoritm = algoritm
            cls._instance = super().__new__(cls)
        return cls._instance

    async def encode(self, payload: Dict) -> Union[str, bytes]:
        encoded_jwt = await jwt.encode(
            payload=payload,
            key=self.secret,
            algorithm=self.algoritm
            )
        return encoded_jwt

    async def decode(self, encoded_jwt: Union[str, bytes]) -> Dict:
        decoded_jwt = await jwt.decode(
            jwt=encoded_jwt,
            key=self.key,
            algorithms=[self.algoritm]
        )
        return decoded_jwt