#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
"""
import os
import sys

def setup_media_directory():
    """
    Ensure the 'media' directory exists and has appropriate permissions.
    """
    media_path = os.path.join(os.getcwd(), 'media')
    try:
        if not os.path.exists(media_path):
            os.makedirs(media_path)  # Create the directory if it doesn't exist
            print(f"Created media directory at {media_path}")
        # Set permissions (only for non-sensitive environments)
        os.chmod(media_path, 0o755)  # rwxr-xr-x
    except Exception as e:
        print(f"Error setting up media directory: {e}")
        sys.exit(1)

def main():
    """
    Run administrative tasks.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv('DJANGO_SETTINGS_MODULE', 'backend.settings'))
    setup_media_directory()
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
