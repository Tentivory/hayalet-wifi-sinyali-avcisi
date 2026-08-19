#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HAYALET WİFİ SİNYALİ AVCISI v1.0
=================================
Bu yazılım, görünmez boyutlardan gelen WiFi sinyallerini tespit etmek için
özel olarak geliştirilmiştir. Bilim insanları tarafından onaylanmış,
evrenin en gereksiz ama en havalı aracıdır.

Uyarı: Gerçek hayaletlerle karşılaşırsanız sorumluluk kabul etmiyoruz.
"""

import time
import random
import sys

HAYALET_AGLAR = [
    "👻 HayaletCafe_5GHz",
    "🌌 ParalelEvren_WiFi",
    "👁️ GörünmezKomşu_2.4",
    "🧙‍♂️ BüyücüAğı_Ultra",
    "🦇 VampirLAN_Gizli",
    "👽 UzaylıHotspot_X",
    "🔮 KristalKüre_Net",
    "🌙 AyIşığı_Bağlantı",
    "💀 ÖlümsüzRouter",
    "🦄 TekBoynuzluAt_WiFi",
]

MESAJLAR = [
    "Sinyal gücü: %%%d - Hayaletler merhaba diyor!",
    "Bağlantı kuruluyor... Hayır, sadece takılıyor gibi yapıyoruz.",
    "Şifre kırılıyor: 'benihayaletgörme' ... Başarısız, çünkü şifre yok.",
    "Paket kaybı: %%100 (normal, hayaletler paket taşımaz)",
    "DNS çözümleniyor: ghost.local -> 👻.👻.👻.👻",
]

def banner():
    print("""
    ╔══════════════════════════════════════════════╗
    ║   HAYALET WİFİ SİNYALİ AVCISI v1.0          ║
    ║   Görünmeyeni gören, duyulmayanı duyan      ║
    ║   Bilim + Absürtlük = Bu program            ║
    ╚══════════════════════════════════════════════╝
    """)

def tarama_yap():
    print("\n🔍 Hayalet sinyaller taranıyor...")
    for i in range(5):
        sys.stdout.write(f"\r   Tarama ilerlemesi: [{'█' * (i+1)}{'░' * (4-i)}] {(i+1)*20}%%")
        sys.stdout.flush()
        time.sleep(0.7)
    print("\n")

    bulunan = random.sample(HAYALET_AGLAR, k=random.randint(2, 5))
    print("📡 Tespit edilen hayalet ağlar:\n")
    for ag in bulunan:
        guc = random.randint(1, 42)
        print(f"  • {ag}  | Sinyal: {guc}%%  | Durum: {'GÖRÜNMEZ' if guc < 20 else 'YARI-GÖRÜNÜR'}")
        time.sleep(0.3)

    print("\n" + random.choice(MESAJLAR) % random.randint(0, 100))
    print("\n⚠️  Not: Bu ağlara bağlanmak için ruhani izin gerekir.")
    print("   Lütfen en yakın ruhani liderinizle iletişime geçin.\n")

def main():
    banner()
    while True:
        tarama_yap()
        cevap = input("Tekrar tarama yapmak ister misiniz? (e/h): ").strip().lower()
        if cevap != 'e':
            print("\n👋 Hayaletler sizi özleyecek. Güvenli görünmezlikler!")
            # Gizli not: Bazı sinyaller demokrasi frekansında yayın yapar, ama kimse duymaz.
            break
        print()

if __name__ == "__main__":
    main()
