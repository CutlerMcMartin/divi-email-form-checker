from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin

## Turorial Being used: https://www.thepythoncode.com/article/extracting-and-submitting-web-page-forms-in-python
url = "https://falcanna.com/"

session = HTMLSession()

def get_all_forms(url):
    """Returns all form tags found on a web page's `url` """
    # GET request
    res = session.get(url)
    # for javascript driven website
    # res.html.render()
    soup = BeautifulSoup(res.html.html, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """Returns the HTML details of a form,
    including action, method and list of form controls (inputs, etc)"""
    details = {}
    # get the form action (requested URL)
    action = form.attrs.get("action").lower()
    # get the form method (POST, GET, DELETE, etc)
    # if not specified, GET is the default in HTML
    method = form.attrs.get("method", "get").lower()
    # get all form inputs
    inputs = []
    for input_tag in form.find_all("input"):
        # get type of input form control
        input_type = input_tag.attrs.get("type", "text")
        # get name attribute
        input_name = input_tag.attrs.get("name")
        # get the default value of that input tag
        input_value =input_tag.attrs.get("value", "")
        # add everything to that list
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    # put everything to the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

first_form = get_all_forms(url)[0]

form_details = get_form_details(first_form)

# the data body we want to submit
data = {}
for input_tag in form_details["inputs"]:
    if input_tag["type"] == "hidden":
        # if it's hidden, use the default value
        data[input_tag["name"]] = input_tag["value"]
    elif input_tag["type"] != "submit":
        # all others except submit, prompt the user to set it
        value = input(f"Enter the value of the field '{input_tag['name']}' (type: {input_tag['type']}): ")
        data[input_tag["name"]] = value

# join the url with the action (form request URL)
url = urljoin(url, form_details["action"])

if form_details["method"] == "post":
    res = session.post(url, data=data)
elif form_details["method"] == "get": 
    res = session.get(url, params=data)

first_form = get_all_forms(url)[0]

form_details = get_form_details(first_form)
