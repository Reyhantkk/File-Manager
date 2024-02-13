import os
import shutil

def dosya_listele(dizin):
    """Belirtilen dizindeki dosya ve dizinleri listeler."""
    with os.scandir(dizin) as dosyalar:
        for dosya in dosyalar:
            print(dosya.name)

def dosya_kopyala(kaynak, hedef):
    """Bir dosyayı kaynak dizininden hedef dizine kopyalar."""
    shutil.copy(kaynak, hedef)
    print(f"{kaynak} -> {hedef} kopyalandı.")

def dosya_tasi(kaynak, hedef):
    """Bir dosyayı kaynak dizininden hedef dizine taşır."""
    shutil.move(kaynak, hedef)
    print(f"{kaynak} -> {hedef} taşındı.")

def dosya_sil(dosya_yolu):
    """Belirtilen yoldaki dosyayı siler."""
    os.remove(dosya_yolu)
    print(f"{dosya_yolu} silindi.")


if __name__ == "__main__":
    mevcut_dizin = os.getcwd()
    print("Mevcut Dizin:", mevcut_dizin)
    dosya_listele(mevcut_dizin)
    

    kaynak_dosya = 'ornek.txt'
    hedef_dizin = 'yedek'
    hedef_dosya = os.path.join(hedef_dizin, kaynak_dosya)
    
   
    dosya_kopyala(kaynak_dosya, hedef_dosya)
    dosya_tasi(hedef_dosya, kaynak_dosya)


    # Örnek dosya yollarını ve işlemleri belirleyin
    # Dosya işlemlerini test et
    # Not: Test etmeden önce 'ornek.txt' dosyasının mevcut dizinde olduğundan ve 'yedek' adında bir dizin olduğundan emin olun
    # dosya_sil('silinecek_dosya.txt')  # Dikkat: Bu işlem dosyayı kalıcı olarak siler
