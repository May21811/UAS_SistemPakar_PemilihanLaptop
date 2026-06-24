class CertaintyFactor:
    @staticmethod
    def hitung_cf(rules_aktif, cf_user_dict):
        # cf_user_dict berbentuk dicitonary { 'G01': 1.0, 'G06': 0.8 }
        cf_laptop = {} # Menyimpan hasil gabungan cf per laptop
        
        for rule in rules_aktif:
            laptop_id = rule['kesimpulan']
            cf_pakar = rule['cf_pakar']
            
            # Cari nilai CF evidence terkecil dari kondisi kriteria yang menyusun rule
            cf_evidence = min([cf_user_dict.get(gid, 0.0) for gid in rule['kondisi']])
            cf_aturan = cf_evidence * cf_pakar
            
            if laptop_id not in cf_laptop:
                cf_laptop[laptop_id] = cf_aturan
            else:
                # Formula Kombinasi CF (Jika keduanya positif)
                cf_lama = cf_laptop[laptop_id]
                cf_laptop[laptop_id] = cf_lama + cf_aturan * (1 - cf_lama)
                
        return cf_laptop