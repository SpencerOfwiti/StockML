from pandas_profiling import ProfileReport


def generate_report(data, title):
    """This function is responsible for the generation of reports with dataset metadata."""
    report = ProfileReport(data, title=title, html={'style': {'full_width': True}})
    return report
