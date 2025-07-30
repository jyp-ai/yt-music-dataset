### YT-Music-Dataset-Maker
- Singing Voice Dataset 확보를 위한 YouTube 음악 다운로더
- `yt-dlp` 패키지 활용

### 설치
```
git clone https://github.com/jyp-ai/yt-music-dataset.git
conda create -n yt-music-dataset python=3.12 -y
conda activate yt-music-dataset
pip install -r requirements.txt
```

### 실행 방법
1. 노션에서 다운받은 csv 파일을 songs_list 폴더 내에 위치시킨다.
2. 루트 디렉토리에서 아래 명령어를 실행하여 다운받는다.
    ```
    python main.py --song_file <실제 csv 파일명>
    # 예시) python main.py --song_file yeji_songs.csv
    ```

### Pipeline
- `songs_list/blackpink_songs.csv`를 DataFrame으로 읽어서, 다운받을 곡 리스트를 추출
- 파일 저장을 어떤 이름으로?
    - 형식은 `artist-album_number-track_number-song`
    - 앨범 제목이나 곡 제목에 띄어쓰기 있는 경우는 `_` 로 대체
    - 예시) `blackpink-04-01-뚜두뚜두_(DDU-DU_DDU-DU).wav`