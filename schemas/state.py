from typing import TypedDict, Annotated
import operator


class PharmaState(TypedDict):

    query: str

    retrieved_docs: list

    literature_analysis: dict

    mechanism_analysis: dict

    final_response: str

    metrics: Annotated[dict, operator.or_]