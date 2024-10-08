# DON'T RUN THIS; DON'T OVERWRITEW THE _variables.yml FILE


# import hashlib
# import re
# from pathlib import Path

# import click
# import yaml

# import icsspy
# from icsspy.paths import root

# logger = icsspy.initialize_logger()


# def find_yaml_files(directory):
#     yaml_files = [
#         file
#         for file in directory.rglob("*.yaml")
#         if not file.is_symlink() and "pdpp" not in file.name
#     ]
#     yaml_files.extend(
#         [
#             file
#             for file in directory.rglob("*.yml")
#             if not file.is_symlink() and "pdpp" not in file.name
#         ]
#     )
#     return yaml_files


# def load_yaml_files(yaml_files):
#     yaml_contents = []
#     seen_hashes = set()

#     for file in yaml_files:
#         with file.open("r") as f:
#             content = f.read()
#             content_hash = hashlib.md5(content.encode("utf-8")).hexdigest()

#             if content_hash not in seen_hashes:
#                 seen_hashes.add(content_hash)
#                 yaml_contents.append((file, yaml.safe_load(content)))

#     return yaml_contents


# def flatten_dict(d, parent_key="", sep="_"):
#     items = []
#     for k, v in d.items():
#         new_key = f"{parent_key}{sep}{k}" if parent_key else k
#         if isinstance(v, dict):
#             items.extend(flatten_dict(v, new_key, sep=sep).items())
#         elif isinstance(v, list):
#             # Join list items into a string separated by ', ' and enclose in ""
#             joined_list = ", ".join(map(str, v))
#             items.append((new_key, f'"{joined_list}"'))
#         else:
#             if isinstance(v, str):
#                 # Replace spaces in the middle of strings with hyphens
#                 v = re.sub(r"(?<!^)\s(?!$)", "-", v)
#                 # Enclose in double quotes
#                 v = f'"{v}"'
#             items.append((new_key, v))
#     return dict(items)


# def write_combined_yaml(yaml_contents, output_file):
#     with output_file.open("w") as f:
#         f.write(
#             "# This file was generated by `poetry run collect-configs`, do not edit\n\n"
#         )

#         for file, content in yaml_contents:
#             # Write a comment with the file path
#             f.write(f"# {file}\n")

#             # Flatten the content
#             flattened_content = flatten_dict(content)

#             # Dump the current flattened content as YAML after the comment
#             yaml.dump(
#                 flattened_content, f, default_flow_style=False, width=float("inf")
#             )
#             f.write("\n")


# @click.command()
# @click.option(
#     "--directory",
#     default=str(root / "pipelines/youtube"),
#     help="Path to the directory containing YAML files.",
# )
# @click.option(
#     "--output_file",
#     default=str(root / "slides/_variables.yml"),
#     help="Path to the output YAML file.",
# )
# def main(directory, output_file):
#     directory = Path(directory)
#     output_file = Path(output_file)

#     yaml_files = find_yaml_files(directory)
#     if not yaml_files:
#         logger.info(f"No YAML files found in directory: {directory}")
#         return

#     yaml_contents = load_yaml_files(yaml_files)
#     write_combined_yaml(yaml_contents, output_file)
#     logger.info(f"Combined YAML written to: {output_file}")


# if __name__ == "__main__":
#     main()
