import os
import requests


def get_linear_chain(id):
    return "https://music.163.com/song/media/outer/url?id="+str(id)+".mp3"


def download_mp3(url, path):
    res = requests.get(url)
    open(path, "wb").write(res.content)
    print("下载成功：" + path)


def download_playlist(songs):
    cur_path = os.path.dirname(os.path.abspath(__file__))
    download_path = os.path.join(cur_path, "download")
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    for song in songs:
        file_name = song["name"]+" - "+song["ar"][0]["name"]
        file_name = file_name.replace("/", "\\")
        file_path = os.path.join(download_path, file_name+".mp3")
        print("开始下载：" + file_name + " -> " + str(song['id']))
        download_mp3(get_linear_chain(song["id"]), file_path)


if __name__ == "__main__":
    playlist_url = "https://netease-cloud-music-api-livid-seven.vercel.app/playlist/track/all?id="
    playlist_id = input("请输入歌单id：")
    resp = requests.get(playlist_url + playlist_id)
    resp_json = resp.json()
    print(resp_json)
    if resp_json["code"] == 200:
        download_playlist(resp_json["songs"])
    else:
        print("获取歌单失败！" + str(resp_json["code"]))
