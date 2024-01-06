from pydantic import BaseModel


class BaseLLM(BaseModel):
    name: str

    class Config:
        arbitrary_types_allowed = True

    def __call__(self, prompt) -> str | None:
        raise NotImplementedError("Subclasses must implement this method")
