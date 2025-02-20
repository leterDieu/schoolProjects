'''
Main
'''

from typing import Any
import argparse
from tabulate import tabulate
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

    parser.add_argument("-cuu", "--change-user-username", type = str, nargs = 2,
                        metavar = ('user id', 'new username'),
                        help = "Changes user's username.")

    parser.add_argument("-cue", "--change-user-email", type = str, nargs = 2,
                        metavar = ('user id', 'new email'),
                        help = "Changes user's email.")

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
                        help = "Gets profile by phone.")

    parser.add_argument("-gfi", "--get-profile-info", type = str, nargs = 1,
                        metavar = 'profile id',
                        help = "Gets profile's info.")

    parser.add_argument("-gfu", "--get-profile-user", type = str, nargs = 1,
                        metavar = ('profile id'),
                        help = "Gets user's id.")

    parser.add_argument("-cfb", "--change-profile-bio", type = str, nargs = 2,
                        metavar = ('profile id', 'new bio'),
                        help = "Changes profile's bio.")

    parser.add_argument("-cfp", "--change-profile-phone", type = str, nargs = 2,
                        metavar = ('profile id', 'new phone'),
                        help = "Changes profile's phone.")

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

    parser.add_argument("-cpt", "--change-project-title", type = str, nargs = 2,
                        metavar = ('project id', 'new title'),
                        help = "Changes project's title.")

    parser.add_argument("-cpd", "--change-project-description", type = str, nargs = 2,
                        metavar = ('project id', 'new description'),
                        help = "Changes project's description.")

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

    parser.add_argument("-ct", "--complete-task", type = str, nargs = 1,
                        metavar='task id',
                        help = "Sets task's status as complete.")

    parser.add_argument("-ctt", "--change-task-title", type = str, nargs = 2,
                        metavar = ('task id', 'new title'),
                        help = "Changes task's title.")

    # sync (s)
    parser.add_argument("-sup", "--sync-user-project", type = str, nargs = 2,
                        metavar = ('user id', 'project id'),
                        help = "Syncs user to project.")

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
    if args.change_user_username is not None:
        user = session.query(User).filter_by(id=args.change_user_username[0]).first()
        if user is not None:
            user.username = args.change_user_username[1]
    if args.change_user_email is not None:
        user = session.query(User).filter_by(id=args.change_user_email[0]).first()
        if user is not None:
            user.email = args.change_user_email[1]

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
    if args.change_profile_bio is not None:
        profile = session.query(Profile).filter_by(id=args.change_profile_bio[0]).first()
        if profile is not None:
            profile.bio = args.change_profile_bio[1]
    if args.change_profile_phone is not None:
        profile = session.query(Profile).filter_by(id=args.change_profile_phone[0]).first()
        if profile is not None:
            profile.phone = args.change_profile_phone[1]

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
    if args.change_project_title is not None:
        project = session.query(Project).filter_by(id=args.change_project_title[0]).first()
        if project is not None:
            project.title = args.change_project_title[1]
    if args.change_project_description is not None:
        project = session.query(Project).filter_by(id=args.change_project_description[0]).first()
        if project is not None:
            project.description = args.change_project_description[1]

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
    if args.complete_task is not None:
        task = session.query(Task).filter_by(id=args.complete_task[0]).first()
        if task is not None:
            task.status = True
    if args.change_task_title is not None:
        task = session.query(Task).filter_by(id=args.change_task_title[0]).first()
        if task is not None:
            task.title = args.change_task_title[1]

    # sync
    if args.sync_user_project is not None:
        user = session.query(User).filter_by(id=args.sync_user_project[0]).first()
        project = session.query(Project).filter_by(id=args.sync_user_project[1]).first()
        if project is not None and user is not None:
            project.users.append(user)


    session.commit()

if __name__ == "__main__":
    main()
