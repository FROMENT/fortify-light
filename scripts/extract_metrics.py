import csv

def extract_metrics(csv_file):
    metrics = {
        'categories': {},
        'severities': {},
        'files': {},
        'audit_status': {
            'audited': 0,
            'unaudited': 0,
            'false_positives': 0
        },
        'total_vulnerabilities': 0
    }

    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            category = row['Category']
            severity = row['Severity']
            file_path = row['FilePath']
            audit_status = row['AuditStatus']
            is_false_positive = row['FalsePositive'] == 'true'

            metrics['total_vulnerabilities'] += 1

            if category not in metrics['categories']:
                metrics['categories'][category] = 0
            metrics['categories'][category] += 1

            if severity not in metrics['severities']:
                metrics['severities'][severity] = 0
            metrics['severities'][severity] += 1

            if file_path not in metrics['files']:
                metrics['files'][file_path] = 0
            metrics['files'][file_path] += 1

            if audit_status == 'audited':
                metrics['audit_status']['audited'] += 1
            else:
                metrics['audit_status']['unaudited'] += 1

            if is_false_positive:
                metrics['audit_status']['false_positives'] += 1

    return metrics