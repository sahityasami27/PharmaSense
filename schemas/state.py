from typing import TypedDict, List, Dict


class PharmaState(TypedDict):
    query: str
    retrieved_docs: List[Dict]

    literature_analysis: Dict
    mechanism_analysis: Dict

    metrics: Dict

    final_response: str