from enum import Enum

class LLMQueryTypes(Enum):
    SIMPLE="simple"
    INVALID="invalid"
    SEEK="seek"
    CREATE="create"
    ERROR="error"