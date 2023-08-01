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

   You can add multiple files of the same type, however that is just an
   overengineered feature and is not useful for our usecase lol.

   Full command example:

   ```bash
   python index.py -s tf.pdf -s sl.pdf >> out.json
   ```

   Change the output file's name to the corresponding language, then copy it
   back the midnight repo, and then format it's content in vscode.

   **WARNING**: This tool currently only supports "zh-TW"
