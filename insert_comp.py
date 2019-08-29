import os
import requests

if __name__ == '__main__':

    record = {
        "comp_title": "全球数据智能大赛(2024)",
        "comp_subtitle": "“数字人体”赛场一：肺部CT多病种智能诊断",
        "comp_range": "Jul 31 - Oct 31, 2019",
        "comp_url": "https://tianchi.aliyun.com/competition/entrance/231724/",
        "comp_description": "赛场一“数字人体”挑战赛以肺部CT多病种智能诊断为课题，开放高质量CT标注数据，要求选手提出并综合运用目标检测、深度学习等人工智能算法，识别肺结节、索条（条索状影）、动脉硬化或钙化、淋巴结钙化等多个病种，避免同一部位单病种的反复筛查，提高检测的速度和精度，辅助医生进行诊断。",
        "comp_host_name": "天池",
        "comp_host_url": "https://tianchi.aliyun.com/home/",
        "prize_currency": "USD",
        "prize_amount": "10000",
        "publish_time": "2019-07-23",
        "update_time": "2019-08-01",
        "deadline": "2020-10-31 23:59:59",
        "timezone": "UTC",
        "comp_scenario": ["CV", "NLP"],
        "data_feature": "一维数组",
        "contributor_id": "233"
    }

    result = requests.post("http://174.137.53.253:30500/api/competition",
                           data=record)

    print(result)

    pass


# curl -X DELETE 174.137.53.253:30500/api/competition/5d46b86180e246bb7f206bf7

# curl http://174.137.53.253:30500/api/competition/competition-name/fuzzy/2019
# curl http://174.137.53.253:30500/api/competition/hostname/fuzzy/天池


# http://174.137.53.253:30500/api/usage