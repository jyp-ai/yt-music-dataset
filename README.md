### YT-Music-Dataset-Maker
- Singing Voice Dataset 확보를 위한 YouTube 음악 다운로더
- `yt-dlp` 패키지 활용

### Pipeline
- `songs_list/blackpink_songs.csv`를 DataFrame으로 읽어서, 다운받을 곡 리스트를 추출
- 파일 저장을 어떤 이름으로?
    - 형식은 `artist-album_number-track_number-song`
    - 앨범 제목이나 곡 제목에 띄어쓰기 있는 경우는 `_` 로 대체
    - 예시) `blackpink-04-01-뚜두뚜두_(DDU-DU_DDU-DU).wav`