from fetch_data import fetch_projects, fetch_project_versions, fetch_updated_issues
from initialize_db import initialize_database
from extract_metrics import extract_metrics
from save_metrics import save_metrics_to_db
from copy_metrics import copy_metrics_from_previous_week

def main():
    initialize_database()
    last_update_date = '2024-01-01T00:00:00Z'
    projects = fetch_projects()
    if projects is not None:
        for project in projects:
            project_id = project['id']
            versions = fetch_project_versions(project_id)
            if versions is not None:
                for version in versions:
                    version_id = version['id']
                    issues = fetch_updated_issues(version_id, last_update_date)
                    if issues is not None and len(issues) > 0:
                        # Assuming you have a way to convert issues to a CSV file named 'data/vulnerabilities.csv'
                        metrics = extract_metrics('data/vulnerabilities.csv')
                        save_metrics_to_db(metrics, project_id, version_id)
                    else:
                        print(f"No changes for version ID: {version_id}. Copying metrics from previous week.")
                        copy_metrics_from_previous_week(project_id, version_id)
            else:
                print(f"Failed to fetch versions for project ID: {project_id}")
    else:
        print("Failed to fetch projects")

if __name__ == "__main__":
    main()