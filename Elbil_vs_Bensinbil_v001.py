# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:19:01 2024

@author: knutj
"""

Ant_km = 10000 ## Antall kjørt km i året
Eb_Fo = 5000 ## Elbil forsikring
Bb_Fo = 7500 ##Bensinbil forsikring
Tf = 8.33*365 ## Trafikkforsikring 8.33 kr/dag
Eb_Bp = 0.1*Ant_km ## Bompenger for Elbil er 0.1 kr/km
Bb_Bp = 0.3*Ant_km ## Bompenger for Bensinbil er 0,3/km
Eb_Forb = 0.2*2*Ant_km ## Elbil forbruk er 0,2kWt/km. Pris 2 kr/kWt
Bb_Forb = 1*Ant_km ## Bensinbil forbruk er 1 kr/km

Eb_Kost = Eb_Fo + Eb_Bp + Tf + Eb_Forb ## Elbil kost er lik Forsikring + Trafikkforsikring + Bompenger + Forbruk
print(Eb_Kost)

Bb_Kost = Bb_Fo + Bb_Bp + Tf + Bb_Forb ## Bensinbil kost er lik Forsikring + Trafikkforsikring + Bompenger + Forbruk
print(Bb_Kost)

Diff = Bb_Kost - Eb_Kost
print(f"Forskjell i driftskostnader mellom Elbil og Bensinbil er {Diff:.2f}kr") ## Forskjellen er formatert med 2 desimaler