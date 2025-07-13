"""
Single Responsibility Principle (SRP)

A class should have one, and only one, reason to change.

This principle helps us build focused, maintainable, and testable components.
"""

# ❌ Anti-Example: Violates SRP by mixing data, formatting, and I/O
class Report:
    """
    Handles report data, formatting, and saving — too many responsibilities.
    """
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def format_html(self):
        return f"<h1>{self.title}</h1><p>{self.content}</p>"

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.format_html())


# ✅ SRP-Compliant Version
class Report:
    """
    Represents report data only.
    """
    def __init__(self, title, content):
        self.title = title
        self.content = content


class HTMLFormatter:
    """
    Responsible for formatting a Report as HTML.
    """
    def format(self, report: Report) -> str:
        return f"<h1>{report.title}</h1><p>{report.content}</p>"


class FileSaver:
    """
    Responsible for saving content to a file.
    """
    def save(self, content: str, filename: str):
        with open(filename, 'w') as f:
            f.write(content)


# ✅ Usage Example
if __name__ == "__main__":
    report = Report("Quarterly Update", "All systems operational.")
    formatter = HTMLFormatter()
    saver = FileSaver()

    html_content = formatter.format(report)
    saver.save(html_content, "report.html")
