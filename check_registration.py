import requests

def check_registration_status():
    try:
        response = requests.get(
            "https://ucfrwc.org/Program/GetOfferingsForSemester?semesterId=276e379b-939e-41c1-ae07-3df89a7cb08b&programId=c796a51a-d7eb-4dcd-982a-3ba4917882ea",
            headers={
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'cookie': 'ASP.NET_SessionId=b3lpc3yhxrjfztsdjzjzf5q2; __RequestVerificationToken=6LwWnGfdvdkDQ_CFx-E_Ba1DQV782cN6xJFqNzs9HxFAFnSFnfpKGoNsPG3RFa6MI_ht-6gJoUx5eU7JKjhaeb20cUIyCtOZrZ1iTe1B44U1; _gid=GA1.2.1438545243.1729780619; _shibsession_64656661756c7468747470733a2f2f7563667277632e6f72672f73686962626f6c657468=_72f81dcedbbb413a948552ffe454086b; .AspNet.ApplicationCookie=VfqtnVWOgCEE7znRgaA0XToNll_2nAmUflcIwbt3wjjShpd23KFBPDlpcok6DYxDSwjqH9HmNRdH3mqAK_bFR6MUSwEniOP3nSrKTYmgrwabGAzSxGPdRSmdTD8M7r9yrBV4dMuJHp895au6s0ur7-U21MBuIFoiLzQQIxc2hs4pia-Qn6b1VVFPYEMMaw7i1XgLJbwvH14UBkt2sC3hV-0dvvdT5m5xJX86DstgMKyFyAk_hSaBtqg9FUceHd8OdgqA_s7urA_AbB7_VsZPQINpIeb7U_CkyAgmGK62ho4yAzMMWDdaabGz_e2ZxDwd5QtnCw6ej7TxG0gaA-OybgL9hGPQRZI9CzPZuNejQcBUSLZGSHiPEmdXSuoDPF8B; _gat_gtag_UA_40907193_21=1; _ga_R9YQE9JCC6=GS1.1.1729866401.4.1.1729867291.0.0.0; _ga=GA1.2.1829211566.1729780619',
                'priority': 'u=1, i',
                'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest'
            }
        )
        response.raise_for_status()
        if "Registration Not Open" in response.text:
            # Send message to Discord webhook
            discord_webhook_url = "https://discord.com/api/webhooks/1194121970602737756/LusPVjMKlLC1-VaTTALvf4g5JLQqVlfi0wTPy-_UazoEUasVMTFUvLPc7ohEXhxbO_9j"
            discord_data = {"content": "Registration is open"}
            requests.post(discord_webhook_url, json=discord_data)
    except requests.exceptions.RequestException as e:
        print(f"Error while checking registration status: {e}")

if __name__ == "__main__":
    check_registration_status()
