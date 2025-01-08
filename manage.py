#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import webbrowser
import time

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chiddhu.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Open the browser after a short delay to ensure the server is running
    def open_browser():
        time.sleep(1)  # Give the server a moment to start
        webbrowser.open('http://127.0.0.1:8000')

    if 'runserver' in sys.argv:
        # Start the browser in a new thread
        import threading
        threading.Thread(target=open_browser).start()

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

