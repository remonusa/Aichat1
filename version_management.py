# version_management.py - Git version management helper script
# Location: Root directory of the application

import subprocess
import sys
import os
from datetime import datetime

def run_command(command):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def check_git_status():
    """Check if we're in a git repository"""
    success, stdout, stderr = run_command("git status")
    return success

def initialize_git():
    """Initialize git repository if not already done"""
    if not check_git_status():
        print("Initializing Git repository...")
        success, stdout, stderr = run_command("git init")
        if success:
            print("✅ Git repository initialized")
        else:
            print("❌ Failed to initialize Git repository")
            return False
    return True

def add_and_commit():
    """Add all files and commit"""
    print("Adding files to Git...")
    success, stdout, stderr = run_command("git add .")
    if not success:
        print("❌ Failed to add files")
        return False
    
    print("Committing changes...")
    commit_message = f"AI Chat Version 1 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    success, stdout, stderr = run_command(f'git commit -m "{commit_message}"')
    if success:
        print("✅ Changes committed successfully")
        return True
    else:
        print("❌ Failed to commit changes")
        return False

def create_tag(tag_name):
    """Create a Git tag"""
    print(f"Creating tag '{tag_name}'...")
    success, stdout, stderr = run_command(f"git tag {tag_name}")
    if success:
        print(f"✅ Tag '{tag_name}' created successfully")
        return True
    else:
        print(f"❌ Failed to create tag '{tag_name}'")
        return False

def push_to_github():
    """Push to GitHub (requires remote to be set up)"""
    print("Pushing to GitHub...")
    success, stdout, stderr = run_command("git push origin main")
    if success:
        print("✅ Pushed to GitHub successfully")
        return True
    else:
        print("❌ Failed to push to GitHub")
        print("Make sure you have set up the remote repository")
        return False

def push_tags():
    """Push tags to GitHub"""
    print("Pushing tags to GitHub...")
    success, stdout, stderr = run_command("git push origin --tags")
    if success:
        print("✅ Tags pushed to GitHub successfully")
        return True
    else:
        print("❌ Failed to push tags to GitHub")
        return False

def show_help():
    """Show help information"""
    print("""
AI Chat Version Management Script

Usage:
    python version_management.py [command]

Commands:
    init        - Initialize Git repository and create first commit
    tag <name>  - Create a new tag (e.g., python version_management.py tag ver1)
    push        - Push to GitHub (requires remote setup)
    help        - Show this help message

Examples:
    python version_management.py init
    python version_management.py tag ver1
    python version_management.py push

To download a specific version:
    git clone <repository-url>
    git checkout <tag-name>
    Example: git checkout ver1
    """)

def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    if command == "init":
        if initialize_git():
            if add_and_commit():
                print("✅ Repository initialized and first commit created")
            else:
                print("❌ Failed to create initial commit")
        else:
            print("❌ Failed to initialize repository")

    elif command == "tag":
        if len(sys.argv) < 3:
            print("❌ Please provide a tag name")
            print("Example: python version_management.py tag ver1")
            return
        
        tag_name = sys.argv[2]
        if create_tag(tag_name):
            print(f"✅ Tag '{tag_name}' created successfully")
            print(f"To push this tag: python version_management.py push")

    elif command == "push":
        if push_to_github():
            push_tags()
        else:
            print("❌ Failed to push to GitHub")

    elif command == "help":
        show_help()

    else:
        print(f"❌ Unknown command: {command}")
        show_help()

if __name__ == "__main__":
    main() 