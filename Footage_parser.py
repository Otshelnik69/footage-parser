import requests
import os


def download_multiple_videos(query, api_key, count=3):

    url = f"https://api.pexels.com/videos/search?query={query}&per_page={count}&orientation=portrait"
    headers = {"Authorization": api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()


        videos = data.get('videos', [])

        if not videos:
            print("Ничего не найдено :(")
            return


        folder_name = "my_footages"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        print(f"Найдено видео: {len(videos)}. Начинаю загрузку...")

        for i, v in enumerate(videos):

            link = v['video_files'][0]['link']


            file_name = f"{folder_name}/{query.replace(' ', '_')}_{i + 1}.mp4"


            v_data = requests.get(link).content
            with open(file_name, 'wb') as f:
                f.write(v_data)

            print(f"[{i + 1}/{len(videos)}] Сохранено: {file_name}")

    except Exception as e:
        print(f"Ошибка в коде: {e}")



MY_API_KEY = "КЛЮЧ API"
download_multiple_videos("НАШ ЗАПРОС", MY_API_KEY, count=5)