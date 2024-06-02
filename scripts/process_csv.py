import csv

def issues_to_csv(issues, csv_file):
    fieldnames = [
        'Category', 'Severity', 'FilePath', 'AuditStatus', 'FalsePositive'
    ]
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for issue in issues:
            writer.writerow({
                'Category': issue['category'],
                'Severity': issue['severity'],
                'FilePath': issue['primaryLocation']['filePath'],
                'AuditStatus': issue['audited'],
                'FalsePositive': issue['auditorComment'] == 'False Positive'
            })

if __name__ == "__main__":
    # Sample data for testing
    issues = [
        {
            'category': 'SQL Injection',
            'severity': 'High',
            'primaryLocation': {'filePath': 'src/app.py'},
            'audited': 'audited',
            'auditorComment': 'False Positive'
        }
    ]
    issues_to_csv(issues, 'data/vulnerabilities.csv')
    print("CSV file generated.")