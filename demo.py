from datetime import datetime
from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode
from roadmapper.group import Group
from roadmapper.task import Task


def demo01(
    mode: TimelineMode = TimelineMode.MONTHLY,
    start_date: str = "2023-01-01",
    number_of_items: int = 12,
    file_name: str = "demo01.png",
) -> None:
    roadmap = Roadmap(1200, 312)
    roadmap.set_title("My Demo Roadmap")
    roadmap.set_timeline(mode, start_date, number_of_items)
    with roadmap.add_group("Core Product Work Stream") as group:
        with group.add_task("Base Functionality", "2022-11-01", "2023-10-31") as task:
            task.add_milestone("v.1.0", "2023-02-15")
            task.add_milestone("v.1.1", "2023-08-01")
            task.add_milestone("v.1.2", "2023-09-30")
            with task.add_parellel_task(
                "Enhancements", "2023-11-15", "2024-03-31"
            ) as task1a:
                task1a.add_milestone("v.2.0", "2024-03-30")
        with group.add_task("Showcase #1", "2023-03-01", "2023-05-07") as task:
            with task.add_parellel_task(
                "Showcase #2", "2023-06-01", "2023-08-07"
            ) as parellel_task:
                pass

    with roadmap.add_group("Mobility Work Stream") as group:
        with group.add_task(
            "Mobile App Development", "2023-02-01", "2024-12-07"
        ) as task:
            task.add_milestone("iOS App", "2023-04-15")
            task.add_milestone("Android App", "2023-09-07")

    roadmap.set_footer("Generated by Roadmap Generator")
    roadmap.draw()
    roadmap.save(file_name)


def demo02_barestyle(
    mode: TimelineMode = TimelineMode.MONTHLY,
    start_date: str = "2023-01-01",
    number_of_items: int = 12,
    file_name: str = "demo01.png",
) -> None:
    roadmap = Roadmap(1200, 312)

    roadmap.set_title("My Demo Roadmap")
    roadmap.set_timeline(mode, start_date, number_of_items)

    group: Group
    task: Task
    parallel_task: Task

    group = roadmap.add_group("Core Product Work Stream")
    task = group.add_task("Base Functionality", "2022-11-01", "2023-10-31")
    task.add_milestone("v.1.0", "2023-02-15")
    task.add_milestone("v.1.1", "2023-08-01")
    task.add_milestone("v.1.2", "2023-09-30")
    parallel_task = task.add_parallel_task("Enhancements", "2023-11-15", "2024-03-31")
    parallel_task.add_milestone("v.2.0", "2024-03-30")

    task = group.add_task("Showcase #1", "2023-03-01", "2023-05-07")
    task.add_parallel_task("Showcase #2", "2023-06-01", "2023-08-07")

    group = roadmap.add_group("Mobility Work Stream")
    task = group.add_task("Mobile App Development", "2023-02-01", "2024-12-07")
    task.add_milestone("iOS App", "2023-04-15")
    task.add_milestone("Android App", "2023-09-07")

    roadmap.set_footer(
        "Generated by Roadmap Generator on "
        + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    roadmap.draw()
    roadmap.save(file_name)
    roadmap.print_roadmap()


def demo03(
    mode: TimelineMode = TimelineMode.MONTHLY,
    start_date: str = "2023-01-01",
    number_of_items: int = 12,
    file_name: str = "demo01.png",
) -> None:
    roadmap = Roadmap(1200, 312)
    roadmap.set_title("My Demo Roadmap!!!")
    roadmap.set_timeline(mode, start_date, number_of_items)

    group = roadmap.add_group("Core Product Work Stream")
    task = group.add_task("Base Functionality", "2022-11-01", "2023-10-31")
    task.add_milestone("v.1.0", "2023-02-15")
    task.add_milestone("v.1.1", "2023-08-01")
    parellel_task = task.add_parallel_task("Enhancements", "2023-11-15", "2024-03-31")
    parellel_task.add_milestone("v.2.0", "2024-03-30")

    task = group.add_task("Showcase #1", "2023-03-01", "2023-05-07")
    task.add_parallel_task("Showcase #2", "2023-06-01", "2023-08-07")

    roadmap.set_footer("Generated by Roadmap Generator")
    roadmap.draw()
    roadmap.save(file_name)
    roadmap.print_roadmap()


# demo01(file_name="demo01.png")
# demo01(TimelineMode.WEEKLY, "2023-02-01", 16, "demo02.png")
# demo01(TimelineMode.QUARTERLY, "2023-02-01", 4, "demo03.png")
# demo01(TimelineMode.HALF_YEARLY, "2023-02-01", 3, "demo04.png")
# demo01(TimelineMode.YEARLY, "2023-02-01", 2, "demo05.png")

# demo02_barestyle(file_name="demo01.png")
# demo02_barestyle(TimelineMode.WEEKLY, "2023-02-01", 16, "demo02.png")
# demo02_barestyle(TimelineMode.QUARTERLY, "2023-02-01", 4, "demo03.png")
# demo02_barestyle(TimelineMode.HALF_YEARLY, "2023-02-01", 3, "demo04.png")
# demo02_barestyle(TimelineMode.YEARLY, "2023-02-01", 2, "demo05.png")

demo03(file_name="demo07.png")
