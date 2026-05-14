from Bio import Entrez
from Bio import Medline


Entrez.email = "sahityasami27@gmail.com"


def fetch_pubmed(query="neuroinflammation", max_results=10):

    search_handle = Entrez.esearch(
        db="pubmed",
        term=query,
        retmax=max_results
    )

    search_results = Entrez.read(search_handle)

    ids = search_results["IdList"]

    fetch_handle = Entrez.efetch(
        db="pubmed",
        id=ids,
        rettype="medline",
        retmode="text"
    )

    records = Medline.parse(fetch_handle)

    papers = []

    for idx, record in enumerate(records):

        title = record.get("TI", "No title")

        abstract = record.get("AB", "No abstract")

        papers.append({
            "id": f"paper_{idx}",
            "title": title,
            "abstract": abstract
        })

    return papers


if __name__ == "__main__":

    papers = fetch_pubmed()

    print(papers[:2])