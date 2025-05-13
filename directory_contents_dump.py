import os

def write_full_file_dump(base_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as out:
        for root, dirs, files in os.walk(base_path):
            # Filter out node_modules directories
            dirs[:] = [d for d in dirs if d.lower() != 'node_modules']

            for file_name in files:
                file_path = os.path.join(root, file_name)
                rel_path = os.path.relpath(file_path, base_path)
                out.write(f"{rel_path}\n")
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                        contents = f.read()
                        out.write(contents)
                except Exception as e:
                    out.write(f"[Error reading file: {e}]")
                out.write("\n\n")  # Double newline for readability

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Dump all file paths and their contents to a single file.")
    parser.add_argument("directory", help="Path to the directory to scan")
    parser.add_argument("output", help="Path to the output file to write the dump")

    args = parser.parse_args()
    write_full_file_dump(args.directory, args.output)
    print(f"File dump written to {args.output}")
