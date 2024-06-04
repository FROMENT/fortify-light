# Résumé des Appels API Fortify SSC et des Tables de Données
https://fortify-dev.tools.sap/ssc/html/docs/api-reference/index.jsp)
## Détails des Appels API

### Obtenir la Liste des Projets
- **Endpoint**: `/api/v1/projects`
- **Méthode**: `GET`
- **Description**: Récupère la liste de tous les projets disponibles dans Fortify SSC.
- **Exemple de Requête**: `GET https://your-ssc-server/ssc/api/v1/projects`
- **Champs de Réponse Importants**:
  - `id`: Identifiant unique du projet
  - `name`: Nom du projet
  - `description`: Description du projet
  - `created`: Date de création du projet
  - `updated`: Date de la dernière mise à jour du projet

### Obtenir les Versions de Projet
- **Endpoint**: `/api/v1/projects/{projectId}/versions`
- **Méthode**: `GET`
- **Description**: Récupère les versions d'un projet spécifique.
- **Exemple de Requête**: `GET https://your-ssc-server/ssc/api/v1/projects/{projectId}/versions`
- **Champs de Réponse Importants**:
  - `id`: Identifiant unique de la version
  - `name`: Nom de la version
  - `created`: Date de création de la version
  - `updated`: Date de la dernière mise à jour de la version
  - `startDate`: Date de début de la version
  - `dueDate`: Date d'échéance de la version

### Obtenir les Issues d'une Version de Projet
- **Endpoint**: `/api/v1/projectVersions/{projectVersionId}/issues`
- **Méthode**: `GET`
- **Description**: Récupère les vulnérabilités d'une version spécifique de projet.
- **Exemple de Requête**: `GET https://your-ssc-server/ssc/api/v1/projectVersions/{projectVersionId}/issues`
- **Champs de Réponse Importants**:
  - `issueId`: Identifiant unique de la vulnérabilité
  - `issueName`: Nom de la vulnérabilité
  - `status`: Statut de la vulnérabilité
  - `audited`: Indicateur si la vulnérabilité a été auditée
  - `removed`: Indicateur si la vulnérabilité a été supprimée
  - `foundDate`: Date de découverte de la vulnérabilité
  - `lastUpdateDate`: Date de la dernière mise à jour de la vulnérabilité
  - `firstDetectedDate`: Première date de détection de la vulnérabilité
  - `removedDate`: Date de suppression de la vulnérabilité

### Obtenir les Détails d'une Issue
- **Endpoint**: `/api/v1/issues/{issueId}`
- **Méthode**: `GET`
- **Description**: Récupère les détails d'une vulnérabilité spécifique.
- **Exemple de Requête**: `GET https://your-ssc-server/ssc/api/v1/issues/{issueId}`
- **Champs de Réponse Importants**:
  - `issueId`: Identifiant unique de la vulnérabilité
  - `issueName`: Nom de la vulnérabilité
  - `status`: Statut de la vulnérabilité
  - `audited`: Indicateur si la vulnérabilité a été auditée
  - `removed`: Indicateur si la vulnérabilité a été supprimée
  - `foundDate`: Date de découverte de la vulnérabilité
  - `lastUpdateDate`: Date de la dernière mise à jour de la vulnérabilité
  - `firstDetectedDate`: Première date de détection de la vulnérabilité
  - `removedDate`: Date de suppression de la vulnérabilité
  - `primaryLocation`: Localisation principale de la vulnérabilité dans le code
  - `analysisType`: Type d'analyse (e.g., Static, Dynamic)
  - `auditorComment`: Commentaire de l'auditeur
  - `reviewed`: Indicateur si la vulnérabilité a été revue
  - `scanStatus`: Statut du scan de la vulnérabilité
  - `details`: Détails supplémentaires de la vulnérabilité

### Obtenir l'Historique des Audits d'une Issue
- **Endpoint**: `/api/v1/issues/{issueId}/auditHistory`
- **Méthode**: `GET`
- **Description**: Récupère l'historique des audits d'une vulnérabilité spécifique.
- **Exemple de Requête**: `GET https://your-ssc-server/ssc/api/v1/issues/{issueId}/auditHistory`
- **Champs de Réponse Importants**:
  - `id`: Identifiant unique de l'audit
  - `issueId`: Identifiant unique de la vulnérabilité associée
  - `date`: Date de l'audit
  - `userName`: Nom de l'utilisateur ayant réalisé l'audit
  - `comment`: Commentaire de l'audit
  - `action`: Action réalisée lors de l'audit
  - `lastUpdateDate`: Date de la dernière mise à jour de l'audit

## Détails des Tables de Données

### Table: projects
- **Champs**:
  - `id`: INTEGER PRIMARY KEY
  - `name`: TEXT NOT NULL
  - `description`: TEXT
  - `created_at`: TEXT NOT NULL
  - `updated_at`: TEXT NOT NULL

### Table: project_versions
- **Champs**:
  - `id`: INTEGER PRIMARY KEY
  - `project_id`: INTEGER NOT NULL
  - `name`: TEXT NOT NULL
  - `description`: TEXT
  - `created_at`: TEXT NOT NULL
  - `updated_at`: TEXT NOT NULL
  - `start_date`: TEXT
  - `due_date`: TEXT
  - `FOREIGN KEY (project_id) REFERENCES projects(id)`

### Table: vulnerabilities
- **Champs**:
  - `id`: INTEGER PRIMARY KEY
  - `project_version_id`: INTEGER NOT NULL
  - `issue_name`: TEXT NOT NULL
  - `status`: TEXT NOT NULL
  - `audited`: BOOLEAN NOT NULL
  - `removed`: BOOLEAN NOT NULL
  - `found_date`: TEXT NOT NULL
  - `last_update_date`: TEXT NOT NULL
  - `first_detected_date`: TEXT
  - `removed_date`: TEXT
  - `primary_location`: TEXT
  - `analysis_type`: TEXT
  - `auditor_comment`: TEXT
  - `reviewed`: BOOLEAN
  - `scan_status`: TEXT
  - `created_at`: TEXT NOT NULL
  - `updated_at`: TEXT NOT NULL
  - `FOREIGN KEY (project_version_id) REFERENCES project_versions(id)`

### Table: analysis_details
- **Champs**:
  - `id`: INTEGER PRIMARY KEY
  - `vulnerability_id`: INTEGER NOT NULL
  - `severity`: TEXT
  - `category`: TEXT
  - `recommendation`: TEXT
  - `file_path`: TEXT
  - `line_number`: INTEGER
  - `code_snippet`: TEXT
  - `created_at`: TEXT NOT NULL
  - `updated_at`: TEXT NOT NULL
  - `FOREIGN KEY (vulnerability_id) REFERENCES vulnerabilities(id)`

### Table: audit_logs
- **Champs**:
  - `id`: INTEGER PRIMARY KEY
  - `vulnerability_id`: INTEGER
  - `action`: TEXT
  - `timestamp`: TEXT NOT NULL
  - `comment`: TEXT
  - `created_at`: TEXT NOT NULL
  - `FOREIGN KEY (vulnerability_id) REFERENCES vulnerabilities(id)`
