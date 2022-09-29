import json
from faker import Faker
import random
from datetime import datetime
import requests
import urllib3
from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


wait_time = 5
fake = Faker()

browser = [fake.chrome(), fake.safari(), fake.firefox()]
os = [fake.windows_platform_token(), fake.mac_platform_token(), fake.android_platform_token()]
cookies = [True, False]


def random_int(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return random.randint(range_start, range_end)


def output_data_prep(seq):
    output = {
        'seq_id': {'0': seq},
        'accept_language': {'0': random_int(3)},
        'browser': {'0': random.choice(browser)},
        'browser_height': {'0': random_int(3)},
        'browser_width': {'0': random_int(3)},
        'c_color': {'0': random_int(2)},
        'carrier': {'0': 't-mobile.nl:t-mobile netherlands b.v.'},
        'code_ver': {'0': 'JS-2.22.4-LCUM'},
        'color': {'0': fake.hex_color()},
        'connection_type': {'0': random_int(3)},
        'cookies': {'0': random.choice(cookies)},
        'country': {'0': fake.city()},
        'curr_factor': {'0': random_int(1)},
        'curr_rate': {'0': 1.0},
        'currency': {'0': 'EUR'},
        'date_time': {'0': round(datetime.timestamp(datetime.now()))},
        'domain': {'0': fake.domain_name()},
        'evar1': {'0': random_int(1)},
        'evar2': {'0': 'www:essent:energie:klant-worden'},
        'evar4': {'0': 'ESC keuzehulp:keuzehulp verbruik inschatten:type huis'},
        'evar6': {'0': 'https://www.essent.nl/energie/klant-worden'},
        'evar97': {'0': 'type huis:appartement'},
        'event_list': {'0': '203,100,101,103,105,196'},
        'first_hit_page_url': {'0': 'https://www.essent.nl/'},
        'first_hit_pagename': {'0': 'www:essent'},
        'first_hit_ref_type': {'0': random_int(1)},
        'first_hit_referrer': {'0': '%OriginalReferrer%'},
        'first_hit_time_gmt': {'0': round(datetime.timestamp(datetime.now()))},
        'geo_city': {'0': fake.city()},
        'geo_country': {'0': fake.city()},
        'geo_region': {'0': 'zh'},
        'geo_zip': {'0': '3032 aa'},
        'hit_source': {'0': random_int(1)},
        'hit_time_gmt': {'0': round(datetime.timestamp(datetime.now()))},
        'hitid_high': {'0': random_int(19)},
        'hitid_low': {'0': random_int(19)},
        'homepage': {'0': 'U'},
        'ip': {'0': fake.ipv4()},
        'j_jscript': {'0': '1.6'},
        'java_enabled': {'0': 'N'},
        'javascript': {'0': random_int(1)},
        'language': {'0': random_int(2)},
        'last_hit_time_gmt': {'0': round(datetime.timestamp(datetime.now()))},
        'mcvisid': {'0': random_int(38)},
        'mobile_id': {'0': random_int(8)},
        'os': {'0': random.choice(os)},
        'page_event': {'0': random_int(2)},
        'page_event_var2': {'0': 'tool-fieldcomplete'},
        'page_url': {'0': 'https://www.essent.nl/energie/klant-worden'},
        'pagename': {'0': 'www:essent:energie:klant-worden'},
        'persistent_cookie': {'0': 'Y'},
        'post_browser_height': {'0': random_int(3)},
        'post_browser_width': {'0': random_int(3)},
        'post_cookies': {'0': 'Y'},
        'post_currency': {'0': 'EUR'},
        'post_cust_hit_time_gmt': {'0': round(datetime.timestamp(datetime.now()))},
        'post_evar1': {'0': random_int(1)},
        'post_evar2': {'0': 'www:essent:energie:klant-worden'},
        'post_evar4': {'0': 'ESC keuzehulp:keuzehulp verbruik inschatten:type huis'},
        'post_evar6': {'0': 'https://www.essent.nl/energie/klant-worden'},
        'post_evar21': {'0': 'www.essent.nl:main'},
        'post_evar36': {'0': '%BestOfferValue%'},
        'post_evar44': {'0': '%LaunchInfo%'},
        'post_evar55': {'0': '3178A17E7F5721C9-60001AFAB4E85311'},
        'post_evar97': {'0': 'type huis:appartement'},
        'post_evar200': {'0': '0.10128864801487336_1659978492638'},
        'post_event_list': {'0': '203,100,101,103,105,196'},
        'post_java_enabled': {'0': 'N'},
        'post_page_event': {'0': random_int(3)},
        'post_page_event_var2': {'0': 'tool-fieldcomplete'},
        'post_persistent_cookie': {'0': 'Y'},
        'post_product_list': {'0': ';;;;'},
        'post_prop6': {'0': 'https://www.essent.nl/energie/klant-worden'},
        'post_t_time_info': {'0': datetime.now().strftime('%Y-%m-%dT%H:%M:%S')},
        'post_visid_high': {'0': random_int(19)},
        'post_visid_low': {'0': random_int(19)},
        'post_visid_type': {'0': random_int(1)},
        'post_zip': {'0': '::hash::0'},
        'prop6': {'0': 'https://www.essent.nl/energie/klant-worden'},
        'ref_type': {'0': random_int(1)},
        'resolution': {'0': random_int(3)},
        's_resolution': {'0': '412x915'},
        'sampled_hit': {'0': 'Y'},
        'service': {'0': 'pe'},
        'stats_server': {'0': 'anedge-69c8d8cc76-nnbpx.fra8'},
        't_time_info': {'0': datetime.now().strftime('%Y-%m-%dT%H:%M:%S')},
        'truncated_hit': {'0': 'N'},
        'user_agent': {
            '0': 'Mozilla/5.0 (Linux; Android 12; Pixel 6) Chrome/103.0.0.0 Mobile Safari/537.36'},
        'user_hash': {'0': random_int(10)},
        'userid': {'0': random_int(9)},
        'username': {'0': 'advessnlprodes'},
        'va_closer_detail': {'0': 'originalreferrer'},
        'va_closer_id': {'0': random_int(2)},
        'va_finder_detail': {'0': 'originalreferrer'},
        'va_finder_id': {'0': random_int(2)},
        'visid_high': {'0': random_int(19)},
        'visid_low': {'0': random_int(19)},
        'visid_new': {'0': 'N'},
        'visid_timestamp': {'0': round(datetime.timestamp(datetime.now()))},
        'visid_type': {'0': random_int(1)},
        'visit_num': {'0': random_int(1)},
        'visit_page_num': {'0': random_int(2)},
        'visit_ref_type': {'0': random_int(1)},
        'visit_referrer': {'0': '%OriginalReferrer%'},
        'visit_start_page_url': {'0': 'https://www.essent.nl/'},
        'visit_start_pagename': {'0': 'www:essent'},
        'visit_start_time_gmt': {'0': round(datetime.timestamp(datetime.now()))}
    }
    return json.dumps(output)


def final_data_prep(seq):
    final_output = {
        "topic": f"{topic_name}-{datetime.today().strftime('%Y-%m-%d')}",
        "record_key": f"{topic_name}_{datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}",
        "record_value": output_data_prep(seq),
        "metadata": {
            "first_name": "string",
            "last_name": "string",
            "email": "string",
            "city": "string",
            "phone": "integer",
            "ip_address": "string",
            "url": "string",
            "company": "string",
            "datetime": "string"
        }
    }
    return json.dumps(final_output)


def async_requests(number_of_events, url, run_num, max_workers=4):
    with FuturesSession(session=requests.Session(), max_workers=max_workers) as session:
        futures = [session.post(url,
                                data=final_data_prep(f"{run_num}_{seq}"),
                                verify=False) for seq in range(number_of_events)]
        for future in as_completed(futures):
            print(f"Status: {future.result()}, {future.result().content}")


if __name__ == "__main__":

    topic_name = "50K-Trial2"
    number_of_events = 100
    for run_num in range(10):
        async_requests(number_of_events,
                       url="https://ix3ib9v40b.execute-api.eu-central-1.amazonaws.com/dev/produce_data",
                       max_workers=4,
                       run_num=run_num)
