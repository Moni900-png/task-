import pandas as pd

json_data = {
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}

user_data = json_data['data']
support_data = json_data['support']

df = pd.DataFrame({
    'ID': [user_data['id']],
    'Email': [user_data['email']],
    'First Name': [user_data['first_name']],
    'Last Name': [user_data['last_name']],
    'Avatar': [user_data['avatar']],
    'Support URL': [support_data['url']],
    'Support Text': [support_data['text']]
})

excel_filename = 'user_data.xlsx'
df.to_excel(excel_filename, index=False)

print(f'Excel file "{excel_filename}" created successfully.')
