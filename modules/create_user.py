import gitlab
from modules.envs import GITLAB_TOKEN, GITLAB_URL
from modules.parse import gitlab_user_data

gl = gitlab.Gitlab(
    GITLAB_URL,
    private_token=GITLAB_TOKEN
)



def init_gitlab_users(sheet):    
    init_data = gitlab_user_data(sheet)
    existing_group = "main-group"

    for first_name, user_name, password, email in init_data:
        try:
            user_data = {
                'name': first_name,
                'username': user_name,
                'password': password,
                'email': email,
                'skip_confirmation': True
            }
            new_user = gl.users.create(user_data)
            print(f"user: {user_name} created successfully")
            
            try:
                group = gl.groups.get(f"{existing_group}")
            except gitlab.exceptions.GitlabGetError:
                print(f"user: {user_name} create failed, group not found")
                continue
            try:
                group.members.create({
                    'user_id': new_user.id,
                    'access_level': gitlab.const.AccessLevel.REPORTER
                })
                print(f"user: {user_name} added to group {group}")
            except gitlab.exceptions.GitlabGetError:
                print(f"user: {user_name} added to group failed")

            try:
                project = gl.projects.create({
                    'name': f"{first_name}-project",
                    'namespace_id': group.id
                    })
                print(f"project created for user: {user_name}, the url is: {project.web_url}")
            except gitlab.exceptions.GitlabGetError:
                print(f"user: {user_name} create project failed")

        except Exception as e:
            print(f"user: {user_name} create failed.")
            print(f"{e}")
