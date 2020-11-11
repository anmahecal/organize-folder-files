# :file_folder: Organize-Folder-Files

CLI named **groot** develop to automate folders organization by spliting files into extension related folders.

## :card_index_dividers: Supported file extensions and folders

|File type | Extensions |
| -------- | ---------- |
| PDF: | `.pdf` |
| Images: | `.jpg` `.jpeg` `.png` |
| Office Files: | `.docx` `.xlsx` `.pptx`|
| MS Installers and executables: | `.exe` `.msi` |

## Installation

Install groot via **pip** from project root folder (where setup.py is).

`pip install .`

## Cli commands

#### Organize file in current folder

`groot organize`

#### Show supported extensions

`groot extensions`

#### Create a custom settings file 
`groot extensions --create`

#### Edit file using notepad

`groot extensions --edit`