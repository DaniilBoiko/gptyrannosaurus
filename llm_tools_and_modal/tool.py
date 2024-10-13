import modal
import pubchempy as pcp

image = modal.Image.debian_slim().pip_install("pubchempy")
app = modal.App("name2smiles", image=image)


def get_molecule_info(query):
    results = pcp.get_compounds(query, 'name')
    if len(results) == 0:
        return None
    return results[0].to_dict()


@app.function()
@modal.web_endpoint()
def name2info(name: str):
    return get_molecule_info(name)
