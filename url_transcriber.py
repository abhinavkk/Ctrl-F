import requests
from urllib.parse import urlparse, parse_qs
from xml.etree import ElementTree
from url_transcript import getTranscribedUrl

OK = 200

def VideoId(url):

    " Get youtube id from the url"
    
    if not url:
        return ""

    # If URL is embedded
    if "embed" in url:
        return url.split("/")[-1]

    parse_result = urlparse(url)
    query = parse_qs(parse_result.query)
    return query["v"][0]


def transcribedVideo(youtube_url):

    "Transcribe youtube video"
    
    id = videoId(youtube_url)

    url = getTranscribedUrl("https://www.youtube.com/watch?v={}".format(id))

    print(url)
    response = requests.get(url)

    return response.status_code, response.content


def searchKeyword(youtube_url, keyword):

    "Search for the keyword provided in the video"

    timestamps = list()

    if not keyword or not youtube_url:
        return timestamps

    status_code, content = transcribedVideo(youtube_url)

    if not content:
        print("NO CONTENT")
        return timestamps

    if status_code == OK:

        tree = ElementTree.fromstring(content)

        for node in tree:

            if keyword in node.text:
                print(node.text)
                print(node.attrib)
                timestamps.append(float(node.attrib["start"]))

    return timestamps
