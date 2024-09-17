from pydantic import BaseModel
from core.schema.validate import error_handler

class NucleiRequest(BaseModel):
    url: str
    
    async def custom_validation(self, errors, db=None, record_id=None):
        
        if (
        not (
            self.url.startswith("http://")
            or self.url.startswith("https://")
        )
        ):
            error_handler(
                "Please enter a valid URL",
                "url",
                errors
            )
        return errors