# Sponge

[English](./README_EN.md)

Sponge 是一款為了駕照筆試練習網站
[midnight](https://github.com/cheetosysst/midnight) 所撰寫的小工具。Sponge
能夠將自[中華民國交通部公路總局-筆試題庫](https://www.thb.gov.tw/cl.aspx?n=12)下載的檔案整理成能供
midnight 讀取的格式。

## 安裝

1. 複製本 repo

   ```bash
   git clone https://github.com/cheetosysst/sponge --depth=1
   cd sponge
   ```

2. 啟動 venv

   請根據您所使用的作業系統環境，執行對應的 activate
   腳本，相關的說明可以在網路上搜尋到。

3. Execute
   - `-s`: 指定選擇題的檔案，例如： `-s file.pdf`
   - `-t`: 指定是非題的檔案，例如： `-t file.pdf`

   你可以指定多個同類型檔案

   完整範例：

   ```bash
   python index.py -s tf.pdf -s sl.pdf >> out.json
   ```

   更改輸出檔案的名子為對應的語言，複製該檔案到 midnight 中，並且使用 vscode
   內建排版功能整理檔案內容。

## TODO

- 支援更多語言
- 支援圖片

最後一點可能會有點不好處理，我希望可以讓這個工具完全自動化，但是我可能仍需要手動整理圖片，甚至自行製作
svg 圖片。

## 貢獻

歡迎貢獻直接建立新的 PR 或是 issue，如果您沒有在一週內獲得回應，歡迎透過 E-Mail
聯絡，我會盡快回應。
