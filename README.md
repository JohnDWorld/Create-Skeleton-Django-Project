# Générateur de projets Django

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Django](https://img.shields.io/badge/Django-Automation-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

## 📌 Description

Ce projet permet de générer automatiquement une structure Django complète à partir d'un fichier JSON de configuration. L'objectif est d'accélérer la mise en place de projets en automatisant la création des applications, modèles, templates et autres éléments essentiels.

### ✅ Actions réalisées par `main.py` :

- 📂 Création de l'environnement virtuel `src/venv`.
- 📦 Installation des dépendances renseignées dans l'environnement virtuel.
- 🏗️ Création du projet Django dans `projects/`.
- 🛠️ Mise à jour de `settings.py` pour gérer les fichiers statiques et intégrer les applications créées.
- 🔗 Mise à jour du fichier `urls.py`.
- 🎨 Création des templates à partir des fichiers présents dans `templates/html`.
- 📁 Mise en place du dossier `uploads` (si demandé).
- 💅 Intégration automatique de Bootstrap 5 (si demandé).

### 🔧 Actions réalisées par application créée :

- 🏗️ Mise à jour de `models.py` et création de `forms.py` (si demandé).
- 🔗 Modification du fichier `urls.py`.
- 🛠️ Mise à jour de `admin.py`.
- 🎨 Création des templates à partir des fichiers présents dans `templates/html`.

Il ne vous reste plus qu'à ajuster les paramètres dans `models.py` et à peaufiner l'interface utilisateur de votre projet.

ℹ️ **Si vous modifiez** `project_config.json` **et relancer** `main.py`**, vous aurez le choix de réécrire ou de conserver les fichiers Python existants.**

‼️ **ATTENTION : Les templates originaux sont disponibles dans le dossier** `templates`**. Cependant, si vous retirez les balises {bootstrapscript} et {bootstrapcss} dans template/base.html, l'intégration automatique de Bootstrap ne sera plus effectuée.** ‼️

---

## 🚀 Prérequis

- Python installé sur votre machine (version 3.x recommandée).

## 🏗️ Installation

1. **Cloner le projet**

   ```sh
   git clone https://github.com/JohnDWorld/Create-Skeleton-Django-Project.git
   cd Create-Skeleton-Django-Project
   ```

2. **Préparer le fichier de configuration**

   - Copier `skeleton.json` depuis `documentation/`, le coller dans `src/` et le renommer en `project_config.json`.
   - Adapter les paramètres selon vos besoins.
   - Les dépendances seront installées automatiquement en fonction de la liste renseignée dans `project_config.json`.

3. **Lancer la génération du projet**
   ```sh
   python src/main.py
   ```

Le projet sera créé dans le dossier `projects/`.

---

## ⚙️ Configuration

Le fichier `project_config.json` permet de définir :

- 📌 Le nom du projet.
- 🛢️ Les paramètres de la base de données.
- 📂 Les applications et modèles à générer.
- 🎨 Les templates et fichiers statiques associés.

### 📜 Exemple de structure :

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
  },
  "dependencies": [],
  "uploads": false,
  "bootstrap": true
}
```

---

## 🎯 Fonctionnalités

✔️ Création automatique des modèles avec administration Django.  
✔️ Génération des templates et fichiers statiques.  
✔️ Structure prête à l’emploi pour un projet Django.  
✔️ Ajout de la gestion des dépendances.  
✔️ Intégration automatique de Bootstrap 5.

---

## 🔮 Améliorations futures

- 🚀 Installation automatique de React JS.
- 🚀 Utilisation d'un autre type de BDD.

---

## 📜 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🤝 Contribuer

Les contributions sont les bienvenues ! Pour proposer une amélioration :

1. Forkez le projet 🍴.
2. Créez une branche (`git checkout -b feature-amazing-feature`).
3. Commitez vos modifications (`git commit -m 'Ajout d’une fonctionnalité géniale'`).
4. Poussez vers la branche (`git push origin feature-amazing-feature`).
5. Ouvrez une Pull Request 🚀.

---

## 📞 Contact

👤 **JohnDWorld**  
📧 Email : j.demory40@gmail.com
🐙 GitHub : [JohnDWorld](https://github.com/JohnDWorld)

Merci d'utiliser ce générateur de projets Django ! 🎉
