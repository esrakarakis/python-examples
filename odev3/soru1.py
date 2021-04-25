class WebPush:
    def __init__(self, platform, optin, global_frequency_capping, start_date,
                 end_date, language, push_type):
        self.platform = platform
        self.optin = bool(optin)
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_push(self):
        if self.optin:
            print("Push Gönderildi!")
        else:
            print("Kullanıcı optin değil. Push gönderilemez")


class TriggerPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date,
                 end_date, language, push_type, trigger_page):
        super().__init__(platform, optin, global_frequency_capping, start_date,
                         end_date, language, push_type)
        self.trigger_page = trigger_page


class BulkPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date,
                 end_date, language, push_type, send_date):
        super().__init__(platform, optin, global_frequency_capping, start_date,
                         end_date, language, push_type)
        self.send_date = send_date


class SegmentPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date,
                 end_date, language, push_type, segment_name):
        super().__init__(platform, optin, global_frequency_capping, start_date,
                         end_date, language, push_type)
        self.segment_name = segment_name


class PriceAlertPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date,
                 end_date, language, push_type, price_info, discount_rate):
        super().__init__(platform, optin, global_frequency_capping, start_date,
                         end_date, language, push_type)
        self.price_info = price_info
        self.discount_rate = discount_rate

    def discountPrice(self):
        return round(self.price_info * (self.discount_rate / 100), 2)


class InstockPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date,
                 end_date, language, push_type, stock_info):
        super().__init__(platform, optin, global_frequency_capping, start_date,
                         end_date, language, push_type)
        self.stock_info = stock_info

    def stockUpdate(self, stock_info):
        self.stock_info = stock_info
        return bool(self.stock_info)


wp = WebPush("Windows", True, "1", "21/08/2021", "23/08/2021", "tr", "mobile")
tp = TriggerPush("Linux", False, "1", "21/05/2021", "23/05/2021", "en", "mobile", "cart_page")
bp = BulkPush("MacOsx", True, "1", "21/04/2021", "23/04/2021", "cn", "mobile", "21/05/2021")
sp = SegmentPush("Windows", True, "1", "21/07/2021", "23/07/2021", "es", "mobile", "returning-user-segment")
pap = PriceAlertPush("MacOsx", True, "1", "21/09/2021", "23/09/2021", "fr", "mobile", 200, 15)
ip = InstockPush("MacOsx", False, "1", "21/09/2021", "23/09/2021", "de", "mobile", False)

print("----web push----")
wp.send_push()
print("----trigger push----")
tp.send_push()
print("----bulk push----")
bp.send_push()
print("----segment push----")
sp.send_push()

print("----price alert push----")
print("indirim oranı: ", pap.discountPrice())
pap.send_push()

print("----instock push----")
print("stok durumu:", ip.stock_info)
ip.stockUpdate(True)
print("stok durumu : ", ip.stock_info)
ip.send_push()
