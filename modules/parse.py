def get_contacts(sheet):
    data = sheet.get_all_records()
    contacts = []
    try:
        for row in data:
            first_name = row.get("FIRST NAME")
            last_name = row.get("LAST NAME")
            contacts.append((first_name, last_name))
        return contacts

    except Exception as e:
        return False


def gitlab_user_data(sheet):
    data = sheet.get_all_records()
    init_data = []

    try:
        for row in data:
            first_name = row.get("FIRST NAME")
            user_name = row.get("USERNAME")
            password = row.get("PASSWORD")
            email = row.get("EMAIL")
            init_data.append((first_name, user_name, password, email))
        return init_data

    except Exception as e:
        return False

