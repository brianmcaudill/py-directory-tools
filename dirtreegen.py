import os
import argparse
from pathlib import Path

class DirectoryTreeGenerator:
    def __init__(self, root_dir, output_file="directory_structure.md", ignore_patterns=None):
        """
        Initialize the directory tree generator.
        
        Args:
            root_dir (str): Root directory path
            output_file (str): Output markdown file name
            ignore_patterns (list): List of patterns to ignore (e.g., ['.git', '__pycache__'])
        """
        self.root_dir = Path(root_dir)
        self.output_file = output_file
        self.ignore_patterns = ignore_patterns or ['.git', '__pycache__', '.pytest_cache', 'node_modules']
        
    def should_ignore(self, path):
        """Check if the path should be ignored based on ignore patterns."""
        return any(pattern in str(path) for pattern in self.ignore_patterns)
    
    def generate_tree(self, directory=None, prefix='', is_last=True, level=0):
        """
        Recursively generate the directory tree structure.
        
        Args:
            directory (Path): Current directory being processed
            prefix (str): Prefix for the current line
            is_last (bool): Whether this is the last item in the current level
            level (int): Current directory depth
            
        Returns:
            list: Lines of the tree structure
        """
        if directory is None:
            directory = self.root_dir
            
        tree_lines = []
        
        # Add the root directory only at the first level
        if level == 0:
            tree_lines.append(f"{directory.name}/")
        
        # Get all items in the directory
        items = sorted(list(directory.iterdir()), key=lambda x: (x.is_file(), x.name.lower()))
        items = [item for item in items if not self.should_ignore(item)]
        
        for index, item in enumerate(items):
            is_last_item = index == len(items) - 1
            
            # Create the appropriate prefix
            if level > 0:
                current_prefix = prefix + ('└── ' if is_last_item else '├── ')
            else:
                current_prefix = prefix
            
            # Add the current item to the tree
            tree_lines.append(f"{current_prefix}{item.name}{'/' if item.is_dir() else ''}")
            
            # Recursively process directories
            if item.is_dir():
                # Calculate the new prefix for the next level
                new_prefix = prefix + ('    ' if is_last_item else '│   ')
                # Recursively generate tree for subdirectory
                tree_lines.extend(self.generate_tree(
                    item,
                    new_prefix,
                    is_last_item,
                    level + 1
                ))
        
        return tree_lines
    
    def save_to_markdown(self):
        """Generate and save the directory tree to a markdown file."""
        tree_lines = self.generate_tree()
        
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write("# Directory Structure\n\n")
            f.write("```\n")
            f.write("\n".join(tree_lines))
            f.write("\n```\n")
        
        print(f"Directory tree has been saved to {self.output_file}")

def main():
    parser = argparse.ArgumentParser(description='Generate a directory tree structure in markdown format.')
    parser.add_argument('directory', help='Root directory path')
    parser.add_argument('-o', '--output', default='directory_structure.md',
                       help='Output markdown file name (default: directory_structure.md)')
    parser.add_argument('-i', '--ignore', nargs='+', default=None,
                       help='Patterns to ignore (e.g., .git __pycache__)')
    
    args = parser.parse_args()
    
    try:
        generator = DirectoryTreeGenerator(
            args.directory,
            args.output,
            args.ignore
        )
        generator.save_to_markdown()
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()