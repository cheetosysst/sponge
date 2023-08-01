# Sponge

Sponge is a simple PDF data extraction tool, built specifically for parsing data
from [中華民國交通部公路總局-筆試題庫](https://www.thb.gov.tw/cl.aspx?n=12), and
for use in the [midnight](https://github.com/cheetosysst/midnight) project.

## Installation

1. Cloning

   ```bash
   git clone <https://github.com/sponge> --depth=1
   cd sponge
   ```

2. Activate

   Please activate the virtual env enviroment by running scripts compatible with
   you're system.

3. Execute
   - `-s`: Specifies selection quesiton file, for example: `-s file.pdf`
   - `-t`: Specifies true false quesiton file, for example: `-t file.pdf`

   You can add multiple files of the same type.

   Full command example:

   ```bash
   python index.py -s tf.pdf -s sl.pdf >> out.json
   ```

   Change the output file's name to the corresponding language, then copy it
   back the midnight repo, and then format it's content in vscode.

## TODO

- Support more languages
- Support extracting images

The last part is kinda awkward. I would love to make it fully automated, but the
reality is I probably still need to compile the images manually, or even make
svg files myself.

## Contribution

Just submit PRs and issues. If you don't receive feedback within a week, feel
free to contact me via email.
