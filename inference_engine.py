class ForwardChaining:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def inferensi(self, kriteria_terpilih):
        # kriteria_terpilih berbentuk list ID kriteria, contoh: ['G01', 'G06']
        fakta = set(kriteria_terpilih)
        rules_aktif = []
        
        for rule in self.kb.rules:
            kondisi = set(rule['kondisi'])
            # Cek apakah seluruh kondisi pada rule terpenuhi oleh fakta pengguna
            if kondisi.issubset(fakta):
                rules_aktif.append(rule)
                
        return rules_aktif