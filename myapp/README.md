## Database

### Why SQLite?

For this stage of the project, SQLite was chosen because it requires no separate
database server to install or configure — the entire database lives in a single
file. This makes the project easy to run on any machine with zero setup beyond
cloning the repo, which is ideal for a learning project focused on understanding
how an API layer talks to a persistent storage layer. Since the API design already
separates routes from storage logic, moving to a heavier database (e.g. PostgreSQL)
later would require no changes to the API itself.

### Where the database is stored

The database is stored in a single file, `tasks.db`, created automatically in the
project root the first time the application runs. If the file or the `tasks` table
doesn't exist yet, both are created automatically on startup, and three example
tasks are inserted only if the table is empty.

### How to run the project

```bash
git clone <your-repo-url>
cd <your-repo-folder>
python3 -m venv venv
source venv/bin/activate
pip install fastapi "uvicorn[standard]"
uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`, with interactive docs at
`http://localhost:8000/docs`. The database file (`tasks.db`) and its table are
created automatically on first run — no manual setup required.

### Database viewer screenshot

_Screenshot taken using DB Browser for SQLite, showing the `tasks` table after
a few CRUD operations via the API._

### Example SQL query

```sql
SELECT * FROM tasks WHERE done = 1;
```

This query returns all tasks marked as completed. Running it directly in the
SQLite viewer confirmed that changes made through the API (e.g. marking a task
done via `PUT /tasks/{id}`) are reflected immediately in the underlying database.
