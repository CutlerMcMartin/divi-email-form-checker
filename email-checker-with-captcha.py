# %%
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

# %%

post_body = {
    "et_pb_contact_name_0":"Cutler",
    "t_pb_contact_email_0":"cutler.mcmartin%40gmail.com",
    "et_pb_contact_details_0":"yeet",
    "et_pb_contactform_submit_0":"et_contact_proccess",
    "et_pb_contact_captcha_0": "11",
    "_wpnonce-et-pb-contact-form-submitted-0":"3755f140e5",
    "_wp_http_referer":"%2Fdelete-later%2F",
    "et_pb_contact_email_fields_0":"%5B%7B%22field_id%22%3A%22et_pb_contact_name_0%22%2C%22original_id%22%3A%22name%22%2C%22required_mark%22%3A%22required%22%2C%22field_type%22%3A%22input%22%2C%22field_label%22%3A%22Name%22%7D%2C%7B%22field_id%22%3A%22et_pb_contact_email_0%22%2C%22original_id%22%3A%22email%22%2C%22required_mark%22%3A%22required%22%2C%22field_type%22%3A%22email%22%2C%22field_label%22%3A%22Email+Address%22%7D%2C%7B%22field_id%22%3A%22et_pb_contact_details_0%22%2C%22original_id%22%3A%22details%22%2C%22required_mark%22%3A%22required%22%2C%22field_type%22%3A%22text%22%2C%22field_label%22%3A%22Project+Details%22%7D%5D",
    "token":""
}

r = requests.post('https://marshalledmakers.com', data=post_body)

print(r)

# %%

url = "https://marshalledmakers.com/delete-later/"

session = HTMLSession()

res = session.get(url)
# for javascript driven website
# res.html.render()
soup = BeautifulSoup(res.html.html, "html.parser")
soup = soup.find_all("form")[1]
soup = soup.find_all("input")[-3]
captcha_attributes = soup.attrs
captcha_numbers = [captcha_attributes['data-first_digit'], captcha_attributes['data-second_digit']]
print(captcha_numbers)

# %%
