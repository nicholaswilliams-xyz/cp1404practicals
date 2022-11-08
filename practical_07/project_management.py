"""

Estimated completion time: 3h
Actual completion time:
"""

from project import Project
from datetime import datetime
from operator import attrgetter

NAME_INDEX = 0
START_DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_ESTIMATE_INDEX = 3
COMPLETION_PERCENTAGE_INDEX = 4

MENU = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit

>>> """


def main():
    menu_choice = input(MENU).upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            projects = load_projects()
        elif menu_choice == "S":
            try:
                save_projects(projects)
            except UnboundLocalError:
                print("Projects must first be loaded")
        elif menu_choice == "D":
            try:
                display_projects(projects)
            except UnboundLocalError:
                print("Projects must first be loaded")
        elif menu_choice == "F":
            try:
                show_projects_after_date(projects)
            except UnboundLocalError:
                print("Projects must first be loaded")
        elif menu_choice == "A":
            try:
                add_new_project(projects)
            except UnboundLocalError:
                print("Projects must first be loaded")
        elif menu_choice == "U":
            print("TODO")
        else:
            print("Invalid menu choice")
        menu_choice = input(MENU).upper()


def load_projects():
    projects = []
    filename = get_valid_string("Filename: ")
    done = False
    while not done:
        try:
            in_file = open(filename, 'r')
            in_file.readline()  # Skip header
            for line in in_file:
                parts = line.strip().split('\t')
                project = Project(str(parts[NAME_INDEX]),
                                  (datetime.strptime(parts[START_DATE_INDEX], '%d/%m/%Y').date()),
                                  int(parts[PRIORITY_INDEX]),
                                  float(parts[COST_ESTIMATE_INDEX]), int(parts[COMPLETION_PERCENTAGE_INDEX]))
                projects.append(project)
            in_file.close()
            print(f"Projects loaded")
            done = True
        except FileNotFoundError:
            print("File not found")
            filename = get_valid_string("Filename: ")
    return projects


def display_projects(projects):
    print("Completed projects:")
    projects.sort()  # Sort projects by priority
    for project in projects:
        if project.is_complete():
            print(f"    {project}")
    print("Uncompleted projects:")
    for project in projects:
        if not project.is_complete():
            print(f"    {project}")


def save_projects(projects):
    filename = get_valid_string("Filename: ")
    done = False
    while not done:
        try:
            out_file = open(filename, 'w')
            print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)  # Print headers
            for project in projects:
                print(
                    f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
                    file=out_file)
            out_file.close()
            print(f"Projects saved in {filename}")
            done = True
        except FileExistsError:
            print(f"File {filename} already exists")
            filename = get_valid_string("Filename: ")


def show_projects_after_date(projects):
    input_date = get_valid_date("Show projects that begin after date (dd/mm/yyyy): ")
    projects.sort(key=attrgetter('start_date'))
    for project in projects:
        if input_date <= project.start_date:
            print(project)


def add_new_project(projects):
    name = get_valid_string("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yyyy): ")
    priority = get_valid_positive_int("Priority: ")
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = get_valid_positive_int("Percent complete: ")
    new_project = Project(str(name), start_date, int(priority), float(cost_estimate), int(completion_percentage))
    projects.append(new_project)


def get_valid_string(prompt):
    item = input(prompt)
    while item == "":
        print("Invalid")
        item = input(prompt)
    return item


def get_valid_date(prompt):
    input_date = input(prompt)
    try:
        input_date = datetime.strptime(input_date, '%d/%m/%Y').date()
    except ValueError:
        print("Invalid date format. Use dd/mm/yyyy format")
        input_date = input(prompt)
        input_date = datetime.strptime(input_date, '%d/%m/%Y').date()
    return input_date


def get_valid_positive_int(prompt):
    done = False
    while not done:
        try:
            positive_int = int(input(prompt))
            if positive_int < 0:
                done = False
                print("Input whole positive integers only")
            else:
                done = True
        except ValueError:
            print("Input whole positive integers only")
    return positive_int  # Ignore error


if __name__ == "__main__":
    main()
