import json

class CittaApertaProject:
    def __init__(self, name="Città Aperta / Orizonturi Culturale", budget_eur=250000):
        self.name = name
        self.budget_eur = budget_eur
        self.token_supply = 1_000_000  # 1 Milion tokenuri culturale CACT
        self.virtual_tour_access = "Free / Public Open Access" # Gratuitatea atrage publicul
        self.charity_support_pct = 15.0  # Procent din încasări direcționat spre cauze caritabile și tineri artiști

    def calculate_budget_allocation(self):
        return {
            "Dezvoltare Platforma Web & Blockchain": self.budget_eur * 0.30,  # 75.000 EUR[cite: 6]
            "Amenajare & Inchiriere Spatiu Fizic": self.budget_eur * 0.24,     # 60.000 EUR[cite: 6]
            "Echipa, Personal & Management": self.budget_eur * 0.28,         # 70.000 EUR[cite: 6]
            "Marketing, Promovare & B2B Travel": self.budget_eur * 0.12,     # 30.000 EUR[cite: 6]
            "Fond de Rezerva & Imprevizibile": self.budget_eur * 0.06         # 15.000 EUR[cite: 6]
        }

    def generate_json_manifest(self):
        manifest = {
            "project": self.name,
            "total_budget_eur": self.budget_eur,
            "virtual_tour_model": self.virtual_tour_access,
            "monetization_strategy": "B2B Travel Packages, Physical Hub Services & Tokenization",
            "charity_fund_percentage": self.charity_support_pct,
            "allocations_eur": self.calculate_budget_allocation(),
            "token_supply": self.token_supply,
            "token_symbol": "CACT",
            "license": "Open-Source / Zero Cost / Free Public Distribution"
        }
        return json.dumps(manifest, indent=4)

if __name__ == "__main__":
    project = CittaApertaProject()
    print("=== Manifest Oficial Proiect Città Aperta (Model Freemium) ===")
    print(project.generate_json_manifest())
