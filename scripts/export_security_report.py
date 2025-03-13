import json  # Import JSON module for report generation
import os  # Import OS module for file handling

def export_report(scan_results, output_file="data/reports/vulnerability_report.json"):  # Function to export scan results
    """Export scan results to a JSON file."""
    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Ensure directory exists
        with open(output_file, "w") as file:  # Open file in write mode
            json.dump(scan_results, file, indent=4)  # Write scan results as formatted JSON
        print(f"Report successfully exported to {output_file}")  # Confirmation message
    except Exception as e:
        print(f"Error exporting report: {e}")  # Print error message if export fails

if __name__ == "__main__":  # Main entry point for script execution
    sample_results = {
        "pipelines": ["Pipeline 1: No issues", "Pipeline 2: Secret exposed"],
        "builds": ["Build 10: Sensitive data detected"],
        "repositories": ["Repo A: Vulnerability found"]
    }  # Sample scan results
    export_report(sample_results)  # Call export function with sample data
