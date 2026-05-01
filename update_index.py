#!/usr/bin/env python3
"""
Script de mise à jour des index de prospection
Usage: python update_index.py
"""
import os
import yaml

vault = os.path.dirname(os.path.abspath(__file__))

def scan_prospects():
    prospects = []
    for folder in ['Artisans', 'Fast-Food']:
        folder_path = os.path.join(vault, folder)
        if not os.path.exists(folder_path):
            continue
        for filename in os.listdir(folder_path):
            if filename.endswith('.md') and filename != 'Index.md':
                filepath = os.path.join(folder_path, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        try:
                            fm = yaml.safe_load(parts[1])
                            fm['fichier'] = f"{folder}/{filename}"
                            prospects.append(fm)
                        except:
                            pass
    return prospects

# ... (fonctions de génération identiques)
# Pour l'instant ce script est un placeholder - le vrai script est exécuté par l'agent

if __name__ == '__main__':
    print("Utilisez l'agent pour régénérer les index")
