# Algorytm Kruskala – Minimalne Drzewo Rozpinające

**Projekt zaliczeniowy z przedmiotu: Grafy i Sieci**  
**Autorzy:** Jakub Szych, Jakub Orchowski  
**Termin:** czerwiec 2025

---

## 📌 Opis

Celem projektu jest zaimplementowanie algorytmu Kruskala w języku Python do wyznaczania **minimalnego drzewa rozpinającego (MST)** w spójnym, nieskierowanym grafie z wagami dodatnimi.

Minimalne drzewo rozpinające (MST) znajduje zastosowania m.in. w:
- projektowaniu sieci komputerowych,
- optymalizacji połączeń transportowych,
- redukcji kosztów w systemach połączeń.

---

## 📁 Zawartość repozytorium

| Plik / folder                 | Opis                                                                 |
|------------------------------|----------------------------------------------------------------------|
| `AlgKruskal.py`              | Główna implementacja algorytmu Kruskala w Pythonie                  |
| `graph.txt`                  | Przykładowe dane wejściowe do programu                              |
| `mst.txt`                    | Przykładowy wynik działania programu                                |
| `Sprawozdanie_Kruskal_FINAL.docx` | Gotowe sprawozdanie do oddania                                     |
| `dist/AlgKruskal.exe`        | Skonwertowany program do pliku `.exe` (wersja Windows)              |
| `build/`, `AlgKruskal.spec`  | Pliki tymczasowe utworzone przez PyInstaller                        |

---

## 🔧 Uruchamianie programu

### ✔️ Wersja Python
Upewnij się, że masz zainstalowanego Pythona (3.7+), a następnie uruchom:

```bash
python AlgKruskal.py graph.txt


