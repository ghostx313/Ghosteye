import socket
import time

import requests


class Ip_infogo:
    def infogo(self):
        self.get = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def get_info(self):
        ip = self.get.gethostbyname()

        url = f"http://ipwho.is/{ip}"

        try:
            res = requests.get(url)
            res.raise_for_status()
            data = res.json()

            if not data.get("success", False):
                print("api error or invaild ip_address")
                time.sleep(3)
                return
            print("ip_address: {ip}\n")
            print("success:", data["success"])
            print("continent:", data["continen"])
            print("Region_code ", data["region_code"])
            print("type:", data["type"])
            print("Country: ", data["country"])
            print("Data: ", data["region"])
            print("City: ", data["city"])
            print("Latitude: ", data["latitude"])
            print("Longitude: ", data["longitude"])
            print("postal: ", data["postal"])
            print("calling_code: ", data["calling_code"])
            print("capital_code: ", data.get("capital_code", "N/A"))
            print("capital: ", data.get("capital", "N/A"))
            print("Border", data.get("borders"))
            print("Continent code: ", data["continent_code"])
            print("Is eu", data["is_eu"])

            lat = data["latitude"]
            long = data["longitude"]
            print(f"map: https://www.google.com/maps/@{lat},{long}")

            connection = data.get("connection, {}")
            print("ASN :", connection.get("asn", "N/A"))
            print("org :", connection.get("org", "N/A"))
            print("isp :", connection.get("isp", "N/A"))

            timezone = data.get("timezone", {})
            print("Time zone id :", timezone.get("id", "N/A"))
            print("abbr:", timezone.get("abbr", "N/A"))
            print("DST:", connection.get("dst", "N/A"))
            print("offset :", timezone.get("offset", "N/A"))
            print("UTC:", timezone.get("utc", "N/A"))
            print("current_time: ", timezone.get("current_time", "N/A"))
        except Exception as e:
            return e


# geo = Ip_infogo()
# geo.get_info()
