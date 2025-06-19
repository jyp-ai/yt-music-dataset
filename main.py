import os
import re
import pandas as pd
import yt_dlp
from tqdm import tqdm
from config import SONG_URL_FILE


# url과 file_name을 받아 해당 파일을 download 하고 저장하는 함수
def download_and_save(url, file_name):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"./output/{file_name}.%(ext)s",  # 저장 위치 및 파일명 지정
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
        "quiet": False,  # 필요시 로그 끄기
        "noplaylist": True,  # 플레이리스트가 아닌 단일 URL만
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# csv를 읽어 url과 파일을 파싱한 후, row를 돌며 download 로직을 실행하는 함수
def read_csv_and_iterate(file_path: str) -> list:
    df = pd.read_csv(file_path)
    failed_rows = []

    for idx, row in tqdm(df.iterrows(), total=len(df)):
        try:
            url = row["url"]
            artist = row["artist"].lower().replace(" ", "_")
            album_number = f"{row["album_number"]:02}"
            track_number = f"{row["track_number"]:02}"
            song = row["song"].lower().replace(" ", "_")
            file_name = f"{artist}-{album_number}-{track_number}-{song}"
            # file_name = re.sub(r'[^\w\-]', '', file_name)
            download_and_save(url, file_name)

        except Exception as e:
            print(f"❌ 다운로드 실패: {row.get('url')} | 이유: {str(e)}")
            failed_rows.append(row)

    if failed_rows:
        failed_df = pd.DataFrame(failed_rows)
        failed_df.to_csv("failed_downloads.csv", index=False)
        print(
            f"\n⚠️ {len(failed_rows)}개 다운로드 실패 → 'failed_downloads.csv'에 저장됨"
        )


if __name__ == "__main__":
    os.makedirs("./output", exist_ok=True)
    file_path = f"./songs_list/{SONG_URL_FILE}"
    read_csv_and_iterate(file_path)
