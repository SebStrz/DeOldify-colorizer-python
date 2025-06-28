# 🎨 DeOldify Photo Colorizer

Aplikacja oparta na bibliotece **DeOldify**, umożliwiająca automatyczne kolorowanie czarno-białych zdjęć przy użyciu sztucznej inteligencji.

---

## 📦 Wymagania

Aby uruchomić projekt, potrzebujesz:

- ✅ **Python 3.8+** *(zalecana instalacja przez Anaconda)*
- ✅ **pip** *(zazwyczaj dołączony do Pythona)*
- ✅ **Anaconda** *(https://www.anaconda.com/download)*

> 💡 Zalecana instalacja przez Anacondę zapewnia łatwe zarządzanie środowiskami i zależnościami.

---

## 🚀 Instalacja i uruchomienie

### 1. Zainstaluj Anacondę

Pobierz i zainstaluj Anacondę dla swojego systemu operacyjnego:
👉 https://www.anaconda.com/download

---

### 2. Otwórz **Anaconda Prompt**

Wyszukaj „Anaconda Prompt” i uruchom go jako administrator (jeśli to możliwe).

---

### 3. Przejdź do katalogu projektu

```bash
cd ŚCIEŻKA\DO\REPOZYTORIUM
cd src
```

Zamień `ŚCIEŻKA\DO\REPOZYTORIUM` na ścieżkę, gdzie sklonowałeś repozytorium.

---

### 4. Utwórz środowisko Conda

```bash
conda env create -f environment.yml
```

---

### 5. Aktywuj środowisko

```bash
source activate deoldify
```

> Na Windowsie możesz też użyć:
> ```bash
> conda activate deoldify
> ```

---

### 6. Uruchom program

```bash
python main.py
```

---

## 🧪 Testowe zdjęcie

Po uruchomieniu, program poprosi o podanie ścieżki do zdjęcia.
Zostanie ono automatycznie pokolorowane i zapisane w folderze wynikowym.

## Podstawowe GUI

Aby uruchomić GUI które stworzyłem:

### 1. Dociągnij wymagane biblioteki:
```bash
pip install tkinterdnd2 pillow
```

---

### 2. Uruchom aplikacje:
```bash
python front.py
```
