from config import client
import pandas as pd



async def extract_id():
    dic ={}
    # # You can print all the dialogs/conversations that you are part of:
    async for dialog in client.iter_dialogs():
        # print(dialog.name, 'has ID', dialog.id)
        try:
            if dialog.name:
                dic[dialog.name] = dialog.id
        except Exception as e:
            print(e)
        else:
            # print(dic)
            # Extract names and UIDs from the dictionary keys
            names = [key.split(',')[0] for key in dic.keys()]
            uids = list(dic.values())

            # Create a DataFrame with the extracted data
            df = pd.DataFrame({'name': names, 'uid': uids})
            df = df.sort_values(by='name')
            reset_df = df.reset_index(drop=True)
            reset_df.to_csv(path_or_buf='data/allid.csv')

with client:
    client.loop.run_until_complete(extract_id())