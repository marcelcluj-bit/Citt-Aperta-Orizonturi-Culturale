import json
import os


class CittaApertaProject:
    """Clasă pentru gestionarea parametrilor financiari, a modelului Freemium

    și a generării manifestului proiectului Città Aperta.
    """

    def __init__(
        self,
        name: str = "Città Aperta / Orizonturi Culturale",
        budget_eur: float = 250000.0,
    ):
        self.name = name
        self.budget_eur = budget_eur
        self.token_supply = 1_000_000  # 1 Milion tokenuri culturale CACT
        self.virtual_tour_access = (
            "Free / Public Open Access"  # Tururi virtuale gratuite
        )
        self.charity_support_pct = 15.0  # 15% pentru sprijin tineri artiști și restaurare patrimoniu

    def calculate_budget_allocation(self) -> dict:
        """Calculează defalcarea bugetară pe cele 5 categorii oficiale."""
        return {
            "Dezvoltare Platforma Web & Blockchain": self.budget_eur * 0.30,  # 75.000 EUR
            "Amenajare & Inchiriere Spatiu Fizic": self.budget_eur * 0.24,  # 60.000 EUR
            "Echipa, Personal & Management": self.budget_eur * 0.28,  # 70.000 EUR
            "Marketing, Promovare & B2B Travel": self.budget_eur * 0.12,  # 30.000 EUR
            "Fond de Rezerva & Imprevizibile": self.budget_eur * 0.06,  # 15.000 EUR
        }

    def generate_manifest_dict(self) -> dict:
        """Construiește dicționarul cu structura completă a proiectului."""
        return {
            "project": self.name,
            "version": "1.0.0",
            "total_budget_eur": self.budget_eur,
            "virtual_tour_model": self.virtual_tour_access,
            "monetization_strategy": (
                "B2B Travel Packages, Physical Hub Services & Tokenization"
            ),
            "charity_fund_percentage": self.charity_support_pct,
            "allocations_eur": self.calculate_budget_allocation(),
            "token_details": {
                "name": "Citta Aperta Cultural Token",
                "symbol": "CACT",
                "total_supply": self.token_supply,
                "standard": "ERC-20",
            },
            "license": "MIT / Open-Source Public Domain",
        }

    def generate_json_manifest(self) -> str:
        """Returnează reprezentarea JSON formatată a manifestului."""
        return json.dumps(self.generate_manifest_dict(), indent=4)

    def save_manifest_to_file(self, filepath: str = "project_manifest.json"):
        """Salvează manifestul generat pe disc."""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self.generate_json_manifest())
        print(f"[+] Manifest salvat cu succes în: {filepath}")


if __name__ == "__main__":
    project = CittaApertaProject()
    print("=== Manifest Proiect Città Aperta (Model Freemium) ===")
    print(project.generate_json_manifest())

    # Generare fișier manifest JSON în directorul de configurare
    output_path = os.path.join("config", "project_manifest.json")
    project.save_manifest_to_file(output_path)
