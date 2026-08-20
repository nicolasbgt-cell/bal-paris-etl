# bal-paris-etl

*[English](#english) | [Français](#français)*

---

## English

An ETL (Extract, Transform, Load) pipeline that loads address data from the Local Address Base (BAL) for the 15th arrondissement of Paris, cleans it, and inserts it into a SQLite database.

### Description

This project takes an official export from the [Base Adresse Locale](https://adresse.data.gouv.fr) (French national address database) in CSV format — geolocated addresses, street numbers, street names, coordinates — and turns it into a queryable SQLite database.

The goal is to practice the standard ETL pattern on a real-world dataset:

- **Extract**: load the raw CSV
- **Transform**: clean the data (duplicates, coordinate validation, type handling)
- **Load**: insert into a SQLite database (`adresses.db`)

### Project structure

```
bal-paris-etl/
├── data/
│   └── bal-75115.csv       # raw source (BAL, Paris 15th arrondissement)
├── src/
│   ├── extract.py           # E step
│   ├── transform.py         # T step
│   └── load.py              # L step
├── adresses.db               # generated SQLite database (not versioned)
├── requirements.txt
└── README.md
```

### Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Usage

Run the full pipeline:

```bash
python src/load.py
```

This script runs extraction, transformation, and loading in sequence, and prints the number of rows inserted into `adresses.db`.

#### Running a single step

```bash
python src/extract.py     # check raw CSV loading
python src/transform.py   # check cleaning (prints missing values per column)
```

#### Querying the database

```bash
sqlite3 adresses.db "SELECT COUNT(*) FROM adresses;"
sqlite3 adresses.db "SELECT voie_nom, numero FROM adresses LIMIT 5;"
sqlite3 adresses.db "SELECT voie_nom, COUNT(*) as nb FROM adresses GROUP BY voie_nom ORDER BY nb DESC LIMIT 5;"
```

### Data

Source: [adresse.data.gouv.fr](https://adresse.data.gouv.fr) — **Local Format (BAL)** export, Paris 15th arrondissement (INSEE code 75115).

Main columns in the source CSV: `cle_interop`, `commune_nom`, `voie_nom`, `numero`, `suffixe`, `commune_insee`, `position`, `x`, `y`, `cad_parcelles`, `source`, `date_der_maj`, `long`, `lat`, `certification_commune`, `id_ban_commune`, `id_ban_toponyme`, `id_ban_adresse`.

### Cleaning applied

- Removed duplicates on `cle_interop` (the address's unique identifier)
- Converted `lat`/`long` to numeric, with invalid-value handling
- Removed rows without usable coordinates

### Database

- Engine: SQLite (local file, no server setup needed)
- Table: `adresses`
- `adresses.db` is regenerated on every run (`if_exists="replace"`) — no duplicate accumulation between runs

---

## Français

Pipeline ETL (Extract, Transform, Load) qui charge les adresses de la Base Adresse Locale (BAL) du 15e arrondissement de Paris, les nettoie, et les insère dans une base SQLite.

### Description

Ce projet prend en entrée un export officiel de la [Base Adresse Locale](https://adresse.data.gouv.fr) au format CSV (adresses géolocalisées, numéros, voies, coordonnées) et le transforme en une base de données SQLite exploitable via des requêtes SQL.

L'objectif est de pratiquer le pattern ETL de base sur un vrai jeu de données :

- **Extract** : chargement du CSV brut
- **Transform** : nettoyage (doublons, validation des coordonnées, gestion des types)
- **Load** : insertion dans une base SQLite (`adresses.db`)

### Structure du projet

```
bal-paris-etl/
├── data/
│   └── bal-75115.csv       # source brute (BAL, 15e arrondissement de Paris)
├── src/
│   ├── extract.py           # étape E
│   ├── transform.py         # étape T
│   └── load.py              # étape L
├── adresses.db               # base SQLite générée (non versionnée)
├── requirements.txt
└── README.md
```

### Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Utilisation

Lancer le pipeline complet :

```bash
python src/load.py
```

Ce script exécute successivement l'extraction, la transformation, puis le chargement, et affiche le nombre de lignes insérées dans `adresses.db`.

#### Exécuter une étape isolément

```bash
python src/extract.py     # vérifie le chargement du CSV brut
python src/transform.py   # vérifie le nettoyage (affiche les valeurs manquantes)
```

#### Interroger la base

```bash
sqlite3 adresses.db "SELECT COUNT(*) FROM adresses;"
sqlite3 adresses.db "SELECT voie_nom, numero FROM adresses LIMIT 5;"
sqlite3 adresses.db "SELECT voie_nom, COUNT(*) as nb FROM adresses GROUP BY voie_nom ORDER BY nb DESC LIMIT 5;"
```

### Données

Source : [adresse.data.gouv.fr](https://adresse.data.gouv.fr) — export **Format Local (BAL)**, commune de Paris 15e (code INSEE 75115).

Colonnes principales du CSV source : `cle_interop`, `commune_nom`, `voie_nom`, `numero`, `suffixe`, `commune_insee`, `position`, `x`, `y`, `cad_parcelles`, `source`, `date_der_maj`, `long`, `lat`, `certification_commune`, `id_ban_commune`, `id_ban_toponyme`, `id_ban_adresse`.

### Nettoyage appliqué

- Suppression des doublons sur `cle_interop` (identifiant unique de l'adresse)
- Conversion de `lat`/`long` en numérique, avec gestion des valeurs invalides
- Suppression des lignes sans coordonnées exploitables

### Base de données

- Moteur : SQLite (fichier local, aucune configuration serveur)
- Table : `adresses`
- Le fichier `adresses.db` est régénéré à chaque exécution (`if_exists="replace"`) — pas d'accumulation de doublons entre deux lancements
