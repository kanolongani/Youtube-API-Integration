import googleapiclient.discovery
import pandas as pd


def  fetch_data(search_term):
# API information
    api_service_name = "youtube"
    api_version = "v3"
# API key
    DEVELOPER_KEY = ""
# API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)
# 'request' variable is the only thing you must change
# depending on the resource and method you need to use
# in your query

# search_term=input("enter the topic name")
    request = youtube.search().list(part="id,snippet",
            type='video',
            q=search_term,
            maxResults=20
    )
    # Query execution
    response = request.execute()
    # Print the results
    #print(response)

    video_details = {
        'id':[],
        'duration':[],
        'views':[],
        'likes':[],
        'favorites':[],
        'comments':[],
        'thumbnail':[]
    }

    for x in response['items']:
        
        kano=x['id']['videoId']
        kk= youtube.videos().list(
            part="statistics,contentDetails,snippet",
            id=kano,
            fields="items(statistics,snippet(thumbnails)" + \
                        "contentDetails(duration))"
        ).execute()


        print(kk)
        try:
            duration = kk['items'][0]['contentDetails']['duration']
            rep=duration.replace('PT','')
            sp=rep.split('M')
            
            ba = sp[1].replace('S','') if sp[1].replace('S','') else 0
            
            sp_=sp[0].split('H')
            if len(sp_)==2:
                ab= (int(sp_[0])*3600)+(int(sp_[1])*60)
            else:
                ab=int(sp_[0])*60

            try:
                u = kk['items'][0]['snippet']['thumbnails']['standard']['url']
                video_details['thumbnail'].append(f'<img src="{u}" width="100" height="100">')
            except:
                video_details['thumbnail'].append("")
            
            second_=ab + int(ba)
            #print(second_)

            





            try:
                views = kk['items'][0]['statistics']['viewCount']
            except:
                views = "Not availabel"

            try:
                likes = kk['items'][0]['statistics']['likeCount']
            except:
                likes = "Not availabel"

            try:
                favorites = kk['items'][0]['statistics']['favoriteCount']
            except:
                favorites = "Not availabel"

            try:
                comments = kk['items'][0]['statistics']['commentCount']
            except:
                comments = "Not availabel"


            video_details['id'].append(kano)
            video_details['duration'].append(second_)
            video_details['views'].append(views)
            video_details['likes'].append(likes)
            video_details['favorites'].append(favorites)
            video_details['comments'].append(comments)

        except Exception as e:
            print(duration)
            print(e)
            pass


    
    df = pd.DataFrame(data=video_details)
    print(df)



    return df


    # df.to_csv(search_term+".csv", index=False)


if __name__ == '__main__':
    fetch_data('tarak')




    









