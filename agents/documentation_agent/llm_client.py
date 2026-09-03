from abc import ABC, abstractmethod


class LLMClient(ABC):

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Recibe un prompt y retorna
        la respuesta generada por el modelo.
        """
        raise NotImplementedError
