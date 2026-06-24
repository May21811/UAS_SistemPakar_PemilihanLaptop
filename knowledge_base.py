import json
import os

class KnowledgeBase:
    def __init__(self, data_dir='data'):
        # Memastikan Python mencari folder 'data' di tempat file ini berada (di USB)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(base_dir, data_dir)
        
        self.gejala = {}
        self.penyakit = {}
        self.rules = []
        self._load_data()

    def _load_data(self):
        try:
            # Jalur file JSON
            gejala_path = os.path.join(self.data_dir, 'gejala.json')
            penyakit_path = os.path.join(self.data_dir, 'penyakit.json')
            rules_path = os.path.join(self.data_dir, 'rules.json')

            # Load Gejala
            with open(gejala_path, 'r', encoding='utf-8') as f:
                for g in json.load(f)['gejala']:
                    self.gejala[g['id']] = g
                    
            # Load Penyakit
            with open(penyakit_path, 'r', encoding='utf-8') as f:
                for p in json.load(f)['penyakit']:
                    self.penyakit[p['id']] = p
                    
            # Load Aturan
            with open(rules_path, 'r', encoding='utf-8') as f:
                self.rules = json.load(f)['rules']
                
        except FileNotFoundError as e:
            import streamlit as st
            st.error(f"File tidak ditemukan! Pastikan file JSON ada di folder 'data'. Detail: {e}")
        except json.JSONDecodeError as e:
            import streamlit as st
            st.error(f"Ada kesalahan format penulisan (tanda koma/kurung) di dalam file JSON Anda! Detail: {e}")

    def get_semua_gejala(self):
        return list(self.gejala.values())