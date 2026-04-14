import requests
from bs4 import BeautifulSoup
import json
import re

def verify_rock(label_name):
    base_url = "https://luarocks.org"
    print(f"--- VERIFICANDO LABEL: {label_name} ---")
    
    # 1. Lista de Rocks en el Label
    res = requests.get(f"{base_url}/labels/{label_name}")
    soup = BeautifulSoup(res.text, 'lxml')
    first_rock_link = soup.select_one("li.module_row .main a.title")
    
    if not first_rock_link:
        print("No se encontraron rocks en este label.")
        return
    
    rock_path = first_rock_link['href']
    rock_name = first_rock_link.text.strip()
    print(f"Rock seleccionado: {rock_name} ({base_url}{rock_path})")
    
    # 2. Detalle del Rock
    res = requests.get(f"{base_url}{rock_path}")
    soup = BeautifulSoup(res.text, 'lxml')
    
    description = soup.select_one(".description")
    desc_text = description.get_text(separator="\n").strip() if description else "VACÍO"
    
    homepage_link = soup.select_one("a.external_url")
    homepage_url = homepage_link['href'] if homepage_link else None
    
    print(f"\n[DESCRIPCIÓN LUAROCKS]:\n{desc_text[:300]}...")
    print(f"\n[HOMEPAGE]: {homepage_url}")
    
    # 3. Intento de GitHub Deep Scrape
    final_content = desc_text
    if homepage_url and "github.com" in homepage_url:
        print("Detectada Homepage en GitHub. Intentando extraer README raw...")
        # Normalizar URL de github
        raw_url = homepage_url.replace("github.com", "raw.githubusercontent.com")
        raw_url = re.sub(r'/(tree|blob)/[^/]+', '', raw_url).rstrip('/')
        
        found = False
        for branch in ["/master/README.md", "/main/README.md", "/master/README.markdown", "/master/README"]:
            target = raw_url + branch
            try:
                readme_res = requests.get(target, timeout=5)
                if readme_res.status_code == 200:
                    final_content = readme_res.text
                    print(f"README encontrado en: {target}")
                    found = True
                    break
            except:
                continue
        if not found:
            print("No se pudo obtener el README raw de GitHub automáticamente.")
    
    print(f"\n--- RESULTADO FINAL (Primeros 500 chars) ---\n")
    print(final_content[:500])
    print("\n-------------------------------------------")

if __name__ == "__main__":
    verify_rock("http")
