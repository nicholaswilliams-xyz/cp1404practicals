"""

Estimated completion time: 3h
Actual completion time:
"""

from project import Project
import datetime

PROJECTS = "projects.txt"
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
            print("TODO")
        elif menu_choice == "S":
            print("TODO")
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            print("TODO")
        elif menu_choice == "A":
            print("TODO")
        elif menu_choice == "U":
            print("TODO")
        else:
            print("Invalid menu choice")
        menu_choice = input(MENU).upper()


def load_projects():
    projects = []
    in_file = open(PROJECTS, 'r')
    in_file.readline()  # Skip header
    for line in in_file:
        parts = line.strip().split('\t')
        project = Project(str(parts[NAME_INDEX]), parts[START_DATE_INDEX], int(parts[PRIORITY_INDEX]),
                          float(parts[COST_ESTIMATE_INDEX]), int(parts[COMPLETION_PERCENTAGE_INDEX]))
        projects.append(project)
    in_file.close()
    return projects


def display_projects(projects):
    print("Completed projects:")
    projects.sort()  # Sort project by priority
    for project in projects:
        if project.is_complete():
            print(f"    {project}")
    print("Uncompleted projects:")
    for project in projects:
        if not project.is_complete():
            print(f"    {project}")


if __name__ == "__main__":
    main()
