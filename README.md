# Générateur de projets Django

## Description  
Ce projet permet de générer automatiquement une structure Django complète à partir d'un fichier JSON de configuration. L'objectif est d'accélérer la mise en place de projets en automatisant la création des applications, modèles, templates et autres éléments essentiels.

## Prérequis  
- Python installé sur votre machine (version 3.x recommandée)  
- `virtualenv` (optionnel mais recommandé)  

## Installation  

1. **Cloner le projet**  
   ```sh
   git clone <URL_DU_REPO>
   cd <NOM_DU_PROJET>
   ```

2. **Créer un environnement virtuel**  
   ```sh
   python -m venv src/venv
   ```

3. **Activer l’environnement virtuel**  
   - Sur Windows :  
     ```sh
     src/venv/Scripts/activate
     ```
   - Sur Mac/Linux :  
     ```sh
     source src/venv/bin/activate
     ```

4. **Préparer le fichier de configuration**  
   - Copier le fichier `skeleton.json` depuis `documentation/` et le renommer en `project_config.json`  
   - Adapter les paramètres selon vos besoins  

5. **Lancer la génération du projet**  
   ```sh
   python src/main.py
   ```

Le projet sera créé dans le dossier `projects/`.

## Configuration  
Le fichier `project_config.json` permet de définir :  
- Le nom du projet  
- Les paramètres de la base de données  
- Les applications et modèles à générer  
- Les templates et fichiers statiques associés  

Exemple de structure :
```json
{
  "project": "MonProjet",
  "settings": {
    "language_html": "fr",
    "database": "sqlite3"
  },
  "apps": {
    "website": {
      "webpage": {
        "templates": true,
        "static": true
      }
    }
  }
}
```

## Fonctionnalités  
✔️ Création automatique des modèles avec administration Django  
✔️ Génération des templates et fichiers statiques  
✔️ Structure prête à l’emploi pour un projet Django  

## Améliorations futures  
- Ajout de la gestion des dépendances  
- Intégration de Bootstrap automatique  
- Génération des vues et URLs  

