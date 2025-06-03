from modules.sheet_auth import sheet
from modules.create_user import init_gitlab_users
from modules.bot import app



def main():
    print(init_gitlab_users(sheet))
    app.run()


if __name__ == "__main__":
    main()
