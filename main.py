



from pyrogram import Client
import asyncio, zipfile, pandas as pd, os

API_ID = 20898349
API_HASH = "9fdb830d1e435b785f536247f49e7d87"
SESSION = "BQE-4i0ARa9y1y2YBwjOAnbtDAgKth73-wAYL5DA_mCb2nOjsLIENWtdPd2vT4bSMZcTwIKMEUb4DLTkFtyksAJBl1HUbTW25q3VBogqR0iq9eQAxoxgjsLzvKxF7uGriPE7TQWq7ZLgsOj_fW2W7B_RsR9S8AZCji8H2ksKJ3ibrxQiQupvJ1rZqy-EgJH_vWus1lXxkjZ4cLCmYlTElm9UNpxri2qUgAPbDpHWoFGeqysiP6Jho7IvI6qY0ye2mnInKREr4bXK4c_qsMfGtof-Mb5N6l2jIJ5BRMROAogxq2cc_XqOBExptNKNpTTsJvbgEfXvbdtwcFb_aKPPAHJJuUw2agAAAAHALwpfAA"
CHANNEL = "BOM_BOM68"  # tera user ID jahan result aayega

app = Client("s", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)

async def main():
    async with app:
        print("Downloading Part 1...")
        await app.download_media(
            await app.get_messages(CHANNEL, 970),
            file_name="/home/user/part1.zip"
        )
        print("Part 1 Done!")

        print("Downloading Part 2...")
        await app.download_media(
            await app.get_messages(CHANNEL, 971),
            file_name="/home/user/part2.zip"
        )
        print("Download Done! Merging...")

        os.system("cat /home/user/part1.zip /home/user/part2.zip > /home/user/full.zip")
        print("Merged!")

        print("Processing CSV...")
        results = []
        with zipfile.ZipFile('/home/user/full.zip', 'r') as z:
            print("Files inside zip:", z.namelist())
            csv_name = z.namelist()[0]
            with z.open(csv_name) as f:
                for chunk in pd.read_csv(f, chunksize=100000):
                    results.append(chunk)

        final = pd.concat(results)
        print(f"Total rows: {len(final)}")
        final.to_csv('/home/user/result.csv', index=False)

        print("Sending to Telegram...")
        await app.send_document(YOUR_ID, '/home/user/result.csv', caption="✅ Done!")
        print("All Done!")

asyncio.run(main())
