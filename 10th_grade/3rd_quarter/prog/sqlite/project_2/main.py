'''
Main
'''

from typing import Any
import argparse
from sqlalchemy.orm import Query
from db.models import (
    User,
    Profile,
    Project,
    Task,)
from db import Session


def custom_print(info: Query[Any] | list[Any]) -> None:
    '''
    custom print with tabulate
    '''
    for item in info:
        print(item)


def main() -> None:
    '''
    main func
    '''
    session = Session()

    parser = argparse.ArgumentParser(description = "db manager")

    # users (u)
    parser.add_argument("-au", "--all-users", nargs = '*',
                        help = "Shows all users.")

    parser.add_argument("-nu", "--new-user", type = str, nargs = 2,
                        metavar = ('username', 'email'),
                        help = "Creates a new user.")

    parser.add_argument("-rmu", "--remove-user", type = str, nargs = 1,
                        metavar = 'user id',
                        help = "Removes user by id.")

    parser.add_argument("-gu", "--get-user", type = str, nargs = 1,
                        metavar = ('username'),
                        help = "Gets user by username.")

    parser.add_argument("-gui", "--get-user-info", type = str, nargs = 1,
                        metavar = 'user id',
                        help = "Gets user's info.")

    parser.add_argument("-guf", "--get-user-profile", type = str, nargs = 1,
                        metavar = ('user id'),
                        help = "Gets profile's id.")

    # profiles (f)
    parser.add_argument("-af", "--all-profiles", nargs = '*',
                        help = "Shows all profiles.")

    parser.add_argument("-nf", "--new-profile", type = str, nargs = 3,
                        metavar = ('bio', 'phone', 'user id'),
                        help = "Creates a new profile.")

    parser.add_argument("-rmf", "--remove-profile", type = str, nargs = 1,
                        metavar = 'profile id',
                        help = "Removes profile by id.")

    parser.add_argument("-gf", "--get-profile", type = str, nargs = 1,
                        metavar = ('phone'),
                        help = "Gets profile by phone")

    parser.add_argument("-gfi", "--get-profile-info", type = str, nargs = 1,
                        metavar = 'profile id',
                        help = "Gets profile's info.")

    parser.add_argument("-gfu", "--get-profile-user", type = str, nargs = 1,
                        metavar = ('profile id'),
                        help = "Gets user's id.")

    # projects (p)
    parser.add_argument("-ap", "--all-projects", nargs = '*',
                        help = "Shows all projects.")

    parser.add_argument("-np", "--new-project", type = str, nargs = 2,
                        metavar = ('title', 'description'),
                        help = "Creates a new project.")

    parser.add_argument("-rmp", "--remove-project", type = str, nargs = 1,
                        metavar = 'project id',
                        help = "Removes project by id.")

    parser.add_argument("-gp", "--get-project", type = str, nargs = 1,
                        metavar = ('title'),
                        help = "Gets prject by title.")

    parser.add_argument("-gpi", "--get-project-info", type = str, nargs = 1,
                        metavar = 'project id',
                        help = "Gets project's info.")

    # tasks (s)
    parser.add_argument("-at", "--all-tasks", nargs = '*',
                        help = "Shows all tasks.")

    parser.add_argument("-nt", "--new-task", type = str, nargs = 2,
                        metavar = ('title', 'project_id'),
                        help = "Creates a new task.")

    parser.add_argument("-rmt", "--remove-task", type = str, nargs = 1,
                        metavar = 'task id',
                        help = "Removes task by id.")

    parser.add_argument("-gt", "--get-task", type = str, nargs = 1,
                        metavar = ('title'),
                        help = "Gets task by title.")

    parser.add_argument("-gti", "--get-task-info", type = str, nargs = 1,
                        metavar = 'task id',
                        help = "Gets task's info.")

    parser.add_argument("-git", "--get-incomplete-tasks", type = str, nargs = '*',
                        help = "Gets incomplete tasks.")

    parser.add_argument("-gct", "--get-complete-tasks", type = str, nargs = '*',
                        help = "Gets complete tasks.")


    args = parser.parse_args()

    # users
    if args.all_users is not None:
        custom_print(session.query(User).all())
    if args.new_user is not None:
        new_user = User()
        new_user.username=args.new_user[0]
        new_user.email=args.new_user[1]
        session.add(new_user)
    if args.remove_user is not None:
        user_to_delete = session.query(User).filter_by(id=args.remove_user[0])
        user_to_delete.delete()
    if args.get_user is not None:
        custom_print(session.query(User).filter_by(username=args.get_user[0]))
    if args.get_user_info is not None:
        custom_print(session.query(User).filter_by(id=args.get_user_info[0]))
    if args.get_user_profile is not None:
        custom_print(session.query(Profile).filter_by(user_id=args.get_user_profile[0]))

    # profiles
    if args.all_profiles is not None:
        custom_print(session.query(Profile).all())
    if args.new_profile is not None:
        new_profile = Profile()
        new_profile.bio = args.new_profile[0]
        new_profile.phone = args.new_profile[1]
        new_profile.user_id = args.new_profile[2]
        session.add(new_profile)
    if args.remove_profile is not None:
        profile_to_delete = session.query(Profile).filter_by(id=args.remove_profile[0])
        profile_to_delete.delete()
    if args.get_profile is not None:
        custom_print(session.query(Profile).filter_by(phone=args.get_profile[0]))
    if args.get_profile_info is not None:
        custom_print(session.query(Profile).filter_by(id=args.get_profile_info[0]))
    if args.get_profile_user is not None:
        profile = session.query(Profile).filter_by(id=args.get_profile_user[0]).first()
        if profile is not None:
            print(profile.user)

    # projects
    if args.all_projects is not None:
        custom_print(session.query(Project).all())
    if args.new_project is not None:
        new_project = Project()
        new_project.title = args.new_project[0]
        new_project.description = args.new_project[1]
        session.add(new_project)
    if args.remove_project is not None:
        project_to_delete = session.query(Project).filter_by(id=args.remove_project[0])
        project_to_delete.delete()
    if args.get_project is not None:
        custom_print(session.query(Project).filter_by(title=args.get_project[0]))
    if args.get_project_info is not None:
        custom_print(session.query(Project).filter_by(id=args.get_project_info[0]))

    # tasks
    if args.all_tasks is not None:
        custom_print(session.query(Task).all())
    if args.new_task is not None:
        new_project = Task()
        new_project.title = args.new_task[0]
        new_project.project_id = args.new_task[1]
        session.add(new_project)
    if args.remove_task is not None:
        task_to_delete = session.query(Task).filter_by(id=args.remove_task[0])
        task_to_delete.delete()
    if args.get_task is not None:
        custom_print(session.query(Task).filter_by(title=args.get_task[0]))
    if args.get_task_info is not None:
        custom_print(session.query(Task).filter_by(id=args.get_task_info[0]))
    if args.get_incomplete_tasks is not None:
        custom_print(session.query(Task).filter_by(status=False))
    if args.get_complete_tasks is not None:
        custom_print(session.query(Task).filter_by(status=True))

    session.commit()

if __name__ == "__main__":
    main()
