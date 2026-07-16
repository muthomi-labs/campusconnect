"""
starter_code.py — Group Activity: SQL Subquery Patterns
=========================================================
CONTEXT: CampusConnect, a course-enrollment system

Three tables are already built and seeded for you below - you don't need
to change anything above the "YOUR TASKS START HERE" line.

Your job: fill in the three TODO queries, one per subquery pattern.
Each one is a real question CampusConnect's admin team actually needs
answered.

Run this file at any time to check your progress:
    python3 starter_code.py

Stuck? Re-read the "Think First" question in the worksheet before you
touch the keyboard - the goal is to reason out what the answer SHOULD
be first, then write the query that gets there.
"""

import sqlite3

# ---------------------------------------------------------------------------
# DATABASE SETUP - already done for you
# ---------------------------------------------------------------------------

conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("""
    CREATE TABLE courses (
        id       INTEGER PRIMARY KEY,
        title    TEXT,
        category TEXT
    )
""")

cur.execute("""
    CREATE TABLE students (
        id   INTEGER PRIMARY KEY,
        name TEXT
    )
""")

cur.execute("""
    CREATE TABLE enrollments (
        id          INTEGER PRIMARY KEY,
        student_id  INTEGER,
        course_id   INTEGER
    )
""")

courses = [
    (1, "Python Basics",     "Programming"),
    (2, "Web Development",   "Programming"),
    (3, "Data Structures",   "Programming"),
    (4, "UI/UX Design",      "Design"),
    (5, "Cloud Computing",   "Infrastructure"),  # nobody has enrolled - yet
]

students = [
    (1, "Amina"),
    (2, "Brian"),
    (3, "Cynthia"),
    (4, "David"),
    (5, "Grace"),
    (6, "Hassan"),  # hasn't enrolled in anything - yet
]

enrollments = [
    # id, student_id, course_id
    (1, 1, 1),  # Amina    -> Python Basics
    (2, 1, 2),  # Amina    -> Web Development
    (3, 2, 1),  # Brian    -> Python Basics
    (4, 3, 1),  # Cynthia  -> Python Basics
    (5, 3, 3),  # Cynthia  -> Data Structures
    (6, 3, 4),  # Cynthia  -> UI/UX Design
    (7, 4, 2),  # David    -> Web Development
    (8, 5, 1),  # Grace    -> Python Basics
    (9, 5, 3),  # Grace    -> Data Structures
]

cur.executemany("INSERT INTO courses VALUES (?, ?, ?)", courses)
cur.executemany("INSERT INTO students VALUES (?, ?)", students)
cur.executemany("INSERT INTO enrollments VALUES (?, ?, ?)", enrollments)
conn.commit()


def run(title, sql):
    print("\n" + "=" * 65)
    print(title)
    print("-" * 65)
    if sql is None:
        print("  (not written yet - this is your job!)")
        return
    try:
        rows = cur.execute(sql).fetchall()
    except sqlite3.Error as e:
        print(f"  SQL error: {e}")
        return
    if not rows:
        print("  (query ran, but returned no rows)")
        return
    headers = rows[0].keys()
    for r in rows:
        print("  " + " | ".join(f"{h}: {r[h]}" for h in headers))


# ===========================================================================
# YOUR TASKS START HERE
# ===========================================================================
#
# For every task: write ONE query with a subquery inside it.
# Put your SQL as a Python string, then pass it into run(...) below.
# See the worksheet for the "Think First" question for each task.

# ---------------------------------------------------------------------------
# TASK 1 - Scalar subquery (returns ONE value)
# Question: "Which courses have MORE enrollments than the average course?"
# ---------------------------------------------------------------------------
task_1_sql = None  # <-- replace None with your SQL string, in triple quotes

# ---------------------------------------------------------------------------
# TASK 2 - IN subquery (returns a LIST)
# Question: "Which students are enrolled in Python Basics?"
# ---------------------------------------------------------------------------
task_2_sql = None  # <-- replace None with your SQL string

# ---------------------------------------------------------------------------
# TASK 3 - NOT IN subquery (finds what's MISSING)
# Question: "Which students are not enrolled in ANY course?"
# ---------------------------------------------------------------------------
task_3_sql = None  # <-- replace None with your SQL string


# ===========================================================================
# Do not edit below this line - this just runs and displays your work
# ===========================================================================
if __name__ == "__main__":
    run("TASK 1: Courses with above-average enrollments", task_1_sql)
    run("TASK 2: Students enrolled in Python Basics", task_2_sql)
    run("TASK 3: Students enrolled in nothing", task_3_sql)
    conn.close()